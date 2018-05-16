from tkinter import *
from tkinter import ttk
from functions import *
from PIL import ImageTk, Image
#import psycopg2

class Signup_frame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, width = window_width, height = window_height, bg = 'SystemButtonFace')#'SystemButtonFace')
        self.pack_propagate(0)

        title = Frame(self)
        Label(title, text="Signup as a Member").pack(side="top")
        title.pack(side='top')

        first_line = Frame(self)
        Label(first_line, text="name:").pack(side="left")
        Entry(first_line).pack(side="left")
        first_line.pack(side="top")

        second_line = Frame(self)
        Label(second_line, text="age:").pack(side="left")
        Entry(second_line).pack(side="left")
        second_line.pack(side="top")


        third_line = Frame(self)
        Label(third_line, text="password:").pack(side="left")
        Entry(third_line).pack(side="left")
        third_line.pack(side="top")

        forth_line = Frame(self)
        Label(forth_line, text="email:").pack(side="left")
        Entry(forth_line).pack(side="left")
        forth_line.pack(side="top")



        last_line = Frame(self)
        back_button = Button(last_line, text="back", command=self.back).pack(side="left")
        submit_button = Button(last_line, text="submit", command=self.submit).pack(side="left")
        last_line.pack(side="top")


    def back(self):
        top_frame.tkraise()
        center_frame.tkraise()
        bottom_frame.tkraise()

    def submit(self):
        return



class Application(Frame):
    #function to search all the game with a title
    def search_games(self):
        self.text_select.config(state='normal')
        self.text_select.delete('1.0', END)
        attribute = self.combobox_tag.get()
        input = self.entry_input.get()
        tempcur = select_from_table("game", attribute, input)

        del self.id_list[:]
        if (tempcur==None):

            self.id_list.append(None)
            return

        new_line = False
        for (game_id,title,year,developer,publisher) in tempcur:
            self.id_list.append(game_id)
            if (new_line == True) :
                self.text_select.insert(INSERT, "\n")
            self.text_select.insert(INSERT, (title,year,developer,publisher))
            new_line = True

        self.text_select.config(state=DISABLED)


    #function to signup
    def signup(self):
        #signup_window = Signup(frame)
        #frame.wait_window(signup_window)
        signup_frame.tkraise()
        return

    #function to review game
    def review_game(self):
        gameid = int(self.entry_gameid.get("1.0", END))
        memid = self.entry_memid.get();
        score = self.entry_score.get();
        gamereview = self.entry_review.get()
        currtime = time.ctime()
        insert_review(gameid, memid, score, gamereview, currtime);

    #function to show all games in the database
    def show_games(self):
        self.text_select.config(state='normal')
        tempcur = select_all_from_table("game")
        self.text_select.delete('1.0', END)

        del self.id_list[:]
        new_line = False
        for (game_id,title,year,developer,publisher) in tempcur:
            self.id_list.append(game_id)
            if (new_line == True) :
                self.text_select.insert(INSERT, "\n")
            self.text_select.insert(INSERT, (title,year,developer,publisher))
            new_line = True
        self.text_select.config(state=DISABLED)

    #function to show game requirements and poster at click
    def callback(self, event):
        line_start = self.text_select.index("@%s,%s linestart" % (event.x, event.y))
        line_end = self.text_select.index("%s lineend" % line_start)
        self.text_select.tag_remove("highlight", 1.0, "end")
        self.text_select.tag_add("highlight", line_start, line_end)
        self.text_select.tag_configure("highlight", background="bisque")

        #part that shows the requirements
        self.text_req_select.config(state='normal')
        game_id = self.id_list[(int(float(line_start))-1)]
        if (game_id==None):
            return
        tempcur = select_requirements(game_id)
        self.text_req_select.delete('1.0', END)
        for tuple in tempcur:
            self.text_req_select.insert(INSERT, tuple)
            self.text_req_select.insert(INSERT, "\n")
        self.text_req_select.config(state=DISABLED)

        #part for game_id in reviews
        self.entry_gameid.config(state='normal')
        self.entry_gameid.delete('1.0', END)
        self.entry_gameid.insert(INSERT, game_id)
        self.entry_gameid.config(state=DISABLED)

        #part that changes the poster
        tempcur = select_posters(game_id)
        for tuple in tempcur:
            path = ("posters/%s.jpg"%(tuple))
        img = Image.open(path)
        img = img.resize((self.img_width, self.img_height), Image.ANTIALIAS)
        global image
        image = ImageTk.PhotoImage(img)
        global image_on_canvas
        self.canvas.itemconfig(image_on_canvas, image = image)


    def __init__(self, master = None):
        self.id_list = list()
        self.id_list.append(None)

        #GUI functions
        #width = frame.winfo_screenwidth()-100
        #height = frame.winfo_screenheight()-100
        #frame.geometry("%dx%d"%(width,height))
        frame.title("PIPE")


        #three frames for the GUI
        global top_frame
        top_frame = Frame(frame)
        top_frame.grid(row=0)
        global center_frame
        center_frame = Frame(frame)
        center_frame.grid(row=1)
        global bottom_frame
        bottom_frame = Frame(frame)
        bottom_frame.grid(row=2)






        # for game search
        self.button_search = Button(top_frame, text="search games", command=self.search_games)
        self.combobox_tag = ttk.Combobox(top_frame, state="readonly", values=("title", "year", "developer", "publisher", "rating", "genre", "price"))
        self.combobox_tag.set("title")
        self.entry_input = Entry(top_frame, width=50)
        self.button_show = Button(top_frame, text="Show all games", command=self.show_games)
        self.text_select = Text(center_frame, width=80, height=20, cursor='arrow')



        # for requirements
        self.text_select.bind("<Button-1>", self.callback)
        self.text_req_select = Text(center_frame, width=60, height=4, cursor='arrow')


        # for reviews
        self.button_review = Button(bottom_frame, text="Review", command=self.review_game)
        self.label_gameid = Label(bottom_frame, text="Game Id:")
        self.entry_gameid = Text(bottom_frame,width = 4, height=1, state='disabled', cursor='arrow')
        self.label_memid = Label(bottom_frame, text="Member Id:")
        self.entry_memid = Entry(bottom_frame, width = 4)
        self.label_score = Label(bottom_frame, text="Review Score:")
        self.entry_score = Entry(bottom_frame, width = 4)
        self.label_review = Label(bottom_frame, text="Review:")
        self.entry_review = Entry(bottom_frame, width = 70)

        # for signup
        self.button_signup = Button(top_frame, text="Signup", command=self.signup)




        #grid positioning
        #top frame
        self.button_search.grid(padx=(5), pady=(5), row=0,column=0)
        self.combobox_tag.grid(padx=(5), pady=(5), row=0,column=1)
        self.entry_input.grid(padx=(5), pady=(5), row=0,column=3)
        self.button_show.grid(padx=(5), pady=(5), row=0, column=4)
        self.button_signup.grid(padx=(400, 5), pady=(5), row=0, column=6)
        #center frame
        self.text_select.grid(padx=(10,0), pady=(0,0),row=0,column=0, rowspan=2)
        self.text_req_select.grid(padx=(10), pady=(10),row=1,column=3)
        #bottom frame
        self.button_review.grid(padx=(5), pady=(5), row=0, column=0)
        self.label_gameid.grid(padx=(5,0), pady=(5), row=0, column=1)
        self.entry_gameid.grid(padx=(0,5), pady=(5), row=0, column=2)
        self.label_memid.grid(padx=(5,0), pady=(5), row=0, column=3)
        self.entry_memid.grid(padx=(0,5), pady=(5), row=0, column=4)
        self.label_score.grid(padx=(5,0), pady=(5), row=0, column=5)
        self.entry_score.grid(padx=(0,5), pady=(5), row=0, column=6)
        self.label_review.grid(padx=(5,0), pady=(5), row=0, column=7)
        self.entry_review.grid(padx=(0,5), pady=(5), row=0, column=8)



        #for scrollbar
        self.text_select.update()
        self.scroll_height = int(10*self.text_select.winfo_height()/24)
        self.vsb = Scrollbar(center_frame, orient="vertical", command=self.text_select.yview)
        self.vsb.grid(row=0, column=2, rowspan=2, ipady = self.scroll_height)
        self.text_select.configure(yscrollcommand=self.vsb.set)


        #for image
        self.text_req_select.update()
        self.img_width = int(self.text_req_select.winfo_width()/2)
        self.img_height = int(7*self.text_select.winfo_height()/8)

        self.canvas = Canvas(center_frame, width = self.img_width , height = self.img_height)
        self.canvas.grid(pady=(10,0),row=0, column=3)
        img = Image.open("posters/Welcome.jpg")
        img = img.resize((self.img_width, self.img_height), Image.ANTIALIAS)
        global image
        image = ImageTk.PhotoImage(img)
        global image_on_canvas
        image_on_canvas = self.canvas.create_image(0,0, anchor=NW, image=image)

        self.text_select.insert(INSERT, "Welcome!")
        connect()

        frame.update()
        global window_height
        window_height = frame.winfo_height()
        global window_width
        window_width = frame.winfo_reqwidth()
        global signup_frame
        signup_frame = Signup_frame(parent=frame)
        signup_frame.grid(row=0, rowspan=3)

        top_frame.tkraise()
        center_frame.tkraise()
        bottom_frame.tkraise()



#main window
frame = Tk()
app = Application(master=frame)
frame.mainloop()