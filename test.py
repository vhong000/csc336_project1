from tkinter import *
from functions import *
import psycopg2


#function to search all the game with a title
def search_games():
    text_select.config(state='normal')
    name = entry_name.get()
    year = entry_year.get()
    if (name == "" and year != ""):
        tempcur = select_from_table("game", "year", year)
    elif (name != "" and year == ""):
        tempcur = select_from_table("game", "title", name)

    text_select.delete('1.0', END)
    for tuple in tempcur:
        text_select.insert(INSERT, tuple)
        text_select.insert(INSERT, "\n")
    text_select.config(state=DISABLED)

#function to show all games in the database
def show_games():
    text_select.config(state='normal')
    tempcur = select_all_from_table("game")

    text_select.delete('1.0', END)
    for tuple in tempcur:
        text_select.insert(INSERT, tuple)
        text_select.insert(INSERT, "\n")
    text_select.config(state=DISABLED)

def show_requirements():
    text_req_select.config(state='normal')
    name = entry_name.get()
    tempcur = select_requirements(name)

    text_req_select.delete('1.0', END)
    for tuple in tempcur:
        text_req_select.insert(INSERT, tuple)
        text_req_select.insert(INSERT, "\n")
    text_req_select.config(state=DISABLED)

    
class MyDialog:

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


    
#GUI functions
frame = Tk()
width = frame.winfo_screenwidth()/2
height = frame.winfo_screenheight()/2
frame.title("PIPE")
frame.geometry("%dx%d"%(width,height))
top_frame = Frame(frame)
top_frame.grid()
bottom_frame = Frame(frame)
bottom_frame.grid()

# for games
button_search = Button(top_frame, text="search games", command=search_games)
label_name = Label(top_frame, text="name:")
label_year = Label(top_frame, text="year:")
entry_name = Entry(top_frame)
entry_year = Entry(top_frame)
button_show = Button(top_frame, text="Show all games", command=show_games)
#label_results = Label(top_frame, text="results")

# for requirements
req_search = Button(bottom_frame, text="search requirements", command=show_requirements)
label_req_name = Label(bottom_frame, text="name: ")
entry_req_name = Entry(bottom_frame)
#button_req_show = Button(bottom_frame, text="Show all members")

button_search.grid(row=0,column=0)
label_name.grid(row=0,column=1)
entry_name.grid(row=0,column=2)
#label_year.grid(row=0,column=3)
#entry_year.grid(row=0,column=4)
button_show.grid(row=0, column=5)
#label_results.grid(row=1, column=3)
text_select = Text(frame, width=100, height=20)
text_select.grid(pady=(10,100))

req_search.grid(row=1,column=0)
text_req_select = Text(frame, width=100, height=20)
text_req_select.grid(pady=(10,100))

text_select.insert(INSERT, "/Search only works with title for now")

d = MyDialog(frame)
frame.wait_window(d.top)
connect()


frame.mainloop()



