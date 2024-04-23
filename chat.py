# pycharm

from dotenv import load_dotenv
import streamlit as st
import os
import pymysql
import google.generativeai as genai

# Load environment variables
load_dotenv()
print("DB_PORT:", os.getenv("port"))
print("DB_HOST:", os.getenv("host"))

# Database connection configuration
db_config = {
    "host": os.getenv("host"),
    "port": int(os.getenv("port")),
    "database": os.getenv("database"),
    "user": os.getenv("username"),
    "password": os.getenv("password"),
}

# Establish a connection to the database
connection = pymysql.connect(**db_config)

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Set page configuration
st.set_page_config(page_title="MineMentor", page_icon="🚀", layout="wide")

# Main content
st.header("Welcome to MineMentor")
st.subheader("Transforming Mining with AI for Enhanced Efficiency and Informed Decision-Making")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input and submission
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    if response:
        # Add user query and response to the MySQL database
        with connection.cursor() as cursor:
            for chunk in response:
                user_query = input
                bot_response = chunk.text
                sql = "INSERT INTO response.user (user_prompt, bot_response) VALUES (%s, %s)"
                cursor.execute(sql, (user_query, bot_response))
            connection.commit()

        # Add user query and response to session state chat history
        st.session_state.chat_history.append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state.chat_history.append(("Bot", chunk.text))

# Display chat history
st.subheader("The Chat History is")

# Ensure that 'chat_history' is initialized before trying to access it
if 'chat_history' in st.session_state:
    for role, text in st.session_state.chat_history:
        st.write(f"{role}: {text}")

# Close the database connection when done
connection.close()
