# 📦 Import required libraries
import os  # 🗂️ Used to access environment variables
from dotenv import load_dotenv  # 🔐 Load variables from a .env file
import google.generativeai as genai  # 🤖 Gemini AI (Google's language model)

# 📥 Load API key from the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # 🔑 Get Gemini API Key

# 🚫 If API key is missing, show error and exit
if not api_key:
    print("❌ Error: GEMINI_API_KEY is not set in the env file!.")
    exit()

# 🔧 Configure Gemini AI with the API key
genai.configure(api_key=api_key)

# 🌍 List of supported languages
languages = [
    "Urdu", "Sindhi", "Bengali", "Chinese", "English", "Greek", "Russian", "Hindi",
    "Vietnamese", "Arabic", "Turkish", "Swedish", "Hebrew", "Romanian", "Finnish",
    "Balochi", "Punjabi", "Siraki", "Pashto", "Thai"
]

# ✏️ Get user input text to translate
text = input("📝 Enter English or Urdu text to translate: ")

# 📋 Display available languages
print("\n🌐 Available languages:")
print("\n".join(languages))

# 🌐 Ask user to choose a target translation language
lang = input("\n🈯 Choose language to translate to: ")

try:
    # 🤖 Load the Gemini AI model
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    # 🧠 Create a smart prompt for translation
    prompt = f"""
    You are a professional translator assistant. Detect whether the input is in English or Urdu,
    and then translate the text to {lang}:

    Text: {text}
    """
    
    # 🧾 Generate the translation using the model
    response = model.generate_content(prompt)
    
    # 📤 Display the translated text
    print(f"\n🌍 Translated to {lang}:\n{response.text}")

except Exception as e:
    # ⚠️ Handle any errors
    print(f"❗Error: {str(e)}")
