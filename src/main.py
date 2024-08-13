from src.dynasty_setup import setup_fresh_dynasty, progress_to_next_season

# Main program loop
def main():
    while True:
        # Print menu options
        print("1. Start a new dynasty")
        print("2. Progress to the next season")

        # Get user choice
        choice = input("Enter your choice: ")

        # Handle user choice
        if choice == "1":
            setup_fresh_dynasty()
            print("Dynasty setup complete.")
            print("About to print CSV file contents...")
            with open('data/dynasty.csv', 'r') as file:
                print(file.read())
        # Start a new dynasty
        elif choice == "2":
            progress_to_next_season()  # Progress to the next season
        else:
            print("Invalid choice. Please try again.")

        

if __name__ == "__main__":
    main()