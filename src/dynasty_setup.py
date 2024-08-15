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
  # Read previous season data
  
  records = get_records(dynasty_tb)
  if not records:
    print("No records found in dynasty_tb!")
    return
  last_season = records[-1]
  print(last_season)
  # Ask for updated team and coach details
  coach_name = (input("Enter your coach name (press enter to keep the same as last year ): ") or last_season['fields'].get('Coach Name', ''))
  coach_position = (input("Enter your coach position (press enter to keep the same as last year ): ") or last_season['fields'].get('Coach Position', ''))
  team_name = (input("Enter your team name (press enter to keep the same as last year ): ") or last_season['fields'].get('Team Name', ''))
  team_ovr = int(input("Enter your team overall (press enter to keep the same as last year ): ") or last_season['fields'].get('Team Overall', 0))
  conference = (input("Enter your conference (press enter to keep the same as last year ): ") or last_season['fields'].get('Conference', ''))

  

  # Update data with the new season's details
  #season_year = int(last_season.get('Season Year', 0)) + 1
  season_year = last_season['fields']['Season Year'] + 1
  coach_name = coach_name or last_season['fields'].get('Coach Name', '')
  coach_position = coach_position or last_season['fields'].get('Coach Position', '')
  team_name = team_name or last_season['fields'].get('Team Name', '')
  #team_ovr = team_ovr or last_season.get('Team Overall', '')
  conference = conference or last_season['fields'].get('Conference', '')

  data: dict = {
    'Season Year': season_year,
    'Coach Name': coach_name,
    'Coach Position': coach_position,
    'Team Name': team_name,
    'Team Overall': team_ovr,
    'Conference': conference
  }
  dynasty_tb.create(data)
  #update_record(dynasty_tb, last_season.get('id',''), data)