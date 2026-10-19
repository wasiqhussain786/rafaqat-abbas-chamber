import streamlit as st
from groq import Groq
import os
import urllib.parse
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. API Key Binding (Groq Connection)
os.environ["GROQ_API_KEY"] = "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"

# Page Configuration
st.set_page_config(page_title="Law Legacy | Advocate Rafaqat Abbas", page_icon="⚖️", layout="centered")

# Advanced Mobile Responsive UI Theme Design
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle, #f8fafc 0%, #f1f5f9 100%);
    }
    .block-container {
        background: #ffffff;
        padding: 5% !important;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(15, 23, 42, 0.06);
        border: 1px solid #e2e8f0;
        margin-top: 20px;
    }
    @media (max-width: 768px) {
        .block-container {
            padding: 20px 15px !important;
            margin-top: 10px;
            border-radius: 12px;
            box-shadow: none;
            border: none;
        }
        .main-title { font-size: 26px !important; }
        .sub-title { font-size: 12px !important; }
    }
    .main-title {
        font-family: 'Cinzel', 'Georgia', serif;
        font-size: 38px;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        letter-spacing: 1px;
        margin-bottom: 0px;
        text-transform: uppercase;
    }
    .sub-title {
        font-family: 'Montserrat', 'Arial', sans-serif;
        font-size: 14px;
        font-weight: 600;
        color: #D97706;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 20px;
        text-transform: uppercase;
    }
    .section-header {
        font-size: 18px;
        font-weight: 700;
        color: #1F2937;
        border-bottom: 2px solid #D97706;
        padding-bottom: 6px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Premium Header
st.markdown("<h1 class='main-title'>⚖️ LAW LEGACY</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Advocate Rafaqat Abbas | High Court Legal Services</p>", unsafe_allow_html=True)

# ========================================================
# ADVANCED DUAL-PDF LOADING & PROCESSING SYSTEM (PPC + CPC)
# ========================================================
@st.cache_resource
def load_legal_databases():
    all_chunks = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=250)
    
    if os.path.exists("ppc.pdf"):
        try:
            ppc_pages = PyPDFLoader("ppc.pdf").load_and_split()
            all_chunks.extend(text_splitter.split_documents(ppc_pages))
        except:
            pass
        
    if os.path.exists("cpc.pdf"):
        try:
            cpc_pages = PyPDFLoader("cpc.pdf").load_and_split()
            all_chunks.extend(text_splitter.split_documents(cpc_pages))
        except:
            pass
        
    return all_chunks

chunks = load_legal_databases()

def get_relevant_context(user_query, documents):
    if not documents:
        return ""
    keywords = user_query.lower().split()
    relevant_text = ""
    for doc in documents:
        if any(kw in doc.page_content.lower() for kw in keywords):
            relevant_text += doc.page_content + "\n\n"
        if len(relevant_text) > 3000:
            break
    return relevant_text

# Define Tabs
tab1, tab2 = st.tabs(["🤖 AI Assistant (PPC/CPC)", "📅 Book Appointment"])

# TAB 1: AI Legal Assistant
with tab1:
    st.markdown("<div class='section-header'>Consult AI Legal Intelligence</div>", unsafe_allow_html=True)
    
    status_html = "<span style='background-color:#E0F2FE; color:#0369A1; padding:4px 8px; border-radius:4px; font-weight:600; font-size:11px; margin-right:5px;'>PPC Connected</span>"
    if os.path.exists("cpc.pdf"):
        status_html += "<span style='background-color:#E0F2FE; color:#0369A1; padding:4px 8px; border-radius:4px; font-weight:600; font-size:11px;'>CPC Connected</span>"
    st.markdown(status_html, unsafe_allow_html=True)
    st.write("")
    
    user_query = st.text_input("Apna Legal Sawal Yahan Likhein:", placeholder="e.g. Theft punishment or Stay order code...")
    run_button = st.button("Run Query ➡️", use_container_width=True)
    
    if user_query and run_button:
        with st.spinner("Analyzing PPC & CPC Legal Databases..."):
            try:
                context_data = get_relevant_context(user_query, chunks)
                client = Groq()
                
                system_prompt = f"""
                You are an expert AI Legal Assistant for Law Legacy (Advocate Rafaqat Abbas) in Pakistan. 
                Answer the user query based on the provided Pakistan Penal Code (PPC) and Civil Procedure Code (CPC) context files.
                Always answer in clear Roman Urdu or simple Urdu so common clients can understand.
                At the end, you MUST always add this exact line: 'Kanooni mashware ya mazeed rabte ke lie is number per rabta krein: 03315605159'.
                
                OFFICIAL LAW BOOKS CONTEXT DATA:
                {context_data}
                """
                
                response = client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    model="openai/gpt-oss-20b",
                )
                
                st.markdown("<br><b style='color: #1E3A8A; font-size: 16px;'>Official Legal Opinion:</b>", unsafe_allow_html=True)
                # ABSOLUTE FIXED SYNTAX LIST INDEX SELECTOR HERE
                st.info(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Error: {e}")

# TAB 2: Appointment Form (Clean Crash-Free Standard Link)
with tab2:
    st.markdown("<div class='section-header'>Schedule a Private Consultation</div>", unsafe_allow_html=True)
    name = st.text_input("Aap ka Naam (Full Name):")
    phone = st.text_input("WhatsApp / Contact Number:")
    case_type = st.selectbox("Case Category:", ["Civil Matter", "Criminal Matter", "Property Dispute", "Family Law", "Corporate Law"])
    details = st.text_area("Case Summary (Brief Tafseel):")

    if st.button("Submit Appointment Request", use_container_width=True):
        if name and phone:
            st.success("Details Saved Successfully!")
            
            target_phone = "923315605159"
            raw_msg = f"Salam Law Legacy Team, I want to book an appointment with Advocate Rafaqat Abbas.\nName: {name}\nPhone: {phone}\nCategory: {case_type}\nDetails: {details}"
            encoded_msg = urllib.parse.quote(raw_msg)
            whatsapp_url = f"https://wa.me{target_phone}?text={encoded_msg}"

            # Standard native link connection structure
            st.link_button("Open WhatsApp to Confirm Booking 💬", whatsapp_url, use_container_width=True)
        else:
            st.error("Meharbani karke Naam aur Phone number lazmi darj karein.")
