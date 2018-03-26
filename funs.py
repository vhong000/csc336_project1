#All the functions to manipulate database
#functions to create and drop tables
def drop_table(cursor, table):
    query = ("Drop table %s" %(table))
    cursor.execute(query)
    
def create_table_game(cursor):
    query = ("""CREATE TABLE game (
    game_id VARCHAR(8) NOT NULL,
    title VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    developer VARCHAR(50),
    publisher VARCHAR(50),
    rating FLOAT NOT NULL,
    genre VARCHAR(50), 
    price FLOAT, 
    description VARCHAR(50),
    PRIMARY KEY (game_id)
    );""")
    cursor.execute(query)
	
def create_table_member(cursor):
    query = ("""CREATE TABLE member (
    member_id VARCHAR(8) NOT NULL,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    balance FLOAT,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,	
    PRIMARY KEY (member_id)
    );""")
    cursor.execute(query)


def create_table_shopping_cart(cursor):
    query = ("""CREATE TABLE shopping_cart (
    member_id VARCHAR(8) NOT NULL,
    num_of_items INT,
    game_id VARCHAR(8) NOT NULL,
    PRIMARY KEY (member_id, game_id),
    CONSTRAINT no_member FOREIGN KEY\
    (member_id) REFERENCES member(member_id),
    CONSTRAINT no_game FOREIGN KEY\
    (game_id) REFERENCES game(game_id)
    );""")
    cursor.execute(query)

def create_table_admin(cursor):
    query = ("""CREATE TABLE admin (
    admin_id VARCHAR(8) NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    rank INT NOT NULL,			
    PRIMARY KEY (admin_id)
    );""")
    cursor.execute(query)
	
def create_table_poster(cursor):
    query = ("""CREATE TABLE poster (
    game_id VARCHAR(8) NOT NULL,
    link VARCHAR(100) NOT NULL,	
    PRIMARY KEY(game_id),
    CONSTRAINT no_game FOREIGN KEY\
    (game_id) REFERENCES game(game_id)
    );""")
    cursor.execute(query)
	
def create_table_friends(cursor):
    query = ("""CREATE TABLE friends (
    member_id VARCHAR(8) NOT NULL,
    friend_id VARCHAR(8) NOT NULL,				
    PRIMARY KEY (member_id, friend_id),
    CONSTRAINT no_member FOREIGN\
    KEY (member_id) REFERENCES member(member_id),
    CONSTRAINT no_friend FOREIGN\
    KEY (friend_id) REFERENCES member(member_id)
    );""")
    cursor.execute(query)
	
def create_table_reviews(cursor):
    query = ("""CREATE TABLE reviews (
    game_id VARCHAR(8) NOT NULL,
    member_id VARCHAR(8) NOT NULL,
    score FLOAT,
    feedbck VARCHAR(200) NOT NULL,
    time TIMESTAMP NOT NULL,				
    PRIMARY KEY (member_id, time),
    CONSTRAINT no_game FOREIGN KEY\
    (game_id) REFERENCES game(game_id),
    CONSTRAINT no_member FOREIGN KEY\
    (member_id) REFERENCES member(member_id)
    );""")
    cursor.execute(query)

def create_table_requirements(cursor):
    query = ("""CREATE TABLE requirements (
    game_id VARCHAR(8) NOT NULL,
    min_cpu VARCHAR(50),
    min_storage VARCHAR(50),
    min_ram VARCHAR(50),
    min_gpu VARCHAR(50),				
    PRIMARY KEY (game_id),
    CONSTRAINT no_game FOREIGN\
    KEY (game_id) REFERENCES game(game_id)
    );""")
    cursor.execute(query)

	
	
#functions to add a tuple into table	
def add_game(cur, game_id,title,year,\
    developer,publisher,rating,genre,price,description):
    query = ("""INSERT INTO game (game_id, 
    title, year, developer, publisher, 
    rating,genre,price,description) VALUES
    ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s')"""\
    %(game_id, title, year, developer,
    publisher, rating, genre, price, description))
    cur.execute(query)

def add_member(cur, member_id, name,\
    age, balance, password, email):
    query = (""""INSERT INTO member (
    member_id, name, age, balance,
    password, email) VALUES (
    '%s','%s','%s','%s','%s','%s')"""\
    %(member_id, name, age,
    balance, password, email))
    cur.execute(query)

def add_shopping_cart(cur, member_id,\
    num_of_items, game_ids):
    query = ("""INSERT INTO shopping_cart (
    member_id, num_of_items, game_ids) 
    VALUES ('%s', '%s', '%s')"""\
    %(member_id, num_of_items, game_ids))
    cur.execute(query)

def add_admin(cur, admin_id, name,\
    email, password, rank):
    query = ("""INSERT INTO admin (
    admin_id, name, email, password,
    rank) VALUES ('%s', '%s', '%s', '%s', '%s')"""\
    %(admin_id, name, email, password, rank))
    cur.execute(query)

def add_poster(cur, game_id, link):
    query = ("""INSER INTO posters (
    game_id, link) VALUES ('%s', '%s')"""\
    %(game_id, link))
    cur.execute(query)

def add_friend(cur, member_id, friend_id):
    query = ("INSERT INTO friends (\
    member_id, friend_id) VALUES\
    ('%s', '%s')" %(member_id, friend_id))
    cur.execute(query)

def add_review(cur, game_id, member_id,\
    score, feedback, datetime):
    query = ("""INSERT INTO reviews (
    game_id, member_id, score,
    feedback, date/time)"""\
    %(game_id, member_id, score,\
    feedback, data/time))
    cur.execute(query)

def add_requirements(cur, game_id,\
    min_cpu, min_storage, min_ram):
    query = ("""INSERT INTO requirements 
    (game_id, min_cpu, min_storage,
    min_ram)""" %(game_id, min_cpu,\
    min_storage, min_ram))
    cur.execute(query)

def add_player_number(cur, game_id,\
    single, online, local_co_op, online_co_op):
    query = ("""INSERT INTO player_number (
    game_id, single, online, local_co_op,
    online_co_op)""" %(game_id, single,\
    online, local_co_op, online_co_op))
    cur.execute(query)

	
#functions to retrive values from the database
def select_all_from_table(cursor, table):
	query = ("""Select * from %s""" %(table))
	cursor.execute(query)
	return cursor
    #for tuple in cursor:
    #    print(f"{tuple}")

def select_from_table(cursor, table, attribute, value):
	query = ("""Select * from %s where %s='%s'""" %(table, attribute, value))
	cursor.execute(query)
	return cursor
    #for tuple in cursor:
    #    print(f"{tuple}")

