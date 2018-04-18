from tkinter import *
from tkinter import ttk
from functions import *
from PIL import ImageTk, Image
import psycopg2

id_list = list()
id_list.append(None)

#function to search all the game with a title
def search_games():
    text_select.config(state='normal')
    text_select.delete('1.0', END)
    attribute = combobox_tag.get()
    input = entry_input.get()    
    tempcur = select_from_table("game", attribute, input)

    del id_list[:]
    if (tempcur==None):
        
        id_list.append(None)
        return
    
    new_line = False
    for (game_id,title,year,developer,publisher) in tempcur:
        id_list.append(game_id)
        if (new_line == True) :
            text_select.insert(INSERT, "\n")
        text_select.insert(INSERT, (title,year,developer,publisher))
        new_line = True
        
    text_select.config(state=DISABLED)
    
   

#function to review game
def review_game():
    gameid = int(entry_gameid.get("1.0", END))
    memid = entry_memid.get();
    score = entry_score.get();
    gamereview = entry_review.get()
    currtime = time.ctime()
    insert_review(gameid, memid, score, gamereview, currtime);
    
#function to show all games in the database
def show_games():
    text_select.config(state='normal')
    tempcur = select_all_from_table("game")
    text_select.delete('1.0', END)
    
    del id_list[:]
    new_line = False
    for (game_id,title,year,developer,publisher) in tempcur:
        id_list.append(game_id)
        if (new_line == True) :
            text_select.insert(INSERT, "\n")
        text_select.insert(INSERT, (title,year,developer,publisher))
        new_line = True
    text_select.config(state=DISABLED)

#function to show game requirements and poster at click
def callback(event):
    line_start = text_select.index("@%s,%s linestart" % (event.x, event.y))
    line_end = text_select.index("%s lineend" % line_start)
    text_select.tag_remove("highlight", 1.0, "end")
    text_select.tag_add("highlight", line_start, line_end)
    text_select.tag_configure("highlight", background="bisque")
    
    #part that shows the requirements
    text_req_select.config(state='normal')
    game_id = id_list[(int(float(line_start))-1)]
    if (game_id==None):
        return
    tempcur = select_requirements(game_id)
    text_req_select.delete('1.0', END)
    for tuple in tempcur:
        text_req_select.insert(INSERT, tuple)
        text_req_select.insert(INSERT, "\n")
    text_req_select.config(state=DISABLED)
    
    #part for game_id in reviews
    entry_gameid.config(state='normal')
    entry_gameid.delete('1.0', END)
    entry_gameid.insert(INSERT, game_id)
    entry_gameid.config(state=DISABLED)
    
    #part that changes the poster
    tempcur = select_posters(game_id)
    for tuple in tempcur:
        path = ("posters/%s.jpg"%(tuple))
    img = Image.open(path) 
    img = img.resize((img_width, img_height), Image.ANTIALIAS)  
    global image
    image = ImageTk.PhotoImage(img) 
    global image_on_canvas
    canvas.itemconfig(image_on_canvas, image = image)
    
    
#GUI functions 
#main window
frame = Tk()
#width = frame.winfo_screenwidth()-100
#height = frame.winfo_screenheight()-100
#frame.geometry("%dx%d"%(width,height))
frame.title("PIPE")

#three frames for the GUI
top_frame = Frame(frame)
top_frame.grid(row=0)
center_frame = Frame(frame)
center_frame.grid(row=1)
bottom_frame = Frame(frame)
bottom_frame.grid(row=2)


# for game search
button_search = Button(top_frame, text="search games", command=search_games)
combobox_tag = ttk.Combobox(top_frame, state="readonly", values=("title", "year", "developer", "publisher", "rating", "genre", "price")) 
combobox_tag.set("title")
entry_input = Entry(top_frame, width=50)
button_show = Button(top_frame, text="Show all games", command=show_games)
text_select = Text(center_frame, width=80, height=20, cursor='arrow')



# for requirements
text_select.bind("<Button-1>", callback)
text_req_select = Text(center_frame, width=60, height=4, cursor='arrow')


# for reviews
button_review = Button(bottom_frame, text="Review", command=review_game)
label_gameid = Label(bottom_frame, text="Game Id:")
entry_gameid = Text(bottom_frame,width = 4, height=1, state='disabled', cursor='arrow')
label_memid = Label(bottom_frame, text="Member Id:")
entry_memid = Entry(bottom_frame, width = 4)
label_score = Label(bottom_frame, text="Review Score:")
entry_score = Entry(bottom_frame, width = 4)
label_review = Label(bottom_frame, text="Review:")
entry_review = Entry(bottom_frame, width = 70)


#grid positioning
#top frame
button_search.grid(padx=(5), pady=(5), row=0,column=0)
combobox_tag.grid(padx=(5), pady=(5), row=0,column=1)
entry_input.grid(padx=(5), pady=(5), row=0,column=3)
button_show.grid(padx=(5), pady=(5), row=0, column=4)
#center frame 
text_select.grid(padx=(10,0), pady=(0,0),row=0,column=0, rowspan=2)
text_req_select.grid(padx=(10), pady=(10),row=1,column=3)
#bottom frame
button_review.grid(padx=(5), pady=(5), row=0, column=0)
label_gameid.grid(padx=(5,0), pady=(5), row=0, column=1)
entry_gameid.grid(padx=(0,5), pady=(5), row=0, column=2)
label_memid.grid(padx=(5,0), pady=(5), row=0, column=3)
entry_memid.grid(padx=(0,5), pady=(5), row=0, column=4)
label_score.grid(padx=(5,0), pady=(5), row=0, column=5)
entry_score.grid(padx=(0,5), pady=(5), row=0, column=6)
label_review.grid(padx=(5,0), pady=(5), row=0, column=7)
entry_review.grid(padx=(0,5), pady=(5), row=0, column=8)



#for scrollbar
text_select.update()
scroll_height = int(10*text_select.winfo_height()/24)
vsb = Scrollbar(center_frame, orient="vertical", command=text_select.yview)
vsb.grid(row=0, column=2, rowspan=2, ipady = scroll_height)
text_select.configure(yscrollcommand=vsb.set)


#for image
text_req_select.update()
img_width = int(text_req_select.winfo_width()/2)
img_height = int(7*text_select.winfo_height()/8)

canvas = Canvas(center_frame, width = img_width , height = img_height)      
canvas.grid(pady=(10,0),row=0, column=3)   
img = Image.open("posters/Welcome.jpg") 
img = img.resize((img_width, img_height), Image.ANTIALIAS)  
image = ImageTk.PhotoImage(img)
image_on_canvas = canvas.create_image(0,0, anchor=NW, image=image)


text_select.insert(INSERT, "Welcome!")
connect()
frame.mainloop()
