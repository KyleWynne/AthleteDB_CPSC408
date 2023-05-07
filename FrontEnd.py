# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter 
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

import Backend as Backend

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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, Add_Team, Add_Athlete, Add_Club, Add_League, Add_Game):
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

        self.menu_options = ('Athlete','League','Club','Sport','Game')
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

        self.EnterName = tk.Entry(self,)
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

        self.menu_options = ('Athlete','League','Club','Team','Game')
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
        print(self.option_var.get())
    
    def NextPressedAdd(self, *args):

        if self.option_var.get() == "Athlete":
            self.controller.show_frame("Add_Athlete")

        if self.option_var.get() == "League":
            self.controller.show_frame("Add_League")
        
        if self.option_var.get() == "Club":
            self.controller.show_frame("Add_Club")

        if self.option_var.get() == "Team":
            self.controller.show_frame("Add_Team")
        
        if self.option_var.get() == "Game":
            self.controller.show_frame("Add_Game")


class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remove Info From Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Add_Athlete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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

class Add_League(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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

class Add_Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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

class Add_Club(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add A Club To The System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame("PageThree"))
        button1.pack()

        label2 = tk.Label(self, text="Input the information for each field then hit \"Finish\":", font=controller.Subsection_font)
        label2.pack()

class Add_Team(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()