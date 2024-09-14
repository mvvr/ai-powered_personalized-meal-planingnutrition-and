from openai import OpenAI
import openai
import os

# Set your OpenAI API key

openai.api_key = ' '
'''openai_api_key = "sk-oBW6oms1OrJ-ruDbWTK_sAY8yfmh6AWVNo8vBXMhpPT3BlbkFJhvmMyzL4Dj0wCMEyD5z-xSqIa1b9wp0ueMm6xlktYA"
api_base = "https://api.openai.com/v1"
client = OpenAI(api_key=openai_api_key, base_url=api_base)
'''


def get_ai_meal_recommendation(name, daily_calories, diet_pref):
    """Get personalized meal recommendations using OpenAI's GPT-3.5 Turbo."""
    
    # Define the prompt for the AI model
    prompt = f"""
    Create a meal plan for {name}, with {daily_calories} calories daily intake, considering a {diet_pref} diet. 
    Include breakfast, lunch, dinner, and two snacks. Make sure to include nutritional information.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the GPT-3.5 Turbo model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract and return the response content
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"
