"""
This file combines all the functions that can access nd modify the database. Both programs use this
file to execute necessary operations on the database. If any other file would use following functions
it first must call connect() function to create a connection to the database. SQLite3 is used as the
database for this program, if there is any intent to use postgres there are few minor differences in the
syntax which must corrected first. There is one trigger in this database, additional information is available
by inspecting create_reviews_table() function
"""
import csv
import sqlite3


def connect():
    '''     #this commented section can be used to connect to the postgres database.
    with open('config.csv', 'r') as config_data:
        reader = csv.reader(config_data)
        next(config_data)
        row = next(reader)
        config = {
                    "user": row[0],
                    "password": row[1],
                    "host": row[2],
                    "database": row[3]
                } 
    global conn
    conn = psycopg2.connect(**config)
    '''
    try:
        global conn
        conn = sqlite3.connect('SQLite3.db')
        cursor = conn.cursor()
        cursor.execute("""PRAGMA foreign_keys = ON;""")


    except sqlite3.Error as e:
        print(e)
    return None;


#function names are self explanatory
#query in each function is a string that will be passed to cursors execute() function
#notice this does not run the query until connections commit() function is called

def check_table_exists(tablename):
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE name = '%s'" %(tablename))  #FROM information_schema.tables WHERE table_name = '%s'
    if cur.fetchone()[0] == 1:
        cur.close()
        return True

    cur.close()
    return False

def drop_table(table):
    cur = conn.cursor()
    query = ("Drop table %s" %(table))
    cur.execute(query)
    print("table %s dropped" %(table))
    conn.commit()
    cur.close()

def create_game_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE game (
    game_id VARCHAR(8) NOT NULL, 
    title VARCHAR(50) NOT NULL, 
    year INT NOT NULL, 
    developer VARCHAR(50), 
    publisher VARCHAR(50), 
    rating VARCHAR NOT NULL, 
    genre VARCHAR(50), 
    price FLOAT, 
    description VARCHAR(50),            
    PRIMARY KEY (game_id)
    );""")
    cur.execute(query)
    print("table game created")
    conn.commit()
    cur.close()

def create_member_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE member (
    member_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    balance FLOAT,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,

    PRIMARY KEY (member_id)
    );""")
    cur.execute(query)
    print("table member created")
    conn.commit()
    cur.close()

def create_shopping_cart_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE shopping_cart (
    member_id VARCHAR(8) NOT NULL,
    num_of_items INT,
    game_id VARCHAR(8) NOT NULL,

    PRIMARY KEY (member_id, game_id),
    CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id),
    CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
    );""")
    cur.execute(query)
    print("table shopping_cart created")
    conn.commit()
    cur.close()

def create_admin_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE admin (
    admin_id VARCHAR(8) NOT NULL,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    rank INT NOT NULL,
    
    PRIMARY KEY (admin_id)
    );""")
    cur.execute(query)
    print("table admin created")
    conn.commit()
    cur.close()

def create_poster_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE poster (
    game_id VARCHAR(8) NOT NULL,
    link VARCHAR(100) NOT NULL,
    
    PRIMARY KEY(game_id),
    CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
    );""")
    cur.execute(query)
    print("table poster created")
    conn.commit()
    cur.close()

def create_friends_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE friends (
    member_id VARCHAR(8) NOT NULL,
    friend_id VARCHAR(8) NOT NULL,
    
    PRIMARY KEY (member_id, friend_id),
    CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id),
    CONSTRAINT no_friend FOREIGN KEY (friend_id) REFERENCES member(member_id)
    );""")
    cur.execute(query)
    print("table friends created")
    conn.commit()
    cur.close()

def create_reviews_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE reviews (
    game_id VARCHAR(8) NOT NULL,
    member_id VARCHAR(8) NOT NULL,
    score FLOAT,
    feedback VARCHAR(200) NOT NULL,
    time TIMESTAMP NOT NULL,
    
    PRIMARY KEY (game_id, member_id),
    CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id),
    CONSTRAINT no_member FOREIGN KEY (member_id) REFERENCES member(member_id)
    );""")
    cur.execute(query)
    cur.execute("""CREATE TRIGGER reviews_trig AFTER insert ON reviews
                   BEGIN
                   update reviews SET time = datetime('now') WHERE game_id = NEW.game_id  and member_id = NEW.member_id;
                   END;""")
    print("table reviews created")
    conn.commit()
    cur.close()

def create_requirements_table():
    cur = conn.cursor()
    query = ("""CREATE TABLE requirements (
    game_id VARCHAR(8) NOT NULL,
    min_cpu VARCHAR(50),
    min_storage VARCHAR(50),
    min_ram VARCHAR(50),
    
    PRIMARY KEY (game_id),
    CONSTRAINT no_game FOREIGN KEY (game_id) REFERENCES game(game_id)
    );""")
    cur.execute(query)
    print("table requirements created")
    conn.commit()
    cur.close()

def add_game(game_id,title,year,developer,publisher,rating,genre,price,description):
    cur = conn.cursor()
    query = ("INSERT INTO game (game_id,title,year,developer,publisher,rating,genre,price,description) VALUES ('%s', '%s', '%s','%s', '%s', '%s','%s', '%s', '%s')" %(game_id, title, year, developer, publisher, rating, genre, price, description))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_member(id, name, age, balance, password, email):
    cur = conn.cursor()
    query = ("INSERT INTO member (member_id, name, age, balance, password, email) VALUES ('%s','%s','%s','%s','%s','%s')" %(id, name, age, balance, password, email))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_shopping_cart(id, num_of_items, game_ids):
    cur = conn.cursor()
    query = ("INSERT INTO shopping_cart (id, num_of_items, game_ids) VALUES ('%s', '%s', '%s')" %(id, num_of_items, game_ids))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_admin(admin_id, name, email, password, rank):
    cur = conn.cursor()
    query = ("INSERT INTO admin (admin_id, name, email, password, rank) VALUES ('%s', '%s', '%s', '%s', '%s')" %(admin_id, name, email, password, rank))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_poster(game_id, link):
    cur = conn.cursor()
    query = ("INSERT INTO poster (game_id, link) VALUES ('%s', '%s')" %(game_id, link))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_friend(id, friend_id):
    cur = conn.cursor()
    query = ("INSERT INTO friends (id, friend_id) VALUES ('%s', '%s')" %(id, friend_id))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_review(game_id, id, score, feedback, datetime):
    cur = conn.cursor()
    query = ("INSERT INTO reviews (game_id, member_id, score, feedback, time) VALUES ('%s', '%s', '%s', '%s', '%s')" %(game_id, id, score, feedback, datetime))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_requirements(game_id, min_cpu, min_storage, min_ram):
    cur = conn.cursor()
    query = ("INSERT INTO requirements (game_id, min_cpu, min_storage, min_ram) VALUES ('%s', '%s', '%s', '%s', '%s')" %(game_id, min_cpu, min_storage, min_ram))
    cur.execute(query)
    conn.commit()
    cur.close()

def add_player_number(game_id, single, online, local_co_op, online_co_op):
    cur = conn.cursor()
    query = ("INSERT INTO player_number (game_id, single, online, local_co_op, online_co_op) VALUES ('%s', '%s', '%s', '%s', '%s')" %(game_id, single, online, local_co_op, online_co_op))
    cur.execute(query)
    conn.commit()
    cur.close()

def fill_games():
    cur = conn.cursor()
    with open('game_data.csv', 'r') as games:
        reader = csv.reader(games)
        next(games)
        for row in reader:
            cur.execute("INSERT INTO game (game_id,title,year,developer,publisher,rating,genre,price,description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            row
            )
    conn.commit()
    cur.close()


def fill_members():
    cur = conn.cursor()
    with open('member_data.csv', 'r') as members:
        reader = csv.reader(members)
        next(members)
        for row in reader:
            cur.execute("INSERT INTO member (member_id, name, age, balance, password, email) VALUES (?, ?, ?, ?, ?, ?)",
            row
            )
    conn.commit()
    cur.close()

def fill_requirements():
    cur = conn.cursor()
    with open('req_data.csv', 'r') as reqs:
        reader = csv.reader(reqs)
        next(reqs)
        for row in reader:
            cur.execute("INSERT INTO requirements (game_id, min_cpu, min_storage, min_ram) VALUES (?, ?, ?, ?)",
            row
            )
    conn.commit()
    cur.close()
    
def fill_posters():
    cur = conn.cursor()
    query = ("Select game_id,title from game")
    cur.execute(query)
    for (game_id, title) in cur:
        add_poster(game_id, title)    
    

#functions to retrive values from the database
def select_all_from_table(table):
    cur = conn.cursor()
    query = ("Select game_id,title,year,developer,publisher from %s" %(table))
    cur.execute(query)
    conn.commit()
    return cur

def select_from_table(table, attribute, value):
    cur = conn.cursor()
    if(value==""):
        return None
    if (attribute == "year" or attribute == "price"):
        if (not value.isnumeric()):
            return None
        else :
            query = ("Select game_id,title,year,developer,publisher from %s where %s = '%s'" %(table, attribute, value))
            cur.execute(query)
    else:
        query = ("Select game_id,title,year,developer,publisher from %s where %s = '%s' COLLATE NOCASE" %(table, attribute, value))
                 #UPPER(%s) ~ UPPER('%s') %(table, attribute, value))
        cur.execute(query)
    
    conn.commit()
    return cur

def select_requirements(game_id):
    cur = conn.cursor()
    query = ("Select title,year,min_cpu,min_storage,min_ram FROM (game NATURAL JOIN requirements) WHERE game_id = '%s'" %(game_id))
    cur.execute(query)
    return cur

def select_posters(game_id):
    cur = conn.cursor()
    query = ("Select link FROM poster WHERE game_id = '%s'" %(game_id))
    cur.execute(query)
    return cur

def select_greatest_user_id():
    cur = conn.cursor()
    query = ("Select member_id FROM member order by member_id desc")
    cur.execute(query)
    row = cur.fetchone()
    return row[0]

def select_email(email):
    cur = conn.cursor()
    query = ("Select count(1) from member where email='%s'" %(email))
    cur.execute(query)
    row = cur.fetchone()
    if (row[0] == 1):
        return True
    else:
        return False

#login
def login_user(email, password):
    cur = conn.cursor()
    query = ("Select count(1) from member where email='%s' and password='%s'" %(email, password))
    cur.execute(query)
    conn.commit()
    row = cur.fetchone();
    if (row[0] == 1):
        query = ("select member_id from member where email='%s'" %(email));
        cur.execute(query);
        row = cur.fetchone();
        mem_id = row[0];
        return mem_id;
    else:
        return False;
