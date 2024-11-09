# streamlit_app.py

from langchain_community.llms import HuggingFaceEndpoint    
import streamlit as st
from langchain.chains import LLMChain
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities.sql_database import SQLDatabase
import json
import os

# Set up environment variables
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ['SERPAPI_API_KEY'] = 'b02fa9624dd946db520ca243c0c95426b40a42f5ddf595bae102e869fe73883e'

# Title and Description
st.title("GenAI SQL LLM Project")
st.markdown("""
A Streamlit app that uses GenAI and LangChain to interact with SQL databases.
Query and retrieve insightful data using SQL queries backed by an LLM.
""")

# Set up database
db_user = "root"
db_password = "ritiksql"
db_host = "localhost"
db_name = "atliq_tshirts"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

# Initialize LLM with HuggingFace endpoint
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=200, temperature=0.7)

# Define a template for prompting SQL queries
query_prompt_template = PromptTemplate(
    input_variables=["query"],
    template="Answer this SQL-based question: {query}"
)

# Initialize SQLDatabaseChain with Prompt
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=query_prompt_template)

# Function for few-shot prompting setup
def setup_few_shot_prompt():
    few_shots = [
        {'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
         'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'"},
        {'Question': "How much is the total price of the inventory for all S-size t-shirts?",
         'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'"},
    ]
    flattened_metadatas = [{k: (json.dumps(v) if isinstance(v, dict) else v) for k, v in shot.items()} for shot in few_shots]

    # Set up embeddings
    embeddings = HuggingFaceEmbeddings(model_name="D:/python programs/All/.venv/Include/GenAI/Equity_Research_tool/models--sentence-transformers--all-mpnet-base-v2/snapshots/9a3225965996d404b775526de6dbfe85d3368642")
    vectorstore = Chroma.from_texts([shot['Question'] for shot in few_shots], embeddings, metadatas=flattened_metadatas)
    return vectorstore

vectorstore = setup_few_shot_prompt()

# Set up Conversation Memory and chain
memory = ConversationBufferMemory()
convo_chain = LLMChain(llm=llm, memory=memory, prompt=query_prompt_template)

# User input section
st.subheader("Enter Your Query")
query = st.text_input("Type a SQL-based question (e.g., 'How many white color Levi's T-shirts do we have?')")

if st.button("Run Query"):
    if query:
        try:
            # Run query on db_chain, passing input as dictionary
            result = db_chain.run({"query": query})
            st.write("**Result:**", result)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query before running.")

# Display SQL schema and information
# st.subheader("Database Schema")
# st.text(db.table_info)

# Display Conversation Memory (Optional)
if st.checkbox("Show Conversation History"):
    st.write(convo_chain.memory.buffer)

# To run: `streamlit run streamlit_app.py`
