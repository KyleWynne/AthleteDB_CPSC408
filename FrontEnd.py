# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter 
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

import Backend as Backend
import AddObjects as AddObjects

#class to host and organize the other frames
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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, Add_Team, Add_Athlete, Add_Award, Add_League, Add_Game, AboutPage, Update_Game, Update_Team, Update_Athlete, Update_Award, view, export, fancy_search):
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

#start page that serves as a hub for the whole system
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Welcome To The Athlete DB App", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        #create the menu buttons
        button1 = tk.Button(self, text="Search Page", 
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Update Page",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Add Page", 
                            command=lambda: controller.show_frame("PageThree"))
        button4 = tk.Button(self, text="Delete Page", 
                            command=lambda: controller.show_frame("PageFour")) 
        button6 = tk.Button(self, text="View All", 
                            command=lambda: controller.show_frame("view")) 
        button7 = tk.Button(self, text="Export", 
                            command=lambda: controller.show_frame("export"))
        button5 = tk.Button(self, text="About Page", 
                            command=lambda: controller.show_frame("AboutPage"))     
        button8 = tk.Button(self, text="Fancy Search", 
                            command=lambda: controller.show_frame("fancy_search")) 

        button1.pack()
        button8.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button6.pack()
        button7.pack()        
        button5.pack()

#This is the basic search page
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        #create a list of menu options and instantiate objects
        self.menu_options = ('Athlete','League','Award','Team','Game')
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
        #create the dropdown menu
        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.optionChanged
        )
        option_menu.pack()

        self.output_label = tk.Label(self, font=controller.Info_font)
        self.output_label.pack()
        #labels display instructions and the Entry field collects user data that is typed
        label3 = tk.Label(self, text="Please Enter the Name of what you are searching: ", font=controller.Subsection_font)
        label3.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        label4 = tk.Label(self, text="Enter Team 2 name Here (only for games):", font=controller.Info_font)
        label4.pack()

        self.EnterName2 = tk.Entry(self)
        self.EnterName2.pack()

        button3 = tk.Button(self, text="Search", command=self.NameInput)
        button3.pack()
        #ouput Label label is updated when the button is pressed
        self.label5 = tk.Label(self, font=controller.Info_font)
        self.label5.pack()
        
    def NameInput(self, *args):
        #determine what function to use based off the dropdown menu
        #this code only runs when the button is pressed
        if self.option_var.get() == "Athlete":
            self.KeyValue = self.Adder.find_table_tuple(1, self.EnterName.get(), self.EnterName2.get())
            self.label5['text'] = f'That Key Data is: {self.KeyValue}'
        
        if self.option_var.get() == "League":
            self.KeyValue = self.Adder.find_table_tuple(5, self.EnterName.get(), self.EnterName2.get())
            self.label5['text'] = f'That Key Data is: {self.KeyValue}'

        if self.option_var.get() == "Game":
            self.KeyValue = self.Adder.find_table_tuple(3, self.EnterName.get(), self.EnterName2.get())
            self.label5['text'] = f'That Key Data is: {self.KeyValue}'

        if self.option_var.get() == "Award":
            self.KeyValue = self.Adder.find_table_tuple(4, self.EnterName.get(), self.EnterName2.get())
            self.label5['text'] = f'That Key Data is: {self.KeyValue}'

        if self.option_var.get() == "Team":
            self.KeyValue = self.Adder.find_table_tuple(2, self.EnterName.get(), self.EnterName2.get())
            self.label5['text'] = f'That Key Data is: {self.KeyValue}'

    def optionChanged(self, *args):
        pass
        # self.output_label['text'] = f'You selected: {self.option_var.get()}'

#update home page
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menu_options = ('Athlete','Award','Team','Game')
        self.option_var = tk.StringVar(self)

        label = tk.Label(self, text="Make A Change To Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text="What Type of data would you like to Change?", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.UpdateOptionChanged
        )
        option_menu.pack()

        button1 = tk.Button(self, text="Next",
                           command=self.NextPressedUpdate)
        button1.pack()

    def UpdateOptionChanged(self, *args):
        pass
    #use a dropdown menu and button to take the user to the nescessary page
    #each table needs their own page because the fields vary
    def NextPressedUpdate(self, *args):

        if self.option_var.get() == "Athlete":
            self.controller.show_frame("Update_Athlete")
        
        if self.option_var.get() == "Award":
            self.controller.show_frame("Update_Award")

        if self.option_var.get() == "Team":
            self.controller.show_frame("Update_Team")
        
        if self.option_var.get() == "Game":
            self.controller.show_frame("Update_Game")

#update page specifically for the athlete table
class Update_Athlete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #setup objects including object that calls functions from the AddObjects Class
        self.menu_options = ('Name','Salary','Age','Sport', 'Number of Trophies', 'Team')
        self.option_var = tk.StringVar(self)
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #Create instruction fields and inputs
        label = tk.Label(self, text="Update Player Information", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Page",
                           command=lambda: self.controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                           command=lambda: self.controller.show_frame("PageTwo"))
        button1.pack()

        label2 = tk.Label(self, text="What Aspect Would you like to Change?", font=self.controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.AthleteOptionChanged
        )
        option_menu.pack()
        #use the name to find a key and get the record that they want
        label1 = tk.Label(self, text="Type The Name Of The Player You Would Like To Update", font=self.controller.Subsection_font)
        label1.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()
        #get the new data with a second entry field at the same time so both the search and the update can be done at the same time
        label3 = tk.Label(self, text="Type Your New Value Here", font=self.controller.Subsection_font)
        label3.pack()

        self.EnterValue = tk.Entry(self)
        self.EnterValue.pack()

        button2 = tk.Button(self, text="Enter", command=self.UpdateEnterPressed)
        button2.pack()
    
    def AthleteOptionChanged(self, *args):
        pass
    #runs when the button is pressed 
    def UpdateEnterPressed(self, *args):
        #determine what the field being updated is based off the dropdown menu
        #then scrape the data that was typed for both the name and the updated field
        if self.option_var.get() == "Name":
            self.ErrorHandle = self.Adder.update_records(1, 1, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")
        
        if self.option_var.get() == "Salary":
            self.ErrorHandle = self.Adder.update_records(1, 2, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")            

        if self.option_var.get() == "Team":
            self.ErrorHandle = self.Adder.update_records(1, 6, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")

        if self.option_var.get() == "Age":
            self.ErrorHandle = self.Adder.update_records(1, 3, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")

        if self.option_var.get() == "Sport":
            self.ErrorHandle = self.Adder.update_records(1, 4, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")

        if self.option_var.get() == "Number of Trophies":
            self.ErrorHandle = self.Adder.update_records(1, 5, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")

#update page specifically for the team
class Update_Team(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #code used from previous frames with different list values
        self.menu_options = ('Name', 'Number of Trophies')
        self.option_var = tk.StringVar(self)
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Update Team Information", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageTwo"))
        button1.pack()

        label2 = tk.Label(self, text="What Aspect Would you like to Change?", font=self.controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.TeamOptionChanged
        )
        option_menu.pack()

        label1 = tk.Label(self, text="Type The Name Of The Team You Would Like To Update", font=self.controller.Subsection_font)
        label1.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        label3 = tk.Label(self, text="Type Your New Value Here", font=self.controller.Subsection_font)
        label3.pack()

        self.EnterValue = tk.Entry(self)
        self.EnterValue.pack()

        button2 = tk.Button(self, text="Enter", command=self.UpdateEnterPressed)
        button2.pack()
    
    def TeamOptionChanged(self, *args):
        pass

    def UpdateEnterPressed(self, *args):
        #run update functions based off the fields above
        #if a faulty input is given nothing happens on the front end
        if self.option_var.get() == "Name":
            self.ErrorHandle = self.Adder.update_records(2, 1, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")
        
        if self.option_var.get() == "Number of Trophies":
            self.ErrorHandle = self.Adder.update_records(2, 2, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")               

#update page specifically for trophies
class Update_Award(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #code used from earlier update functions with new list values
        self.menu_options = ('Most Recent Player Winner','Most Recent Team Winner')
        self.option_var = tk.StringVar(self)
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Update Award Information", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageTwo"))
        button1.pack()

        label2 = tk.Label(self, text="What Aspect Would you like to Change?", font=self.controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.AwardOptionChanged
        )
        option_menu.pack()

        label1 = tk.Label(self, text="Type The Name Of The Award You Would Like To Update", font=self.controller.Subsection_font)
        label1.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()

        label3 = tk.Label(self, text="Type Your New Value Here", font=self.controller.Subsection_font)
        label3.pack()

        self.EnterValue = tk.Entry(self)
        self.EnterValue.pack()

        button2 = tk.Button(self, text="Enter", command=self.UpdateEnterPressed)
        button2.pack()

    def AwardOptionChanged(self, *args):
        pass

    def UpdateEnterPressed(self, *args):
        #run update functions with the user inputs from above
        if self.option_var.get() == "Most Recent Player Winner":
            self.ErrorHandle = self.Adder.update_records(4, 1, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")
        
        if self.option_var.get() == "Most Recent Team Winner":
            self.ErrorHandle = self.Adder.update_records(4, 2, self.EnterValue.get(), self.EnterName.get(), "")
            self.controller.show_frame("PageTwo")    

#update page for games
class Update_Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #used code from earlier with 1 exeception
        self.menu_options = ('Team 1 Score','Team 2 Score','Outcome')
        self.option_var = tk.StringVar(self)
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)

        label = tk.Label(self, text="Update Game Information", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("PageTwo"))
        button1.pack()

        label2 = tk.Label(self, text="What Aspect Would you like to Change?", font=self.controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.GameOptionChanged
        )
        option_menu.pack()

        label1 = tk.Label(self, text="Type The Names Of The Teams Who Played (You will only update their most recent game)", font=self.controller.Subsection_font)
        label1.pack()

        self.EnterName = tk.Entry(self)
        self.EnterName.pack()
        #second name field because we need both team names to find the specific game that a user would like to alter
        self.EnterName2 = tk.Entry(self)
        self.EnterName2.pack()

        label3 = tk.Label(self, text="Type Your New Value Here", font=self.controller.Subsection_font)
        label3.pack()

        self.EnterValue = tk.Entry(self)
        self.EnterValue.pack()

        button2 = tk.Button(self, text="Enter", command=self.UpdateEnterPressed)
        button2.pack()

    def GameOptionChanged(self, *args):
        pass

    def UpdateEnterPressed(self, *args):
        #update function takes input from all 4 sources unlike the previous update pages
        if self.option_var.get() == "Team 1 Score":
            self.ErrorHandle = self.Adder.update_records(3, 1, self.EnterValue.get(), self.EnterName.get(), self.EnterName2.get())
            self.controller.show_frame("PageTwo")
        
        if self.option_var.get() == "Team 2 Score":
            self.ErrorHandle = self.Adder.update_records(3, 2, self.EnterValue.get(), self.EnterName.get(), self.EnterName2.get())
            self.controller.show_frame("PageTwo") 
        
        if self.option_var.get() == "Outcome":
            self.ErrorHandle = self.Adder.update_records(3, 3, self.EnterValue.get(), self.EnterName.get(), self.EnterName2.get())
            self.controller.show_frame("PageTwo") 

#add data homepage        
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #hub page for the insert functions since each table has different collumns and numbers of collumns
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
        #take the user to the specific add page they need to go to with the dropdown menu  and next button
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

#delete page (all data on this frame since we just need to find the tuple and delete in the Backend)
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #Delete objects from the list we do not allow league deletion
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
        #this input line is only for games since its the only one we need 2 names to find
        label4 = tk.Label(self, text="For games only put team 2 here: (can be left balank for all others)", font=controller.Subsection_font)
        label4.pack()

        self.EnterName2 = tk.Entry(self)
        self.EnterName2.pack()

        button2 = tk.Button(self, text="Delete",
                           command=self.DelplayerInfo)
        button2.pack()

    def DelOptionChanged(self, *args):
        pass

    #once we have info collected from the fields find and delete tuple 
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
            self.controller.show_frame("StartPage")

#Add page specifically for athlete
class Add_Athlete(tk.Frame):

    def __init__(self, parent, controller):
        #instantiate objects
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #create an entry field and instructions for each piece of data needed
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
        #for individual athletes like gold have them put a 1 in to assign them to a ghost team
        label7 = tk.Label(self, text="Team Name if no team than put 1:", font=controller.Subsection_font)
        label7.pack()

        self.EnterTeamID = tk.Entry(self,)
        self.EnterTeamID.pack() 

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    #runs the entry code and has error handling for if a team name given was not in the system
    #for a player to be on a team that team must be in our system prior to the player being inserted
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Athlete(self.EnterName.get(), self.EnterSalary.get(), self.EnterAge.get(), self.EnterSport.get(), self.EnterTrophies.get(), self.EnterTeamID.get())
        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            
            self.controller.show_frame("PageThree")

#Add a league to the database
class Add_League(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        #pritn all fields with instructions
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
    #there is no error handling since there are no foreign keys in this table
    def EnterLeagueInfo(self, *args):
        self.Adder.Insert_League(self.EnterName.get(), self.EnterSport.get(), self.EnterCounrty.get())
        
        self.controller.show_frame("PageThree")

#add a game to the database
class Add_Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #put in info on a game TEAM sports only
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

        label3 = tk.Label(self, text="Team 1 Name:", font=controller.Subsection_font)
        label3.pack()

        self.EnterT1ID = tk.Entry(self)
        self.EnterT1ID.pack()

        label4 = tk.Label(self, text="Team 2 Name:", font=controller.Subsection_font)
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

    #insert into the games table and check that both team names are valid if one is not it will put a message up
    def EnterGameInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Game(self.EnterT1ID.get(), self.EnterT2ID.get(), self.EnterT1S.get(), self.EnterT2S.get(), self.EnterOutcome.get())
        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            
            self.controller.show_frame("PageThree")

#add an award to the database
class Add_Award(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #awards fields and instructions there is no null league since every sport is played in some type of league
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

        label4 = tk.Label(self, text="League Name", font=controller.Subsection_font)
        label4.pack()

        self.EnterLeagueID = tk.Entry(self,)
        self.EnterLeagueID.pack()

        label5 = tk.Label(self, text="Year", font=controller.Subsection_font)
        label5.pack()

        self.EnterYear = tk.Entry(self,)
        self.EnterYear.pack() 
        #for player specific awards put in player name here and a 1 in team name fo our querys can distinguish between the two
        label6 = tk.Label(self, text="Player Name (for a league championship put in player ID 1)", font=controller.Subsection_font)
        label6.pack()  

        self.EnterPlayerID = tk.Entry(self,)
        self.EnterPlayerID.pack()    
        #same for team but switched and championship must have a one for player name
        label6 = tk.Label(self, text="Team Name (for a player award put in Team ID 1):", font=controller.Subsection_font)
        label6.pack()

        self.EnterTeamID = tk.Entry(self,)
        self.EnterTeamID.pack()  

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    #insert with error handling for all three different foreign keys
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Award(self.EnterName.get(), self.EnterLeagueID.get(), self.EnterPlayerID.get(), self.EnterTeamID.get(), self.EnterYear.get())

        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid Team, Player or League Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            
            self.controller.show_frame("PageThree")     

#add a team to the database
class Add_Team(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        self.ErrorHandle = tk.StringVar(self)
        #add a team to the system there is one foreign key which is the league name
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
        #the league entered here must exist in the system if it doesnt an error will be thrown
        label5 = tk.Label(self, text="League Name:", font=controller.Subsection_font)
        label5.pack()

        self.EnterLID = tk.Entry(self,)
        self.EnterLID.pack() 

        button3 = tk.Button(self, text="Enter",
                           command=self.EnterplayerInfo)
        button3.pack()
    #try the insert if the league is not in the system it will throw an error
    def EnterplayerInfo(self, *args):
        self.ErrorHandle = self.Adder.Insert_Team(self.EnterName.get(), self.EnterLID.get(), self.EnterChamps.get())

        if self.ErrorHandle == "invalid input":
            label8 = tk.Label(self, text="Invalid League Name", font=self.controller.Subsection_font)
            label8.pack()
        else:
            self.controller.show_frame("PageThree")

#about page to show all of the quirks of the system
class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #create labels to show important information about the system
        label = tk.Label(self, text="About This System", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label1 = tk.Label(self, text="How to Insert:", font=controller.Subsection_font)
        label1.pack()

        label3 = tk.Label(self, text="There is a hierarchy for inserting league->team->player,awards,games; games are only between two TEAMS individual sports will not be reprisented  ", font=controller.Info_font)
        label3.pack()

        label4 = tk.Label(self, text="this is because for a player to be on a team or a team to be in a league that object must already exist", font=controller.Info_font)
        label4.pack()

        label5 = tk.Label(self, text="How to Search:", font=controller.Subsection_font)
        label5.pack()

        label6 = tk.Label(self, text="There are two types: a normal and fancy search", font=controller.Info_font)
        label6.pack()

        label7 = tk.Label(self, text="a classic will retuen one record while the fancy searches are more specific and can return many records", font=controller.Info_font)
        label7.pack()

        label8 = tk.Label(self, text="for view all records and fancy search sometimes the output doesnt show up till a second search is also used", font=controller.Info_font)
        label8.pack()

        label9 = tk.Label(self, text="How to Delete:", font=controller.Subsection_font)
        label9.pack()

        label10 = tk.Label(self, text="you can delete a record by typing the name, if the page does not change then that record could not be found", font=controller.Info_font)
        label10.pack()

        label11 = tk.Label(self, text="How to Update:", font=controller.Subsection_font)
        label11.pack()

        label12 = tk.Label(self, text="you can update a record by typing the name, but you cannot update a league's information", font=controller.Info_font)
        label12.pack()

        label13 = tk.Label(self, text="How to Export:", font=controller.Subsection_font)
        label13.pack()

        label14 = tk.Label(self, text="you can choose a table and hit export to have a csv file made in the current directory with all the values in that table", font=controller.Info_font)
        label14.pack()

#view all page shows all tupes in a table with joins to show names from foreign keys
class view(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        #List options we will not display all games
        self.menu_options = ('Athlete','League','Team','Team Award', 'Player Award')
        self.option_var = tk.StringVar(self)
        self.KeyValue = tk.StringVar(self)
        self.KeyName = tk.StringVar(self)

        label = tk.Label(self, text="Search Through our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text ="View all records For?", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.optionC
        )
        option_menu.pack()

        self.output_label = tk.Label(self, font=controller.Info_font)
        self.output_label.pack()

        button3 = tk.Button(self, text="Search", command=self.viewall)
        button3.pack()


    def optionC(self, *args):
        pass
    #each time the search button is hit a new listbox is created which can be scrolled through and will show all records
    #listboxes will not be deleted even if the user moves away from the page this is because they can be finiky when destructing and can crash the system
    def viewall(self, *args):
        if self.option_var.get() == 'Athlete':
            self.langs = self.Adder.dataClean(1)

            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'League':
            self.langs = self.Adder.dataClean(3)
            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'Team':
            self.langs = self.Adder.dataClean(2)
            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'Team Award':
            self.langs = self.Adder.dataClean(5)

            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'Player Award':
            self.langs = self.Adder.dataClean(4)
            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

#export data to a csv by table
class export(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()

        self.menu_options = ('Athlete','League','Team','Award', 'Game')
        self.option_var = tk.StringVar(self)
        self.KeyValue = tk.StringVar(self)
        self.KeyName = tk.StringVar(self)

        label = tk.Label(self, text="Search Through our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text ="Export all records For?", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.optionC
        )
        option_menu.pack()

        self.output_label = tk.Label(self, font=controller.Info_font)
        self.output_label.pack()

        button3 = tk.Button(self, text="Export", command=self.viewall)
        button3.pack()


    def optionC(self, *args):
        pass
    #select a table and hit next for all data in that table to be exported to a csv titled after that table
    def viewall(self, *args):
        if self.option_var.get() == 'Athlete':
            self.Adder.export(1)

        if self.option_var.get() == 'League':
            self.Adder.export(3)

        if self.option_var.get() == 'Team':
            self.Adder.export(2)

        if self.option_var.get() == 'Award':
            self.Adder.export(4)

        if self.option_var.get() == 'Game':
            self.Adder.export(5)

#call the search functions that use subjerys 3 joins and aggregates
class fancy_search(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Adder = AddObjects.AddObjects()
        #dropdown menu with specific names for what each query does and what they need
        #this was done instead of giving these there own frame
        self.menu_options = ('return the names of all players who have won a trophy the same year as a specific player','total number of trophies won by each team given a sport','given a league name find the names of all players who have won trophies')
        self.option_var = tk.StringVar(self)
        self.KeyValue = tk.StringVar(self)
        self.KeyName = tk.StringVar(self)

        label = tk.Label(self, text="Search Through our System with specific filters!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        label2 = tk.Label(self, text ="Select a Query Filter", font=controller.Subsection_font)
        label2.pack()

        option_menu = tk.OptionMenu(
            self,
            self.option_var,
            *self.menu_options,
            command=self.optionC
        )
        option_menu.pack()

        self.output_label = tk.Label(self, text="Enter Query Value Here:", font=controller.Info_font)
        self.output_label.pack()

        self.EnterName = tk.Entry(self,)
        self.EnterName.pack()

        button3 = tk.Button(self, text="Search", command=self.viewall)
        button3.pack()


    def optionC(self, *args):
        pass

    def viewall(self, *args):
        #when search is clicked execute  the specific query and return results in a listbox like the view all since there can be multiple responses
        #like the view all listboxes it will not deconstruct itself
        if self.option_var.get() == 'return the names of all players who have won a trophy the same year as a specific player':
            self.langs = self.Adder.query_data(1, self.EnterName.get())

            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'total number of trophies won by each team given a sport':
            self.langs = self.Adder.query_data(3, self.EnterName.get())
            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

        if self.option_var.get() == 'given a league name find the names of all players who have won trophies':
            self.langs = self.Adder.query_data(4, self.EnterName.get())

            self.listbox=tk.Listbox(self)
            for item in self.langs:
                self.listbox.insert(tk.END, item)
            self.listbox.pack()

#runs the front end constructor
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()