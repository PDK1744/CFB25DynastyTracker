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

  # Update data with the new season's details
  season_year = int(data[-1][0]) + 1
  if coach_name: data[-1][1] = coach_name
  if coach_position: data[-1][2] = coach_position
  if team_name: data[-1][3] = team_name
  if team_ovr: data[-1][4] = team_ovr
  if conference: data[-1][5] = conference

  with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)