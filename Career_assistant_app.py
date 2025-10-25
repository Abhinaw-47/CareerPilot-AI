import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

from pathlib import Path

BASE_DIR = Path(__file__).parent

MODEL_PATH = BASE_DIR / "placement_tier_classifier.pkl"
SCALER_PATH = BASE_DIR / "placement_scaler.pkl"
PROF_DB = BASE_DIR / "Enhanced_Professor_Database.csv"
STUDENT_XLSX = BASE_DIR / "Student_Data_With_Extras.xlsx"

clf = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


@st.cache_data
def load_mentor_data():
    return pd.read_csv(PROF_DB)

mentor_df = load_mentor_data()

# @st.cache_resource
# def load_model():
#     return joblib.load("placement_rf_model.pkl")  # Use your trained RandomForestRegressor model

# placement_model = load_model()


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

# ───────── UI Layout ──────────
st.set_page_config(page_title="CareerPilot AI", layout="centered")
st.title("CareerPilot AI")

tab1, tab2 = st.tabs(["🎓 Mentor Matching", "💼 Placement Predictor"])

# ───────── Mentor Matching ──────────
with tab1:
    st.subheader("Find Your Ideal Mentor")
    field = st.selectbox("Select your Field of Interest", mentor_df['Field_of_Expertise'].unique().tolist())
    top_n = st.slider("Number of Mentors", 1, 10, 3)

    if st.button("🔍 Match Mentors"):
        results = match_top_mentors(field, top_n)
        if not results.empty:
            st.dataframe(results.style.highlight_max(axis=0), use_container_width=True)
        else:
            st.warning("No mentors found for this field.")

# ───────── Placement Predictor ──────────
with tab2:
    st.subheader("Predict Your Placement Tier")

    coding = st.slider("Coding Profile Rating", 1000, 2050, 1500)
    grades = st.slider("Grades (0–10)", 0.0, 10.0, 8.0)
    major_projects = st.slider("Major Projects", 0, 5, 2)
    mini_projects = st.slider("Mini Projects", 0, 10, 3)
    internship = st.slider("Internships", 0, 3, 1)
    hackathon = st.slider("Hackathon Participation", 0, 5, 1)
    skill_score = st.slider("Skill Match Score (%)", 0, 100, 75)
    comms = st.slider("Communication Rating", 0.0, 10.0, 7.5)
    certs = st.slider("Workshops/Certifications", 0, 10, 2)
    attendance = st.slider("Attendance (%)", 0, 100, 85)

    if st.button("📊 Predict Placement Tier"):
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

        st.success(f"🎓 You are predicted to be in **{prediction}** Placement Tier.")

