from Tkinter import *
from functions import *
import psycopg2

#config information for local database 
#(*change it to fit your database)
config = {
    "user": 'victor',
    "database": 'pipesoftdb'
}
#creating connection to the database
conn = psycopg2.connect(**config)


#Connects to the database and populates it with three entries
#next line is used if table game is already in the database (only for the purpose of testing)
#drop_table(cur, "game")
#create_table_game(cur)
#add_game(cur, "00000001","Subnautica","2018","Unknown Worlds","Someone","8.8","survival","19.99","None")
#add_game(cur, "00000002","Half Life","1995","Valve","Someone","8.5","FPS","9.99","None")
#add_game(cur, "00000003","Half Life 2","2005","Unknown Worlds","Someone","9.3","FPS","14.99","None")




#function to search all the game with a title
def search_games():
        text_select.config(state='normal')
	name = entry_name.get()
	year = entry_year.get()
	tempcur = select_from_table("game", "title", name)
	
	text_select.delete('1.0', END)
	for tuple in tempcur:
		text_select.insert(INSERT, tuple)
		text_select.insert(INSERT, "\n")
        tempcur.close
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
req_search = Button(bottom_frame, text="search requirements")
label_req_name = Label(bottom_frame, text="name: ")
entry_req_name = Entry(bottom_frame)
#button_req_show = Button(bottom_frame, text="Show all members")

button_search.grid(row=0,column=0)
label_name.grid(row=0,column=1)
entry_name.grid(row=0,column=2)
label_year.grid(row=0,column=3)
entry_year.grid(row=0,column=4)
button_show.grid(row=0, column=5)
#label_results.grid(row=1, column=3)
text_select = Text(frame, width=100, height=20)
text_select.grid(pady=(10,100))

text_req_select = Text(frame, width=100, height=20)
text_req_select.grid(pady=(10,100))
req_search.grid(row=10,column=0)

text_select.insert(INSERT, "/Search only works with title for now")
frame.mainloop()


