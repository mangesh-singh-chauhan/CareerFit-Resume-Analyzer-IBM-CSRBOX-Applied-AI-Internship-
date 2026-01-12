# 🚀 CareerFit AI: Smart Resume Analyst

### 🎯 Project Overview
**CareerFit AI** is an intelligent career assistant designed to bridge the gap between job seekers and employment opportunities (aligned with **SDG 8: Decent Work & Economic Growth**).

Using Google's **Gemini 2.5 Flash** model, this tool acts as an automated Technical Recruiter. It scans a candidate's PDF resume against a target job description, performs a semantic gap analysis, and provides a quantitative "Match Score" along with actionable upskilling advice.

### ✨ Key Features
* **📄 PDF Resume Parsing:** Extracts unstructured text from PDF documents using `PyPDF2`.
* **🤖 AI Gap Analysis:** Uses Gemini Pro/Flash to compare skills, experience, and context.
* **📊 Visual Dashboard:** Displays a real-time "Match Score" gauge chart using `Plotly`.
* **💡 Smart Feedback:** Identifies missing keywords and suggests specific improvements to beat Applicant Tracking Systems (ATS).

### 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Frontend:** Streamlit
* **AI Model:** Google Gemini (Generative AI)
* **Visualization:** Plotly Graph Objects
* **Data Processing:** PyPDF2, JSON

### ⚙️ Installation & Setup

1.  **Clone the repository (or download files):**
    Ensure `app.py`, `requirements.txt` are in the same folder.

2.  **Install Dependencies:**
    Open your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Get a Gemini API Key:**
    * Visit [Google AI Studio](https://aistudio.google.com/) to get your free key.

4.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

### 📂 File Structure
* `app.py`: The main application logic and UI.
* `requirements.txt`: List of required Python libraries.
* `README.md`: Project documentation.

---
*Developed by Mangesh Singh Chauhan for the IBM SkillsBuild Applied AI Challenge.*