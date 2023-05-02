# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter 
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
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
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

        self.menu_options = ('Athlete','League','Club','Sport','Game')
        self.option_var = tk.StringVar(self)

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
        label = tk.Label(self, text="Add To Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Remove Info From Our System!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()