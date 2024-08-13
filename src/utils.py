import csv

def clear_data():
  files_to_clear = ["data/dynasty.csv", "data/player.csv"]
  print("Are you sure you want to clear? This will wipe everything")
  confirm = input("Enter yes to clear; enter no to return to menu: ")
  if confirm.lower() == "yes":
    for file in files_to_clear:
      with open(file, "w"):
        pass
  else:
    print("Data not cleared")
  

def view_past_seasons():
  csv_file = "data/dynasty.csv"
  with open(csv_file, "r", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)
    
  # Printing avaialble seasons
  print("Past Seasons:")
  for i, season in enumerate(data[1:]):
    print(f"{i}. Season {season[0]}")

  # Asking user to select a season
  season_choice = input("Enter the number of the season you want to view: ")
  selected_season = data[int(season_choice)]

  # Ask user what value they would like to view
  print("What would youo like to view?")
  print("1. All season details")
  print("2. Coach Name")
  print("3. Coach Position")
  print("4. Team Name")
  print("5. Team OVR")
  print("6. Conference")

  view_choice = int(input("Enter number of your choice: "))

  if view_choice == 1:
    # Print all details
    print("Season Details:")
    print(f"Year: {selected_season[0]}")
    print(f"Coach Name: {selected_season[1]}")
    print(f"Coach Position: {selected_season[2]}")
    print(f"Team Name: {selected_season[3]}")
    print(f"Team OVR: {selected_season[4]}")
    print(f"Conference: {selected_season[5]}")

  else:
    # Print selected data
    data_labels = ["Year", "Coach Name", "Coach Position", "Team Name", "Team OVR", "Conference"]
    print(f"{data_labels[view_choice - 1]}:{selected_season[view_choice - 1]}")