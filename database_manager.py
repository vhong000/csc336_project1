"""
database manager program that has a simple graphic user interface to perform simple database manipulations
This program should be used to create and populate SQLite3 database in the same directory, or reset the
database by first dropping all the tables, generating new data, creating tables and finally filling up the
database with generated data. If SQLite3 file exists and it has all the necessary schemas, there is no
need to run this file
"""
from tkinter import *
from functions import *
import functions
from generate_data import *


class Config:
    """config class window was initially used to connect to postgres database,
        as it provided simple GUI for the user to input all the necessary information.
        Since SQLite doesn't require any user configurations, this class is not used."""

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        Label(top, text="Database config").grid(row=0, columnspan=2)

        self.label_user = Label(top, text="user:")
        self.user = Entry(top)
        self.label_user.grid(row=1, column=0)
        self.user.grid(row=1, column=1)
        
        self.label_password = Label(top, text="password:")
        self.password = Entry(top)
        self.label_password.grid(row=2, column=0)
        self.password.grid(row=2, column=1)
        
        self.label_host = Label(top, text="host:")
        self.host = Entry(top)
        self.host.insert(0, "127.0.0.1")
        self.label_host.grid(row=3, column=0)
        self.host.grid(row=3, column=1)
        
        self.label_database = Label(top, text="database:")
        self.database = Entry(top)
        self.label_database.grid(row=4, column=0)
        self.database.grid(row=4, column=1)
     
        b = Button(top, text="OK", command=self.ok)
        b.grid(row=5, columnspan=2)
        parent.lift()

    def ok(self):
        download_dir = "config.csv"
        config_file = open(download_dir, "w")
        columnTitleRow = "user, password, host, database\n"
        config_file.write(columnTitleRow)
        row = (self.user.get() + ',' + self.password.get() + ',' + self.host.get() + ',' + self.database.get())
        config_file.write(row)
        self.top.destroy()

class Manager(Frame):
    """Main class of the database manager program used to get user input and execute corresponding
    management commands. Names of the functions are pretty much self explanatory, while the database
    connection and query execution take place in the functions.py file"""

    def delete_all_tables(self):
        """function to drop all the relations in the database"""

        table_deleted = False
        self.text_select.delete('1.0', END)
        if (check_table_exists('requirements') == True):
            drop_table('requirements')
            self.text_select.insert(INSERT, "Table requirements dropped\n")
            table_deleted = True
        if (check_table_exists('reviews') == True):
            drop_table('reviews')
            self.text_select.insert(INSERT, "Table reviews dropped\n")
            table_deleted = True
        if (check_table_exists('friends') == True):
            drop_table('friends')
            self.text_select.insert(INSERT, "Table friends dropped\n")
            table_deleted = True
        if (check_table_exists('poster') == True):
            drop_table('poster')
            self.text_select.insert(INSERT, "Table poster dropped\n")
            table_deleted = True
        if (check_table_exists('admin') == True):
            drop_table('admin')
            self.text_select.insert(INSERT, "Table admin dropped\n")
            table_deleted = True
        if (check_table_exists('shopping_cart') == True):
            drop_table('shopping_cart')
            self.text_select.insert(INSERT, "Table shopping_cart dropped\n")
            table_deleted = True
        if (check_table_exists('member') == True):
            drop_table('member')
            self.text_select.insert(INSERT, "Table member dropped\n")
            table_deleted = True
        if (check_table_exists('game') == True):
            drop_table('game')
            self.text_select.insert(INSERT, "Table game dropped\n")
            table_deleted = True
        if (table_deleted == False):
            self.text_select.insert(INSERT, "No Tables dropped\n")

    def generate_all_data(self):
        """function to generate three data CSV file filled with 100 entries each"""

        generate_game_data()
        generate_member_data()
        generate_req_data()
        self.text_select.delete('1.0', END)
        self.text_select.insert(INSERT, "Data files generated\n")

    def create_all_teble(self):
        """function to create all the relations in the database"""

        table_created = False
        self.text_select.delete('1.0', END)
        if (check_table_exists('game') == False):
            create_game_table()
            self.text_select.insert(INSERT, "Table game created\n")
            table_created = True
        if (check_table_exists('member') == False):
            create_member_table()
            self.text_select.insert(INSERT, "Table member created\n")
            table_created = True
        if (check_table_exists('shopping_cart') == False):
            create_shopping_cart_table()
            self.text_select.insert(INSERT, "Table shopping_cart created\n")
            table_created = True
        if (check_table_exists('admin') == False):
            create_admin_table()
            self.text_select.insert(INSERT, "Table admin created\n")
            table_created = True
        if (check_table_exists('poster') == False):
            create_poster_table()
            self.text_select.insert(INSERT, "Table poster created\n")
            table_created = True
        if (check_table_exists('friends') == False):
            create_friends_table()
            self.text_select.insert(INSERT, "Table friends created\n")
            table_created = True
        if (check_table_exists('reviews') == False):
            create_reviews_table()
            self.text_select.insert(INSERT, "Table reviews created\n")
            table_created = True
        if (check_table_exists('requirements') == False):
            create_requirements_table()
            self.text_select.insert(INSERT, "Table requirements created\n")
            table_created = True
        if (table_created == False):
            self.text_select.insert(INSERT, "No Tables created\n")

    def fill_tables(self):
        """function to populate three relations in the database using data CSV files generated by
        generate_all_data function. This function requires corresponding data files to exist
        in the same directory, and all the necessary relations to be present in the database.
        Should be the last function to be called in database manager program"""

        self.text_select.delete('1.0', END)
        if (check_table_exists('game') == True):
            try:
                fill_games()
            except:
                functions.conn.rollback()
                self.text_select.insert(INSERT, "Table game could not be filled (duplicate key or no data file)\n")
        else:
            self.text_select.insert(INSERT, "Table game does not exist\n")
        if (check_table_exists('member') == True):
            try:
                fill_members()
            except:
                functions.conn.rollback()
                self.text_select.insert(INSERT, "Table member could not be filled (duplicate key or no data file)\n")
        else:
            self.text_select.insert(INSERT, "Table member does not exist\n")
        if (check_table_exists('requirements') == True):
            try:
                fill_requirements()
            except:
                functions.conn.rollback()
                self.text_select.insert(INSERT, "Table requirements could not be filled (duplicate key or no data file)\n")
        else:
            self.text_select.insert(INSERT, "Table requirements does not exist\n")
        if (check_table_exists('poster') == True):
            try:
                fill_posters()
            except:
                functions.conn.rollback()
                self.text_select.insert(INSERT, "Table poster could not be filled (duplicate key or no data file)\n")
        else:
            self.text_select.insert(INSERT, "Table poster does not exist\n")

        self.text_select.insert(INSERT, "Tables filling ended\n")

    def __init__(self, master = None):
        """GUI components of the database manager program"""

        width = root.winfo_screenwidth() / 2
        height = root.winfo_screenheight() / 2
        root.title("PIPE database manager")
        root.geometry("%dx%d" % (width, height))
        top_frame = Frame(root)
        top_frame.grid()

        button_delete_tables = Button(top_frame, text="Delete Tables", command=self.delete_all_tables)
        button_delete_tables.grid(row=0, column=0)
        button_generate_data = Button(top_frame, text="Generate Data", command=self.generate_all_data)
        button_generate_data.grid(row=0, column=1)
        button_generate_data = Button(top_frame, text="Create Tables", command=self.create_all_teble)
        button_generate_data.grid(row=0, column=2)
        button_generate_data = Button(top_frame, text="Fill Tables", command=self.fill_tables)
        button_generate_data.grid(row=0, column=3)

        self.text_select = Text(root, width=80, height=10)
        self.text_select.grid(pady=(10, 100))

        #d = Config(root)           #should be used if other database like postgres is used
        #root.wait_window(d.top)
        connect()



root = Tk()
app = Manager(master=root)
root.mainloop()