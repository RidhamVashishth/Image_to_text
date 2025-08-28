import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import google.generativeai as genai

# --- Configuration ---
load_dotenv()
# Add a check to ensure the API key is loaded
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
    st.stop()

genai.configure(api_key=api_key)
# Use the recommended model
model = genai.GenerativeModel('gemini-1.5-flash')

# --- App Front-End ---
st.header('🖼️ AI Image-to-Text Converter 📈', divider=True)

# Use columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('📝 Enter Your Prompt')
    prompt = st.text_area(label='Enter campaign details or a question about the image:', height=150)

with col2:
    st.subheader('🖼️ Upload Your Image')
    uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
st.info("Simply upload an image and provide a prompt to generate creative text, or just upload an image for a detailed description.")
# --- Image Display & Logic ---
image = None
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

def get_llm_response(prompt_text, image_data):
    """Generates a response from the Gemini model."""
    # The model needs the image data in its content list
    content = []
    if prompt_text:
        content.append(prompt_text)
    if image_data:
        content.append(image_data)
    
    # Generate content
    response = model.generate_content(content)
    return response.text

# --- Submission Logic ---
submit = st.button('Generate Campaign Text')

if submit:
    # Validate that at least one input is provided
    if not prompt and image is None:
        st.error("Please provide a prompt or upload an image.")
    else:
        with st.spinner("🤖 AI is thinking..."):
            try:
                response = get_llm_response(prompt, image)
                st.subheader(':orange[Generated Response]')
                st.markdown(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
