def calculate_daily_calories(weight, height, age, gender):
    """Calculates the daily calorie intake based on weight, height, age, and gender."""
    if gender == 'Male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_bmi(weight, height):
    """Calculates BMI (Body Mass Index)."""
    height_m = height / 100  # Convert height to meters
    return weight / (height_m ** 2)
