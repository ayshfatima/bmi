print("Calculate your Body Mass Index :)")
name = input("Please enter the user name: ")
option1 = int(input("Enter 1 for height in centimeters or 2 for height in feet and inches: "))
option2 = int(input("Enter 1 for weight in pounds or 2 for weight in kilograms: "))

# Get height input
if option1 == 1:
    height_cm = float(input("Enter your height in centimeters: "))
    height_m = height_cm / 100  # Convert cm to meters
elif option1 == 2:
    feet = int(input("Enter feet part of your height: "))
    inches = float(input("Enter inches part of your height: "))
    height_m = (feet * 12 + inches) * 0.0254  # Convert feet and inches to meters
else:
    print("Invalid height option.")
    height_m = None

# Get weight input
if option2 == 1:
    weight_lb = float(input("Enter your weight in pounds: "))
    weight_kg = weight_lb * 0.453592  # Convert pounds to kg
elif option2 == 2:
    weight_kg = float(input("Enter your weight in kilograms: "))
else:
    print("Invalid weight option.")
    weight_kg = None

# Calculate BMI if height and weight inputs are valid
if height_m and weight_kg:
    BMI = weight_kg / (height_m * height_m)

    # Determine BMI category
    if BMI < 18.5:
        category = "underweight"
    elif 18.5 <= BMI <= 24.9:
        category = "normal/healthy"
    elif 25 <= BMI <= 29.9:
        category = "overweight"
    else:
        category = "obese"

    # Display result
    print(f"Dear {name}, your BMI is {BMI:.2f}, which is considered {category}.")
else:
    print("Please enter valid height and weight values.")
