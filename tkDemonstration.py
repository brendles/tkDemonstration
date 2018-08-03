import tkinter as tk
from tkinter import ttk #for stylized UI


LARGE_FONT = ("Verdana", 12)


class tkDemonstration(tk.Tk): #doesn't need parenthesis - takes inheritance
    # init method initializes with class, always runs when class is called
    #basically "startup programs"
    def __init__(self, *args, **kwargs): #first variable of every method, then *args or *kwargs
    #args is literally anything passed to it, usually var,
    #kwargs are keyword arguments and they take in dictionaries
        tk.Tk.__init__(self, *args, **kwargs) #init tkinter

        #tk.Tk.iconbitmap(self, default="clienticon.ico") #icon for program *.ico
        tk.Tk.wm_title(self, "tkDemonstration client") #title
        
        container = tk.Frame(self) #basically the window
        #pack can throw all the stuff into one place, for quick programs
        #grid is better for planned out programs
        container.pack(side="top", fill="both", expand = True)
        #define anchor, fill takes up extra space, expand takes space if there is some
        container.grid_rowconfigure(0, weight=1) #tk function, 0 is minimum size
        container.grid_columnconfigure(0, weight=1) #weight is priority in grid

        self.frames = {} #this is going to be a big part of program

        for F in (StartPage, PageOne, PageTwo): #stores proper frame in self.frames
        #add new objects to this, eg pages        
            frame = F(container, self)

            self.frames[F] = frame #brings startpage to front

            frame.grid(row=0, column=0, sticky="nsew")
            #sticky is alignment + stretch functionality or anchor
            #nsew allows it to stretch in all directions, sw in only bottom left

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont] #cont is key of self.frames
        frame.tkraise() #pulls frame to front


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        #essentially the below is a new page
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT) #adds text
        label.pack(pady=10,padx=10) #neatly pads the edges

        #instead of tk.Button, ttk.button for stylized buttons
        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne)) #makes a button
        button1.pack()

        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo)) #makes a button
        button2.pack()

#essentially this one class creates a page with buttons for pagetwo and home
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT) #adds text
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)) #makes a button
        button1.pack()

        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo)) #makes a button
        button2.pack()
#same as PageOne, except directs with button to pageone and home
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT) #adds text
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage)) #makes a button
        button1.pack()

        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne)) #makes a button
        button2.pack()
        

app = tkDemonstration() #assign to app
app.mainloop() #mainloop is tk function
