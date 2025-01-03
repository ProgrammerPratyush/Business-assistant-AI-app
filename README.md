# 🧑‍💻 Business Assistant App 📈

Welcome to the Business Assistant App, your AI-powered digital marketing assistant! This app leverages advanced AI models and web scraping to provide insights, generate keywords, and assist with frequently asked questions (FAQs) related to digital marketing. It's built using Streamlit for the frontend, SQLite for storing user history, and various other Python libraries for data processing and API interactions.

## 🚀 Features ✨

### 1. Know the PPC Trends 📊

Fetch the latest PPC (Pay Per Click) industry benchmarks from trusted sources.


Get an AI-generated explanation of PPC in businesses to understand its importance and application.


Access a source link for the latest PPC Industry Benchmarks from Databox.


### 2. Generate Keywords 🔑

Generate a list of keywords based on your business information like industry, business objective, target audience, location, and more.


Upload a PDF document, and the app will extract the text and generate relevant keywords from it.


Help your digital marketing campaigns by providing you with customized keywords for SEO and PPC.


### 3. Ask FAQs to AI ❓

Ask questions related to digital marketing and get AI-powered answers.


Get insights from GPT-3.5 to help with digital marketing strategies and terminology.


### 4. My History 📜

View your history of queries and AI responses.


All your past interactions are saved in the SQLite database, allowing you to revisit the responses for future reference.


### 🛠 Technologies Used 🛠

***Python*** for backend logic

***Streamlit*** for building the interactive web interface

***OpenAI GPT-3.5*** for generating responses and insights

***SQLite*** for storing user query history

***pdfplumber*** for extracting text from PDF files

***BeautifulSoup*** for web scraping PPC industry trends

***Requests*** for fetching data from external sources

***dotenv*** for securely managing API keys


### 🧑‍💻 How to Run the App Locally 🚀

**1. Clone the Repository**

          git clone https://github.com/yourusername/business-assistant-app.git


          cd business-assistant-app


**2. Set Up Environment**

Create a virtual environment:

          python -m venv venv

          source venv/bin/activate  # For Mac/Linux
          
          venv\Scripts\activate     # For Windows


Install the required dependencies:

          pip install -r requirements.txt


**3. Set Up API Keys**

Create a .env file in the root directory of the project and add your OpenAI API key:


          OPENAI_API_KEY="your-openai-api-key"


**4. Run the App**

          streamlit run app.py

Open the URL provided by Streamlit in your browser to access the app.


### 📄 How the App Works 🛠

***1. Know PPC Trends***

PPC Trends: Fetches industry-standard trends from the web and presents them in a readable format. Users can read about the latest trends in the PPC industry and also view a source link for further reading.

AI-generated Explanation: Provides an expert-level explanation of PPC in businesses, helping users understand what PPC is and how it is beneficial for their business.


***2. Generate Keywords***

Users can input details about their business (industry, objective, target audience, etc.) into the app and generate a list of SEO and PPC keywords.

PDF-based Keyword Generation: Users can upload a PDF document, and the app will extract the text from the file and generate relevant keywords based on the content.


***3. Ask FAQs to AI***

Users can enter any digital marketing-related question, and the app will respond with AI-powered answers generated using the OpenAI GPT-3.5 model.


***4. My History***

The app saves every interaction in a SQLite database, allowing users to view past queries and responses. This feature makes it easy to track the history of all user interactions.

#### 📊 App Demo 🎥
You can watch a demo video of the app in action. It shows all the features mentioned above and provides a walk-through of how to use the app effectively.


### 💡 Contributing 🤝

Feel free to fork the repository and submit pull requests with improvements, bug fixes, or new features. We welcome contributions to make this app better!

Steps to contribute:

Fork the repository

Create a new branch for your feature or fix

Commit your changes

Push your changes to your fork

Open a pull request


### 👨‍💻 Contact 📧
For any questions or suggestions, feel free to reach out:

***Email:*** ppurigoswami2002@gmail.com
***GitHub:*** ProgrammerPratyush


We hope you find this Business Assistant App useful in your digital marketing journey! 🚀
