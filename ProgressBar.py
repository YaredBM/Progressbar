from tkinter import*
from tkinter import ttk
import time

root=Tk()
root.title("Window")
root.geometry("600x400")
def salir():
    root.destroy()

def openwindow():
    for i in  range(101):
        my_progress['value']+=1
        root.update()
        time.sleep(0.001)
    root.withdraw()
    window_dos = Toplevel()
    window_dos.title('Second Window')
    window_dos.geometry('500x500+400+80')
    window_dos.protocol("WM_DELETE_WINDOW", salir)
    window_dos.state('zoomed')
    Label(window_dos, text='WINDOW TWO', font='Arial 40', bg= 'white').pack(expand=True)
    Button(window_dos, text='Exit', font='Arial 10', bg= 'red', command=salir).pack(expand=True)

my_progress=ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode="determinate")
my_progress.place(x=150,y=100)

my_button=Button(root,text="Progress",command=openwindow)
my_button.place(x=275,y=150)
