

def clear_data():
  files_to_clear = ["data/dynasty.csv", "data/player_stats.csv"]

  for file in files_to_clear:
    with open(file, "w"):
      pass
  
  