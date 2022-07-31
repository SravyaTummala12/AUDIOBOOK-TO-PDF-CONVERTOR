from tkinter import *
from PIL import ImageTk,Image
from tkinter.filedialog import *
from tkinter import filedialog
import os
import pyttsx3
import PyPDF2


def Openpdf():
    root=Tk()
    root.title('Read PDF!')
    root.geometry("500x500")
    #Create a textbox
    my_text=Text(root,height=30,width=60)
    my_text.pack(pady=10)

    # Clear a textbox
    def clear_text_box():
        my_text.delete(1.0,END)

    def open_pdf():
        open_file = filedialog.askopenfilename(
            initialdir="ThisPC/",
            title="Open PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", ".")))
        # Check to see if there is a file
        if open_file:
            # Open the pdf file
            pdf_file = PyPDF2.PdfFileReader(open_file)
            # Set the page to read
            page = pdf_file.getPage(0)
            # extract the text from pdf file
            page_stuff = page.extractText()

            # Add text to textbox
            my_text.insert(1.0, page_stuff)
    def saveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "."),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
    #Create a Menu
    my_menu=Menu(root)
    root.config(menu=my_menu)


    #Add some dropdown menu's
    file_menu=Menu(my_menu,tearoff=False)
    my_menu.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Clear", command=clear_text_box)
    file_menu.add_separator()
    file_menu.add_command(label="Save ", command=saveFile)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    my_menu.add_cascade(label="Open", command=open_pdf)






def Notepad():
    def newFile():
        global file
        root.title("Untitled - Notepad")
        file = None
        TextArea.delete(1.0, END)

    def openFile():
        global file
        file = askopenfilename(defaultextension=".txt",
                               filetypes=[("All Files", "."),
                                          ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()

    def saveFile():

        if file == None:
            file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                     filetypes=[("All Files", "."),
                                                ("Text Documents", "*.txt")])
            if file == "":
                file = None

            else:
                # Save as a new file
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()

                root.title(os.path.basename(file) + " - Notepad")
                print("File Saved")
        else:
            # Save the file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def cut():
        TextArea.event_generate(("<>"))

    def copy():
        TextArea.event_generate(("<>"))

    def paste():
        TextArea.event_generate(("<>"))

    def about():
        showinfo("Notepad", "Notepad by GROUP 3(MINI PROJECT")

    if __name__ == '__main__':
        # Basic tkinter setup
        root = Tk()
        root.wm_iconbitmap("icon2.ico")
        root.geometry("455x455")
        root.title("AUDIOBOOK AND NOTEPAD")

        # Add TextArea
        TextArea = Text(root, font="lucida 13")
        file = None
        TextArea.pack(expand=True, fill=BOTH)

        # Lets create a menubar
        MenuBar = Menu(root)

        # File Menu Starts
        FileMenu = Menu(MenuBar, tearoff=0)
        # To open new file
        FileMenu.add_command(label="New", command=newFile)

        # To Open already existing file
        FileMenu.add_command(label="Open", command=openFile)

        # To save the current file

        FileMenu.add_command(label="Save", command=saveFile)
        FileMenu.add_separator()
        MenuBar.add_cascade(label="File", menu=FileMenu)
        # File Menu ends

        # Edit Menu Starts
        EditMenu = Menu(MenuBar, tearoff=0)
        # To give a feature of cut, copy and paste
        EditMenu.add_command(label="Cut", command=cut)
        EditMenu.add_command(label="Copy", command=copy)
        EditMenu.add_command(label="Paste", command=paste)

        MenuBar.add_cascade(label="Edit", menu=EditMenu)

        # Edit Menu Ends

        # Help Menu Starts
        HelpMenu = Menu(MenuBar, tearoff=0)
        HelpMenu.add_command(label="About Notepad", command=about)
        MenuBar.add_cascade(label="Help", menu=HelpMenu)

        # Help Menu Ends

        root.config(menu=MenuBar)

        # Adding Scrollbar using rules from Tkinter lecture no 22
        Scroll = Scrollbar(TextArea)
        Scroll.pack(side=RIGHT, fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)
root = Tk()
f1 = Frame(root, bg="grey",borderwidth=3)
f1.pack(side=TOP)
l = Label(f1, text="WELCOME TO PDF TO AUDIOBOOK CONVERTOR", bg ="white", fg ="red", font="timesnewroman 14 italic")
l.pack()

title_label = Label(text = '''
My installed, saved, and unread pdf books !!!
\nI like reading books. I really do. 
\nI think language and ideas sharing is fascinating. 
\nI have a directory at which I store pdf books that I plan on reading but I never do. 
\nSo I thought hey, why dont I make them audio books and listen to them while I do something else !
\nSo I started planning how the script should look like.
\n # Allow user to pick a .pdf file
\n # Convert the file into one string
\n # Output .mp3 file.''', bg ="white",fg ="red", font="timesnewroman 12", borderwidth=5)
title_label.pack()

f2 = Frame(root, bg="grey",borderwidth=2)
f2.pack(side=LEFT)
def Male_audio():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

def Female_audio():
        book = askopenfilename()
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

def slow_speed():
        book = askopenfilename()
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            engine = pyttsx3.init()
            rate = engine.setProperty('rate', 100)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()

def fast_speed():
        book = askopenfilename()
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.numPages

        for num in range(0, pages):
            page = pdfreader.getPage(num)
            text = page.extractText()
            engine = pyttsx3.init()
            rate = engine.setProperty('rate',250)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()


def volume_down():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 0.5)
        engine.say(text)
        engine.runAndWait()

def volume_up():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 2.0)
        engine.say(text)
        engine.runAndWait()
b1 = Button(f2, fg="red", text = "Open PDF", command= Openpdf)
b1.pack(side=LEFT, padx=23)

b2 = Button(f2, fg="red", text = "Male voice", command = Male_audio)
b2.pack(side=LEFT, padx=23)

b3 = Button(f2, fg="red", text = "Female voice", command = Female_audio)
b3.pack(side=LEFT, padx=23)

b4 = Button(f2, fg="red", text = "Slow speed", command= slow_speed)
b4.pack(side=LEFT, padx=23)

b5 = Button(f2, fg="red", text = "Fast speed", command= fast_speed)
b5.pack(side=LEFT, padx=23)

b6 = Button(f2, fg="red", text = "Volume Up", command= volume_up)
b6.pack(side=LEFT, padx=23)

b7 = Button(f2, fg="red", text = "Volume Down", command= volume_down)
b7.pack(side=LEFT, padx=23)

b8 = Button(f2, fg="red", text = "Notepad", command= Notepad)
b8.pack(side=LEFT, padx=23)

b9 = Button(f2, fg="red", text = "Pause", )
b9.pack(side=LEFT, padx=23)

b10 = Button(f2, fg="red", text = "Exit program", command=root.quit)
b10.pack(side=LEFT, padx=23)

root.mainloop()

