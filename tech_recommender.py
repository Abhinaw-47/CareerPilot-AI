
# STEP 1: Predefined Skill Sets
skill_map = {
    "Data Science": {"Python", "Pandas", "NumPy", "Scikit-learn", "SQL", "Matplotlib"},
    "Web Development": {"HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB"},
    "Cybersecurity": {"Networking", "Linux", "Cryptography", "Ethical Hacking", "Python"},
    "Machine Learning": {"Python", "Scikit-learn", "TensorFlow", "Pandas", "NumPy", "Matplotlib"},
    "Mobile Development": {"Kotlin", "Java", "Flutter", "Dart", "React Native"}
}

# STEP 2: Core Recommendation Function
def recommend_skills(field_of_interest: str, user_skills: set) -> dict:
    required_skills = skill_map.get(field_of_interest, set())

    matched_skills = user_skills & required_skills
    print(matched_skills)
    missing_skills = required_skills - user_skills
    total_required = len(required_skills)
    match_score = round(len(matched_skills) / total_required * 100) if total_required else 0

    return {
        "Field": field_of_interest,
        "Match Score (%)": match_score,
        "Skills You Have": sorted(matched_skills),
        "Skills to Learn": sorted(missing_skills)
    }

# STEP 3: Testable Main Function
def main():
    # Example test case (simulate user input)
    field = "Machine Learning"
    current_skills = {"Python", "SQL", "Matplotlib"}

    print(" Tech Skill Recommender")
    result = recommend_skills(field, current_skills)

    print("\n Recommendation:")
    print(f"Field of Interest     : {result['Field']}")
    print(f"Skill Match Score     : {result['Match Score (%)']}")
    print(f"Skills You Already Know: {', '.join(result['Skills You Have'])}")
    print(f"Skills You Should Learn: {', '.join(result['Skills to Learn'])}")

# Run only if this script is called directly
if __name__ == "__main__":
    main()
