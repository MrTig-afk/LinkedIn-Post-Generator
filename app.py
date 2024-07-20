import requests
from bs4 import BeautifulSoup
import openai
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to get the BBC headline
def get_bbc_headline():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('h2')  # Using 'h2' as an example; adjust if needed
    if results:
        news_title = results[0].text.strip()
        return news_title
    else:
        return "No headlines found."

# Configure the Generative AI model with the API key
genai.configure(api_key=os.environ["API_KEY"])

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate a LinkedIn post based on a title
def generate_linkedin_post(title):
    prompt = f"Write a LinkedIn post of about 500 words about : {title}. Please include relevant hashtags and appropriate emojis, but do not include any tips or tricks for improving the post. Do not ask for any relevant experience in the matter"

    response = model.generate_content(prompt)
    return response.text.strip()

# Fetch the headline
headline = get_bbc_headline()

# Generate the LinkedIn post
linkedin_post = generate_linkedin_post(headline)

# Create the Streamlit app

st.header(headline)
st.write(linkedin_post)
