# bmi_calculator.py

# Input weight and height
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

# Display results
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {round(bmi, 1)}")
print(f"Category: {category}")
