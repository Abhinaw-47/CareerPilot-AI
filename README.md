# AI-Powered Career Assistant (End-to-End)

## Introduction

This project is a **Streamlit web application** designed to assist students in their academic and career journey using Machine Learning models. It includes intelligent modules for:

- Recommending technical skills based on a student's field of interest and current competencies
- Matching students with professors for mentorship based on performance and feedback
- Predicting placement tier based on academic scores, coding profiles, projects, internships, and soft skills

The goal of this project is to create a user-friendly career advisory platform using real and simulated datasets, machine learning models, and an interactive interface.

### Dataset

- Student-related data including academic performance, skills, projects, internships, and placement history.
- Professor-related data including feedback, experience, and mentorship effectiveness.
- Combined and preprocessed into training-ready structured datasets.

## Project Overview

This end-to-end system includes:

1. **Skill Recommender**: Computes match score between a student’s skills and the target domain, and recommends relevant technologies.
2. **Mentor Matching**: Ranks and recommends professors based on their teaching field, student feedback, mentorship quality, and experience.
3. **Placement Prediction**: Classifies students into placement tiers using a Random Forest Classifier model trained on combined academic and professional features.
4. **Streamlit App**: Provides an interactive web interface to access all three modules.
5. **Deployment Ready**: Modular codebase for integration into full-stack apps using Flask or FastAPI in the future.

## Model Download and Directory Structure

### Trained Models:

- Models are saved using `joblib` and used directly in the Streamlit app.

### Directory Structure:

```
career-assistant/
│
├── tech_recommender.py              # Skill matching logic
├── mentor_matcher_app.py            # Streamlit app (UI for skill, mentor, placement)
├── placement_rf_classifier.pkl      # Trained Random Forest Classifier (placement prediction)
├── scaler_for_classifier.pkl        # StandardScaler used for feature preprocessing
├── Enhanced_Professor_Database.csv  # Professor dataset with quality metrics
├── Student_Data_With_Extras.xlsx    # Combined and engineered student dataset
├── README.md                        # Project documentation
└── requirements.txt                 # List of Python dependencies
```

## Setup Instructions

### Step 1: Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

```bash
streamlit run mentor_matcher_app.py
```

The app will be hosted at `http://localhost:8501/`.

## Application Modules

### Skill Recommender

- Input: Field of interest, existing skills
- Output: Match score (%), Recommended skills

### Mentor Matching

- Input: Student’s field of interest
- Output: Top N matched professors based on:
  - Feedback Rating
  - Years of Experience
  - Past Mentee Performance
  - Behavior Rating

### Placement Tier Predictor

- Input: Coding rating, GPA, projects, certifications, communication rating, etc.
- Model: Random Forest Classifier
- Output: Placement tier label (Tier 1–4)

## Model Architecture

The placement model uses the Random Forest algorithm, which is suitable for high-dimensional tabular data with both categorical and continuous features.

### Important Features:

- Coding_Profile_Rating
- Major_Projects and Mini_Projects
- Internships and Hackathons
- Skill_Match_Score (from recommender)
- Communication and Soft Skill Ratings

## Data Preprocessing

- Filled missing values using domain-aware defaults
- Engineered categorical encodings and normalized numerical values
- Created custom labels for placement tiers
- Scaled feature vectors using `StandardScaler`

## Conclusion

This AI-powered platform provides a comprehensive solution for skill analysis, career mentorship, and placement prediction. It demonstrates practical use of machine learning in education and can be expanded for institutional use with more real-world data and integrations.

## Future Enhancements

- Improve UI with animations and interactive charts
- Integrate login/user tracking and history saving
- Deploy to cloud platforms (Streamlit Cloud, Render, Heroku)
- Build frontend in React and backend in FastAPI for scalability
