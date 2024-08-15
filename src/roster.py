from data.at_database import get_records, create_record, update_record
from data.at_database import offense_roster_tb

def setup_offense_roster():
  # Input for player details
  position = input("Enter the position of the player: ")
  player_name = input("Enter the name of the player: ")
  player_overall = input("Enter the overall of the player: ")
  player_dev = input("Enter the dev trait of the player: ")
  player_depth_spot = input("Enter the players depth chart spot: ")

  # Create Offense Roster table
  data: dict = {
    'Position': position,
    'Player Name': player_name,
    'Player Overall': player_overall,
    'Player Dev': player_dev,
    'Player Depth Spot': player_depth_spot
  }
  create_record(offense_roster_tb, data)