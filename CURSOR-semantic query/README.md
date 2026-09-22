# Cursor Semantic Query Engine

### An AI-Powered Multi-Source Retrieval-Augmented Generation (RAG) Platform

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react\&logoColor=black)](https://react.dev/)
[![ChromaDB](https://img.shields.io/badge/Vector_DB-ChromaDB-orange)](https://www.trychroma.com/)
[![LangChain](https://img.shields.io/badge/AI_Framework-LangChain-green)](https://www.langchain.com/)

**Cursor Semantic Query Engine** is an AI-powered document intelligence and semantic search application that enables users to interact with information from multiple data sources using natural language.

The system leverages **Retrieval-Augmented Generation (RAG), vector embeddings, semantic similarity search, and Large Language Models (LLMs)** to retrieve contextually relevant information and generate meaningful responses grounded in ingested content.

Designed with a modular Python backend and an interactive web frontend, the application bridges the gap between traditional document search and intelligent conversational information retrieval.

---

## 📌 Table of Contents

* [Project Overview](#-project-overview)
* [Problem Statement](#-problem-statement)
* [Project Objectives](#-project-objectives)
* [Key Features](#-key-features)
* [Technology Stack](#-technology-stack)
* [System Architecture](#-system-architecture)
* [RAG Pipeline](#-rag-pipeline)
* [Project Structure](#-project-structure)
* [Installation and Setup](#-installation-and-setup)
* [Environment Configuration](#-environment-configuration)
* [Running the Application](#-running-the-application)
* [API Documentation](#-api-documentation)
* [Use Cases](#-use-cases)
* [Security Considerations](#-security-considerations)
* [Future Enhancements](#-future-enhancements)
* [Author](#-author)

---

## 🚀 Project Overview

Modern applications generate large volumes of unstructured information across PDF documents, text files, technical documentation, and web pages. Extracting relevant knowledge from these sources manually can be time-consuming and inefficient.

The Cursor Semantic Query Engine addresses this challenge through an AI-driven semantic retrieval system.

Instead of relying exclusively on keyword matching, the application represents document content as numerical vector embeddings. These embeddings enable the retrieval system to identify semantically similar information based on the meaning and context of a user's query.

The retrieved information is subsequently passed to a configured Large Language Model, which generates a natural-language response based on the available context.

### Core Concept

**Ingest → Process → Embed → Store → Retrieve → Generate**

The application transforms unstructured content into a searchable knowledge base and provides an intuitive interface for interacting with that knowledge.

---

## 🎯 Problem Statement

Traditional search systems often depend on exact keyword matching, which can limit their ability to understand user intent and retrieve contextually relevant information.

When working with large collections of documents, users may encounter the following challenges:

* Difficulty locating specific information across multiple documents.
* Inefficient manual reading and searching.
* Limited understanding of semantic relationships between queries and document content.
* Lack of contextual answers from conventional search interfaces.
* Fragmented information across local documents and web resources.

### Proposed Solution

The Cursor Semantic Query Engine introduces a RAG-based architecture that combines semantic retrieval with generative AI.

By retrieving relevant document segments before generating an answer, the system aims to improve the relevance and contextual grounding of responses while reducing dependence on the LLM's pretrained knowledge alone.

---

## 🎯 Project Objectives

1. Develop a unified platform for ingesting content from multiple sources.
2. Implement semantic search using vector embeddings and a vector database.
3. Integrate Retrieval-Augmented Generation for context-aware question answering.
4. Build a modular backend using FastAPI and Python.
5. Provide an interactive frontend for document ingestion and conversational querying.
6. Support configurable LLM integrations.
7. Improve information accessibility through natural-language interaction.
8. Establish a foundation for an extensible AI-powered knowledge retrieval system.

---

## ✨ Key Features

### 1. Multi-Source Data Ingestion

Accept supported document formats and web URLs as knowledge sources.

### 2. Intelligent Document Processing

Extract readable text from supported documents and web pages using dedicated parsing and extraction libraries.

### 3. Semantic Search

Retrieve content based on semantic similarity rather than relying exclusively on exact keyword matches.

### 4. Retrieval-Augmented Generation

Combine retrieved document context with an LLM to generate relevant natural-language answers.

### 5. Vector Database Integration

Use ChromaDB to store and retrieve vector embeddings and associated document metadata.

### 6. Interactive Query Interface

Provide a web-based interface for submitting questions and viewing AI-generated responses.

### 7. RESTful Backend Architecture

Use FastAPI to expose backend functionality through HTTP endpoints.

### 8. Configurable LLM Integration

Support model-provider configurations compatible with the implemented backend, allowing the generation component to be adapted to different environments.

---

## 🛠️ Technology Stack

The project combines modern frontend technologies, Python-based backend development, document-processing libraries, and AI retrieval infrastructure.

### Technology Stack Overview

| Technology        | Category             | Purpose                                              |
| ----------------- | -------------------- | ---------------------------------------------------- |
| Python 3.11+      | Programming Language | Backend logic, data processing, and AI orchestration |
| FastAPI           | Backend Framework    | REST API development and request handling            |
| Uvicorn           | ASGI Server          | Running the FastAPI application                      |
| React.js          | Frontend Library     | Building interactive user interfaces                 |
| Vite              | Frontend Build Tool  | Development server and frontend bundling             |
| Tailwind CSS      | CSS Framework        | Responsive UI styling                                |
| LangChain         | AI Framework         | Document processing and RAG orchestration            |
| ChromaDB          | Vector Database      | Storing and retrieving vector embeddings             |
| PyMuPDF           | Document Processing  | Extracting text from PDF files                       |
| BeautifulSoup     | HTML Parsing         | Extracting readable content from web pages           |
| Requests          | HTTP Client          | Retrieving web content                               |
| Ollama            | Local LLM Runtime    | Running supported language models locally            |
| Google Gemini API | LLM Provider         | Cloud-based language model integration               |
| Groq API          | LLM Provider         | Cloud-based inference for supported models           |
| Git & GitHub      | Version Control      | Source code management and collaboration             |

*The exact provider, embedding model, and dependency versions depend on the project's current configuration.*

### Frontend Technologies

#### React.js

Used to develop reusable UI components and manage interactive application behavior.

#### Vite

Provides a development server and build tooling for the React application.

#### Tailwind CSS

Enables utility-based styling to create a responsive and maintainable user interface.

### Backend Technologies

#### Python

Implements the core application logic, document-processing workflow, retrieval operations, and integration with AI services.

#### FastAPI

Provides the REST API layer responsible for receiving user requests, processing inputs, and returning responses.

#### Uvicorn

Serves the FastAPI application using an ASGI-compatible server.

### AI and Retrieval Technologies

#### LangChain

Supports the orchestration of document-processing and retrieval workflows, depending on the modules used in the implementation.

#### ChromaDB

Acts as the vector storage and similarity-search layer. It stores embeddings and associated metadata for retrieval during query processing.

#### Large Language Models

The project supports configurable LLM integrations, including:

* **Ollama:** Local model inference.
* **Google Gemini API:** Cloud-based LLM inference.
* **Groq API:** Cloud-based inference for supported models.

The selected provider must be configured according to the application's environment and implementation.

### Document Processing Technologies

#### PyMuPDF

Extracts textual content from PDF documents for downstream processing.

#### BeautifulSoup

Parses HTML content to support extraction of readable text from web pages.

#### Requests

Handles HTTP requests used to retrieve external web content.

---

## 🏗️ System Architecture

The application follows a modular architecture that separates the user interface, backend API, document-processing pipeline, vector retrieval system, and LLM response-generation layer.

```text
┌─────────────────────────────────────────┐
│              USER                       │
│                                         │
│  Upload Document / Submit URL / Query   │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│           FRONTEND APPLICATION          │
│                                         │
│          React + Vite + Tailwind        │
│                                         │
│     User Interaction & Result Display   │
└───────────────────┬─────────────────────┘
                    │ HTTP Requests
                    ▼
┌─────────────────────────────────────────┐
│             FASTAPI BACKEND             │
│                                         │
│       API Routes & Request Handling     │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          DOCUMENT INGESTION             │
│                                         │
│          PDF / Text / Web URL            │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│       TEXT EXTRACTION & CHUNKING        │
│                                         │
│       PyMuPDF / BeautifulSoup           │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│         EMBEDDING GENERATION             │
│                                         │
│       Text → Vector Representations     │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│              CHROMADB                   │
│                                         │
│       Vector Storage & Retrieval        │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          SEMANTIC RETRIEVAL             │
│                                         │
│      Relevant Document Chunks           │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          LLM GENERATION LAYER           │
│                                         │
│        Context-Aware Answer             │
└───────────────────┬─────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│           RESPONSE TO USER              │
│                                         │
│       Natural-Language Answer            │
└─────────────────────────────────────────┘
```

---

## 🧠 RAG Pipeline

The core intelligence of the Cursor Semantic Query Engine is based on Retrieval-Augmented Generation.

RAG combines information retrieval with language generation, allowing the application to retrieve relevant external context before generating an answer.

### Phase 1: Document Ingestion

The user uploads a supported document or provides a web URL.

The backend receives the input and identifies the appropriate processing method.

### Phase 2: Text Extraction

The application extracts textual content from the source.

* PDF documents are processed using PyMuPDF.
* Web pages are parsed using BeautifulSoup.
* Supported text files are processed by the relevant ingestion logic.

### Phase 3: Text Chunking

The extracted content is divided into smaller segments called chunks.

Chunking enables the retrieval system to search smaller, more focused portions of the source rather than processing an entire document for every query.

### Phase 4: Embedding Generation

Each text chunk is converted into a vector representation using the configured embedding model.

These embeddings capture semantic characteristics of the text and enable similarity-based retrieval.

### Phase 5: Vector Storage

The generated embeddings, text chunks, and relevant metadata are stored in ChromaDB.

This creates a searchable knowledge base for subsequent user queries.

### Phase 6: Query Embedding and Retrieval

When a user submits a question, the query is converted into a vector representation using the compatible embedding model.

The retrieval component searches the vector database for relevant document chunks based on semantic similarity.

### Phase 7: Context Construction

The retrieved chunks are assembled into contextual information for the generation component.

The quality of this context directly affects the relevance and grounding of the final response.

### Phase 8: LLM Response Generation

The retrieved context and user's query are passed to the configured LLM.

The model generates a natural-language response based on the supplied context and its generation instructions.

### Phase 9: Response Delivery

The backend returns the generated response to the frontend, where it is displayed to the user.

---

## 📂 Project Structure

The following structure illustrates the expected separation of frontend and backend responsibilities. Verify directory names against the actual repository before treating this as the exact file tree.

```text
CURSOR-SEMANTIC-QUERY/
│
├── backend/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── upload.py
│   │   └── ...
│   │
│   ├── rag/
│   │   ├── loaders.py
│   │   └── ...
│   │
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

Follow these steps to configure and run the application locally.

### Prerequisites

Ensure the following tools are installed:

| Requirement            | Purpose                |
| ---------------------- | ---------------------- |
| Python 3.11+           | Backend execution      |
| Node.js and npm        | Frontend development   |
| Git                    | Repository management  |
| Supported LLM provider | AI response generation |

A local Ollama installation is required if you choose to run a compatible model locally.

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd <YOUR_PROJECT_DIRECTORY>
```

### 2. Configure the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the appropriate directory based on your backend configuration.

Add the required environment variables for the selected LLM provider, embedding model, and other integrations.

Example:

```env
# Example only — use variable names expected by your code.
GEMINI_API_KEY=your_api_key_here
```

Do not add real API keys or credentials to the repository.

### 4. Configure the Frontend

Open a separate terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install the required packages:

```bash
npm install
```

### 5. Start the Backend

From the backend directory, run:

```bash
uvicorn main:app --reload
```

The backend should start on the configured host and port.

If the application uses the default Uvicorn configuration, the backend will be accessible at:

```text
http://127.0.0.1:8000
```

### 6. Start the Frontend

From the frontend directory, run:

```bash
npm run dev
```

Vite will display the frontend development URL in the terminal.

Open that URL in your browser to access the application.

---

## 🔌 API Documentation

The backend uses FastAPI to expose application functionality through REST endpoints.

FastAPI can generate interactive API documentation when the corresponding documentation routes are enabled.

For a default local configuration, Swagger UI is typically available at:

```text
http://127.0.0.1:8000/docs
```

The exact API routes and request schemas should be verified against the running backend.

Potential API categories include:

| API Category        | Responsibility                                     |
| ------------------- | -------------------------------------------------- |
| Authentication      | User authentication and session-related operations |
| Document Upload     | Accept and process supported documents             |
| URL Ingestion       | Retrieve and process web content                   |
| Semantic Query      | Retrieve relevant context and generate responses   |
| Document Management | Manage previously ingested sources, if implemented |

Refer to the actual backend route definitions for supported endpoints, HTTP methods, and required parameters.

---

## 🧪 Testing and Validation

Testing is important to verify the reliability of the ingestion, retrieval, and response-generation pipeline.

Recommended testing areas include:

* Document upload validation.
* PDF and web content extraction.
* Text chunking and embedding generation.
* ChromaDB storage and retrieval.
* Semantic query relevance.
* LLM response generation.
* API request validation and error handling.
* Authentication and authorization.
* URL ingestion security.
* Frontend-to-backend integration.

Automated tests should be executed using the testing framework and commands configured in the repository.

---

## 💡 Use Cases

### Academic Research

Retrieve relevant information from research papers, reports, and study materials.

### Document Intelligence

Query large documents without manually searching through every page.

### Knowledge Base Search

Build a searchable knowledge base from internal documentation and reference materials.

### Technical Documentation Assistant

Retrieve relevant information from technical documents and development resources.

### Web Content Analysis

Extract and query information from supported web pages.

### AI-Powered Learning Assistant

Support natural-language exploration of educational content and reference materials.

---

## 🔐 Security Considerations

Security is an important part of deploying an AI-powered document retrieval system.

The following practices are recommended:

* Store API keys and credentials in environment variables.
* Exclude `.env` files and sensitive configuration from Git tracking.
* Validate uploaded files and restrict unsupported formats.
* Apply appropriate authentication and authorization controls.
* Validate URLs before making server-side HTTP requests.
* Restrict access to localhost, private IP addresses, and internal network resources during URL ingestion.
* Validate redirect destinations to prevent SSRF bypasses.
* Apply request timeouts and response-size limits.
* Avoid logging sensitive user content or credentials.

These measures should be implemented and tested before exposing the application to untrusted users.

---

## 🚧 Future Enhancements

The project can be extended with additional features to improve retrieval quality, usability, and operational reliability.

### AI and Retrieval Improvements

* Advanced retrieval strategies and hybrid search.
* Cross-encoder or model-based reranking.
* Improved chunking strategies.
* Query rewriting and contextual retrieval.
* Source citations and document-level traceability.

### User Experience Improvements

* Persistent conversation history.
* Document management dashboard.
* Source preview and retrieved-context inspection.
* Improved loading states and error handling.
* Responsive UI enhancements.

### Backend and Infrastructure Improvements

* Asynchronous document processing.
* Background ingestion tasks.
* Improved caching and retrieval performance.
* Comprehensive automated test coverage.
* Structured logging and monitoring.
* Containerized deployment.
* Improved authentication and access control.

---

## 📈 Project Significance

The Cursor Semantic Query Engine demonstrates the practical integration of modern AI technologies with full-stack software development.

The project brings together:

* Python-based backend development.
* REST API design using FastAPI.
* React-based frontend development.
* Document processing and information extraction.
* Vector database integration.
* Semantic search and retrieval.
* LLM-based response generation.
* RAG pipeline implementation.

It provides a foundation for developing AI-powered knowledge retrieval applications capable of transforming unstructured data into accessible, searchable information.

---

## 👨‍💻 Author

**Jayasurya L.**

B.E. Computer Science and Engineering
K. Ramakrishnan College of Technology

GitHub: [jayasurya-0007](https://github.com/jayasurya-0007)

LinkedIn: [Jayasurya L.](https://www.linkedin.com/in/jayasurya-l-1ab17b2a3)

---

## 📜 License

This project is intended for educational and development purposes.

If you plan to distribute or maintain the project as open-source software, add a `LICENSE` file specifying the applicable license.

---

⭐ **If you find this project interesting, consider exploring the repository and its implementation.**
