import csv
csv_file = "skycast_log.csv"

total_entries = 0
total_temp = 0
total_humidity = 0
condition_counts = {}
high_rain_count = 0

try:
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total_entries += 1

            temp = float(row["Temperature (°C)"])
            humidity = float(row["Humidity (%)"])
            condition = row["Condition"]
            rain_prob = row["Rain Probability"]

            total_temp += temp
            total_humidity += humidity

            if condition in condition_counts:
                condition_counts[condition] += 1
            else:
                condition_counts[condition] = 1

            if rain_prob == "High":
                high_rain_count += 1

    if total_entries > 0:
        avg_temp = total_temp / total_entries
        avg_humidity = total_humidity / total_entries
    else:
        avg_temp = 0
        avg_humidity = 0

    print("\n🛰️  SkyCast Historical Weather Summary")
    print("----------------------------------------")
    print(f"Total logged entries: {total_entries}")
    print(f"Average temperature: {avg_temp:.2f} °C")
    print(f"Average humidity: {avg_humidity:.2f} %")
    print("\nCondition counts:")
    for cond, count in condition_counts.items():
        print(f"- {cond}: {count}")
    print(f"\nTimes rain probability was HIGH: {high_rain_count}")

except FileNotFoundError:
    print("⚠️  No weather log found. Please run SkyCast and create logs first.")
