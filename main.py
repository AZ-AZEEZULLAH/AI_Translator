# 📦 Importing necessary libraries
import os  # for accessing environment variables like API keys
import streamlit as st  # for creating the web app
from dotenv import load_dotenv  # to load environment variables from .env file
from openai import OpenAI  # not used in this code – can be removed if unnecessary
import google.generativeai as genai  # type: ignore # Gemini's generative AI library

# 📥 Load environment variables from the .env file
load_dotenv()

# 🔑 Get your Gemini API key from environment
api_key = os.getenv("GEMINI_API_KEY")

# 🛠️ Configure the Gemini AI with your API key
genai.configure(api_key=api_key)

# 🌍 List of available languages for translation
language = [
    "Urdu", "Sindhi", "Bengali", "Chinese", "English", "Greek", "English", "Russian", "Hindi",
    "Vietnamese", "Arabic", "Turkish", "Swedish", "Hebrew", "Romanian", "Finnnish",
    "Balochi", "Punjabi", "Siraki", "Pashto", "Thai"
]

# 🧱 Set page configuration for the Streamlit app
st.set_page_config(
    page_title="Translator by 💥Azeezullah_Noohpoto💥",
    layout="centered"
)

# 🖼️ Title and description of the app
st.title("🌐 AI Translator")
st.write("Created by **©Azeezullah** - Translate your English text into various languages using AI.")

# 📝 Text area for user to enter English text
text = st.text_area("Enter English text to translate:", height=150)

# 🌐 Dropdown to select a language from the list
selected_lang = st.selectbox("Choose language to translate to:", language)

# 🔘 Button to trigger translation
btn = st.button("Translate")

# ⚙️ When the button is clicked and there's text
if btn and text:
    try:
        # 🧠 Load the Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # ✍️ Create the prompt for translation
        prompt = f"Translate the following text to {selected_lang}:\n\n{text}"

        # 🔄 Send the prompt to Gemini and get the response
        response = model.generate_content(prompt)

        # ✅ Display the translated text
        st.success(f"✅ Translated to {selected_lang}")
        st.markdown(f"**{response.text}**")

    except Exception as e:
        # ❌ If something goes wrong, show the error
        st.error(f"❎ Error: {str(e)}")
