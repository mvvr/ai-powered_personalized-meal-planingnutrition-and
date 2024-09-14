import pandas as pd

def fetch_nutritional_data(diet_pref):
    """Fetch nutritional data from an online CSV."""
    # URL to an online CSV file (replace with your own source if needed)
    url = 'utils/nutrition_diet.csv'
    
    # Load the CSV into a pandas DataFrame
    df = pd.read_csv(url)

    # Filter by diet preference if necessary
    if diet_pref != "None":
        df = df[df['Diet Preference'] == diet_pref]

    # Return relevant columns like food item, calories, protein, carbs, and fats
    return df[['Food Item', 'Measure', 'Grams', 'Calories', 'Protein', 'Carbohydrate', 'Fat', 'Sat.Fat', 'Category']]
