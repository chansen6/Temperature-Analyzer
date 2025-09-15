temperature_list = [87, 80, 69, 72, 82, 80]

def calculate_temperature(temp):
    total = sum(temp)
    avg = total / len(temp)
    high = max(temp)
    low = min(temp)

    return {
        "Total": total,
        "Average": avg,
        "Highest": high,
        "Lowest": low
    }

def print_report(temp, stats):
    print("\n Temperature Report ")
    print("All readings:", temperature_list)
    print("Total:", stats["Total"])
    print("Average:", stats["Average"])
    print("Highest:", stats["Highest"])
    print("Lowest:", stats["Lowest"])

stats = calculate_temperature(temperature_list)
print_report(temperature_list, stats)