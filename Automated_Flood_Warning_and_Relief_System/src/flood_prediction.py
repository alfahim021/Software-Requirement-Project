"""
Automated Flood Warning and Relief System
Simple prototype for water level monitoring and alert.
"""

def check_water_level(level, threshold=5.0):
    """
    Check if water level crosses threshold.
    """
    if level >= threshold:
        return "Flood Warning: Water level is high!"
    else:
        return "Water level is normal."

if __name__ == "__main__":
    # Example usage
    current_level = float(input("Enter current water level (m): "))
    alert = check_water_level(current_level)
    print(alert)
