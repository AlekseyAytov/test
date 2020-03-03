from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def set_num(n):
	value = num.get()
	value += n
	num.set(value)

def set_op(x):
	value = num.get()
	if value:
		if value[-1] in ['*', '+', '-', '/']:
			value = value[:-1] + x
		else:
			value += x
		num.set(value)

def set_res(*args):
	value = num.get()
	if value:
		res = eval(value)
		num.set(res)

def reset():
	num.set('')

root = Tk()
root.title("Calculator")

mainframe = ttk.Frame(root, padding="5", relief='groove')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

s = ttk.Style()
print(s.theme_names())
print(s.theme_use())
print(s.layout('TButton'))
print(s.element_options('TButton.label'))

s.configure('TButton', font='helvetica 12')

num = StringVar()
num_label = ttk.Label(mainframe, width=10, textvariable=num, font='helvetica 24', foreground='#64545A', background='#FFFFFF')
num_label.grid(column=0, row=0, sticky=(W, E, N, S), columnspan=4)

ttk.Button(mainframe, text="1", command=lambda: set_num('1')).grid(column=0, row=1, sticky=W)
ttk.Button(mainframe, text="2", command=lambda: set_num('2')).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="3", command=lambda: set_num('3')).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="/", command=lambda: set_op('/')).grid(column=3, row=1, sticky=W)
ttk.Button(mainframe, text="4", command=lambda: set_num('4')).grid(column=0, row=2, sticky=W)
ttk.Button(mainframe, text="5", command=lambda: set_num('5')).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="6", command=lambda: set_num('6')).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="*", command=lambda: set_op('*')).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="7", command=lambda: set_num('7')).grid(column=0, row=3, sticky=W)
ttk.Button(mainframe, text="8", command=lambda: set_num('8')).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="9", command=lambda: set_num('9')).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="-", command=lambda: set_op('-')).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="0", command=lambda: set_num('0')).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="+", command=lambda: set_op('+')).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="C", command=reset).grid(column=0, row=5, sticky=W)
ttk.Button(mainframe, text="=", command=set_res).grid(column=3, row=5, sticky=W)

# кнопки изменения темы
ttk.Button(mainframe, text="winnative", command=lambda: s.theme_use('winnative')).grid(column=4, row=1)
ttk.Button(mainframe, text="clam", command=lambda: s.theme_use('clam')).grid(column=4, row=2)
ttk.Button(mainframe, text="alt", command=lambda: s.theme_use('alt')).grid(column=4, row=3)
ttk.Button(mainframe, text="default", command=lambda: s.theme_use('default')).grid(column=4, row=4)
ttk.Button(mainframe, text="classic", command=lambda: s.theme_use('classic')).grid(column=4, row=5)
ttk.Button(mainframe, text="vista", command=lambda: s.theme_use('vista')).grid(column=4, row=6)
ttk.Button(mainframe, text="xpnative", command=lambda: s.theme_use('xpnative')).grid(column=4, row=7)
ttk.Button(mainframe, text="Press", command=lambda: messagebox.showinfo(message='Have a nice day')).grid(column=1, row=7)

root.bind('<Return>', set_res)

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)
# mainframe.columnconfigure(0, weight=1, size= 80)
# mainframe.columnconfigure(1, weight=1, minsize= 80)
# mainframe.columnconfigure(2, weight=1, minsize= 80)
# mainframe.columnconfigure(3, weight=1, minsize= 80)
# mainframe.rowconfigure(0, weight=1, minsize= 50)
# mainframe.rowconfigure(1, weight=1, minsize= 35)
# mainframe.rowconfigure(2, weight=1, minsize= 35)
# mainframe.rowconfigure(3, weight=1, minsize= 35)
# mainframe.rowconfigure(4, weight=1, minsize= 35)
# mainframe.rowconfigure(5, weight=1, minsize= 35)

# блокировка изменений размеров окна
root.resizable(FALSE,FALSE) 

for child in mainframe.winfo_children(): 
	child.grid_configure(padx=5, pady=5)

root.mainloop()
