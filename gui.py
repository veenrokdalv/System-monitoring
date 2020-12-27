import tkinter as tk
import process

class MainWindow(process.SystemMonitoring, tk.Tk):

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.widget_ram()
        self.mainloop()
    
    def init_gui(self):
        self.geometry('300x480')
        self.resizable(width=False, height=False)
    
    def widget_ram(self):
        widget_text = 'Total memory ram: ' + str(self.get_total_memory()[0]) + self.get_total_memory()[1] +\
            '\nUsed memory ram: ' + str(self.get_used_memory()[0]) + self.get_total_memory()[1] +\
            '\nAvailabel memory ram: ' + str(self.get_availabel_memory()[0]) + self.get_total_memory()[1]
        label = tk.Label(self, text=widget_text)
        label.pack()
        label.bind('<Enter>', )