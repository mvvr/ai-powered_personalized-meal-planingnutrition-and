

# AI-Powered Personalized Nutrition and Meal Planning

This project is a **Streamlit** app designed to provide personalized nutrition recommendations and meal planning based on individual  dietary preferences. The app uses machine learning, nutritional analysis, and OpenAI's API to generate custom meal plans and analyze the nutritional needs of users.

## Features

- **Personalized Nutrition Recommendations:** Tailored dietary suggestions based on user's health metrics (e.g., BMI, activity level).
- **Meal Planning:** AI-generated meal plans that match user preferences and dietary restrictions.
- **Nutritional Data Analysis:** Fetches nutritional data from online sources to calculate daily nutrient needs.
- **AI-Powered Responses:** Integrated with OpenAI API for AI-driven recommendations and recipe generation.

## Project Structure

```bash
├── app.py                     # Main Streamlit app
├── utils/
│   ├── data_fetcher.py         # Fetches data from online sources
│   ├── nutrition_calculator.py # Calculates daily nutritional needs and BMI
│   ├── ai_recommendation.py    # Handles AI-based meal planning and recommendations
│   ├── design.py               # Custom design and styling for Streamlit app
├── requirements.txt            # Dependencies list
├── README.md                   # Project documentation
```

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/personalized-nutrition-app.git
cd personalized-nutrition-app
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
```bash
conda create -name venv python=3.9
conda activate venv   
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up OpenAI API:**

You will need to set your OpenAI API key in the environment. To do this, add the following line to your `secrete.toml` file or export it in your shell session:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

## Usage

1. **Run the Streamlit app:**

```bash
streamlit run app.py
```

2. **Use the app:**

- Input personal information like age, weight, height, activity level, and dietary preferences.
- Get AI-driven meal plans and nutrition suggestions based on your inputs.
- Adjust recommendations based on health goals.

## AI-Powered Meal Suggestions

This app uses OpenAI's API to generate custom meal suggestions based on the user's profile. The AI models can suggest different meal options and recipes that meet the user's nutritional requirements.

## Future Enhancements

- **Mobile App Integration:** Expand the app to include mobile versions.
- **Wearable Data Integration:** Sync data from wearable devices to improve recommendation accuracy.
- **Real-Time Feedback:** Implement a feedback mechanism for users to fine-tune recommendations.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

