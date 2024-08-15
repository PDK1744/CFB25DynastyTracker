import csv
import pandas as pd
import airtable as at
from pyairtable import Table
import sys
sys.path.insert(0, './data/at_database')
from data.at_database import base_id, api

def clear_data():

  print("Are you sure you want to clear? This will wipe everything")
  confirm = input("Enter yes to clear; enter no to return to menu: ")
  if confirm.lower() == "yes":
    tables_to_clear = ["dynasty", "players"]
    for table_name in tables_to_clear:
      table = Table(api, base_id, table_name)
      records = table.all()
      record_ids = [record['id'] for record in records]
      table.batch_delete(record_ids)
    
  

def view_past_seasons():
  df = pd.read_csv("data/dynasty.csv")
    
  # Printing avaialble seasons
  print("Past Seasons:")
  for i, season in enumerate(df["Season Year"].unique(), start=1):
    print(f"{i}. Season {season}")

  # Asking user to select a season
  season_choice = input("Enter the number of the season you want to view: ")
  selected_season = df["Season Year"].unique()[int(season_choice) - 1]

  # Filter the DataFrame to show only the selected season's data
  season_data = df[df["Season Year"] == selected_season]

  # Print the selected season's data
  print(season_data)

# View full dynasty table
def view_dynasty_table():
  df = pd.read_csv("data/dynasty.csv")
  print(df)