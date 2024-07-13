import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title('Python Text Editor')
w = 800
h = 650
root.geometry(f'{w}x{h}')


#yes i copied most of open and save lol
def Save():
    file=tk.filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if file:
        file.write(text_area.get("1.0", "end-1c"))
        root.title(f'Python Text Editor')
        file.close()
        text_area.delete(1.0, "end")

def Open():
    files = filedialog.askopenfiles(mode='r', defaultextension=".txt")
    
    if files:
        for file in files:
            filename = os.path.basename(file.name)
            content = file.read()
            
            root.title(f'Python Text Editor [{filename}]')
            text_area.delete(1.0, "end")
            text_area.insert("end", content)
            file.close()

def Font(font):
    font = font_option.get()
    if font == 'Fonts':
        pass
    else:
        font_str.set(font)
        text_area.config(font=(font_str.get(), font_size.get()))

def FontSize(size):
    size = font_sz.get()
    font_size.set(size)
    text_area.config(font=(font_str.get(), font_size.get()))



ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

font_str = tk.StringVar()
font_str.set('Arial')

available_fonts = ['Terminal', 'Roman', 'Courier', 'MS Sans Serif', 'Arial', 'Comic Sans MS']
available_size = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]

font_size = tk.IntVar()
font_size.set(10)

# Grid configuration
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Toolbar
toolbar = tk.Frame(root, height=int(h / 16))
toolbar.grid(row=0, column=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)

#ChatGpt ahh textarea lmaoo
textVar=tk.StringVar()
text_area = tk.Text(root,font=(font_str, font_size.get()))
text_area.grid(row=1, column=0, sticky=tk.NSEW, padx=5, pady=5)

scrollbar = tk.Scrollbar(root, orient='vertical', command=text_area.yview)
scrollbar.grid(row=1, column=1, sticky=tk.NS)


text_area.config(yscrollcommand=scrollbar.set)

# Buttons on toolbar
open_button = tk.Button(toolbar, text='Open', command=Open)
open_button.grid(row=0, column=0, padx=5)

save_button = tk.Button(toolbar, text='Save', command=Save)
save_button.grid(row=0, column=1, padx=5)

font_option = tk.StringVar(toolbar)
font_option.set('Fonts')
font_button = tk.OptionMenu(toolbar, font_option, *available_fonts, command=Font)
font_button.grid(row=0, column=2, padx=5)

font_sz = tk.StringVar(toolbar)
font_sz.set('10')
font_size_button = tk.OptionMenu(toolbar, font_sz, *available_size, command=FontSize)
font_size_button.grid(row=0, column=3, padx=5)

root.mainloop()
