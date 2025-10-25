import pandas as pd
from pathlib import Path

BASE_DIR = Path(_file_).parent

MODEL_PATH = BASE_DIR / "placement_tier_classifier.pkl"
SCALER_PATH = BASE_DIR / "placement_scaler.pkl"
PROF_DB = BASE_DIR / "Enhanced_Professor_Database.csv"
STUDENT_XLSX = BASE_DIR / "Student_Data_With_Extras.xlsx"

prof_df = pd.read_csv(PROF_DB)

def match_top_mentors(field_interest, top_n=3):
    """
    Returns top N recommended professors for the given field of interest,
    based on weighted multi-criteria ranking.
    """

    relevant_profs = prof_df[prof_df['Field_of_Expertise'].str.lower() == field_interest.lower()].copy()

    if relevant_profs.empty:
        return f"No professors found for the field: {field_interest}"

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

field = "AI/ML"
top_mentors = match_top_mentors(field_interest=field, top_n=5)
print(top_mentors)
