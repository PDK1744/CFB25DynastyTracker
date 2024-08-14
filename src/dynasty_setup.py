from data.at_database import get_records, create_record, update_record
from data.at_database import dynasty_tb

def setup_fresh_dynasty():
  # Ask for intial season details(2024)
  season_year = 2024
  coach_name = input("Enter your coach name: ")
  coach_position = input("Enter your coach position: ")
  team_name = input("Enter your team name: ")
  team_ovr = int(input("Enter your team overall: "))
  conference = input("Enter your conference: ")

  # Create dynasty table
  data: dict = {
    'Season Year': season_year,
    'Coach Name': coach_name,
    'Coach Position': coach_position,
    'Team Name': team_name,
    'Team Overall': team_ovr,
    'Conference': conference
  }
  create_record(dynasty_tb, data)

def progress_to_next_season():
  # Ask for updated team and coach details
  coach_name = input("Enter your coach name(press enter to keep the same as last year ): ")
  coach_position = input("Enter your coach position(press enter to keep the same as last year ): ")
  team_name = input("Enter your team name(press enter to keep the same as last year ): ")
  team_ovr = input("Enter your team overall(press enter to keep the same as last year ): ")
  conference = input("Enter your conference(press enter to keep the same as last year ): ")

  # Read previous season data
  last_season = get_records(dynasty_tb)[-1]

  # Update data with the new season's details
  season_year = int(last_season.get('Season Year', 0)) + 1
  coach_name = coach_name or last_season.get('Coach Name', '')
  coach_position = coach_position or last_season.get('Coach Position', '')
  team_name = team_name or last_season.get('Team Name', '')
  team_ovr = team_ovr or last_season.get('Team Overall', '')
  conference = conference or last_season.get('Conference', '')

  data: dict = {
    'Season Year': season_year,
    'Coach Name': coach_name,
    'Coach Position': coach_position,
    'Team Name': team_name,
    'Team Overall': team_ovr,
    'Conference': conference
  }
  update_record(dynasty_tb, last_season.get('id',''), data)