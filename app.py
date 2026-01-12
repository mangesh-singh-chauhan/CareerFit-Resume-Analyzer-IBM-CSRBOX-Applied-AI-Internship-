import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf
import json
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="CareerFit AI", layout="wide")

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🚀 CareerFit AI Analyst")
st.markdown("### SDG 8: Decent Work & Economic Growth")

# Sidebar
with st.sidebar:
    st.header("🔑 Authentication")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    if api_key:
        genai.configure(api_key=api_key)
        st.success("System Ready")
    st.markdown("---")
    st.info("💡 **Tip:** Analysis uses Gemini 2.5 Flash for high-speed recruiting insights.")

# Main Inputs
col1, col2 = st.columns(2)
with col1:
    st.subheader("1️⃣ Target Job Description")
    jd = st.text_area("Paste the JD here:", height=300)
with col2:
    st.subheader("2️⃣ Your Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type="pdf")

# PDF Extraction
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Analysis Button
if st.button("Analyze Resume Fit"):
    if not api_key or not jd or not uploaded_file:
        st.error("⚠️ Please fill all fields.")
    else:
        with st.spinner("🤖 Analyzing profile..."):
            try:
                text = input_pdf_text(uploaded_file)
                
                # Strict Prompt
                input_prompt = f"""
                Act as a strict HR Analyst.
                RESUME: {text}
                JOB DESCRIPTION: {jd}

                Output valid JSON:
                {{
                    "JD_Match": "percentage string (e.g. '85%')",
                    "MissingKeywords": ["keyword1", "keyword2"],
                    "ProfileSummary": "Concise summary.",
                    "ImprovementTips": ["tip1", "tip2"]
                }}
                """
                
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(input_prompt)
                
                # Parsing
                response_text = response.text.replace("```json", "").replace("```", "").strip()
                data = json.loads(response_text)
                
                # Extract Number from String (e.g., "75%" -> 75)
                # Handle cases where AI might give just a number
                raw_match = str(data['JD_Match']).replace("%", "")
                match_score = int(raw_match)

                # --- VISUALIZATION LAYER ---
                st.markdown("---")
                st.header("📊 Analysis Report")
                
                col_a, col_b = st.columns([1, 2])
                
                with col_a:
                    # GAUGE CHART
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = match_score,
                        title = {'text': "Match Score"},
                        gauge = {
                            'axis': {'range': [0, 100]},
                            'bar': {'color': "#007bff"},
                            'steps' : [
                                {'range': [0, 50], 'color': "#ffebee"}, # Red zone
                                {'range': [50, 80], 'color': "#e3f2fd"}, # Blue zone
                                {'range': [80, 100], 'color': "#e8f5e9"} # Green zone
                            ],
                        }
                    ))
                    st.plotly_chart(fig, use_container_width=True)
                
                with col_b:
                    st.subheader("📝 Summary")
                    st.info(data['ProfileSummary'])
                    
                    st.subheader("⚠️ Missing Skills")
                    # Display missing skills as nice tags
                    st.write(", ".join([f"`{k}`" for k in data['MissingKeywords']]))
                    
                    st.subheader("💡 Recommendations")
                    for tip in data['ImprovementTips']:
                        st.write(f"- {tip}")

            except Exception as e:
                st.error(f"Error: {e}")