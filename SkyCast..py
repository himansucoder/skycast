import csv
from datetime import date

your_state = input("Please enter your state: ")
current_temperature = float(input("Enter the current temperature (°C): "))
current_condition = input("Enter the current weather condition (Sunny / Cloudy / Rainy / Snowy): ").capitalize()
humidity_level = float(input("Enter the humidity level (%): "))
speed_of_wind = float(input("Enter the wind speed (km/h): "))


def weather_condition(temp, condition, humidity, wind):
    if condition == "Rainy" and humidity > 70:
        probability = "High"
        forecast = "Continued rain likely tomorrow."
    elif condition == "Cloudy" and humidity > 60:
        probability = "Medium"
        forecast = "Possibility of light rain."
    elif condition == "Sunny" and humidity < 40:
        probability = "Low"
        forecast = "Clear skies expected."
    elif condition == "Snowy":
        probability = "Medium"
        forecast = "Snow may continue."
    else:
        probability = "Uncertain"
        forecast = "Weather is unpredictable."

    print("\n🛰️  SkyCast Weather Analysis Report")
    print("-------------------------------------")
    print(f"📍 Location: {your_state}")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"🌤️  Condition: {condition}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️  Wind Speed: {wind} km/h")
    print(f"📈 Probability of rain tomorrow: {probability}")
    print(f"🗓️  Forecast: {forecast}")

    print("\n💡 Smart Suggestions")
    if condition == "Rainy":
        print("☂️  Don't forget your umbrella.")
        if humidity > 80:
            print("🧼 High humidity — stay hydrated.")
    elif condition == "Sunny":
        print("🧢 Wear sunscreen and sunglasses.")
        if temp > 35:
            print("🔥 It's super hot. Avoid going out in the afternoon.")
    elif condition == "Cloudy":
        print("🤔 Might rain, might not... carry a light jacket.")
    elif condition == "Snowy":
        print("🧤 Dress warm, roads may be slippery.")
    
    if wind > 30:
        print("🌬️ Strong winds — secure outdoor items and avoid rooftops.")
    elif wind < 5:
        print("🍃 Very calm winds — great day to fly a kite!")

    if humidity < 30:
        print("💧 Dry air — use moisturizer or drink extra water.")
    elif humidity > 85:
        print("😓 Muggy weather — take it slow.")


    return probability, forecast

probability, forecast =  weather_condition(
    current_temperature,
    current_condition,
    humidity_level,
    speed_of_wind)

today = date.today()
csv_file = "skycast_log.csv"
try:
    with open(csv_file, "r") as f:
        is_empty = f.read() == ""
except FileNotFoundError:
    is_empty = True

with open(csv_file, "a", newline="") as file:
    writer = csv.writer(file)
        
    if is_empty:
        writer.writerow([
            "Date",
            "State",
            "Temperature (°C)",
            "Condition",
            "Humidity (%)",
            "Wind Speed (km/h)",
            "Rain Probability",
            "Forecast"])
    
    writer.writerow([
        today,
        your_state,
        current_temperature,
        current_condition,
        humidity_level,
        speed_of_wind,
        probability,
        forecast])

print("\n✅ Weather data saved successfully to skycast_log.csv.")