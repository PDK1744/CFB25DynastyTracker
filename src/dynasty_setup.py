import csv

def setup_fresh_dynasty():
  # Ask for intial season details(2024)
  season_year = 2024
  coach_name = input("Enter your coach name: ")
  coach_position = input("Enter your coach position: ")
  team_name = input("Enter your team name: ")
  team_ovr = input("Enter your team overall: ")
  conference = input("Enter your conference: ")

  # Create intial csv file
  csv_file = "data/dynasty.csv"
  column_headers =  ["Season Year", "Coach Name", "Coach Position", "Team Name", "Team Overall", "Conference"]
  with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(column_headers)
    writer.writerow([season_year, coach_name, coach_position, team_name, team_ovr, conference])

def progress_to_next_season():
  # Ask for updated team and coach details
  coach_name = input("Enter your coach name(press enter to keep the same as last year ): ")
  coach_position = input("Enter your coach position(press enter to keep the same as last year ): ")
  team_name = input("Enter your team name(press enter to keep the same as last year ): ")
  team_ovr = input("Enter your team overall(press enter to keep the same as last year ): ")
  conference = input("Enter your conference(press enter to keep the same as last year ): ")

  # Read previous season data
  csv_file = "data/dynasty.csv"
  with open(csv_file, "r", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

  # Get last season's details
  last_season = data[-1]

  # Update data with the new season's details
  season_year = int(last_season[0]) + 1
  coach_name = coach_name or last_season[1]
  coach_position = coach_position or last_season[2]
  team_name = team_name or last_season[3]
  team_ovr = team_ovr or last_season[4]
  conference = conference or last_season[5]

  new_season = [str(season_year), coach_name, coach_position, team_name, team_ovr, conference]
  with open(csv_file, "a") as file:
    writer = csv.writer(file)
    writer.writerow(new_season)