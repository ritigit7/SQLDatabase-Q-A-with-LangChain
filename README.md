# AtliQ T-Shirts - SQL Database Q&A with LangChain

Welcome to the **AtliQ T-Shirts** project! This Streamlit application enables users to interact with an inventory database of T-shirts through natural language queries, powered by **LangChain** and a **Hugging Face** model. The application translates questions into SQL to provide accurate responses based on real-time database information.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## Project Overview

The **AtliQ T-Shirts** app aims to simplify access to inventory data by allowing users to ask questions in plain English. This app converts natural language queries into SQL commands using few-shot learning, making it ideal for non-technical users. 

### Objective

- **User-Friendly Q&A**: Easy data retrieval for inventory management.
- **Automatic SQL Generation**: Converts natural language to SQL queries.
- **Enhanced Accuracy**: Few-shot learning helps refine query understanding.

---

## Features

- **Natural Language Queries**: Users can interact using plain language, no SQL knowledge required.
- **Few-shot Learning**: Enhanced accuracy with examples for contextual understanding.
- **Interactive UI**: Streamlit-based, clean, and easy to navigate.

---

## Screenshots

### Query Example
![Query Example](https://github.com/ritigit7/SQLDatabase-Q-A-with-LangChain/blob/main/Screenshot%202024-11-09%20120511.png)

---

## Installation

### Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed.
2. **MySQL Database**: Create a MySQL database named `atliq_tshirts` and set up tables for T-shirt inventory.
3. **API Tokens**: Sign up for **Hugging Face** and **SERP API** to obtain API tokens.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/AtliQ-T-Shirts-QA.git
   cd AtliQ-T-Shirts-QA

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt

3. **Set Up Database**:
   Create the MySQL database and tables as per the SQL schema provided (optional SQL file for structure).
   Populate the database with sample data.

4. **API Key Configuration**:
   ```bash
   export HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"
   export SERPAPI_API_KEY="your_serpapi_api_key"

## Usage

- Run the Streamlit Application:
- streamlit run app.py
- Access the Application: Open your browser and go to http://localhost:8501.

Interacting with the App: Enter natural language queries like:

- "Show all available T-shirts in size M."
- "List colors in stock for size L."
- "What’s the quantity of black T-shirts in size S?"
- The app translates these queries to SQL and retrieves accurate inventory information.


## Project Structure

AtliQ-T-Shirts-QA/
- ├── app.py                   # Streamlit application entry point
- ├── langchain_helper.py      # LangChain and SQL configuration
- ├── few_shots.json           # Few-shot examples for the model
- ├── requirements.txt         # List of dependencies
- ├── README.md                # Project documentation
- └── LICENSE                  # License information


## Technologies Used
- LangChain: For handling language model operations.   
- Hugging Face Transformers: NLP model to interpret queries.
- Streamlit: Web-based UI for user interaction.
- MySQL: Database to store inventory data.
- Few-shot Learning: For improved accuracy in SQL query generation.
