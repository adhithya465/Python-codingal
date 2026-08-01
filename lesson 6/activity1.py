temperature=int(input(" Enter today's temperature "))

is_raining=(input(" Is it raining today? (yes/no)"))

wind_speed=int(input(" Enter the wind speed "))

has_puddles=input(" Are there puddles? ")


if temperature <=20:
    outfit= "jacket"
    print(" It is cold today ")
    print("Wear a ",outfit)
else:
    outfit= "t-shirt"
    print(" It is not cold today")
    print("Wear a ",outfit)
if is_raining=="yes":
    print("Bring an Umbrella")