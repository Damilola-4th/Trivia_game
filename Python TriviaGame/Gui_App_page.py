from tkinter import *
from tkinter import ttk
root = Tk()
# Title of Gui application
root.title('Trivia game')
root.iconbitmap('C:/Users/doluw/PycharmProjects/pythonProject/OOP Proj With Tkinter/Trivia_game_Icon.ico')
root.geometry("500x400")
# creat a mainframe:
scrollbar_Frame = Frame(root)
scrollbar_Frame.pack(fill=BOTH, expand=1)

# create a canvas
main_canvas = Canvas(scrollbar_Frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add a scroll bar to our canvas note: positioning the scroll bar in the fram and attack that frame into the canvas
scrollbar = ttk.Scrollbar(scrollbar_Frame, orient=VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# create another frame to put the trivia game inside:
gameFrame = Frame(main_canvas)

# put that new frame into a new window
main_canvas.create_window((0, 0), window=gameFrame, anchor='nw')

#configure scrollbar
main_canvas.configure(yscrollcommand=scrollbar.set)
#NOTE IF U EVER DO A SCROLL BAR, MAKE SURE U BIND THAT SCROLL BAR TO THE FRAME THAT U WANT IT TO SCROLL FOR. NOT THE MAIN_CANVAS ITSELF THAT THE FRAMES ARE IN BUT THE FRAME THAT THE SCROLL BAR IS SUPPOSE TO SCROLL FOR
gameFrame.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))
