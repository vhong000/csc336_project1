import random 
import csv

# list of years
years = [2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981, 1980, 1979, 1978, 1977, 1976, 1975]

# list of prices
prices = [60.00, 30.00, 45.00, 15.00, 5.00, 80.00, 35.00]

# list of ratings
ratings = ['E', 'E10', 'T', 'M', 'A']

# list of developers
developers = ['2K Games', '3D Realms', 'Activision', 'Bandai Namco Studios', 'Bethesda Game Studios', 'BioWare', 'Blizzard Entertainment', 'Bohemia Interactive', 'Capcom', 'CD Projekt Red', 'Crytek', 'DICE Los Angeles', 'Double Fine Productions', 'Eidos Interactive', 'Electronic Arts', 'Epic Games', 'Frontier Developments', 'Game Freak', 'Harebrained Schemes', 'id Software', 'Irrational Games', 'Koei', 'Konami', 'LucasArts']

# list of publishers
publishers = ['Nintendo', 'Ubisoft', 'Electronic Arts', 'Sony', 'Square Enix', 'Microsoft', 'Bandai Namco Games', 'Activision Blizzard', 'Telltale Games', 'Konami', 'Capcom', 'Paradox Interactive']

# list of genres
genres = ['Action-Adventure', 'Action', 'Adventure', 'Card Battle', 'Casual', 'Puzzle', 'Rhythm', 'Role-Playing', 'Simulation', 'Strategy', 'Racing']

# list of games
title = ['Counter-Strike', 'Dota 2', 'League of Legends', 'FIFA', 'Grand Theft Auto', 'Rocket League', 'PubG', 'Burnout', 'Pokemon', 'Pong', 'Space Invaders', 'Pac-man', 'Donkey Kong', 'Frogger', 'Tetris', 'Super Mario Bros.', 'The Legend of Zelda', 'Contra', 'Mike Tyson\'s Punch-Out!!', 'Mega Man 2', 'Wolfenstein 3D', 'Super Mario Kart', 'EarthBound', 'Chrono Trigger', 'Super Mario 64', 'BioShock', 'Portal', 'Red Dead Redemption', 'Super Meat Boy', 'Dark Souls', 'Bloodborne', 'The Witcher', 'Deus Ex', 'EverQuest', 'StarCraft', 'Half-Life', 'GoldenEye 007']

# create csv file
download_dir = "game_data.csv"
csv = open(download_dir, "w")
columnTitleRow = "game_id, title, year, developer, publisher, rating, genre, price, description\n"
csv.write(columnTitleRow)

# for loop to generate/write to csv file
for x in range(100):
   rand_year = years[random.randint(0, len(years)-1)];
   rand_price = prices[random.randint(0, len(prices)-1)];
   rand_rating = ratings[random.randint(0, len(ratings)-1)];
   rand_developer = developers[random.randint(0, len(developers)-1)];
   rand_publisher = publishers[random.randint(0, len(publishers)-1)];
   rand_genre = genres[random.randint(0, len(genres)-1)];
   rand_title = title[random.randint(0, len(title)-1)];
   row = str(x) + "," + rand_title + ',' + str(rand_year) + ',' + rand_developer + ',' + rand_publisher + ',' + rand_rating + ',' + rand_genre + ',' + str(rand_price) + "\n"
   csv.write(row)
