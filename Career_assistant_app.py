import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# ──────────── Setup ─────────────
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "placement_tier_classifier.pkl"
SCALER_PATH = BASE_DIR / "placement_scaler.pkl"
PROF_DB = BASE_DIR / "Enhanced_Professor_Database.csv"
STUDENT_XLSX = BASE_DIR / "Student_Data_With_Extras.xlsx"

clf = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

st.set_page_config(
    page_title="CareerPilot AI - Professional Career Guidance",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ──────────── Enhanced Custom CSS ─────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

/* Dark Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29, #1a1a2e);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    25% { background-position: 50% 100%; }
    50% { background-position: 100% 50%; }
    75% { background-position: 50% 0%; }
    100% { background-position: 0% 50%; }
}

/* Floating Particles Effect */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.15) 2px, transparent 2px),
        radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.15) 2px, transparent 2px),
        radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.1) 1px, transparent 1px),
        radial-gradient(circle at 30% 70%, rgba(168, 85, 247, 0.1) 1px, transparent 1px);
    background-size: 300px 300px, 400px 400px, 250px 250px, 350px 350px;
    animation: particleFloat 25s linear infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes particleFloat {
    0% { background-position: 0 0, 0 0, 0 0, 0 0; }
    100% { background-position: 300px 300px, -400px 400px, 250px -250px, -350px 350px; }
}

/* Glowing Orbs Effect */
.stApp::after {
    content: '';
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: 
        radial-gradient(circle at 20% 30%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 70%, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
    animation: orbFloat 30s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes orbFloat {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(30px, -30px) rotate(120deg); }
    66% { transform: translate(-30px, 30px) rotate(240deg); }
}

/* Navigation Bar */
.navbar {
    background: rgba(15, 12, 41, 0.8);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 1.5rem 3rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.5);
    border: 1px solid rgba(99, 102, 241, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    z-index: 10;
}

.navbar-brand {
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: flex;
    align-items: center;
    gap: 0.8rem;
    text-shadow: 0 0 30px rgba(99, 102, 241, 0.5);
    animation: titleGlow 3s ease-in-out infinite;
    letter-spacing: 1px;
}

@keyframes titleGlow {
    0%, 100% { filter: brightness(1); }
    50% { filter: brightness(1.3); }
}

/* Main Content Container */
.main {
    background: rgba(15, 12, 41, 0.6);
    border-radius: 25px;
    padding: 3rem;
    box-shadow: 0 15px 50px 0 rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(99, 102, 241, 0.2);
    margin: 1rem auto;
    max-width: 1400px;
    position: relative;
    z-index: 1;
}

/* Headings */
h1 {
    color: #FFFFFF !important;
    text-align: center;
    font-size: 3.8rem !important;
    font-weight: 800 !important;
    margin-bottom: 0.5rem !important;
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 0 40px rgba(99, 102, 241, 0.4);
    animation: textPulse 3s ease-in-out infinite;
    letter-spacing: 2px;
}

@keyframes textPulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.02); }
}

h2 {
    color: #FFFFFF !important;
    text-align: center;
    font-size: 2.4rem !important;
    font-weight: 700 !important;
    margin: 2rem 0 1.5rem 0 !important;
    text-shadow: 0 0 20px rgba(139, 92, 246, 0.5);
}

h3 {
    color: #c7d2fe !important;
    font-size: 1.6rem !important;
    font-weight: 600 !important;
    margin: 1.5rem 0 1rem 0 !important;
}

h4 {
    color: #e0e7ff !important;
    font-weight: 500 !important;
    font-size: 1.3rem !important;
    margin-bottom: 2rem !important;
    text-align: center;
}

/* Paragraph text */
p, div {
    font-size: 1.1rem;
    line-height: 1.8;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
    color: white;
    font-weight: 700;
    font-size: 1.2rem;
    border: none;
    border-radius: 15px;
    padding: 1rem 2.5rem;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    box-shadow: 0 8px 25px 0 rgba(99, 102, 241, 0.5);
    width: 100%;
    margin-top: 1.5rem;
    letter-spacing: 1px;
    position: relative;
    overflow: hidden;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.stButton > button:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 15px 40px 0 rgba(99, 102, 241, 0.8);
    background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 50%, #6366f1 100%);
}

.stButton > button:active {
    transform: translateY(-2px) scale(0.98);
}

.stButton > button:active::before {
    width: 300px;
    height: 300px;
}

/* Click Ripple Effect */
@keyframes ripple {
    0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -50%) scale(4);
        opacity: 0;
    }
}

/* Input Elements */
.stSlider label, .stSelectbox label {
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 1.15rem !important;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    margin-bottom: 0.8rem !important;
}

.stSlider > div > div > div {
    background: rgba(99, 102, 241, 0.3);
}

.stSlider [role="slider"] {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    box-shadow: 0 0 15px rgba(99, 102, 241, 0.8);
}

.stSelectbox > div > div {
    background: rgba(15, 12, 41, 0.8);
    border-radius: 12px;
    border: 2px solid rgba(99, 102, 241, 0.4);
    color: white;
    font-size: 1.1rem;
    font-weight: 500;
}

.stSelectbox > div > div:hover {
    border-color: rgba(139, 92, 246, 0.6);
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.4);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 2rem;
    background: rgba(15, 12, 41, 0.7);
    border-radius: 18px;
    padding: 0.8rem;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #c7d2fe;
    font-weight: 700;
    font-size: 1.3rem;
    border-radius: 12px;
    padding: 1rem 2.5rem;
    transition: all 0.3s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    background: rgba(99, 102, 241, 0.2);
    color: white;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    color: white !important;
    box-shadow: 0 5px 20px rgba(99, 102, 241, 0.6);
}

/* DataFrame Styling */
.dataframe {
    border-radius: 15px !important;
    overflow: hidden !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
    font-size: 1.05rem !important;
}

.dataframe thead tr th {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
}

.dataframe tbody tr {
    background: rgba(15, 12, 41, 0.8) !important;
    color: white !important;
}

.dataframe tbody tr:hover {
    background: rgba(99, 102, 241, 0.3) !important;
}

/* Cards */
.card {
    background: rgba(15, 12, 41, 0.7);
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(99, 102, 241, 0.3);
    transition: all 0.4s ease;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(99, 102, 241, 0.4);
    border-color: rgba(139, 92, 246, 0.5);
}

/* Footer */
.footer {
    background: rgba(15, 12, 41, 0.8);
    backdrop-filter: blur(25px);
    border-radius: 25px;
    padding: 3rem 2rem;
    margin-top: 4rem;
    box-shadow: 0 15px 50px 0 rgba(0, 0, 0, 0.6);
    border: 1px solid rgba(99, 102, 241, 0.3);
    text-align: center;
}

.footer-content {
    color: white;
    margin-bottom: 2rem;
}

.footer-title {
    font-size: 2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1.5rem;
    letter-spacing: 1px;
}

.footer-description {
    color: #c7d2fe;
    font-size: 1.15rem;
    line-height: 1.8;
    margin-bottom: 2rem;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}

.social-links {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.social-link {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    color: white;
    text-decoration: none;
    padding: 0.9rem 1.8rem;
    background: rgba(99, 102, 241, 0.2);
    border-radius: 50px;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    font-weight: 600;
    font-size: 1.1rem;
    border: 2px solid rgba(99, 102, 241, 0.3);
    position: relative;
    overflow: hidden;
}

.social-link::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.2);
    transform: translate(-50%, -50%);
    transition: width 0.5s, height 0.5s;
}

.social-link:hover {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%);
    transform: translateY(-5px) scale(1.05);
    box-shadow: 0 10px 30px rgba(99, 102, 241, 0.6);
    border-color: transparent;
}

.social-link:hover::before {
    width: 300px;
    height: 300px;
}

.social-link:active {
    transform: translateY(-2px) scale(1);
}

.footer-bottom {
    color: #94a3b8;
    font-size: 1.05rem;
    border-top: 1px solid rgba(99, 102, 241, 0.3);
    padding-top: 1.5rem;
    margin-top: 2rem;
    font-weight: 500;
}

.footer-bottom strong {
    color: #c7d2fe;
    font-weight: 700;
}

/* Success Message */
.stSuccess {
    background: rgba(34, 197, 94, 0.2) !important;
    border-left: 4px solid #22c55e !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
    color: #bbf7d0 !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
}

/* Warning Message */
.stWarning {
    background: rgba(251, 146, 60, 0.2) !important;
    border-left: 4px solid #fb923c !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
    color: #fed7aa !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
}

/* Spinner */
.stSpinner > div {
    border-color: #6366f1 transparent transparent transparent !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 12, 41, 0.5);
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);
    box-shadow: 0 0 15px rgba(139, 92, 246, 0.8);
}

/* Glow effect for interactive elements */
@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 5px rgba(99, 102, 241, 0.5);
    }
    50% {
        box-shadow: 0 0 20px rgba(99, 102, 241, 0.8), 0 0 30px rgba(139, 92, 246, 0.6);
    }
}
</style>
""", unsafe_allow_html=True)

# ──────────── Navigation Bar ─────────────
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">
        <span>🚀</span> CareerPilot AI
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────── Load Mentor Data ─────────────
@st.cache_data
def load_mentor_data():
    return pd.read_csv(PROF_DB)

mentor_df = load_mentor_data()

# ──────────── Mentor Matching Function ─────────────
def match_top_mentors(field_interest, top_n=3):
    relevant_profs = mentor_df[mentor_df['Field_of_Expertise'].str.lower() == field_interest.lower()].copy()
    if relevant_profs.empty:
        return pd.DataFrame()

    for col in ['Feedback_Rating', 'Years_of_Experience', 'Past_Mentee_Performance', 'Behavior_Rating']:
        min_val = relevant_profs[col].min()
        max_val = relevant_profs[col].max()
        relevant_profs[col + '_Norm'] = (relevant_profs[col] - min_val) / (max_val - min_val + 1e-6)

    relevant_profs['Final_Score'] = (
        0.4 * relevant_profs['Feedback_Rating_Norm'] +
        0.3 * relevant_profs['Years_of_Experience_Norm'] +
        0.2 * relevant_profs['Past_Mentee_Performance_Norm'] +
        0.1 * relevant_profs['Behavior_Rating_Norm']
    )

    top_matches = relevant_profs.sort_values(by='Final_Score', ascending=False).head(top_n)

    return top_matches[[
        'Professor_Code', 'professor_name', 'Field_of_Expertise',
        'Years_of_Experience', 'Feedback_Rating', 'Past_Mentee_Performance',
        'Behavior_Rating', 'Contact_Email', 'Final_Score'
    ]]

# ──────────── Main Title ─────────────
st.markdown("<h1>🚀 CareerPilot AI</h1>", unsafe_allow_html=True)
st.markdown("<h4>Your AI-powered Mentor & Placement Guidance System</h4>", unsafe_allow_html=True)

# ──────────── Tabs ─────────────
tab1, tab2 = st.tabs(["🎓 Mentor Matching", "💼 Placement Predictor"])

# ──────────── Mentor Matching ─────────────
with tab1:
    st.markdown("<h2 id='mentor-matching'>Find Your Ideal Mentor</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="color: #c7d2fe; text-align: center; font-size: 1.2rem; font-weight: 500;">
            Get matched with top mentors based on expertise, experience, and feedback ratings.
            Our AI-powered system analyzes multiple factors to find the perfect mentor for your career journey.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    
    with col1:
        field = st.selectbox("Select your Field of Interest", mentor_df['Field_of_Expertise'].unique().tolist())
    
    with col2:
        top_n = st.slider("Number of Mentors", 1, 10, 3)

    if st.button("🔍 Match Mentors"):
        with st.spinner("Finding your perfect mentors..."):
            results = match_top_mentors(field, top_n)
            if not results.empty:
                st.markdown("<h3 style='color: #4CAF50;'>✨ Top Matched Mentors</h3>", unsafe_allow_html=True)
                st.dataframe(
                    results.style.highlight_max(axis=0, color='#4CAF50').format({'Final_Score': '{:.2f}'}),
                    use_container_width=True,
                    height=400
                )
                st.success(f"🎉 Found {len(results)} excellent mentors for you!")
            else:
                st.warning("⚠️ No mentors found for this field. Try selecting a different area of expertise.")

# ──────────── Placement Predictor ─────────────
with tab2:
    st.markdown("<h2 id='placement-predictor'>Predict Your Placement Tier</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="color: #c7d2fe; text-align: center; font-size: 1.2rem; font-weight: 500;">
            Get an accurate prediction of your placement tier based on comprehensive performance metrics.
            Our machine learning model analyzes your skills, projects, and achievements.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Academic & Technical Skills")
        coding = st.slider("Coding Profile Rating", 1000, 2050, 1500, help="Your rating on coding platforms")
        grades = st.slider("Grades (0–10)", 0.0, 10.0, 8.0, help="Your academic performance")
        major_projects = st.slider("Major Projects", 0, 5, 2, help="Number of significant projects completed")
        mini_projects = st.slider("Mini Projects", 0, 10, 3, help="Number of smaller projects")
        internship = st.slider("Internships", 0, 3, 1, help="Number of internships completed")

    with col2:
        st.markdown("### 🏆 Extracurricular & Soft Skills")
        hackathon = st.slider("Hackathon Participation", 0, 5, 1, help="Number of hackathons participated")
        skill_score = st.slider("Skill Match Score (%)", 0, 100, 75, help="Alignment with industry requirements")
        comms = st.slider("Communication Rating", 0.0, 10.0, 7.5, help="Your communication skills rating")
        certs = st.slider("Workshops/Certifications", 0, 10, 2, help="Professional certifications earned")
        attendance = st.slider("Attendance (%)", 0, 100, 85, help="Overall attendance percentage")

    if st.button("📊 Predict Placement Tier"):
        with st.spinner("Analyzing your profile..."):
            input_features = pd.DataFrame([{
                'Coding_Profile_Rating': coding,
                'Grades': grades,
                'Major_Projects': major_projects,
                'Mini_Projects': mini_projects,
                'Internship': internship,
                'Hackathon': hackathon,
                'Skill_Match_Score': skill_score,
                'Communication_Skill_Rating': comms,
                'Workshops_Certifications': certs,
                'Attendance': attendance
            }])

            input_scaled = scaler.transform(input_features)
            prediction = clf.predict(input_scaled)[0]

            st.markdown(f"""
            <div class="card" style="background: linear-gradient(135deg, rgba(76, 175, 80, 0.3), rgba(102, 126, 234, 0.3)); text-align: center;">
                <h2 style="color: white !important; margin-bottom: 1rem;">🎯 Prediction Result</h2>
                <h1 style="color: #FFD700 !important; font-size: 2.5rem !important;">{prediction}</h1>
                <p style="color: white; font-size: 1.2rem;">Placement Tier</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            st.success("✅ Analysis complete! Keep working on your skills to improve your placement prospects.")

# ──────────── Footer ─────────────
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-title">🚀 CareerPilot AI</div>
        <div class="footer-description">
            CareerPilot AI is an intelligent career guidance platform that leverages machine learning 
            to match students with the perfect mentors and predict placement outcomes. We combine 
            advanced algorithms with comprehensive data analysis to help students navigate their 
            career journey with confidence and clarity.
        </div>
        <div class="social-links">
            <a href="https://github.com/Abhinaw-47" class="social-link" target="_blank">
                <span>💻</span> GitHub
            </a>
            <a href="https://www.linkedin.com/in/abhinaw-anand-04a64124a/" class="social-link" target="_blank">
                <span>💼</span> LinkedIn
            </a>
            <a href="https://x.com/Abhinaw_Anand96" class="social-link" target="_blank">
                <span>🐦</span> X (Twitter)
            </a>
        </div>
    </div>
    <div class="footer-bottom">
        Made by <strong>Abhinaw Anand</strong> | © 2025 CareerPilot AI. All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)