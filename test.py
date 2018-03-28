from Tkinter import *
from functions import *
import psycopg2



#function to search all the game with a title
def search_games():
	name = entry_name.get()
	year = entry_year.get()
	tempcur = select_from_table("game", "title", name)
	
	text_select.delete('1.0', END)
	for tuple in tempcur:
		text_select.insert(INSERT, tuple)
		text_select.insert(INSERT, "\n")
	tempcur.close
	
#function to show all games in the database
def show_games():
	tempcur = select_all_from_table("game")
	
	text_select.delete('1.0', END)
	for tuple in tempcur:
		text_select.insert(INSERT, tuple)
		text_select.insert(INSERT, "\n")
	

#GUI functions
frame = Tk()
width = frame.winfo_screenwidth()/2
height = frame.winfo_screenheight()/2
frame.title("PIPE")
frame.geometry("%dx%d"%(width,height))
top_frame = Frame(frame)
top_frame.grid()
button_search = Button(top_frame, text="search games", command=search_games)
label_name = Label(top_frame, text="name:")
label_year = Label(top_frame, text="year:")
entry_name = Entry(top_frame)
entry_year = Entry(top_frame)
button_show = Button(top_frame, text="Show all games", command=show_games)


button_search.grid(row=0,column=0)
label_name.grid(row=0,column=1)
entry_name.grid(row=0,column=2)
label_year.grid(row=0,column=3)
entry_year.grid(row=0,column=4)
button_show.grid(row=0, column=5)
text_select = Text(frame, width=80, height=10)
text_select.grid(pady=(10,100))

text_select.insert(INSERT, "/Search only works with title for now")
frame.mainloop()


