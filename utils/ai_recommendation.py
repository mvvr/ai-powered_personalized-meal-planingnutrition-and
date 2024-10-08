from openai import OpenAI
import openai
import os

# Set your OpenAI API key

openai.api_key = ''



def get_ai_meal_recommendation(name, daily_calories, diet_pref):
    """Get personalized meal recommendations using OpenAI's GPT-3.5 Turbo."""
    
    # Define the prompt for the AI model
    prompt = f"""
    Create a meal plan for {name}, with {daily_calories} calories daily intake, considering a {diet_pref} diet. 
    Include breakfast, lunch, dinner, and two snacks. Make sure to include nutritional information.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use the GPT-3.5 Turbo model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response content
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
