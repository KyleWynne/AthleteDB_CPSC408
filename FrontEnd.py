# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter 
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

import Backend as Backend
import AddObjects as AddObjects

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.Subsection_font = tkfont.Font(family='Arial', size=14, weight="bold", slant="italic")
        self.Info_font = tkfont.Font(family='Arial', size=12)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, Add_Team, Add_Athlete, Add_Award, Add_League, Add_Game):
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
        
        label = tk.Label(self, text="Welcome To The Athlete DB App", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Search Page", 
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Update Page",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Add Page", 
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Delete Page", 
                            command=lambda: controller.show_frame("PageFour"))      

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.BE = Backend.Backend()

        self.menu_options = ('Athlete','League','Award','Sport','Game')
        self.option_var = tk.StringVar(self)
        self.KeyValue = tk.StringVar(self)
        self.KeyName = tk.StringVar(self)

        label = tk.Label(self, text="Search Through our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text ="What are you searching For?", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.optionChanged
        )
        option_menu.pack()

        self.output_label = tk.Label(self, font=controller.Info_font)
        self.output_label.pack()

        label3 = tk.Label(self, text="Please Enter the key of what you are searching or use the search by name bar:", font=controller.Subsection_font)
        label3.pack()

        self.EnterKey = tk.Entry(self)
        self.EnterKey.pack()

        button2 = tk.Button(self, text="Next", command=self.KeyInput)
        button2.pack()

        label4 = tk.Label(self, text="Enter player name Here:", font=controller.Info_font)
        label4.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        button3 = tk.Button(self, text="Next", command=self.NameInput)
        button3.pack()

        label5 = tk.Label(self, font=controller.Info_font)
        label5.pack()

    def KeyInput(self, *args):
        self.KeyValue = self.BE.find_table_tuple(self.EnterKey.get())
        
    def NameInput(self, *args):
        self.KeyValue = self.BE.findID(self.option_var.get(), self.EnterName.get())
        self.label5['text'] = f'That Key # is: {self.KeyValue}'

    def optionChanged(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Make A Change To Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.menu_options = ('Athlete','League','Award','Team','Game')
        self.option_var = tk.StringVar(self)

        label = tk.Label(self, text="Add To Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text="What Type of data would you like to Add?", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.AddOptionChanged
        )
        option_menu.pack()

        button1 = tk.Button(self, text="Next",
                           command=self.NextPressedAdd)
        button1.pack()

    def AddOptionChanged(self, *args):
        pass
    
    def NextPressedAdd(self, *args):

        if self.option_var.get() == "Athlete":
            self.controller.show_frame("Add_Athlete")

        if self.option_var.get() == "League":
            self.controller.show_frame("Add_League")
        
        if self.option_var.get() == "Award":
            self.controller.show_frame("Add_Award")

        if self.option_var.get() == "Team":
            self.controller.show_frame("Add_Team")
        
        if self.option_var.get() == "Game":
            self.controller.show_frame("Add_Game")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        self.menu_options = ('Athlete','Award','Team','Game')
        self.option_var = tk.StringVar(self)

        label = tk.Label(self, text="Remove Info From Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.DelOptionChanged
        )

        option_menu.pack()

        label3 = tk.Label(self, text="Object Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        label4 = tk.Label(self, text="For games only put team 2 here: (can be left balank for all others)", font=controller.Subsection_font)
        label4.pack()

        self.EnterName2 = tk.Entry(self)
        self.EnterName2.pack()

        button2 = tk.Button(self, text="Delete",
                           command=self.DelplayerInfo)
        button2.pack()

    def DelOptionChanged(self, *args):
        pass
    
    def DelplayerInfo(self, *args):
        if self.option_var.get() == "Athlete":
            self.ErrorHandle = self.Adder.delete_tuple(1, self.EnterName.get(), self.EnterName2.get())

        if self.option_var.get() == "Team":
            self.ErrorHandle = self.Adder.delete_tuple(2, self.EnterName.get(), self.EnterName2.get())

        if self.option_var.get() == "Award":
            self.ErrorHandle = self.Adder.delete_tuple(4, self.EnterName.get(), self.EnterName2.get())

        if self.option_var.get() == "Game":
            self.ErrorHandle = self.Adder.delete_tuple(3, self.EnterName.get(), self.EnterName2.get())
        
        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            del self.Adder
            self.controller.show_frame("StartPage")



class Add_Athlete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Add An Athlete To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

        label3 = tk.Label(self, text="Player Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self,)
        self.EnterName.pack()

        label4 = tk.Label(self, text="Player Salary (without commas):", font=controller.Subsection_font)
        label4.pack()

        self.EnterSalary = tk.Entry(self,)
        self.EnterSalary.pack()

        label5 = tk.Label(self, text="Player Age:", font=controller.Subsection_font)
        label5.pack()

        self.EnterAge = tk.Entry(self,)
        self.EnterAge.pack() 

        label6 = tk.Label(self, text="Player Sport:", font=controller.Subsection_font)
        label6.pack()  

        self.EnterSport = tk.Entry(self,)
        self.EnterSport.pack()    

        label6 = tk.Label(self, text="Number of player specific acolades (MVP, Ballon d'Or, etc):", font=controller.Subsection_font)
        label6.pack()

        self.EnterTrophies = tk.Entry(self,)
        self.EnterTrophies.pack()  

        label7 = tk.Label(self, text="Team ID if no team than put 1:", font=controller.Subsection_font)
        label7.pack()

        self.EnterTeamID = tk.Entry(self,)
        self.EnterTeamID.pack() 

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Athlete(self.EnterName.get(), self.EnterSalary.get(), self.EnterAge.get(), self.EnterSport.get(), self.EnterTrophies.get(), self.EnterTeamID.get())
        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            del self.Adder
            self.controller.show_frame("PageThree")

class Add_League(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()

        label = tk.Label(self, text="Add A League To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

        label3 = tk.Label(self, text="League Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        label4 = tk.Label(self, text="League Sport:", font=controller.Subsection_font)
        label4.pack()

        self.EnterSport = tk.Entry(self)
        self.EnterSport.pack()

        label5 = tk.Label(self, text="League Counrty:", font=controller.Subsection_font)
        label5.pack()

        self.EnterCounrty = tk.Entry(self)
        self.EnterCounrty.pack() 

        self.button3 = tk.Button(self, text="Enter",
                           command=self.EnterLeagueInfo)
        self.button3.pack()
    
    def EnterLeagueInfo(self, *args):
        self.Adder.Insert_League(self.EnterName.get(), self.EnterSport.get(), self.EnterCounrty.get())
        del self.Adder
        self.controller.show_frame("PageThree")

class Add_Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Add A Game To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

        label3 = tk.Label(self, text="Team 1 ID:", font=controller.Subsection_font)
        label3.pack()

        self.EnterT1ID = tk.Entry(self)
        self.EnterT1ID.pack()

        label4 = tk.Label(self, text="Team 2 ID:", font=controller.Subsection_font)
        label4.pack()

        self.EnterT2ID = tk.Entry(self)
        self.EnterT2ID.pack()

        label5 = tk.Label(self, text="Team 1 Score:", font=controller.Subsection_font)
        label5.pack()

        self.EnterT1S = tk.Entry(self)
        self.EnterT1S.pack() 

        label6 = tk.Label(self, text="Team 2 Score:", font=controller.Subsection_font)
        label6.pack()  

        self.EnterT2S = tk.Entry(self)
        self.EnterT2S.pack()    

        label6 = tk.Label(self, text="Outcome(Win, Loss, Draw, DNF):", font=controller.Subsection_font)
        label6.pack()

        self.EnterOutcome = tk.Entry(self)
        self.EnterOutcome.pack()  

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterGameInfo)
        button3.pack()
    
    def EnterGameInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Game(self.EnterT1ID.get(), self.EnterT2ID.get(), self.EnterT1S.get(), self.EnterT2S.get(), self.EnterOutcome.get())
        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            del self.Adder
            self.controller.show_frame("PageThree")

class Add_Award(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Add A Award To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

        label3 = tk.Label(self, text="Trophy Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self,)
        self.EnterName.pack()

        label4 = tk.Label(self, text="League ID", font=controller.Subsection_font)
        label4.pack()

        self.EnterLeagueID = tk.Entry(self,)
        self.EnterLeagueID.pack()

        label5 = tk.Label(self, text="Year", font=controller.Subsection_font)
        label5.pack()

        self.EnterYear = tk.Entry(self,)
        self.EnterYear.pack() 

        label6 = tk.Label(self, text="Player ID (for a league championship put in player ID 1)", font=controller.Subsection_font)
        label6.pack()  

        self.EnterPlayerID = tk.Entry(self,)
        self.EnterPlayerID.pack()    

        label6 = tk.Label(self, text="Team ID (for a player award put in Team ID 1):", font=controller.Subsection_font)
        label6.pack()

        self.EnterTeamID = tk.Entry(self,)
        self.EnterTeamID.pack()  

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Award(self.EnterName.get(), self.EnterLeagueID.get(), self.EnterPlayerID.get(), self.EnterTeamID.get(), self.EnterYear.get())

        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team, Player or League Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            del self.Adder
            self.controller.show_frame("PageThree")
        

class Add_Team(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Add A Team To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

        label3 = tk.Label(self, text="Team Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self,)
        self.EnterName.pack()

        label4 = tk.Label(self, text="Number of Championships:", font=controller.Subsection_font)
        label4.pack()

        self.EnterChamps = tk.Entry(self,)
        self.EnterChamps.pack()

        label5 = tk.Label(self, text="League ID:", font=controller.Subsection_font)
        label5.pack()

        self.EnterLID = tk.Entry(self,)
        self.EnterLID.pack() 

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Team(self.EnterName.get(), self.EnterLID.get(), self.EnterChamps.get())

        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid League Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            del self.Adder
            self.controller.show_frame("PageThree")


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()