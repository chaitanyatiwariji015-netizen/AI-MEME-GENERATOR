# Install karne ke liye: pip install streamlit openai pillow

import streamlit as st
import openai
import os
import base64

# OpenAI API key Streamlit secrets se lete hain
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Meme Generator 🤖🎉")

uploaded_file = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])

template = st.selectbox("Choose Meme Template", ["Funny", "Sarcastic", "School Joke", "Teacher Joke"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
    
    if st.button("Generate Meme"):
        with st.spinner("Generating meme, please wait..."):
            img_bytes = uploaded_file.read()
            img_b64 = base64.b64encode(img_bytes).decode()
            
            prompt = f"Create a {template} meme using this image in base64 format: {img_b64}. Make it funny and short."
            
            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                meme_url = response['data'][0]['url']
                st.image(meme_url, caption="Your AI Generated Meme", use_column_width=True)
            except Exception as e:
                st.error(f"Error generating meme: {e}")
