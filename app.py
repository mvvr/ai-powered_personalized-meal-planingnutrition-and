import streamlit as st
from utils.data_fetcher import fetch_nutritional_data
from utils.nutrition_calculator import calculate_daily_calories, calculate_bmi
from utils.ai_recommendation import get_ai_meal_recommendation
from utils.design import set_page_style

# Set page design
set_page_style()

# App Title
st.title("AI-Powered Personalized Nutrition and Meal Planning")

# User input section
st.subheader("Enter your details for a personalized meal plan")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=50.0)
gender = st.radio("Gender", ('Male', 'Female'))
diet_pref = st.selectbox("Diet Preference", ['None', 'Vegetarian', 'Non-Vegetarian' ])#'Keto', 'Paleo'

# Calculate daily calorie needs and BMI
if st.button("Calculate My Plan"):
    daily_calories = calculate_daily_calories(weight, height, age, gender)
    bmi = calculate_bmi(weight, height)
    
    st.write(f"Your daily intake needs to be: {daily_calories:.1f} calories")
    st.write(f"Your BMI: {bmi:.2f} ({'Normal' if 18.5 <= bmi < 25 else 'Abnormal'})")

    # Fetch nutritional data from an online source
    nutritional_data = fetch_nutritional_data(diet_pref)

    # Display nutritional information
    st.subheader(f"Nutritional Recommendations ({diet_pref})")
    st.dataframe(nutritional_data)

    
    
    meal_plan = get_ai_meal_recommendation(name, daily_calories, diet_pref)
    print(meal_plan)
    st.write(meal_plan)


    # Get AI-powered meal recommendation
    if st.button("Get AI Meal Plan"):
        meal_plan = get_ai_meal_recommendation(name, daily_calories, diet_pref)
        st.subheader("Your Personalized Meal Plan")
        st.write(meal_plan)
        print(meal_plan)
