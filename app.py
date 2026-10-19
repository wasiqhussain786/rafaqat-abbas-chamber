import streamlit as st
from groq import Groq
import os
import urllib.parse

# 1. API Key Binding (Groq se connect karne ke liye zaroori hai)
os.environ["GROQ_API_KEY"] = "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"

# Page Configuration
st.set_page_config(page_title="Law Legacy | Advocate Rafaqat Abbas", page_icon="⚖️", layout="centered")

# Custom Premium Header Styling
st.markdown("""
    <style>
    .main-title {
        font-family: 'Cinzel', 'Georgia', serif;
        font-size: 40px;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 0px;
        text-transform: uppercase;
    }
    .sub-title {
        font-family: 'Montserrat', 'Arial', sans-serif;
        font-size: 15px;
        font-weight: 600;
        color: #D97706;
        text-align: center;
        letter-spacing: 1px;
        margin-top: 5px;
        margin-bottom: 25px;
        text-transform: uppercase;
    }
    .section-header {
        font-size: 20px;
        font-weight: 700;
        color: #1F2937;
        border-bottom: 2px solid #D97706;
        padding-bottom: 6px;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Premium Header
st.markdown("<h1 class='main-title'>⚖️ LAW LEGACY</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Advocate Rafaqat Abbas | High Court Legal Services</p>", unsafe_allow_html=True)

# Define Tabs
tab1, tab2 = st.tabs(["🤖 AI Legal Assistant (PPC)", "📅 Book Appointment"])

# TAB 1: AI Legal Assistant
with tab1:
    st.markdown("<div class='section-header'>Consult AI Legal Intelligence</div>", unsafe_allow_html=True)
    user_query = st.text_input("Apna Legal Sawal Yahan Likhein:", placeholder="e.g. Theft punishment under PPC...")
    if user_query:
        with st.spinner("Analyzing PPC Legal Database..."):
            try:
                client = Groq()
                # 2. System prompt updated to enforce Roman Urdu and your phone number entry
                system_prompt = "You are an expert AI Legal Assistant for Law Legacy (Advocate Rafaqat Abbas) in Pakistan. Answer the user query based on Pakistan Penal Code (PPC) in clear Roman Urdu. At the end, you MUST always add this exact line: 'Kanooni mashware ya mazeed rabte ke lie is number per rabta krein: 03315605159'."
                
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    model="openai/gpt-oss-20b",  # 3. Model fixed to stable active production version
                )
                
                st.markdown("<br><b style='color: #1E3A8A; font-size: 18px;'>Official Legal Opinion:</b>", unsafe_allow_html=True)
                # 4. Correct response syntax choice extraction applied
                st.info(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")

# TAB 2: Appointment Form
with tab2:
    st.markdown("<div class='section-header'>Schedule a Private Consultation</div>", unsafe_allow_html=True)
    name = st.text_input("Aap ka Naam (Full Name):")
    phone = st.text_input("WhatsApp / Contact Number:")
    case_type = st.selectbox("Case Category:", ["Civil Matter", "Criminal Matter", "Property Dispute", "Family Law", "Corporate Law"])
    details = st.text_area("Case Summary (Brief Tafseel):")

    if st.button("Submit Appointment Request"):
        if name and phone:
            target_phone = "923315605159"
            whatsapp_msg = f"Salam Law Legacy Team, I want to book an appointment with Advocate Rafaqat Abbas.\nName: {name}\nPhone: {phone}\nCategory: {case_type}\nDetails: {details}"
            encoded_msg = urllib.parse.quote(whatsapp_msg)
            whatsapp_url = f"https://wa.me/{target_phone}?text={encoded_msg}"

            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color:#1E3A8A; color:white; padding:12px 24px; border:none; border-radius:8px; font-weight:bold; cursor:pointer; width:100%; font-size:16px;">Confirm Booking via WhatsApp 💬</button></a>', unsafe_allow_html=True)
        else:
            st.error("Meharbani karke Naam aur Phone number lazmi darj karein.")
