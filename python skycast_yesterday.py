import csv
csv_file = "skycast_log.csv"
try:
    with open(csv_file, "r") as file:
        reader = list(csv.DictReader(file))
        
        if not reader:
            print("⚠️ No previous records found.")
        else:
            last_entry = reader[-1]

            print("\n🗓️ Yesterday's SkyCast Weather Record")
            print("--------------------------------------")
            print(f"📍 State: {last_entry['State']}")
            print(f"🌡️  Temperature: {last_entry['Temperature (°C)']}°C")
            print(f"🌤️  Condition: {last_entry['Condition']}")
            print(f"💧 Humidity: {last_entry['Humidity (%)']}%")
            print(f"🌬️  Wind Speed: {last_entry['Wind Speed (km/h)']} km/h")
            print(f"📈 Rain Probability: {last_entry['Rain Probability']}")
            print(f"📝 Forecast: {last_entry['Forecast']}")

except FileNotFoundError:
    print("⚠️ Weather log file not found. Run SkyCast at least once to create it.")
