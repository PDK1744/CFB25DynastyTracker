import os
from pyairtable import Api

api = Api(os.environ['patKRD3tZfLUqI86J.e345abc9f4c38a1bb9bf0feb684253f6d7c1a73c363ee11ed28292ab93fb655b'])
# Tables in database
dynasty_tb = api.table('appma4DOFT5y1SKZj', 'tbl9Z1y2J2QiYc5kP')
player_tb = api.table('appma4DOFT5y1SKZj', 'tbllJfb2sg6CDSqCR')
offense_roster_tb = api.table('appma4DOFT5y1SKZj', 'tblp9LrDb8CLGpJhH')
defense_roster_tb = api.table('appma4DOFT5y1SKZj', 'tblGgrmaE7wHEc4dZ')
special_roster_tb = api.table('appma4DOFT5y1SKZj','tblJncPBDsNN6cfVH')