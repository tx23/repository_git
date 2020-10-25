import sys
import os 
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import Tkinter

window = Tk()
label = Label(window, text="welcome python")
button = Button(window, text = "Click Me")
Label.pack()
button.pack()
window.mainloop()
