"""
OceanWatch: Simple GPS tracking prototype for fishing boats.
"""

class Boat:
    def __init__(self, boat_id, latitude, longitude):
        self.boat_id = boat_id
        self.latitude = latitude
        self.longitude = longitude

    def update_location(self, lat, lon):
        self.latitude = lat
        self.longitude = lon

    def get_location(self):
        return (self.latitude, self.longitude)

def main():
    boat = Boat("Boat123", 22.345, 90.234)
    print(f"Current location of {boat.boat_id}: {boat.get_location()}")
    # Simulate location update
    boat.update_location(22.350, 90.240)
    print(f"Updated location of {boat.boat_id}: {boat.get_location()}")

if __name__ == "__main__":
    main()
