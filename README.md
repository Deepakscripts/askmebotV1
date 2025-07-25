# AskMe Bot V1: Your Intelligent Telegram Assistant

An advanced, multi-purpose Telegram bot that serves as your personal assistant. It can engage in general conversation, read and answer questions about PDF documents you upload, and perform live web searches to provide you with up-to-the-minute information.

## 📜 Table of Contents

* [Project Overview](#-project-overview)
* [Features](#-features)
* [Tools & Technologies](#-tools--technologies)
* [Getting Started: Setup and Installation](#-getting-started-setup-and-installation)
    * [Step 1: Obtain Necessary API Keys](#step-1-obtain-necessary-api-keys)
    * [Step 2: Set Up the Project Locally](#step-2-set-up-the-project-locally)
* [How to Use the Bot](#-how-to-use-the-bot)
* [Project Structure](#-project-structure)
* [Contributing](#-contributing)

---

## 📝 Project Overview

**AskMe Bot V1** is designed to be a versatile and intelligent chatbot on the Telegram platform. It goes beyond simple pre-programmed responses by integrating powerful Large Language Models (LLMs - gpt-4.1-nano) and search technologies. Whether you need a quick answer to a general knowledge question, want to extract information from a lengthy PDF report, or need the latest news on a topic, this bot is equipped to handle your requests efficiently.

The core of this project lies in its modularity, allowing for the seamless integration of different capabilities:
1.  **Conversational AI:** For natural, human-like conversations.
2.  **Document Analysis (RAG):** For deep insights from your documents.
3.  **Live Web Search:** For real-time information retrieval.

---

## ✨ Features

This bot comes packed with three main features that you can interact with directly in your Telegram chat.

### 1. **General Chat & Queries**
You can chat with the bot as you would with a person. It's powered by OpenAI's models, allowing it to answer a wide range of questions, help with brainstorming, translate text, summarize ideas, and much more.

### 2. **PDF Document Analysis (RAG)**
Simply upload a PDF file to the chat, and the bot will read and process it. Once processed, you can ask specific questions about the content of the document. This is incredibly useful for:
* Quickly summarizing long reports or research papers.
* Finding specific facts or data points within a document without reading the whole thing.
* Getting answers based *only* on the information provided in the PDF.
The bot uses a Retrieval-Augmented Generation (RAG) pipeline, which means it finds the most relevant parts of your document and uses that context to generate a precise answer.

### 3. **Live Web Search**
For questions that require the most current information:
* Checking the latest news headlines.
* Getting real-time information like stock prices or weather forecasts.
* Answering questions about recent events that a standard LLM might not know about.

---

## 🛠️ Tools & Technologies

This project leverages a modern stack of technologies to deliver its features.

* **Python:** The core programming language for the bot's logic.
* **python-telegram-bot:** A robust library for interacting with the Telegram Bot API, handling updates, and sending messages.
* **LangChain:** The primary framework used to build the application's logic. It chains together different components, such as LLMs, document loaders, and retrieval systems, to create powerful AI applications.
* **OpenAI API:** Provides the powerful GPT models (gpt-4.1-nano) that serve as the "brain" of the chatbot, responsible for generating responses and understanding user queries.
* **Tavily AI API:** A specialized search engine built for LLMs. It provides a clean, relevant, and accurate search API that is used for the live web search feature.
* **FAISS (Facebook AI Similarity Search):** An extremely efficient library for similarity searching. In this project, it's used to create a vector index of the PDF document's content, allowing the bot to quickly find the most relevant text chunks to answer a user's question.
* **PyPDF2:** A Python library used to read and extract text from PDF files, which is the first step in the document analysis pipeline.

---

## 🚀 Getting Started: Setup and Installation

To get this bot running on your own system, follow these two main steps.

### Step 1: Obtain Necessary API Keys

You will need three API keys to use all the features of this bot.

#### 1. **Telegram Bot Token**
This token allows your code to connect to your bot on Telegram.
1.  Open Telegram and search for a bot called `BotFather`.
2.  Start a chat with `BotFather` and send the command: `/newbot`
3.  Follow the instructions. It will ask you for a name and a username for your bot.
4.  Once you're done, `BotFather` will give you a long string of characters. **This is your bot token.**
5.  Copy it and save it somewhere safe.

#### 2. **OpenAI API Key**
This key gives you access to OpenAI's language models.
1.  Go to the [OpenAI Platform website](https://platform.openai.com/) and create an account or log in.
2.  In the top-right corner, click on your profile, then select **"View API keys"**.
3.  Click the **"+ Create new secret key"** button.
4.  Give the key a name (e.g., "TelegramBotKey") and click **"Create secret key"**.
5.  **Important:** Copy the key immediately and save it. You will not be able to see it again.
*Note: Using the OpenAI API is a paid service. You may need to set up a payment method in your OpenAI account.*

#### 3. **Tavily AI API Key**
This key is for the live web search feature.
1.  Go to the [Tavily AI website](https://tavily.com/) and sign up for an account.
2.  After logging in, navigate to your account dashboard or API key section.
3.  You will find your API key there. Copy it and save it.

### Step 2: Set Up the Project Locally

Now that you have your keys, you can set up the project on your computer.

1.  **Clone the Repository**
    Open your terminal or command prompt and run this command:
    ```bash
    git clone [https://github.com/Deepakscripts/askmebotV1.git](https://github.com/Deepakscripts/askmebotV1.git)
    cd askmebotV1
    ```

2.  **Create a Virtual Environment**
    It's highly recommended to use a virtual environment to keep your project's dependencies separate.
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install all the required Python libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create and Configure the `.env` File**
    This file will securely store your API keys.
    * In the main project directory, create a new file named `.env`.
    * Open the file and add the following lines, pasting the keys you obtained earlier.

    ```env
    OPENAI_API_KEY="your_openai_api_key_here"
    TAVILY_API_KEY="your_tavily_api_key_here"
    TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
    ```

5.  **Run the Bot**
    You're all set! Start the bot with this command:
    ```bash
    python main.py
    ```
    If everything is configured correctly, your terminal will show a message indicating that the bot has started.

---

## 🤖 How to Use the Bot

Once the bot is running, open Telegram and find the bot you created.

* **Start Command:**
    Send `/start` to receive a welcome message and instructions.

* **General Conversation:**
    Simply type any message or question and send it. The bot will respond conversationally.

* **PDF Analysis:**
    1.  **Upload a PDF file** directly to the chat.
    2.  The bot will reply with: `File received and processed. You can now ask me questions about it.`
    3.  Now, send your questions about the document (e.g., "What is the main conclusion of this report?"). The bot will answer based on the PDF's content.

* **Web Search:**
   The bot will perform a live search and give you a summarized answer based on the search results because LLM (gpt-4.1-nano) don't have current information.

---

## 📁 Project Structure

Here is a brief overview of the project's file structure to help you navigate the code:

askmebotV1/
├── bot/
│ ├── core.py # Main bot application logic, sets up handlers
│ ├── handlers.py # Defines how the bot handles messages, commands, and files
│ └── rag.py # Contains the RAG logic for PDF and web search
├── utils/
│ └── llm.py # Initializes and configures the LLMs and search tools
├── .env # Stores secret API keys (you must create this)
├── .gitignore # Specifies files for Git to ignore
├── main.py # The entry point of the application
└── requirements.txt # Lists all Python dependencies

---
