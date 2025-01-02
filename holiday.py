def hotel_cost(num_nights):
    """Calculate the total hotel cost based on the number of nights."""
    price_per_night = 100  # Adjust price per night as needed
    return num_nights * price_per_night

def plane_cost(city_flight):
    """Calculate the flight cost based on the destination city."""
    city_flight = city_flight.lower()
    if city_flight == "new york":
        return 500
    elif city_flight == "paris":
        return 400
    elif city_flight == "tokyo":
        return 700
    elif city_flight == "london":
        return 350
    elif city_flight == "dubai":
        return 600
    elif city_flight == "sydney":
        return 800
    elif city_flight == "rome":
        return 450
    elif city_flight == "mumbai":
        return 550
    elif city_flight == "cape town":
        return 750
    elif city_flight == "singapore":
        return 650
    elif city_flight == "bangkok":
        return 500
    elif city_flight == "los angeles":
        return 550
    elif city_flight == "toronto":
        return 400
    elif city_flight == "barcelona":
        return 420
    elif city_flight == "berlin":
        return 430
    elif city_flight == "amsterdam":
        return 410
    elif city_flight == "hong kong":
        return 700
    elif city_flight == "melbourne":
        return 820
    elif city_flight == "tokyo":
        return 700
    elif city_flight == "istanbul":
        return 480
    elif city_flight == "seoul":
        return 680
    elif city_flight == "buenos aires":
        return 770
    elif city_flight == "moscow":
        return 510
    else:
        return 300  # Default cost for unspecified cities

def car_rental(rental_days):
    """Calculate the car rental cost based on the number of rental days."""
    cost_per_day = 40  # Adjust cost per day as needed
    return rental_days * cost_per_day

def holiday_cost(num_nights, city_flight, rental_days):
    """Calculate the total holiday cost by combining hotel, flight, and car rental costs."""
    total_hotel = hotel_cost(num_nights)
    total_flight = plane_cost(city_flight)
    total_car = car_rental(rental_days)
    return total_hotel + total_flight + total_car

def main():
    print("Welcome to the Holiday Cost Calculator!")

    # Get user inputs
    city_flight = input("Enter the city you are flying to (e.g., New York, Paris, Tokyo, London, etc.): ").strip()
    num_nights = int(input("Enter the number of nights you will stay at the hotel: "))
    rental_days = int(input("Enter the number of days you will rent a car: "))

    # Calculate the total cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    # Print details
    print("\n--- Holiday Details ---")
    print(f"Destination City: {city_flight.capitalize()}")
    print(f"Number of Nights at Hotel: {num_nights}")
    print(f"Number of Rental Days: {rental_days}")
    print(f"Total Hotel Cost: ${hotel_cost(num_nights)}")
    print(f"Total Flight Cost: ${plane_cost(city_flight)}")
    print(f"Total Car Rental Cost: ${car_rental(rental_days)}")
    print(f"Total Holiday Cost: ${total_cost}")

if __name__ == "__main__":
    main()