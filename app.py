import streamlit as st
from groq import Groq
import os
import pandas as pd
import urllib.parse
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Groq API Key Connection Security
os.environ["GROQ_API_KEY"] = "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"

# Page Configuration - Advanced Google SEO Meta Keywords for Rawalpindi & Islamabad
st.set_page_config(
    page_title="Advocate Rafaqat Abbas | High Court Lawyer Rawalpindi & Islamabad", 
    page_icon="⚖️", 
    layout="centered"
)

# Hidden Search Engine Optimization Tags for Google Bots
st.markdown("""
    <!-- Google Search Engine Meta Keywords -->
    <meta name="description" content="Chamber of Advocate Rafaqat Abbas. Best High Court Lawyer and Legal Consultant in Rawalpindi, Islamabad, and Rawalpindi Bar Association. Specializing in PPC and CPC cases.">
    <meta name="keywords" content="Advocate Rafaqat Abbas, Rafaqat Abbas Lawyer, Best Lawyer in Rawalpindi, High Court Advocate Rawalpindi, Islamabad Lawyer, Rawalpindi Bar Association, Legal Assistant Pakistan">
""", unsafe_allow_html=True)

# Executive Luxury Premium Theme Design (Navy & Gold Accent)
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%); }
    .block-container {
        background: #ffffff; padding: 50px !important; border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); border: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 30px; margin-bottom: 30px;
    }
    @media (max-width: 768px) {
        .block-container { padding: 25px 15px !important; margin-top: 10px; border-radius: 16px; }
        .main-title { font-size: 26px !important; }
        .sub-title { font-size: 11px !important; }
        .location-badge { font-size: 10px !important; }
    }
    .main-title {
        font-family: 'Cinzel', 'Times New Roman', serif; font-size: 42px; font-weight: 900; color: #1E3A8A;
        text-align: center; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 0px;
        background: linear-gradient(to right, #1E3A8A, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .sub-title {
        font-family: 'Montserrat', sans-serif; font-size: 15px; font-weight: 700; color: #B45309;
        text-align: center; margin-top: 5px; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 1.5px;
    }
    .location-badge {
        text-align: center; background: linear-gradient(135deg, #1E3A8A 0%, #0F172A 100%); color: #F59E0B;
        padding: 8px 16px; border-radius: 30px; font-weight: 700; font-size: 12px; width: fit-content;
        margin: 0 auto 25px auto; border: 1px solid #D4AF37; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15); letter-spacing: 0.5px;
    }
    .section-header { font-size: 20px; font-weight: 700; color: #1E2937; border-bottom: 3px solid #D4AF37; padding-bottom: 6px; margin-top: 15px; margin-bottom: 20px; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div { border-radius: 10px !important; border: 2px solid #E2E8F0 !important; }
    .status-pill-green { background-color: #DCFCE7; color: #16A34A; padding: 5px 12px; border-radius: 6px; font-weight: 700; font-size: 11px; margin-right: 5px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>⚖️ LAW LEGACY</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Chamber of Advocate Rafaqat Abbas | High Court Legal Services</p>", unsafe_allow_html=True)
st.markdown("<div class='location-badge'>📍 Serving Clients in Rawalpindi & Islamabad | Rawalpindi Bar Association</div>", unsafe_allow_html=True)
st.markdown("<div style='border-top: 1px solid #E2E8F0; margin-bottom: 20px;'></div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🤖 AI Assistant (PPC/CPC)", "📅 Book Appointment", "🔒 Admin Vault"])

# ========================================================
# ADVANCED DUAL-PDF PROCESSING SYSTEM (PPC + CPC)
# ========================================================
@st.cache_resource
def load_legal_databases():
    all_chunks = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=250)
    if os.path.exists("ppc.pdf"):
        try: all_chunks.extend(text_splitter.split_documents(PyPDFLoader("ppc.pdf").load_and_split()))
        except: pass
    if os.path.exists("cpc.pdf"):
        try: all_chunks.extend(text_splitter.split_documents(PyPDFLoader("cpc.pdf").load_and_split()))
        except: pass
    return all_chunks

chunks = load_legal_databases()

def get_relevant_context(user_query, documents):
    if not documents: return ""
    keywords = user_query.lower().split()
    relevant_text = ""
    for doc in documents:
        if any(kw in doc.page_content.lower() for kw in keywords):
            relevant_text += doc.page_content + "\n\n"
        if len(relevant_text) > 3000: break
    return relevant_text

# TAB 1: AI Chatbot Engine
with tab1:
    st.markdown("<div class='section-header'>Consult AI Legal Intelligence</div>", unsafe_allow_html=True)
    p1 = "<span class='status-pill-green'>✓ PPC BOOK ACTIVE</span>"
    if os.path.exists("cpc.pdf"): p1 += "<span class='status-pill-green'>✓ CPC BOOK ACTIVE</span>"
    st.markdown(p1, unsafe_allow_html=True)
    st.write("")
    
    user_query = st.text_input("Apna Legal Sawal Yahan Darj Karein:")
    run_button = st.button("Run Query ➡️", use_container_width=True)
    
    if user_query and run_button:
        with st.spinner("Analyzing Law Books..."):
            try:
                context_data = get_relevant_context(user_query, chunks)
                client = Groq()
                system_prompt = f"You are an expert AI Legal Assistant for Law Legacy (Advocate Rafaqat Abbas) practicing exclusively in Rawalpindi, Islamabad, and the Rawalpindi Bar Association courts. Answer in clear Roman Urdu. End with: 'Kanooni mashware ke lie is number per rabta krein: 03315605159'."
                
                response = client.chat.completions.create(
                    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_query}],
                    model="openai/gpt-oss-20b"
                )
                st.markdown("<br><b>⚖️ Certified Legal Opinion:</b>", unsafe_allow_html=True)
                
                final_answer = response.choices.message.content
                st.info(final_answer)
                
            except Exception as e: 
                st.error(f"Error: {e}")

# TAB 2: Appointment System
db_file = "appointments.csv"
with tab2:
    st.markdown("<div class='section-header'>Schedule a Private Consultation</div>", unsafe_allow_html=True)
    name = st.text_input("Aap ka Naam:")
    phone = st.text_input("WhatsApp Number:")
    case_type = st.selectbox("Case Category:", ["Civil Matter", "Criminal Matter", "Property Dispute", "Family Law", "Corporate Law"])
    details = st.text_area("Case Summary:")

    if st.button("Submit Request 🔒", use_container_width=True):
        if name and phone:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_data = pd.DataFrame([[current_time, name, phone, case_type, details]], columns=["Time", "Name", "Phone", "Category", "Summary"])
            if not os.path.exists(db_file): new_data.to_csv(db_file, index=False)
            else: new_data.to_csv(db_file, mode='a', header=False, index=False)
                
            st.success("🎉 Details Permanent Save ho gayi hain!")
            
            # FIXED CLEAN WHATSAPP LINK PROTOCOL (No Symbol Bugs)
            t_phone = "923315605159"
            clean_text = f"Salam Law Legacy Team, I want to book an appointment with Advocate Rafaqat Abbas. Name: {name}, Phone: {phone}, Category: {case_type}, Details: {details}"
            encoded_msg = urllib.parse.quote(clean_text)
            whatsapp_url = f"https://wa.me{t_phone}?text={encoded_msg}"
            
            st.link_button("📲 Click Here to Open WhatsApp Chat", whatsapp_url, use_container_width=True)
        else: 
            st.error("Naam aur Phone number lazmi likhein.")

# TAB 3: Admin Dashboard Control Vault
with tab3:
    st.markdown("<div class='section-header'>Advocate Secret Control Dashboard</div>", unsafe_allow_html=True)
    admin_password = st.text_input("Enter Key:", type="password")
    if admin_password == "rafaqat786":
        if os.path.exists(db_file):
            df = pd.read_csv(db_file)
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Export Logs", df.to_csv(index=False).encode('utf-8'), "appointments.csv", "text/csv", use_container_width=True)
        else: 
            st.info("No logs captured yet.")
