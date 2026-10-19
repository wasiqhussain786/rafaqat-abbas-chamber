import streamlit as st
import os
import urllib.parse
from groq import Groq

# 1. API Key Binding
os.environ["GROQ_API_KEY"] = "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"
st.set_page_config(page_title="Law Legacy - AI Legal Portal", page_icon="⚖️", layout="centered")

# 2. Executive Corporate Theme Design
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #f8fafc 0%, #f1f5f9 100%);
    }
    .block-container {
        background: #ffffff;
        padding: 50px !important;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.06);
        border: 1px solid #e2e8f0;
        margin-top: 40px;
    }
    h1 {
        font-family: 'Times New Roman', Times, serif;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# Office Identity Brand Headers
st.markdown("<h1 style='text-align: center; color: #1E3A8A; margin-bottom: 0px;'>LAW LEGACY</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B; font-size: 16px; font-weight: 500; margin-top: 5px; letter-spacing: 1px;'>HIGH COURT LEGAL CONSULTANT & AI ASSISTANCE PORTAL</p>", unsafe_allow_html=True)
st.markdown("<div style='border-top: 3px double #D4AF37; width: 60%; margin: 15px auto 30px auto;'></div>", unsafe_allow_html=Tru
# TAB 1: Core AI Chatbot
with tab1:
    st.subheader("Ask about Pakistan Penal Code (PPC)")
    user_query = st.text_input("Apna legal masla ya kanoon yahan darj karein:")
    
    if user_query:
        with st.spinner("Analyzing PPC Legal Database..."):
            try:
client = Groq()
        system_prompt = "You are an expert AI Legal Assistant for Law Legacy (Advocate Rafaqat Abbas) in Pakistan. Answer the user query based on Pakistan Penal Code (PPC)."
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            model="llama-3.3-70b-versatile",
        )
        st.markdown("<br><b style='color: #1E3A8A; font-size: 18px;'>Official Legal Response:</b>", unsafe_allow_html=True)
        st.info(response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {e}")

# TAB 2: Appointment Form Connecting to WhatsApp
with tab2:
    st.subheader("Book Your Appointment Slot")
    name = st.text_input("Aap ka Naam (Full Name):")
    phone = st.text_input("WhatsApp / Contact Number:")
    case_type = st.selectbox("Case Category:", ["Civil Matter", "Criminal Matter", "Property Dispute", "Family Law", "Corporate/Tax", "Other"])
    details = st.text_area("Case Summary (Brief Tafseel):")
    
    if st.button("Submit Appointment Request"):
        if name and phone:
            st.success("Details Saved! Click the button below to complete registration.")
            
            # Message router payload
        target_phone = "923315605159"
        whatsapp_msg = f"Salam Law Legacy Team, I want to book an appointment with Advocate Rafaqat Abbas.\n\nName: {name}\nPhone: {phone}\nCategory: {case_type}\nDetails: {details}"
        encoded_msg = urllib.parse.quote(whatsapp_msg)
        whatsapp_url = f"https://wa.me/{target_phone}?text={encoded_msg}"
        # Link button redirect
        st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">Confirm Booking via WhatsApp</button></a>', unsafe_allow_html=True)
    else:
        st.error("Meharbani karke Naam aur Phone number lazmi darj karein.")`
