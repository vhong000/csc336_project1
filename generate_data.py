import string
import random
import csv

def generate_game_data():

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
	titles = ['Counter-Strike', 'Dota 2', 'League of Legends', 'FIFA', 'Grand Theft Auto', 'Rocket League', 'PubG', 'Burnout', 'Pokemon', 'Pong', 'Space Invaders', 'Pac-man', 'Donkey Kong', 'Frogger', 'Tetris', 'Super Mario Bros.', 'The Legend of Zelda', 'Contra', 'Mike Tyson\'s Punch-Out!!', 'Mega Man 2', 'Wolfenstein 3D', 'Super Mario Kart', 'EarthBound', 'Chrono Trigger', 'Super Mario 64', 'BioShock', 'Portal', 'Red Dead Redemption', 'Super Meat Boy', 'Dark Souls', 'Bloodborne', 'The Witcher', 'Deus Ex', 'EverQuest', 'StarCraft', 'Half-Life', 'GoldenEye 007']

	# list of descriptions
	descriptions = ['Wow what a great game!!', 'A damn good game right here', 'It\'s ok', 'Cool game full of action', 'Eyy that\'s pretty good', 'Wow Mario can jump really high!!', 'Most horrifying game of the year', 'Best seller in 5 states', 'Next level realism', 'Revolutionary game mechanics']

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
		rand_title = titles[random.randint(0, len(titles)-1)];
		rand_desc = descriptions[random.randint(0, len(descriptions)-1)];
		row = str(x) + "," + rand_title + ',' + str(rand_year) + ',' + rand_developer + ',' + rand_publisher + ',' + rand_rating + ',' + rand_genre + ',' + str(rand_price) + ',' + rand_desc + "\n"
		csv.write(row)

        
        
def generate_member_data():

	# list of names
	names = ['James', 'John', 'Robert', 'Michael', 'Mary', 'William', 'David', 'Richard', 'Charles', 'Joseph', 'Thomas', 'Patricia', 'Christopher', 'Linda', 'Barbara', 'Daniel', 'Paul', 'Mark', 'Elizabeth', 'Donald', 'Jennifer', 'George', 'Maria', 'Kenneth', 'Susan', 'Steven', 'Edward', 'Margaret', 'Brian', 'Ronald', 'Dorothy', 'Anthony', 'Lisa', 'Kevin', 'Nancy', 'Karen', 'Betty', 'Helen', 'Jason', 'Matthew', 'Gary', 'Timothy', 'Sandra', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Donna', 'Carol', 'Ruth', 'Scott', 'Eric', 'Stephen', 'Andrew', 'Sharon', 'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah', 'Jessica', 'Raymond', 'Shirley', 'Cynthia', 'Angela', 'Melissa', 'Brenda', 'Amy', 'Jerry', 'Gregory', 'Anna', 'Joshua', 'Virginia', 'Rebecca', 'Kathleen', 'Dennis', 'Pamela', 'Martha', 'Debra', 'Amanda', 'Walter', 'Stephanie', 'Willie', 'Patrick', 'Terry', 'Carolyn', 'Peter', 'Christine', 'Marie', 'Janet', 'Frances', 'Catherine', 'Harold', 'Henry', 'Douglas', 'Joyce', 'Ann', 'Diane', 'Alice', 'Jean', 'Julie']

	# list of email domains
	emails = ['@gmail.com', '@outlook.com', '@yahoo.com', '@aol.com', '@hotmail.com']

	# create csv file
	download_dir = "member_data.csv"
	csv = open(download_dir, "w")
	columnTitleRow = "member_id, name, age, balance, password, email\n"
	csv.write(columnTitleRow)

	# for loop to generate/write to csv file
	for x in range(100):
		rand_name = names[random.randint(0, len(names)-1)];
		rand_age = random.randint(5, 70);
		rand_balance = round(random.uniform(0, 200), 2);
		rand_email = rand_name + str(random.randint(0, 10)) + emails[random.randint(0, len(emails)-1)];
		rand_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
		row = str(x) + "," + rand_name + "," + str(rand_age) + "," + str(rand_balance) + "," + str(rand_password) + "," + rand_email + "\n"
		csv.write(row)

        
def generate_req_data():

# list of cpus
    cpus = ['Core i3 4th gen', 'Core i5 4th gen', 'Core i7 4th gen', 'Core i3 5th gen', 'Core i3 5th gen', 'Core i5 5th gen', 'Core i7 5th gen', 'Core i3 6th gen', 'Core i5 6th gen', 'Core i7 6th gen', 'Core i3 7th gen', 'Core i5 7th gen', 'Core i7 7th gen']

# list of ram storage
    rams = ['512mb', '1gb', '4gb', '6gb', '8gb', '12gb', '16gb', '32gb']

# create csv file
    download_dir = "req_data.csv"
    csv = open(download_dir, "w")
    columnTitleRow = "game_id, min_cpu, min_storage, min_ram\n"
    csv.write(columnTitleRow)

# for loop to generate/write to csv file
    for x in range(100):
        rand_storage = random.randint(5, 60)
        rand_ram = rams[random.randint(0, len(rams)-1)];
        rand_cpu = cpus[random.randint(0, len(cpus)-1)];
        
        row = str(x) + "," + rand_cpu + "," + str(rand_storage) + "," + rand_ram + "\n"
        csv.write(row)
