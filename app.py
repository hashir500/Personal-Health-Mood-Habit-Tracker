import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 1. Setup & Simple Data Loading
st.set_page_config(page_title="Well-being Predictor", page_icon="🧠")
st.title("🧠 Personal Health Dashboard")

@st.cache_data
def load_and_train():
    # Using your high-signal dataset logic
    df = pd.read_csv('synthetic.csv') 
    X = df[['Sleep_Hours', 'Water_Liters', 'Steps']]
    y = df['Mood_Score']
    model = RandomForestRegressor(n_estimators=100, random_state=42).fit(X, y)
    return model

model = load_and_train()

# 2. User Inputs in Sidebar
st.sidebar.header("Today's Habits")
sleep = st.sidebar.slider("Sleep_Hours", 0.0, 12.0, 7.0)
water = st.sidebar.slider("Water_Liters", 0.0, 5.0, 2.0)
steps = st.sidebar.number_input("Steps", 0, 20000, 5000)

# 3. Prediction & Display
prediction = model.predict([[sleep, water, steps]])[0]

st.subheader(f"Predicted Tomorrow's Mood: {prediction:.2f} / 10")
st.progress(prediction / 10)

if prediction > 7:
    st.success("You're on track for a great day!")
else:
    st.warning("Consider more rest or hydration today.")

# 4. Simple Visualization
st.bar_chart(pd.Series(model.feature_importances_, index=['Sleep', 'Water', 'Steps']))