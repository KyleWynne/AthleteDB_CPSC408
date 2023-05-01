try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

# import tkinter as tk

# class HomePage(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.titleLabel = tk.Label(self, text="Welcome to my app!")
#         self.titleLabel.pack(pady=20)

#         self.button1 = tk.Button(self, text="Search Functions", command=self.go_to_page1)
#         self.button1.pack(pady=10)

#         self.button2 = tk.Button(self, text="Add Info", command=self.go_to_page2)
#         self.button2.pack(pady=10)

#         self.button3 = tk.Button(self, text="Delete Info", command=self.go_to_page3)
#         self.button3.pack(pady=10)

#         self.button4 = tk.Button(self, text="Update Info", command=self.go_to_page4)
#         self.button4.pack(pady=10)

#     def go_to_page1(self):
#         self.master.switch_frame(Page1)

#     def go_to_page2(self):
#         self.master.switch_frame(Page2)

#     def go_to_page3(self):
#         self.master.switch_frame(Page3)

#     def go_to_page4(self):
#         self.master.switch_frame(Page4)


# class Page1(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.titleLabel = tk.Label(self, text="Page 1")
#         self.titleLabel.pack(pady=20)


# class Page2(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.titleLabel = tk.Label(self, text="Page 2")
#         self.titleLabel.pack(pady=20)


# class Page3(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.titleLabel = tk.Label(self, text="Page 3")
#         self.titleLabel.pack(pady=20)


# class Page4(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.create_widgets()

#     def create_widgets(self):
#         self.titleLabel = tk.Label(self, text="Page 4")
#         self.titleLabel.pack(pady=20)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("CPSC-408 Athlete App")
#         self.geometry("400x300")
#         self.resizable(False, False)

#         self.homePage = HomePage(self)
#         self.page1 = Page1(self)
#         self.page2 = Page2(self)
#         self.page3 = Page3

# A = App()
# A.mainloop()

# import tkinter as tk
# from tkinter import *

# Home = tk.Tk()

# int AthleteSearchCode = 0 # 1 = name, 2 = 
# int TrophySearchCode = 0 # 1 = 
# int ClubSearchCode = 0 # 1=
# int LeagueSearchCode = 0 # 1=
# int GameSearchCode = 0 #1=

# def HomePage():

#     Home.title("Athele Database App Home Menu")
#     Home.geometry('1500x500')

#     lbl = Label(Home, text="Select a button to choose What you want to do")
#     lbl.grid(column=0, row=0)

#     SearchButton = Button(Home, text="Search Functions", command=Searchclicked)
#     SearchButton.grid(column=4, row=4)


# def Searchclicked():
    
#     widget_list = all_children(Home)
#     for item in widget_list:
#         item.destroy()

#     Home.title("Athele Database App Search Menu")
#     SearchBack = Button(Home, text="Back", command = SearchBackclicked)
#     SearchBack.grid(column=0,row=1400)

#     lbl = Label(Home, text="Please Select what search method you would like to use:")
#     lbl.grid(column=0, row=0)

#     options = [
#         "Search for an Athlete",
#         "Search for a League",
#         "Search for a Club",
#         "Search for a Game",
#         "Search for an Award"
#     ]

#     Athlete_Button = Button(Home, text=options[0], command = AthleteSearch)
#     Athlete_Button.grid(column=1, row = 500)
#     League_Button = Button(Home, text=options[1], command = LeagueSearch)
#     League_Button.grid(column=50, row = 500)
#     Club_Button = Button(Home, text=options[2], command = ClubSearch)
#     Club_Button.grid(column=100, row = 500)
#     Game_Button = Button(Home, text=options[3], command = GameSearch)
#     Game_Button.grid(column=150, row = 500)
#     Award_Button = Button(Home, text=options[4], command = AwardSearch)
#     Award_Button.grid(column=200, row = 500)

#     lbl2 = Label(Home,text="Select a filter to search by")
#     lbl2.grid(column=0,row=600)


# def SearchBackclicked():
#     widget_list = all_children(Home)
#     for item in widget_list:
#         item.destroy()
    
#     HomePage()

# def AthleteSearch():
#     SubButtonDestructor()
#     OptionButton1 = Button(Home, text="Name", command=AthleteSearchName)
#     OptionButton1.grid(column=0,row=800)

# def LeagueSearch():
#     SubButtonDestructor()
#     OptionButton1 = Button(Home, text="Country", command=LeagueSearchCountry)
#     OptionButton1.grid(column=0,row=800)

# def ClubSearch():
#     SubButtonDestructor()
#     OptionButton1 = Button(Home, text="Name")
#     OptionButton1.grid(column=0,row=800)

# def GameSearch():
#     SubButtonDestructor()
#     OptionButton1 = Button(Home, text="Winner")
#     OptionButton1.grid(column=0,row=800)

# def AwardSearch():
#     SubButtonDestructor()
#     OptionButton1 = Button(Home, text="Sport")
#     OptionButton1.grid(column=0,row=800)

# def SubButtonDestructor():
#     OptionButton1.destroy()

# def AthleteSearchName():
#     AthleteSearchCode = 1

# def LeagueSearchCountry():
#     LeagueSearchCode = 1

# def all_children (window):
#     _list = window.winfo_children()

#     for item in _list:
#         if item.winfo_children():
#             _list.extend(item.winfo_children())

#     return _list

# HomePage()
# Home.mainloop()