import os
from airtable import Airtable


api = os.environ['AIRTABLE_API_KEY']
base_id = 'appma4DOFT5y1SKZj'

# Intiialize Airtable API
at = Airtable(base_id, api)

# Tables in database
dynasty_tb = at.table('tbliY8sJ1soWJGd1k')
player_tb = at.table('tbllJfb2sg6CDSqCR')
offense_roster_tb = at.table('tblp9LrDb8CLGpJhH')
defense_roster_tb = at.table('tblGgrmaE7wHEc4dZ')
special_roster_tb = at.table('tblJncPBDsNN6cfVH')

def get_records(table):
  try:
      return list(table.iterate())
  except Exception as e:
      print(f"Error getting records: {table}: {e}")
      return None

def create_record(table, data):
  try:
      return table.create(data)
  except Exception as e:
      print(f"Error creating record: {e}")
      return None

def update_record(table, record_id, data):
  try:
      return table.update(record_id, data)
  except Exception as e:
      print(f"Error updating record: {e}")
      return None

def delete_record(table, record_id):
  try:
      return table.delete(record_id)
  except Exception as e:
      print(f"Error deleting record: {e}")
      return None