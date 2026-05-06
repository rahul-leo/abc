import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Modern Python App", page_icon="🚀", layout="centered")

# Custom CSS for Premium Look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    /* Global styles */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
        font-family: 'Outfit', sans-serif;
    }

    /* Glassmorphism container */
    .stApp {
        background: transparent;
    }
    
    .block-container {
        padding-top: 5rem;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 3rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        text-align: center;
        animation: slideUp 0.8s ease-out;
    }

    .icon-header {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        animation: float 3s ease-in-out infinite;
        display: block;
        text-align: center;
    }

    h1 {
        font-weight: 600;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem;
        background: linear-gradient(to right, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }

    .subtitle {
        color: #94a3b8;
        margin-bottom: 2rem;
        font-weight: 300;
        text-align: center;
        font-size: 1.1rem;
    }

    .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(34, 197, 94, 0.1);
        color: #4ade80;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-size: 0.875rem;
        margin: 0 auto 2.5rem auto;
        width: fit-content;
    }

    .dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        box-shadow: 0 0 10px #22c55e;
        animation: pulse 2s infinite;
    }

    /* Streamlit Button override */
    .stButton > button {
        background: #6366f1 !important;
        color: white !important;
        border: none !important;
        padding: 0.75rem 2.5rem !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.3) !important;
    }

    .stButton > button:hover {
        background: #4f46e5 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.4) !important;
    }

    .response-text {
        margin-top: 2.5rem;
        font-size: 1.25rem;
        font-weight: 400;
        color: #f8fafc;
        text-align: center;
        animation: fadeIn 0.5s ease-in;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.5); opacity: 0.5; }
        100% { transform: scale(1); opacity: 1; }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Main UI Structure
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<span class="icon-header">🚀</span>', unsafe_allow_html=True)
st.markdown('<h1>Python Backend Integration</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Streamlit + Premium Design</p>', unsafe_allow_html=True)

st.markdown("""
<div class="status-indicator">
    <div class="dot"></div> Online & Ready
</div>
""", unsafe_allow_html=True)

if st.button("Fetch Data"):
    with st.spinner("Fetching data..."):
        time.sleep(0.5) # Simulate API delay
        st.markdown('<p class="response-text">Hello from the Python (Streamlit) Backend! ✨</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="response-text" style="color: #94a3b8;">Click the button to see the magic...</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
