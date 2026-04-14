# Personal Health: Mood & Habit Tracker

An interactive Machine Learning dashboard built with Python and Streamlit that predicts daily well-being scores based on lifestyle habits.

---

## Overview

This project explores the relationship between daily habits—sleep, hydration, and physical activity—and their impact on mental well-being. Using a Random Forest Regressor, the application analyzes historical data to provide real-time mood predictions and actionable health advice.

### Key Features

- **Real-time Predictions**  
  Adjust sliders for sleep, water intake, and steps to see instant mood forecasts.

- **Explainable AI**  
  A visual breakdown of feature importance shows which habits impact your score the most.

- **Dynamic Feedback**  
  Personalized health advice generated based on the model's output.

---

## Technical Stack

- **Language:** Python 3.11  
- **Machine Learning:** Scikit-Learn (Random Forest Regressor)  
- **Data Analysis:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **Web Framework:** Streamlit  

---

## Machine Learning Workflow

The workflow includes:
1. Data collection and preprocessing  
2. Feature selection and engineering  
3. Model training using Random Forest Regressor  
4. Model evaluation using Mean Absolute Error (MAE)  
5. Deployment via Streamlit dashboard  

---

## The High Signal Dataset

Originally, the project utilized a raw dataset that contained significant noise, leading to low model accuracy. To improve performance, a high-signal dataset was developed focusing on core features:

- **Sleep Hours** – The primary driver of the well-being score  
- **Steps** – Measurement of physical activity  
- **Water Intake** – Indicator of hydration  

By refining the dataset to focus on these physiological drivers, the model achieved a significantly lower Mean Absolute Error, improving prediction reliability.

---

## Project Structure

```
├── .python-version          # Ensures stable Python 3.11 environment
├── app.py                   # Main Streamlit dashboard script
├── High_Signal_Habits.csv   # Processed dataset for model training
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## Installation and Local Usage

### 1. Clone the Repository
```bash
git clone https://github.com/hashir500/personal-health-mood-habit-tracker.git
cd personal-health-mood-habit-tracker
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

---

## Model Interpretation

The project uses feature importance to ensure interpretability. The model consistently identifies:

1. Sleep as the most significant predictor  
2. Physical activity (steps) as the second  
3. Hydration (water intake) as the third  

This helps users understand how their habits directly influence their well-being score.

---

## Author

**Muhammad Hashir Hassan**  
Computer Science Student at Bahria University  

