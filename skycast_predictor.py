import csv

csv_file = "skycast_log.csv"

current_condition = input("Enter today's weather condition (Sunny / Cloudy / Rainy / Snowy): ").capitalize()
current_humidity = float(input("Enter today's humidity (%): "))

total_similar = 0
rain_prob_counts = {
    "High": 0,
    "Medium": 0,
    "Low": 0,
    "Uncertain": 0}

try:
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            condition = row["Condition"]
            humidity = float(row["Humidity (%)"])
            rain_prob = row["Rain Probability"]

            if condition == current_condition and abs(humidity - current_humidity) <= 10:
                total_similar += 1
                if rain_prob in rain_prob_counts:
                    rain_prob_counts[rain_prob] += 1

    if total_similar == 0:
        print("\n⚠️ No similar past records found. Prediction is uncertai")
    else:
        print(f"\n🔍 Found {total_similar} similar days in your history.")

        most_common_prob = max(rain_prob_counts, key=rain_prob_counts.get)
        
        print(f"\n📈 Prediction based on historical data:")
        print(f"Likely rain probability: {most_common_prob}")

        print("\n🧪 Breakdown:")
        for prob, count in rain_prob_counts.items():
            print(f"- {prob}: {count}")

except FileNotFoundError:
    print("⚠️ Weather log file not found. Please log data with SkyCast first.")
