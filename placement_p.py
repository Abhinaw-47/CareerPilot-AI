import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from tech_recommender import recommend_skills 
from pathlib import Path

BASE_DIR = Path(_file_).parent

MODEL_PATH = BASE_DIR / "placement_tier_classifier.pkl"
SCALER_PATH = BASE_DIR / "placement_scaler.pkl"
PROF_DB = BASE_DIR / "Enhanced_Professor_Database.csv"
STUDENT_XLSX = BASE_DIR / "Student_Data_With_Extras.xlsx"

df = pd.read_excel(STUDENT_XLSX)

def placement_to_tier(salary):
    if salary >= 2000000:
        return 'Tier 1'
    elif salary >= 1000000:
        return 'Tier 2'
    elif salary >= 500000:
        return 'Tier 3'
    else:
        return 'Tier 4'

df['Placement_Tier'] = df['Placement'].apply(placement_to_tier)



def compute_skill_match(row):
    try:
        field = row['Field']
        skills = set(row['Skills'].split(', '))
        result = recommend_skills(field, skills)
        return result['Match Score (%)']
    except:
        return 50 

df['Skill_Match_Score'] = df.apply(compute_skill_match, axis=1)

features = [
    'Coding_Profile_Rating', 'Grades', 'Major_Projects', 'Mini_Projects',
    'Internship', 'Hackathon', 'Skill_Match_Score',
    'Communication_Skill_Rating', 'Workshops_Certifications','Attendance'
]

X = df[features]
y = df['Placement_Tier']


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

import joblib
joblib.dump(clf, "placement_tier_classifier.pkl")
joblib.dump(scaler, "placement_scaler.pkl")
