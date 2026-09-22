# 🧠 Cursor Semantic Query Engine

### AI-Powered Multi-Source Document Question Answering System Using RAG

An AI-powered Semantic Query Engine that enables users to upload documents, provide URLs, and retrieve meaningful answers through natural language queries. Built using Retrieval-Augmented Generation (RAG), the system combines semantic search with Large Language Models (LLMs) to deliver context-aware responses based on user-provided data.

---

## 📌 Project Overview

The **Cursor Semantic Query Engine** is designed to simplify information retrieval from multiple data sources.

Traditional keyword-based search systems often struggle to understand the context and meaning behind a user's query. This project addresses that limitation by leveraging semantic embeddings, vector databases, and LLM-based response generation.

The application processes documents and web content, converts them into vector embeddings, stores them in a vector database, and retrieves relevant information when a user submits a query.

The retrieved context is then passed to an LLM to generate a relevant response.

---

## ✨ Key Features

* **Multi-Source Data Ingestion** – Upload PDF and text documents and process web URLs.
* **Retrieval-Augmented Generation (RAG)** – Generate context-aware answers using retrieved information.
* **Semantic Search** – Retrieve relevant content based on meaning rather than exact keyword matching.
* **Vector Database Integration** – Store and search document embeddings using ChromaDB.
* **AI-Powered Question Answering** – Ask natural-language questions about uploaded content.
* **Interactive Web Interface** – Access document ingestion and query functionality through a web-based UI.
* **Document Processing** – Extract and process content from supported document formats.
* **LLM Integration** – Support configurable LLM providers, depending on the project configuration.
* **REST API Backend** – Handle document ingestion and query processing through FastAPI.

---

## 🏗️ System Architecture

```text
           ┌─────────────────────────────┐
           │         User Interface      │
           │       React + Vite           │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │       FastAPI Backend       │
           │       REST API Layer        │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │      Data Ingestion         │
           │                             │
           │   PDF | Text | Web URLs     │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │    Text Extraction &        │
           │        Chunking             │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │     Embedding Generation    │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │       ChromaDB              │
           │    Vector Storage &        │
           │    Semantic Retrieval       │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │      LLM Response           │
           │       Generation            │
           └──────────────┬──────────────┘
                          │
                          ▼
           ┌─────────────────────────────┐
           │     Contextual Answer       │
           │       to the User           │
           └─────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Component              | Technology                                         |
| ---------------------- | -------------------------------------------------- |
| Frontend               | React.js, Vite, Tailwind CSS                       |
| Backend                | Python, FastAPI                                    |
| AI Framework           | LangChain                                          |
| Vector Database        | ChromaDB                                           |
| Document Processing    | PyMuPDF                                            |
| Web Content Extraction | BeautifulSoup                                      |
| LLM Integration        | Ollama / Gemini / Groq, depending on configuration |
| API Server             | Uvicorn                                            |
| Version Control        | Git & GitHub                                       |

---

## 📂 Project Structure

The following is a representative structure. Refer to the actual repository for the complete implementation.

```text
CURSOR-SEMANTIC-QUERY/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── rag/
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### Prerequisites

Install the following before running the application:

* Python 3.10 or later
* Node.js and npm
* Git
* A supported LLM provider and its required configuration

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd <YOUR_PROJECT_DIRECTORY>
```

### 2. Set Up the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file using the configuration required by your selected LLM provider.

Example:

```env
# Add the variables required by your backend configuration.
# Example:
GEMINI_API_KEY=your_api_key_here
```

Use only the environment variables supported by your actual implementation.

**Important:** Never upload your `.env` file, API keys, access tokens, or other credentials to GitHub.

### 4. Start the Backend Server

From the backend directory, run:

```bash
uvicorn main:app --reload
```

The backend will typically be available at:

```text
http://127.0.0.1:8000
```

If enabled in the FastAPI configuration, interactive API documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

### 5. Set Up the Frontend

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in your terminal by Vite.

---

## 🔍 How It Works

### Step 1: Data Ingestion

Users provide documents or web URLs through the application interface.

### Step 2: Text Extraction

The system extracts readable text from supported sources using document-processing and web-scraping tools.

### Step 3: Text Chunking

Extracted text is divided into smaller chunks to support efficient embedding generation and retrieval.

### Step 4: Embedding Generation

The text chunks are converted into vector embeddings that capture their semantic meaning.

### Step 5: Vector Storage

The embeddings and associated metadata are stored in ChromaDB.

### Step 6: Semantic Retrieval

When a user submits a query, the system retrieves relevant document chunks based on semantic similarity.

### Step 7: Answer Generation

The retrieved context is passed to the configured LLM, which generates a response relevant to the user's question.

---

## 🎯 Use Cases

* Research paper analysis
* Document-based question answering
* Knowledge base search
* Technical documentation retrieval
* Academic learning and study assistance
* Web content analysis
* Context-aware information retrieval

---

## 🔮 Future Enhancements

* Conversation history and persistent chat sessions
* Improved source citations and answer traceability
* Advanced document management and deletion controls
* Support for additional file formats
* Improved retrieval accuracy through reranking
* Enhanced authentication and user management
* More robust error handling and automated testing
* Improved security validation for URL ingestion

---

## 🔐 Security Considerations

* Store API keys and credentials in environment variables.
* Never commit secrets or private configuration files.
* Validate uploaded files and user-provided URLs.
* Restrict backend access to internal network resources.
* Apply appropriate authentication and authorization controls before production deployment.

---

## 👨‍💻 Author

**Jayasurya L.**

B.E. Computer Science and Engineering

GitHub: [jayasurya-0007](https://github.com/jayasurya-0007)

LinkedIn: [Jayasurya L.](https://www.linkedin.com/in/jayasurya-l-1ab17b2a3)

---

## 📜 License

This project is intended for educational and development purposes.

Add a `LICENSE` file to the repository if you intend to distribute the project under a specific open-source license.
