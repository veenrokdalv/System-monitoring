import tkinter as tk
import process

class MainWindow(process.SystemMonitoring, tk.Tk):

    def __init__(self):
        super().__init__()
        self.init_gui()
        self.widget_ram()
        self.widget_rom()
        self.mainloop()
    
    def init_gui(self):
        self.geometry('300x380')
        self.resizable(width=False, height=False)
    
    def widget_ram(self):
        widget_text = [
            f'Total memory ram: {self.get_total_memory_RAM()[0]} {self.get_total_memory_RAM()[1]}',
            f'Used memory ram: {self.get_used_memory_RAM()[0]} {self.get_total_memory_RAM()[1]}',
            f'Availabel memory ram: {self.get_availabel_memory_RAM()[0]} {self.get_total_memory_RAM()[1]}'
        ]
        self.label_ram = tk.Label(self, text=widget_text[0]+'\n'+widget_text[1]+'\n'+widget_text[2])
        self.label_ram.pack()
        self.label_ram.after(100, )
    
    def widget_rom(self):
        widget_text = [
            f'Total memory ROM: {self.get_total_memory_ROM()[0]} {self.get_total_memory_ROM()[1]}',
            f'Used memory ROM: {self.get_used_memory_ROM()[0]} {self.get_used_memory_ROM()[1]}',
            f'Availabel memory ROM: {self.get_availabel_memory_ROM()[0]} {self.get_availabel_memory_ROM()[1]}',

        ]
        self.label_rom = tk.Label(self, text=widget_text[0]+'\n'+widget_text[1]+'\n'+widget_text[2])
        self.label_rom.pack()