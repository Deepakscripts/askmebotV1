AskMe Bot V1: Your Intelligent Telegram Assistant
An advanced, multi-purpose Telegram bot that serves as your personal assistant. It can engage in general conversation, read and answer questions about PDF documents you upload, and perform live web searches to provide you with up-to-the-minute information.

📜 Table of Contents
Project Overview

Features

Tools & Technologies

Getting Started: Setup and Installation

Step 1: Obtain Necessary API Keys

Step 2: Set Up the Project Locally

How to Use the Bot

Project Structure

Contributing

📝 Project Overview
AskMe Bot V1 is designed to be a versatile and intelligent chatbot on the Telegram platform. It goes beyond simple pre-programmed responses by integrating powerful Large Language Models (LLMs) and search technologies. Whether you need a quick answer to a general knowledge question, want to extract information from a lengthy PDF report, or need the latest news on a topic, this bot is equipped to handle your requests efficiently.

The core of this project lies in its modularity, allowing for the seamless integration of different capabilities:

Conversational AI: For natural, human-like conversations.

Document Analysis (RAG): For deep insights from your documents.

Live Web Search: For real-time information retrieval.

✨ Features
This bot comes packed with three main features that you can interact with directly in your Telegram chat.

1. General Chat & Queries
You can chat with the bot as you would with a person. It's powered by OpenAI's models, allowing it to answer a wide range of questions, help with brainstorming, translate text, summarize ideas, and much more.

2. PDF Document Analysis (RAG)
Simply upload a PDF file to the chat, and the bot will read and process it. Once processed, you can ask specific questions about the content of the document. This is incredibly useful for:

Quickly summarizing long reports or research papers.

Finding specific facts or data points within a document without reading the whole thing.

Getting answers based only on the information provided in the PDF.
The bot uses a Retrieval-Augmented Generation (RAG) pipeline, which means it finds the most relevant parts of your document and uses that context to generate a precise answer.

3. Live Web Search
For questions that require the most current information, you can use the web search feature. By using the /web command, you can ask the bot to search the internet for an answer. This is perfect for:

Checking the latest news headlines.

Getting real-time information like stock prices or weather forecasts.

Answering questions about recent events that a standard LLM might not know about.

🛠️ Tools & Technologies
This project leverages a modern stack of technologies to deliver its features.

Python: The core programming language for the bot's logic.

python-telegram-bot: A robust library for interacting with the Telegram Bot API, handling updates, and sending messages.

LangChain: The primary framework used to build the application's logic. It chains together different components, such as LLMs, document loaders, and retrieval systems, to create powerful AI applications.

OpenAI API: Provides the powerful GPT models that serve as the "brain" of the chatbot, responsible for generating responses and understanding user queries.

Tavily AI API: A specialized search engine built for LLMs. It provides a clean, relevant, and accurate search API that is used for the live web search feature.

FAISS (Facebook AI Similarity Search): An extremely efficient library for similarity searching. In this project, it's used to create a vector index of the PDF document's content, allowing the bot to quickly find the most relevant text chunks to answer a user's question.

PyPDF2: A Python library used to read and extract text from PDF files, which is the first step in the document analysis pipeline.

🚀 Getting Started: Setup and Installation
To get this bot running on your own system, follow these two main steps.

Step 1: Obtain Necessary API Keys
You will need three API keys to use all the features of this bot.

1. Telegram Bot Token
This token allows your code to connect to your bot on Telegram.

Open Telegram and search for a bot called BotFather.

Start a chat with BotFather and send the command: /newbot

Follow the instructions. It will ask you for a name and a username for your bot.

Once you're done, BotFather will give you a long string of characters. This is your bot token.

Copy it and save it somewhere safe.

2. OpenAI API Key
This key gives you access to OpenAI's language models.

Go to the OpenAI Platform website and create an account or log in.

In the top-right corner, click on your profile, then select "View API keys".

Click the "+ Create new secret key" button.

Give the key a name (e.g., "TelegramBotKey") and click "Create secret key".

Important: Copy the key immediately and save it. You will not be able to see it again.
Note: Using the OpenAI API is a paid service. You may need to set up a payment method in your OpenAI account.

3. Tavily AI API Key
This key is for the live web search feature.

Go to the Tavily AI website and sign up for an account.

After logging in, navigate to your account dashboard or API key section.

You will find your API key there. Copy it and save it.

Step 2: Set Up the Project Locally
Now that you have your keys, you can set up the project on your computer.

Clone the Repository
Open your terminal or command prompt and run this command:

git clone https://github.com/Deepakscripts/askmebotV1.git
cd askmebotV1

Create a Virtual Environment
It's highly recommended to use a virtual environment to keep your project's dependencies separate.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install Dependencies
Install all the required Python libraries using the requirements.txt file.

pip install -r requirements.txt

Create and Configure the .env File
This file will securely store your API keys.

In the main project directory, create a new file named .env.

Open the file and add the following lines, pasting the keys you obtained earlier.

OPENAI_API_KEY="your_openai_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"

Run the Bot
You're all set! Start the bot with this command:

python main.py

If everything is configured correctly, your terminal will show a message indicating that the bot has started.

🤖 How to Use the Bot
Once the bot is running, open Telegram and find the bot you created.

Start Command:
Send /start to receive a welcome message and instructions.

General Conversation:
Simply type any message or question and send it. The bot will respond conversationally.

PDF Analysis:

Upload a PDF file directly to the chat.

The bot will reply with: File received and processed. You can now ask me questions about it.

Now, send your questions about the document (e.g., "What is the main conclusion of this report?"). The bot will answer based on the PDF's content.

Web Search:

Use the /web command followed by your query.

Example: /web what is the latest news about NASA's Artemis mission?

The bot will perform a live search and give you a summarized answer based on the search results.

📁 Project Structure
Here is a brief overview of the project's file structure to help you navigate the code:

askmebotV1/
├── bot/
│   ├── core.py         # Main bot application logic, sets up handlers
│   ├── handlers.py     # Defines how the bot handles messages, commands, and files
│   └── rag.py          # Contains the RAG logic for PDF and web search
├── utils/
│   └── llm.py          # Initializes and configures the LLMs and search tools
├── .env                # Stores secret API keys (you must create this)
├── .gitignore          # Specifies files for Git to ignore
├── main.py             # The entry point of the application
└── requirements.txt    # Lists all Python dependencies

