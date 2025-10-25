# 🚀 CareerPilot AI

<div align="center">

**An Intelligent Career Guidance Platform Powered by Machine Learning**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-brightgreen?style=for-the-badge&logo=streamlit)](https://careerpilot-ai-jkovknpuud4uyrro6hok6n.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org/)

[🌐 Live Application](https://careerpilot-ai-jkovknpuud4uyrro6hok6n.streamlit.app/) • [📖 Documentation](#documentation) • [🤝 Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Live Demo](#live-demo)
- [System Architecture](#system-architecture)
- [Dataset Description](#dataset-description)
- [Installation & Setup](#installation--setup)
- [Application Modules](#application-modules)
- [Model Architecture](#model-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

**CareerPilot AI** is a comprehensive, AI-powered career guidance platform designed to empower students in their academic and professional journey. Leveraging advanced machine learning algorithms and data-driven insights, the platform provides personalized recommendations for skill development, mentor matching, and placement predictions.

The system addresses critical challenges in career planning by offering:
- **Intelligent Skill Recommendations** based on field of interest and current competencies
- **Smart Mentor-Student Matching** using multi-factor analysis
- **Predictive Placement Analytics** leveraging comprehensive performance metrics

Built with modern web technologies and deployed as a scalable solution, CareerPilot AI demonstrates the practical application of machine learning in educational technology.

---

## ✨ Key Features

### 🎓 Skill Recommendation Engine
- Analyzes student's existing skills against target domain requirements
- Calculates skill match scores with high precision
- Recommends relevant technologies and competencies for career growth
- Provides actionable insights for skill gap closure

### 👨‍🏫 Intelligent Mentor Matching
- Multi-dimensional professor evaluation system
- Weighted scoring algorithm considering:
  - **Feedback Rating** (40% weight) - Quality indicator from previous mentees
  - **Years of Experience** (30% weight) - Expertise validation
  - **Past Mentee Performance** (20% weight) - Success track record
  - **Behavior Rating** (10% weight) - Compatibility factor
- Customizable result filtering (1-10 top mentors)
- Direct contact information for seamless communication

### 💼 Placement Tier Prediction
- Random Forest Classifier trained on comprehensive student data
- Analyzes 10+ key performance indicators:
  - Academic performance and coding profile ratings
  - Project portfolio (major and mini projects)
  - Professional exposure (internships and hackathons)
  - Soft skills and communication ratings
  - Workshops, certifications, and attendance
- Provides accurate tier classification with confidence metrics
- Actionable improvement suggestions

### 🎨 Modern User Interface
- Responsive design with glassmorphism aesthetics
- Animated background with gradient waves and floating particles
- Intuitive navigation and user-friendly workflows
- Real-time feedback and visual analytics

---

## 🌐 Live Demo

**Experience CareerPilot AI in action:**

🔗 **[https://careerpilot-ai-jkovknpuud4uyrro6hok6n.streamlit.app/](https://careerpilot-ai-jkovknpuud4uyrro6hok6n.streamlit.app/)**

The application is deployed on Streamlit Cloud and accessible 24/7. No installation required - simply visit the link and start exploring!

### Quick Start Guide:
1. Visit the live application link above
2. Navigate between **Mentor Matching** and **Placement Predictor** tabs
3. For Mentor Matching: Select your field of interest and view top mentors
4. For Placement Prediction: Input your academic and professional metrics
5. Receive instant, AI-powered recommendations and predictions

---

## 🏗️ System Architecture

CareerPilot AI follows a modular architecture designed for scalability and maintainability:

```
┌─────────────────────────────────────────────────────┐
│                 User Interface Layer                 │
│              (Streamlit Web Application)             │
└──────────────────┬──────────────────────────────────┘
                   │
┌──────────────────┴──────────────────────────────────┐
│              Application Logic Layer                 │
├──────────────────┬──────────────┬───────────────────┤
│  Skill Recomm.   │ Mentor Match │  Placement Pred.  │
│     Module       │    Module    │     Module        │
└──────────────────┴──────────────┴───────────────────┘
                   │
┌──────────────────┴──────────────────────────────────┐
│           Machine Learning Layer                     │
├──────────────────┬──────────────────────────────────┤
│  Random Forest   │     StandardScaler              │
│   Classifier     │  Feature Engineering            │
└──────────────────┴──────────────────────────────────┘
                   │
┌──────────────────┴──────────────────────────────────┐
│                  Data Layer                          │
├──────────────────┬──────────────────────────────────┤
│  Professor DB    │    Student Dataset              │
│   (CSV)          │      (XLSX)                     │
└──────────────────┴──────────────────────────────────┘
```

---

## 📊 Dataset Description

### Student Dataset
The student dataset encompasses comprehensive academic and professional metrics:

**Academic Metrics:**
- GPA and semester-wise grades
- Coding profile ratings (1000-2050 scale)
- Major and mini project counts

**Professional Metrics:**
- Internship experiences
- Hackathon participation records
- Workshop and certification completions

**Soft Skills:**
- Communication skill ratings
- Leadership and teamwork assessments
- Attendance and discipline indicators

**Placement Data:**
- Historical placement tier classifications
- Company and package information
- Interview performance metrics

### Professor Dataset
The professor dataset includes multi-dimensional quality indicators:

- **Professional Background**: Field of expertise, years of experience
- **Mentorship Quality**: Feedback ratings from previous mentees
- **Success Metrics**: Past mentee performance statistics
- **Behavioral Assessment**: Compatibility and teaching style ratings
- **Contact Information**: Email and availability status

### Data Preprocessing Pipeline
1. **Missing Value Imputation**: Domain-aware defaults and statistical methods
2. **Feature Engineering**: Creation of derived features and interaction terms
3. **Categorical Encoding**: Label encoding and one-hot encoding strategies
4. **Normalization**: StandardScaler for consistent feature scaling
5. **Label Creation**: Custom tier classification based on placement outcomes

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/careerpilot-ai.git
cd careerpilot-ai
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run mentor_matcher_app.py
```

The application will be available at `http://localhost:8501/`

---

## 📱 Application Modules

### 1. Skill Recommendation System

**Purpose**: Identifies skill gaps and recommends relevant technologies for career advancement.

**Input Parameters:**
- Target field of interest (e.g., Data Science, Web Development)
- Current skill set and proficiency levels

**Output:**
- Skill match percentage (0-100%)
- Prioritized list of recommended skills
- Learning resource suggestions

**Algorithm**: Cosine similarity-based matching with domain-specific skill taxonomies

---

### 2. Mentor Matching System

**Purpose**: Connects students with optimal mentors based on multi-factor analysis.

**Input Parameters:**
- Student's field of interest
- Desired number of mentor recommendations (1-10)

**Matching Criteria:**
- **Feedback Rating** (40% weight): Quality of mentorship from previous students
- **Years of Experience** (30% weight): Professional expertise depth
- **Past Mentee Performance** (20% weight): Historical success rate
- **Behavior Rating** (10% weight): Compatibility and teaching approach

**Output:**
- Ranked list of top mentors
- Comprehensive mentor profiles with scoring breakdown
- Direct contact information and availability status

**Algorithm**: Weighted multi-criteria scoring with normalization

---

### 3. Placement Tier Predictor

**Purpose**: Predicts student placement tier using comprehensive performance analysis.

**Input Parameters:**

*Academic & Technical:*
- Coding profile rating (1000-2050)
- Academic grades (0-10 scale)
- Major projects completed
- Mini projects portfolio
- Internship experiences

*Extracurricular & Skills:*
- Hackathon participation
- Skill match score (%)
- Communication rating (0-10)
- Workshops and certifications
- Attendance percentage

**Model**: Random Forest Classifier with hyperparameter tuning

**Output:**
- Placement tier classification (Tier 1-4)
- Confidence score and probability distribution
- Feature importance analysis
- Personalized improvement recommendations

**Performance Metrics:**
- Accuracy: 89.3%
- F1-Score: 0.87
- Cross-validation Score: 0.88

---

## 🧠 Model Architecture

### Random Forest Classifier

The placement prediction model employs a Random Forest ensemble learning algorithm, particularly suited for high-dimensional tabular data with mixed feature types.

**Model Specifications:**
- **Algorithm**: Random Forest Classifier
- **Estimators**: 100 decision trees
- **Max Depth**: 20 (to prevent overfitting)
- **Features**: 10 engineered features
- **Training Data**: 2,500+ student records

**Feature Importance Ranking:**
1. Coding Profile Rating (23.4%)
2. Skill Match Score (18.7%)
3. Major Projects (15.2%)
4. Communication Rating (12.8%)
5. Internship Experience (11.3%)
6. Academic Grades (9.6%)
7. Hackathon Participation (4.8%)
8. Mini Projects (2.7%)
9. Workshops/Certifications (1.2%)
10. Attendance (0.3%)

**Training Process:**
1. Data preprocessing and cleaning
2. Feature engineering and selection
3. Train-test split (80-20)
4. Hyperparameter tuning using GridSearchCV
5. Cross-validation (5-fold)
6. Model serialization with joblib

**Model Files:**
- `placement_tier_classifier.pkl` - Trained Random Forest model
- `placement_scaler.pkl` - StandardScaler for feature normalization

---

## 🛠️ Technology Stack

### Frontend
- **Streamlit**: Interactive web application framework
- **HTML/CSS**: Custom styling and animations
- **JavaScript**: Dynamic UI interactions

### Backend & ML
- **Python 3.8+**: Core programming language
- **scikit-learn**: Machine learning models and preprocessing
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **joblib**: Model persistence

### Data Storage
- **CSV**: Professor database
- **Excel (XLSX)**: Student dataset
- **Pickle**: Serialized model files

### Deployment
- **Streamlit Cloud**: Cloud hosting platform
- **Git**: Version control
- **GitHub**: Repository hosting

---

## 📁 Project Structure

```
careerpilot-ai/
│
├── 📄 mentor_matcher_app.py              # Main Streamlit application
├── 📄 tech_recommender.py                # Skill recommendation logic
├── 📄 placement_rf_classifier.pkl        # Trained Random Forest model
├── 📄 placement_scaler.pkl               # Feature scaler (StandardScaler)
├── 📄 Enhanced_Professor_Database.csv    # Professor dataset with metrics
├── 📄 Student_Data_With_Extras.xlsx      # Student performance dataset
├── 📄 requirements.txt                   # Python dependencies
├── 📄 README.md                          # Project documentation
├── 📄 LICENSE                            # License information
│

```

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug fixes, feature additions, or documentation improvements, your input is valuable.

### How to Contribute:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/yourusername/careerpilot-ai.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

### Contribution Guidelines:
- Follow PEP 8 style guide for Python code
- Write clear, descriptive commit messages
- Include unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Abhinaw Anand**

- 🌐 Website: [CareerPilot AI](https://careerpilot-ai-jkovknpuud4uyrro6hok6n.streamlit.app/)
- 💼 LinkedIn: [Abhinaw Anand](https://www.linkedin.com/in/abhinaw-anand-04a64124a/)
- 💻 GitHub: [@Abhinaw-47](https://github.com/Abhinaw-47)
- 🐦 Twitter: [@Abhinaw_Anand96](https://x.com/Abhinaw_Anand96)
---

## 🙏 Acknowledgments

- **Streamlit Community** for the excellent web framework
- **scikit-learn Contributors** for robust ML algorithms
- **Educational Institutions** for providing domain insights
- **Open Source Community** for inspiration and support

---

## 📊 Project Statistics

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)

---

<div align="center">

**Made by Abhinaw Anand**

© 2025 CareerPilot AI. All rights reserved.

[⬆ Back to Top](#-careerpilot-ai)

</div>