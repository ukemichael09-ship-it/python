# PART 1: Ask for today's temperature
temperature = int(input("Enter today's teperature in Celsius:" ))

# PART 2: Decide between a jacket and a t-shirt
if temperature < 20:
    outfit = "jacket" 
    print("it is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

# PART 3: Ask whether it is raining
is_raining = input("Is it raining today? (yes/no): ")

# PART 4: Add an umbrella reminder if it is raining
if is_raining == "yes":
    print("Bring an umbrella!")

# PART 5:Ask for the wind speed
wind_speed = int(input("Enter the win speed in km/h:"))

# PART 6: Decide whether a winbreaker is needed
if wind_speed > 30:
                
    

    