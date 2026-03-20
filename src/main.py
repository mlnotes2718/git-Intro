# src/main.py  ← CORRECT VERSION with pounds support

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float, rounded to 2 decimal places.
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def pounds_to_kg(weight_lb: float) -> float:
    """Convert pounds to kilograms (1 lb = 0.453592 kg)."""
    return round(weight_lb * 0.453592, 4)


def bmi_category(bmi: float) -> str:
    """Return the WHO BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    unit = input("Enter weight unit (kg / lb): ").strip().lower()
    weight = float(input("Enter your weight: "))
    if unit == "lb":
        weight = pounds_to_kg(weight)
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")
