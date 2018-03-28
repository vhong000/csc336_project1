import random
import csv

    #query = ("""CREATE TABLE requirements (
    #    game_id VARCHAR(8) NOT NULL,
    #    min_cpu VARCHAR(50),
    #    min_storage VARCHAR(50),
    #    min_ram VARCHAR(50),
    #    
    #    PRIMARY KEY (game_id),
    #    CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
    #    );""")

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

generate_req_data()
