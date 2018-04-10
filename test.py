from tkinter import *
from tkinter import ttk
from functions import *
import psycopg2


#function to search all the game with a title
def search_games():
    text_select.config(state='normal')
    text_select.delete('1.0', END)
    attribute = combobox_tag.get()
    input = entry_input.get()
    
    tempcur = select_from_table("game", attribute, input)

    for tuple in tempcur:
        text_select.insert(INSERT, tuple)
        text_select.insert(INSERT, "\n")
    text_select.config(state=DISABLED)
   

#function to review game
def review_game():
    gameid = entry_gameid.get()
    gamereview = entry_review.get()
    currtime = time.ctime()
    insert_review(gameid, gamereview, currtime);
    
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
    name = entry_input.get()
    tempcur = select_requirements(name)

    text_req_select.delete('1.0', END)
    for tuple in tempcur:
        text_req_select.insert(INSERT, tuple)
        text_req_select.insert(INSERT, "\n")
    text_req_select.config(state=DISABLED)
    
def callback(event):
    line_start = text_select.index("@%s,%s linestart" % (event.x, event.y))
    line_end = text_select.index("%s lineend" % line_start)
    text_select.tag_remove("highlight", 1.0, "end")
    text_select.tag_add("highlight", line_start, line_end)
    text_select.tag_configure("highlight", background="bisque")
    
    
#GUI functions
frame = Tk()
width = frame.winfo_screenwidth()/2
height = frame.winfo_screenheight()/2
frame.geometry("%dx%d"%(width,height))
frame.state('zoomed')
frame.title("PIPE")
top_frame = Frame(frame)
top_frame.grid(row=0,column=0)
bottom_frame = Frame(frame)
bottom_frame.grid(row=1,column=0)

# for games
button_search = Button(top_frame, text="search games", command=search_games)
#label_name = Label(top_frame, text="name:")
combobox_tag = ttk.Combobox(top_frame, state="readonly", values=("title", "year", "developer", "publisher", "rating", "genre", "price")) 
combobox_tag.set("title")
#label_year = Label(top_frame, text="year:")
entry_input = Entry(top_frame)
#entry_year = Entry(top_frame)
button_show = Button(top_frame, text="Show all games", command=show_games)
#label_results = Label(top_frame, text="results")

# for requirements
req_search = Button(bottom_frame, text="search requirements", command=show_requirements)
label_req_name = Label(bottom_frame, text="name: ")
entry_req_name = Entry(bottom_frame)
#button_req_show = Button(bottom_frame, text="Show all members")

# for reviews
button_review = Button(bottom_frame, text="Review", command=review_game)
label_gameid = Label(bottom_frame, text="Game_id:")
entry_gameid = Entry(bottom_frame,width = 4)
label_review = Label(bottom_frame, text="Review:")
entry_review = Entry(bottom_frame, width = 70)




button_search.grid(row=0,column=0)
combobox_tag.grid(row=0,column=1)
#label_name.grid(row=0,column=2)
entry_input.grid(row=0,column=3)
#label_year.grid(row=0,column=3)
#entry_year.grid(row=0,column=4)
button_show.grid(row=0, column=4)
#label_results.grid(row=1, column=3)
text_select = Text(top_frame, width=100, height=20)
text_select.grid(pady=(10,100),row=1,column=3)
text_select.bind("<Button-1>", callback)
button_review.grid(row=0, column=0)
label_gameid.grid(row=0, column=1)
entry_gameid.grid(row=0, column=2)
label_review.grid(row=0, column=3)
entry_review.grid(row=0, column=4)


req_search.grid(row=1,column=0)
text_req_select = Text(bottom_frame, width=100, height=20)
text_req_select.grid(pady=(10,100),row=1,column=4)



text_select.insert(INSERT, "Welcome!")
connect()
frame.mainloop()


