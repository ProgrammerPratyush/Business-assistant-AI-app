import os
import sqlite3
import pdfplumber
from dotenv import load_dotenv
import openai
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Load API keys from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI
openai.api_key = OPENAI_API_KEY

# SQLite database for storing user history
DB_FILE = "history.db"

# Ensure database exists
def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        feature TEXT,
        user_input TEXT,
        response TEXT
    )
    """)
    conn.commit()
    conn.close()

initialize_db()

# Function to fetch PPC trends
def fetch_ppc_data():
    url = "https://databox.com/ppc-industry-benchmarks"
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find("div", class_="content-column")
        if not content:
            return "Could not find the relevant content on the website."
        text_data = content.get_text(separator="\n", strip=True)
        return text_data
    except Exception as e:
        return f"Error fetching PPC data: {e}"

# Function to generate AI-based PPC definition
def generate_ppc_definition():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in digital marketing."},
                {"role": "user", "content": "Explain PPC in businesses in bullet points."}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error generating PPC definition: {e}"

# Function to extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

# Function to save history in the database
def save_history(feature, user_input, response):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO history (feature, user_input, response) VALUES (?, ?, ?)",
        (feature, user_input, response)
    )
    conn.commit()
    conn.close()

# Function to display history from the database
def display_history():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to generate keywords
def generate_keywords(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in digital marketing."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error generating keywords: {e}"

# Streamlit App
st.set_page_config(page_title="Business Assistant App", layout="wide")

# Sidebar Menu
st.sidebar.title("Description of this App")
st.sidebar.write("""
Welcome to the Business Assistant App!
- **Know the PPC Trends**: Fetch PPC trends from an industry-standard website.
- **Generate Keywords**: Answer questions, generate keywords randomly or based on a PDF.
- **Ask FAQs to AI**: Get answers to your digital marketing questions from an AI assistant.
- **My History**: Review your previous queries and AI responses.
""")

# Sidebar Navigation
menu_option = st.sidebar.selectbox("Navigate", ["Know PPC Trends", "Generate Keywords", "Ask FAQs", "My History"])

# Handle "Know PPC Trends"
if menu_option == "Know PPC Trends":
    st.title("PPC Trends")

    st.subheader("What is PPC in Businesses?")
    ppc_definition = generate_ppc_definition()
    st.markdown(ppc_definition)

    st.subheader("Source of Trends")
    source_link = "https://databox.com/ppc-industry-benchmarks"
    st.write(f"[PPC Industry Benchmarks - Source Link]({source_link})")

    st.subheader("Trends Overview")
    st.write("Fetching PPC trends from the industry benchmarks website...")
    ppc_data = fetch_ppc_data()

    if ppc_data.startswith("Error"):
        st.error(ppc_data)
    else:
        st.success("PPC Trends fetched successfully!")
        st.text_area("PPC Trends", value=ppc_data, height=300)
        save_history("PPC Trends", "N/A", ppc_data)

# Handle "Generate Keywords"
elif menu_option == "Generate Keywords":
    st.title("Generate Keywords")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Generate Keywords Randomly")
        industry = st.text_input("Enter your business industry:")
        objective = st.text_input("Enter your business objective (e.g., lead generation, sales):")
        website = st.text_input("Do you have a website? If yes, please share the URL:")
        social_media = st.text_input("Do you have any social media platforms? If yes, please share the URL(s):")
        ppc = st.text_input("Do you use PPC campaigns? (yes/no):")
        audience = st.text_input("Who are you trying to reach? (e.g., young adults, professionals, etc.):")
        location = st.text_input("What location(s) would you like to target?:")

        if st.button("Generate Keywords Randomly"):
            prompt = (
                f"Generate a list of keywords for a {industry} business with the following details:\n"
                f"- Objective: {objective}\n"
                f"- Website: {website}\n"
                f"- Social Media Platforms: {social_media}\n"
                f"- PPC Campaigns: {ppc}\n"
                f"- Target Audience: {audience}\n"
                f"- Target Locations: {location}"
            )
            keywords = generate_keywords(prompt)
            st.markdown(f"**Generated Keywords:**\n\n{keywords}")
            save_history("Generate Keywords", prompt, keywords)

    with col2:
        st.subheader("Upload PDF to Generate Keywords")
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if uploaded_file and st.button("Extract and Generate Keywords from PDF"):
            pdf_text = extract_text_from_pdf(uploaded_file)
            if pdf_text.startswith("Error"):
                st.error(pdf_text)
            else:
                prompt = f"Generate keywords based on the following content:\n{pdf_text}"
                keywords = generate_keywords(prompt)
                st.markdown(f"**Generated Keywords from PDF:**\n\n{keywords}")
                save_history("Generate Keywords (PDF)", "Uploaded PDF", keywords)

# Handle "Ask FAQs"
elif menu_option == "Ask FAQs":
    st.title("Ask FAQs to AI")
    question = st.text_area("Enter your query:")
    if st.button("Submit Query"):
        prompt = f"Answer the following FAQ: {question}"
        answer = generate_keywords(prompt)
        st.markdown(f"**Answer:**\n\n{answer}")
        save_history("Ask FAQs", question, answer)

# Handle "My History"
elif menu_option == "My History":
    st.title("My History")
    history = display_history()
    for record in history:
        st.write(f"**Feature**: {record[1]}")
        st.write(f"**User Input**: {record[2]}")
        st.write(f"**Response**: {record[3]}")
        st.write("---")
