from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as pltlib
import tkinter
import numpy as np




class App_Window(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.protocol('WM_DELETE_WINDOW', self.close_app)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.wm_title("Hailstone simulator")
        self.label_button = tkinter.Label(self,text="Enter a number: ")
        self.input_number = tkinter.Entry(self)
        self.entry_button = tkinter.Button(self,text = "Simulate!",command=self.plot_hailstone)
        self.label_button.pack()
        self.input_number.pack()
        self.entry_button.pack()
        self.canvasFig=pltlib.figure(1)
        Fig = Figure(figsize=(5,4),dpi=100)
        FigSubPlot = Fig.add_subplot(111)
        x=[]
        y=[]
        self.line1, = FigSubPlot.plot(x,y,'r-')
        self.canvas = FigureCanvasTkAgg(Fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        self.resizable(True,False)
        self.update()

    def refreshFigure(self,x,y):
        self.line1.set_data(x,y)
        ax = self.canvas.figure.axes[0]
        ax.set_xlim(x.min(), x.max())
        ax.set_ylim(y.min(), y.max())        
        self.canvas.draw()

    def plot_hailstone(self):
        number = self.input_number.get()
        trace = self.hailstone(number)
        ox_trace = [i+1 for i in range(len(trace))]
        X = np.array(ox_trace)
        Y = np.array(trace)
        self.refreshFigure(X,Y)

    def hailstone(self,number):
        
        trace = []
        number = int(number)
        while(number>=1):

            if number == 1:
                trace.append(number)
                break

            elif number % 2 == 0:
                trace.append(number)
                number = int(number / 2)
            
            else:
                trace.append(number)
                number = int(number*3 + 1)

        return trace

    def close_app(self):
        if tkinter.messagebox.askokcancel("Close", "Are you sure...?"):
            self.quit()



MainWindow = App_Window(None)
MainWindow.mainloop()

