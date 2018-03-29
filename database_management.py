from tkinter import *
from functions import *
from generate_data import *
import psycopg2

def delete_all_tables():
    table_deleted = False
    text_select.delete('1.0', END)
    if (check_table_exists('requirements') == True):
        drop_table('requirements')
        text_select.insert(INSERT, "Table requirements dropped\n")
        table_deleted = True
    if (check_table_exists('reviews') == True):
        drop_table('reviews')
        text_select.insert(INSERT, "Table reviews dropped\n")
        table_deleted = True
    if (check_table_exists('friends') == True):
        drop_table('friends')
        text_select.insert(INSERT, "Table friends dropped\n")
        table_deleted = True
    if (check_table_exists('poster') == True):
        drop_table('poster')
        text_select.insert(INSERT, "Table poster dropped\n")
        table_deleted = True
    if (check_table_exists('admin') == True):
        drop_table('admin')
        text_select.insert(INSERT, "Table admin dropped\n")
        table_deleted = True
    if (check_table_exists('shopping_cart') == True):
        drop_table('shopping_cart')
        text_select.insert(INSERT, "Table shopping_cart dropped\n")
        table_deleted = True
    if (check_table_exists('member') == True):
        drop_table('member')
        text_select.insert(INSERT, "Table member dropped\n")
        table_deleted = True
    if (check_table_exists('game') == True):
        drop_table('game')
        text_select.insert(INSERT, "Table game dropped\n")
        table_deleted = True
    if (table_deleted == False):
        text_select.insert(INSERT, "No Tables dropped\n")

def generate_all_data():
    generate_game_data()
    generate_member_data()
    generate_req_data()
    text_select.delete('1.0', END)
    text_select.insert(INSERT, "Data files generated\n")
    
def create_all_teble():
    table_created = False
    text_select.delete('1.0', END)
    if (check_table_exists('game') == False):
        create_game_table()
        text_select.insert(INSERT, "Table game created\n")
        table_created = True
    if (check_table_exists('member') == False):
        create_member_table()
        text_select.insert(INSERT, "Table member created\n")
        table_created = True
    if (check_table_exists('shopping_cart') == False):
        create_shopping_cart_table()
        text_select.insert(INSERT, "Table shopping_cart created\n")
        table_created = True
    if (check_table_exists('admin') == False):
        create_admin_table()
        text_select.insert(INSERT, "Table admin created\n")
        table_created = True
    if (check_table_exists('poster') == False):
        create_poster_table()
        text_select.insert(INSERT, "Table poster created\n")
        table_created = True
    if (check_table_exists('friends') == False):
        create_friends_table()
        text_select.insert(INSERT, "Table friends created\n")
        table_created = True
    if (check_table_exists('reviews') == False):
        create_reviews_table()
        text_select.insert(INSERT, "Table reviews created\n")
        table_created = True
    if (check_table_exists('requirements') == False):
        create_requirements_table()
        text_select.insert(INSERT, "Table requirements created\n")
        table_created = True
    if (table_created == False):
        text_select.insert(INSERT, "No Tables created\n")

def fill_tables():
    text_select.delete('1.0', END)
    if (check_table_exists('game') == True):
        try:
            fill_games()
        except:
            conn.rollback()
            text_select.insert(INSERT, "Table game could not be filled (most likely duplicate key)\n")
    else:
        text_select.insert(INSERT, "Table game does not exist\n")
    if (check_table_exists('member') == True):
        try:
            fill_members()
        except:
            conn.rollback()
            text_select.insert(INSERT, "Table member could not be filled (most likely duplicate key)\n")
    else:
        text_select.insert(INSERT, "Table member does not exist\n")
    if (check_table_exists('requirements') == True):
        try:
            fill_requirements()
        except:
            conn.rollback()
            text_select.insert(INSERT, "Table requirements could not be filled (most likely duplicate key)\n")
    else:
        text_select.insert(INSERT, "Table requirements does not exist\n")
    text_select.insert(INSERT, "Tables filling ended\n")

frame = Tk()
width = frame.winfo_screenwidth()/2
height = frame.winfo_screenheight()/2
frame.title("PIPE database manager")
frame.geometry("%dx%d"%(width,height))
top_frame = Frame(frame)
top_frame.grid()


button_delete_tables = Button(top_frame, text="Delete Tables", command=delete_all_tables)
button_delete_tables.grid(row=0,column=0)
button_generate_data = Button(top_frame, text="Generate Data", command=generate_all_data)
button_generate_data.grid(row=0,column=1)
button_generate_data = Button(top_frame, text="Create Tables", command=create_all_teble)
button_generate_data.grid(row=0,column=2)
button_generate_data = Button(top_frame, text="Fill Tables", command=fill_tables)
button_generate_data.grid(row=0,column=3)

text_select = Text(frame, width=80, height=10)
text_select.grid(pady=(10,100))


frame.mainloop()
