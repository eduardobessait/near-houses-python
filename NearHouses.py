import mysql.connector
import numpy

# Configurações do MySQL
host = "localhost"
username = "root"
password = ""
database = "urbihouses"

connectionDatabase = mysql.connector.connect(host=host, user=username, passwd=password)
cursor = connectionDatabase.cursor()

# Fetch five near houses
def fetchNearHouses(latitude, longitude):
    cursor.execute("select id, lat, long, (sqrt(pow(69.1 * (latitud - {}), 2) + pow(69.1 * ({} - longitud) * COS(latitud / 57.3), 2)) * 1.610) AS distance from urbihouses.houses having distance < 30 order by distance asc limit 5".format(latitude, longitude))
    for house in cursor:
        print("HOUSE DISTANCE ID: {}".format(house[0]))
        print("HOUSE DISTANCE URL: {}".format(house[1]))
        print("HOUSE DISTANCE COORDS: {}, {}".format(house[2], house[3]))
        print("HOUSE DISTANCE CALCULATED: {}".format(house[4]))
        print("------------------------------------------------------------------ /// ------------------------------------------------------")

# Fetch house
def fetchHouse():
    cursor.execute("select id, link, latitud, longitud from uda.scraper_back limit 1")
    for house in cursor:
        print("HOUSE ID: {}".format(house[0]))
        print("HOUSE URL: {}".format(house[1]))
        print("HOUSE COORDS: {}, {}".format(house[2], house[3]))
        print("------------------------------------------------------------------ DISTANCE ------------------------------------------------------")
        print("------------------------------------------------------------------ DISTANCE ------------------------------------------------------")
        print("------------------------------------------------------------------ DISTANCE ------------------------------------------------------")
        fetchNearHouses(house[2], house[3])

fetchHouse()

#fetchNearHouses(40.689909, -8.479886)
