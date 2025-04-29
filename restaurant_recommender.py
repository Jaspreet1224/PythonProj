# restaurant_recommender.py

restaurant_data = {
    "indian": ["New Jewel of India", "Taste of India", "Taj Grill"],
    "italian": ["Bella Ciao", "Lombardo", "Tappo"],
    "mexican": ["La Fiesta", "Casa Azul", "La Divina Tacos"],
    "chinese": ["Zhang Buffet", "Ling Ling", "China Taste"],
    "japanese": ["Taisho", "SATO", "Wasabi Restaurant"]
}

def recommend(cuisine):
    cuisine = cuisine.lower()
    if cuisine in restaurant_data:
        print(f"\nHere are some {cuisine.capitalize()} restaurants you might enjoy:")
        for x, restaurant in enumerate(restaurant_data[cuisine], start=1):
            print(f"{x} {restaurant}")
        return True
    else:
        print("\nSorry, we don't have recommendations for that cuisine.")
        return False


def main():
    print("🍽️ Welcome to the Buffalo, NY Restaurant Recommender!")
    print("You can type a type of cuisine (like 'Indian', 'Italian', etc.) to get suggestions.")

    while True:
        user_input = input("\nEnter a cuisine (or type 'exit' to quit): ").strip().lower()
        if user_input == "exit":
            print("Thanks for using the recommender. Goodbye!")
            break

        recommend(user_input)

        again = input("\nWould you like to search for another cuisine? (yes/no): ").strip().lower()
        if again != "yes":
            print("Okay! Come back for more recommendations anytime.")
            break

if __name__ == "__main__":
    main()
