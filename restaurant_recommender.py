# restaurant_recommender.py

restaurant_data = {
    "indian": ["New Jewel of India", "Spicy Punjab", "Curry House"],
    "italian": ["Mamma Mia Pizzeria", "Pasta Villa", "Roma’s Kitchen"],
    "mexican": ["El Sombrero", "Taco Fiesta", "Casa de Salsa"],
    "chinese": ["Dragon Express", "Wok This Way", "Golden Panda"],
    "japanese": ["Sushi Zen", "Ramen House", "Tokyo Table"]
}

def recommend(cuisine):
    cuisine = cuisine.lower()
    if cuisine in restaurant_data:
        print(f"\nHere are some {cuisine.capitalize()} restaurants you might enjoy:")
        for restaurant in restaurant_data[cuisine]:
            print(f"- {restaurant}")
        return True
    else:
        print("\nSorry, we don't have recommendations for that cuisine.")
        return False

def main():
    print("🍽️ Welcome to the Restaurant Recommender!")
    print("You can type a type of cuisine (like 'Indian', 'Italian', etc.) to get suggestions.")
    
    while True:
        user_input = input("\nEnter a cuisine (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Thanks for using the recommender. Goodbye!")
            break
        found = recommend(user_input)
        if found:
            more = input("\nWould you like more suggestions? (yes/no): ").strip().lower()
            if more != "yes":
                print("Okay! Come back for more recommendations anytime.")
                break

if __name__ == "__main__":
    main()
