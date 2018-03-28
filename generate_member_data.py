import string
import random
import csv

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
