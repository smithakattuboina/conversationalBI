

# 🤖 Conversational BI

A full-stack **Conversational Business Intelligence (BI)** application that allows users to interact with business data using natural language.

Instead of manually writing SQL queries or navigating through multiple dashboards, users can ask questions such as:

- "What is the total sales?"
- "Which region has the highest sales?"
- "What is the top-selling brand?"
- "Show me sales by region."
- "Which region performed the best?"
- "What are the key business insights from the data?"

The system converts natural-language questions into meaningful database queries, retrieves the required information from the business database, and presents the result through a conversational interface.

---

 

---

# 📖 Overview

**Conversational BI** is an AI-powered Business Intelligence application designed to make business data analysis easier through natural-language conversations.

Traditional Business Intelligence systems often require users to:

1. Understand the database structure.
2. Write SQL queries.
3. Navigate through dashboards.
4. Understand different KPIs and reports.

This project provides a conversational alternative.

The user can simply type a question in natural language. The application processes the question, understands the requested business information, interacts with the database, and returns a meaningful response.

The system combines:

- Artificial Intelligence
- Natural Language Processing
- Large Language Models
- SQL
- SQLite
- FastAPI
- JavaScript
- HTML/CSS

to create an interactive conversational analytics platform.

---

# ❗ Problem Statement

Business organizations generate large amounts of structured data such as:

- Sales
- Revenue
- Products
- Regions
- Brands
- Customers
- Transactions

However, extracting useful information from this data often requires technical knowledge.

For example, a business user may want to know:

> "Which region generated the highest sales?"

A traditional system may require the user to manually create a SQL query such as:

```sql
SELECT region, SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC
LIMIT 1;

A non-technical user may not know how to write this query.

Conversational BI solves this problem by allowing users to ask the question directly in natural language.

💡 Solution

The proposed system provides a conversational interface between the user and the business database.

Traditional Approach
User
 ↓
Understand Database
 ↓
Write SQL Query
 ↓
Execute Query
 ↓
Analyze Result
Conversational BI Approach
User
 ↓
Natural Language Question
 ↓
AI / LLM
 ↓
Query Understanding
 ↓
SQL Generation
 ↓
Database
 ↓
Query Result
 ↓
Business Response

This makes business analytics accessible to users who may not have SQL knowledge.

🎯 Objectives

The main objectives of the project are:

Build a conversational interface for business data analysis.
Allow users to ask questions using natural language.
Reduce dependency on manual SQL queries.
Connect an AI model with a structured business database.
Generate and execute appropriate database queries.
Provide useful business insights from database results.
Create a modular and scalable backend architecture.
Provide a simple and user-friendly frontend.
Demonstrate the integration of AI with Business Intelligence.
🚀 Key Features
1. Natural Language Queries

Users can ask business questions in normal English.

Example:

Which region has the highest sales?

instead of manually writing SQL.

2. Conversational Interface

The application provides a chat-style interface where users can interact with the business database.

Users can ask multiple questions during the same session.

3. AI-Powered Query Understanding

The AI layer interprets the user's question and determines what information needs to be retrieved from the database.

4. SQL-Based Data Retrieval

The system connects the AI layer with the SQLite database and retrieves the required business information.

5. KPI Analysis

The application can support important business KPIs such as:

Total Sales
Sales by Region
Sales by Brand
Top-Selling Brand
Top-Performing Region
6. Modular Backend

The backend is divided into separate components for:

API handling
AI services
Database management
Business logic
Data models
Request/response schemas

This makes the project easier to maintain and extend.

7. Local AI Model Support

The project uses Ollama for running the AI model locally.

This allows the application to communicate with a locally hosted Large Language Model instead of depending entirely on cloud-based AI APIs.

8. REST API

The backend exposes API endpoints using FastAPI.

The frontend communicates with the backend through these APIs.

9. SQLite Database

SQLite is used as the database for storing and retrieving business data.

It is lightweight and suitable for development and demonstration purposes.

🛠 Technology Stack
Category	Technology
Programming Language	Python
Backend Framework	FastAPI
Database	SQLite
AI/LLM	Ollama
Frontend	HTML
Styling	CSS
Client-side Logic	JavaScript
API Communication	REST API
Data Query Language	SQL
Development Environment	Visual Studio Code
Version Control	Git
Repository	GitHub
🏗 System Architecture

The high-level architecture of the application is:

                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               │ Natural Language
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │    HTML/CSS/JS      │
                    └──────────┬──────────┘
                               │
                               │ HTTP Request
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌─────────────────┐
       │   Chat Service  │          │   AI Service    │
       │ Business Logic  │          │    Ollama       │
       └────────┬────────┘          └────────┬────────┘
                │                            │
                │                            │
                └─────────────┬──────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │    SQL Database     │
                    │       SQLite        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Query Result / KPI  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Conversational      │
                    │ Response            │
                    └─────────────────────┘
📂 Project Structure
conversational-bi/
│
├── backend/
│   └── app/
│       │
│       ├── ai/
│       │   └── ollama_service.py
│       │
│       ├── api/
│       │   └── chat_api.py
│       │
│       ├── config/
│       │
│       ├── database/
│       │   ├── connection.py
│       │   └── session.py
│       │
│       ├── models/
│       │   └── chat.py
│       │
│       ├── schemas/
│       │   └── chat_schema.py
│       │
│       ├── services/
│       │   └── chat_service.py
│       │
│       ├── static/
│       │   ├── script.js
│       │   └── style.css
│       │
│       ├── templates/
│       │   └── index.html
│       │
│       ├── main.py
│       └── ...
│
├── data/
│
├── docs/
│
├── tests/
│
├── .gitignore
├── README.md
└── chat.db

Note: Local database files, virtual environments, API keys, and other sensitive/local files should not be committed to GitHub.

🔍 How the Application Works

The application follows a multi-step process.

Step 1 — User Enters a Question

The user enters a question through the chat interface.

Example:

Which region has the highest sales?
Step 2 — Frontend Sends Request

The JavaScript frontend sends the question to the FastAPI backend using an HTTP request.

Conceptually:

Frontend
   ↓
POST /chat
   ↓
FastAPI
Step 3 — API Receives the Question

The API layer receives the user's request.

The request is validated using the application's schema layer.

Step 4 — Chat Service Processes the Request

The chat service acts as the business-logic layer.

It coordinates between:

User request
AI service
Database
Response generation
Step 5 — AI Processes the Question

The AI service communicates with the locally running Ollama model.

The model analyzes the user's natural-language question.

For example:

User Question:
Which region has the highest sales?

The AI identifies that the user wants:

Region
+
Total Sales
+
Highest Value
Step 6 — SQL Query

The required information is retrieved from the database using SQL.

For example:

SELECT region,
       SUM(sales) AS total_sales
FROM sales
GROUP BY region
ORDER BY total_sales DESC
LIMIT 1;
Step 7 — Database Executes the Query

SQLite executes the query and returns the result.

Example:

Region: South
Total Sales: ₹12,50,000
Step 8 — Response is Returned

The backend sends the result back to the frontend.

The user sees a conversational response such as:

The South region has the highest sales,
with total sales of ₹12,50,000.
🗄 Database

The project uses SQLite as the database.

SQLite provides a lightweight relational database suitable for:

Development
Testing
Prototyping
Academic projects
Small-scale applications

The database contains business-related information used for analysis.

A typical business dataset can contain fields such as:

sales
region
brand
product
date
customer

The database can be extended with additional tables and columns as the project grows.

🤖 AI and Natural Language Processing

The AI component is implemented using Ollama.

Ollama allows Large Language Models to run locally.

The general process is:

Natural Language
       ↓
     LLM
       ↓
Understand Intent
       ↓
Generate/Determine Query
       ↓
Database
       ↓
Result

The AI layer is implemented separately in:

backend/app/ai/ollama_service.py

Keeping the AI functionality separate from the API and database layers makes it easier to change the underlying model in the future.

For example, the project can potentially be extended to support different LLM providers or models.

⚙ Backend

The backend is implemented using FastAPI.

FastAPI is responsible for:

Creating API endpoints
Receiving user requests
Validating requests
Calling application services
Returning responses
Connecting the frontend with backend services
Backend Layers
API Layer

Location:

backend/app/api/

Responsible for handling HTTP requests.

Service Layer

Location:

backend/app/services/

Responsible for application and business logic.

AI Layer

Location:

backend/app/ai/

Responsible for communication with Ollama and AI-related operations.

Database Layer

Location:

backend/app/database/

Responsible for:

Database connection
Database sessions
Database operations
Models

Location:

backend/app/models/

Defines database-related models.

Schemas

Location:

backend/app/schemas/

Defines request and response structures.

🎨 Frontend

The frontend is implemented using:

HTML
CSS
JavaScript

Files:

backend/app/templates/index.html
backend/app/static/style.css
backend/app/static/script.js
HTML

Defines the structure of the conversational interface.

CSS

Controls:

Layout
Colors
Chat bubbles
Buttons
Input area
Overall UI appearance
JavaScript

Handles:

User input
Sending API requests
Receiving responses
Updating the chat interface
🔄 API Flow

The general API flow is:

Browser
   │
   │ POST Request
   ▼
FastAPI
   │
   ▼
Chat API
   │
   ▼
Chat Service
   │
   ├──────────────► Ollama
   │                    │
   │                    ▼
   │               AI Processing
   │
   ▼
Database
   │
   ▼
SQL Result
   │
   ▼
Response
   │
   ▼
Browser
💬 Example Queries

The following are examples of questions that can be asked:

Overall Business Performance
What is the total sales?
Give me an overview of the business performance.
Regional Analysis
Which region has the highest sales?
Show me sales by region.
Which region is performing the best?
Brand Analysis
Which brand has the highest sales?
Show sales by brand.
What is the top-selling brand?
Business Insights
What are the key business insights?
Which region should the company focus on?
Which brand is performing better?
📦 Installation
1. Clone the Repository

Clone the repository using:

git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd conversational-bi
🐍 2. Create a Virtual Environment

Create a Python virtual environment:

Windows
python -m venv venv

Activate it:

venv\Scripts\activate
macOS/Linux
python3 -m venv venv
source venv/bin/activate
📥 3. Install Dependencies

Install the required Python packages:

pip install -r requirements.txt

If a requirements.txt file is not present, install the required packages according to the project's imports.

The main backend dependencies include:

FastAPI
Uvicorn
SQLAlchemy
Pydantic

and the packages required for your Ollama integration.

🧠 4. Install Ollama

Download and install Ollama from the official website:

https://ollama.com/

After installation, verify that Ollama is available:

ollama --version
🤖 5. Download an Ollama Model

Pull the model configured for the project.

For example:

ollama pull llama3.2

The exact model should match the model configured in:

backend/app/ai/ollama_service.py

Start Ollama if required:

ollama serve
⚙️ Configuration

Before running the application, check the configuration files.

Important configuration values may include:

Database URL
Ollama URL
Ollama Model
API configuration

If environment variables are used, create a .env file.

Example:

DATABASE_URL=sqlite:///./chat.db
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

Never commit .env files or API keys to GitHub.

▶️ Running the Application

From the project root:

uvicorn backend.app.main:app --reload

If your project uses a different module path, use the command configured in main.py.

A successful startup will normally show something similar to:

Uvicorn running on http://127.0.0.1:8000

Open the application in your browser:

http://127.0.0.1:8000
📚 FastAPI Documentation

FastAPI automatically provides interactive API documentation.

Once the server is running, open:

http://127.0.0.1:8000/docs

This allows developers to:

View available API endpoints
Test API requests
Inspect request schemas
Inspect responses
🧪 Testing the Application

A basic testing workflow is:

Test 1 — Application Startup

Start the backend:

uvicorn backend.app.main:app --reload

Verify that the server starts successfully.

Test 2 — Open Frontend

Open:

http://127.0.0.1:8000
Test 3 — Ask a Business Question

Example:

What is the total sales?
Test 4 — Test Regional Analysis
Which region has the highest sales?
Test 5 — Test Brand Analysis
Which brand has the highest sales?
🔐 Security Considerations

The following security practices should be followed when deploying this project:

Never commit secrets

Do not upload:

.env
API keys
passwords
database credentials
private tokens
Use .gitignore

The repository includes a .gitignore file to prevent local and sensitive files from being uploaded.

Example:

venv/
__pycache__/
*.pyc
.env
.env.*
*.db
SQL Injection Protection

If user-generated queries are executed against the database, appropriate validation and restrictions should be implemented.

AI-generated SQL should not automatically be treated as trusted input.

A production system should:

Validate generated SQL.
Restrict dangerous commands.
Allow only permitted operations.
Use read-only database access where possible.
Prevent commands such as:
DROP
DELETE
UPDATE
INSERT
ALTER

unless explicitly required and securely controlled.

🌍 Real-World Use Cases

Conversational BI can be useful in multiple industries.

Retail

A manager can ask:

Which product category generated the most revenue?
FMCG

A business analyst can ask:

Which region has the highest sales for our brand?
Finance

A financial analyst can ask:

What was the total revenue last month?
E-Commerce

A manager can ask:

Which product is selling the most?
Sales Management

A sales manager can ask:

Which region needs improvement?
⭐ Advantages
1. Easy to Use

Users can communicate with the system using natural language.

2. Reduces SQL Dependency

Users do not need to know SQL for basic analytics.

3. Faster Data Analysis

Business questions can be answered quickly.

4. AI-Powered

The application uses an LLM to understand natural-language questions.

5. Modular Architecture

The application is divided into independent layers.

6. Local AI

Ollama allows AI models to run locally.

7. Extendable

The project can be extended with:

More datasets
More KPIs
More LLM models
Data visualization
Authentication
Advanced analytics
⚠️ Limitations

The current version has some limitations.

1. Database Size

SQLite is mainly suitable for lightweight applications and development.

Large enterprise deployments would benefit from databases such as:

PostgreSQL
MySQL
Microsoft SQL Server
2. AI Accuracy

LLMs may occasionally misunderstand a question or generate an incorrect query.

Therefore, AI-generated SQL should be validated.

3. Limited Business Context

The quality of the answer depends on the available database schema and business information.

4. Local Model Performance

The performance of the Ollama model depends on:

CPU
RAM
GPU
Model size
🔮 Future Enhancements

The project can be extended in several directions.

1. Data Visualization

Automatically generate:

Bar charts
Line charts
Pie charts
KPI cards
Tables

based on the user's question.

Example:

Show sales by region as a bar chart.
2. Advanced Conversational Memory

The system can remember previous questions.

Example:

User:
What is the highest-selling region?

System:
South.

User:
What about its top brand?

The system can understand that "its" refers to the previously mentioned region.

3. Multi-Database Support

Support databases such as:

PostgreSQL
MySQL
SQL Server
Oracle
4. Authentication

Add:

User login
User roles
Admin dashboard
Role-based access control
5. Enterprise Deployment

The application can be deployed using:

Docker
Cloud platforms
Kubernetes
CI/CD pipelines
6. Advanced BI Features

Future versions can include:

Predictive analytics
Forecasting
Anomaly detection
Automated reports
Business recommendations
KPI monitoring
Alert generation
7. Multiple AI Models

The system can be extended to support different LLMs.

For example:

Ollama
OpenAI
Gemini
Claude
Other open-source LLMs
📈 Future Architecture

A more advanced version could follow:

                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │ Conversational  │
                  │     Interface   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   AI / LLM      │
                  │ Query Planning  │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        SQL Agent      KPI Engine    Analytics
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    Business Database
                           │
                           ▼
                  ┌─────────────────┐
                  │ Data Processing │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Visualization   │
                  │ & Insights      │
                  └─────────────────┘
🧠 Learning Outcomes

This project provides practical experience in:

Python
FastAPI
REST APIs
SQL
SQLite
Database connectivity
Backend architecture
Frontend development
JavaScript
Natural Language Processing
Large Language Models
Prompt Engineering
AI integration
Business Intelligence
Git
GitHub
Software architecture
🧩 Project Architecture Principles

The project follows a modular structure where different responsibilities are separated.

API
 ↓
Service
 ↓
AI / Database
 ↓
Response

This separation provides:

Maintainability

Individual components can be modified without changing the entire application.

Scalability

New services and features can be added easily.

Testability

Individual layers can be tested independently.

Readability

The codebase is easier for developers to understand.

🔧 GitHub Setup

To push the project to GitHub:

git init

Add the files:

git add .

Create the first commit:

git commit -m "Initial commit"

Connect the GitHub repository:

git remote add origin <YOUR_GITHUB_REPOSITORY_URL>

Rename the branch:

git branch -M main

Push the project:

git push -u origin main
📝 Example Git Workflow

After making changes:

git status

Add changes:

git add .

Commit:

git commit -m "Add new conversational BI feature"

Push:

git push
📌 Conclusion

Conversational BI demonstrates how Artificial Intelligence and Business Intelligence can be combined to create a more accessible approach to data analysis.

Instead of requiring users to understand SQL queries and database structures, the system allows them to interact with business data using natural language.

The project combines:

AI
+
Natural Language
+
SQL
+
Database
+
FastAPI
+
Frontend
=
Conversational Business Intelligence

The current implementation provides a foundation that can be extended into a complete enterprise-level conversational analytics platform.

👩‍💻 Author

Smith(a) Kattuboina

B.Tech Student
VIT University

Project

Conversational BI — AI-Powered Business Intelligence using Natural Language
