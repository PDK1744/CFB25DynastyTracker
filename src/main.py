from src.dynasty_setup import setup_fresh_dynasty, progress_to_next_season
from src.utils import clear_data, view_past_seasons, view_dynasty_table


# Main program loop
def main():
    while True:
        # Print menu options
        print("1. Start a new dynasty")
        print("2. Progress to the next season")
        print("3. View Past Seasons")
        print("4. View Dynasty Table")
        print("5. Exit")
        print("6. Clear Data")
    
        # Get user choice
        choice = input("Enter your choice: ")
    
        # Handle user choice
        if choice == "1":
            setup_fresh_dynasty()
            print("Dynasty setup complete.")
            
        # Start a new dynasty
        elif choice == "2":
            progress_to_next_season()  # Progress to the next seasonf
        elif choice == "3":
            view_past_seasons()

        elif choice == "4":
            view_dynasty_table()
        # Exit the program
        elif choice == "5":
            print("Exiting the program.")
            break
        # Clear data
        elif choice == "6":
            clear_data()  # Clear data
            print("Data cleared.")
        else:
            print("Invalid choice. Please try again.")
        

        

if __name__ == "__main__":
    main()