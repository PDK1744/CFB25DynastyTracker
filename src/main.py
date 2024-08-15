from src.dynasty_setup import setup_fresh_dynasty, progress_to_next_season
from src.roster import setup_offense_roster
from src.utils import clear_data, view_past_seasons, view_dynasty_table


# Main program loop
def main():
    while True:
        # Print menu options
        print("1. Start a new dynasty")
        print("2. Add player to Offense Roster")
        print("3. Add player to Defense Roster")
        print("4. Add player to Special Teams Roster")
        print("5. View Offense Roster")
        print("6. View Defense Roster")
        print("7. View Special Teams Roster")
        print("8. Progress to the next season")
        print("9. View Past Seasons")
        print("10. View Dynasty Table")
        print("11. Exit")
        print("12. Clear Data")
    
        # Get user choice
        choice = input("Enter your choice: ")
    
        # Handle user choice
        if choice == "1":
            setup_fresh_dynasty()
            print("Dynasty setup complete.")
        # Add player to Offense Roster
        elif choice == "2":
            setup_offense_roster()
            # Add print statement here
        
        # Add player to Defense Roster
        elif choice == "3":
            # Add code to add player to Defense Roster
            # Add print statement here
            pass
        # Add player to Special Teams Roster
        elif choice == "4":
            # Add code to add player to Special Teams Roster
            # Add print statement here
            pass

        # View Offense Roster
        elif choice == "5":
            # Add code to view Offense Roster
            # Add print statement here
            pass
        # View Defense Roster
        elif choice == "6":
            # Add code to view Defense Roster
            # Add print statement here
            pass

        # View Special Teams Roster
        elif choice == "7":
            # Add code to view Special Teams Roster
            # Add print statement here
            pass
            
        # Start a new dynasty
        elif choice == "8":
            progress_to_next_season()  # Progress to the next seasonf
        elif choice == "9":
            view_past_seasons()

        elif choice == "10":
            view_dynasty_table()
        # Exit the program
        elif choice == "11":
            print("Exiting the program.")
            break
        # Clear data
        elif choice == "12":
            clear_data()  # Clear data
            print("Data cleared.")
        else:
            print("Invalid choice. Please try again.")
        

        

if __name__ == "__main__":
    main()