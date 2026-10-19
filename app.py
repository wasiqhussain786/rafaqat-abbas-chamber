import streamlit as st
from groq import Groq
import urllib.parse

# Page Configuration
st.set_page_config(page_title="Law Legacy", page_icon="⚖️", layout="centered")

# Main Title & Subheader
st.title("LAW LEGACY")
st.subheader("Advocate Rafaqat Abbas | High Court Legal Services")

# Define Tabs
tab1, tab2 = st.tabs(["AI Legal Assistant", "Book Appointment"])

# TAB 1: AI Legal Assistant
with tab1:
    user_query = st.text_input("Apna Legal Sawal Yahan Likhein:")
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
                    model="llama-3.1-70b-versatile",
                )
                st.info(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")

# TAB 2: Appointment Form Connecting to WhatsApp
with tab2:
    st.subheader("Book Your Appointment Slot")
    name = st.text_input("Aap ka Naam (Full Name):")
    phone = st.text_input("WhatsApp / Contact Number:")
    case_type = st.selectbox("Case Category:", ["Civil Matter", "Criminal Matter", "Property Dispute", "Family Law", "Corporate Law"])
    details = st.text_area("Case Summary (Brief Tafseel):")

    if st.button("Submit Appointment Request"):
        if name and phone:
            # Message router payload
            target_phone = "923315605159"
            whatsapp_msg = f"Salam Law Legacy Team, I want to book an appointment with Advocate Rafaqat Abbas.\nName: {name}\nPhone: {phone}\nCategory: {case_type}\nDetails: {details}"
            encoded_msg = urllib.parse.quote(whatsapp_msg)
            whatsapp_url = f"https://wa.me/{target_phone}?text={encoded_msg}"

            # Link button redirect
            st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">Confirm Booking via WhatsApp</button></a>', unsafe_allow_html=True)
        else:
            st.error("Meharbani karke Naam aur Phone number lazmi darj karein.")
