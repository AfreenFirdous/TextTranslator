# from tkinter import *
# from translate import Translator
#
# screen = Tk()
# screen.title("Language Translator")
#
# from_lang = StringVar()
# to_lang = StringVar()
#
# Languages = {'English', 'Chinese', 'German', 'Spanish', 'French'}
# from_lang.set('English')
# to_lang.set('Urdu')
#
#
# def Translate():
#     translator = Translator(from_lang=from_lang.get(), to_lang=to_lang.get())
#     translation = translator.translate(TextVar.get())
#     OutputVar.set(translation)
#
#
# # choice for input language
# from_langMenu = OptionMenu(screen, from_lang, *Languages)
# Label(screen, text="Source Language").grid(row=0, column=1)
# from_langMenu.grid(row=0, column=2)
#
# # choice for target language
# to_langMenu = OptionMenu(screen, to_lang, *Languages)
# Label(screen, text="Target Language").grid(row=0, column=3)
# to_langMenu.grid(row=0, column=4)
#
# Label(screen, text="Enter Text").grid(row=2, column=0)
# TextVar = StringVar()
# TextBox = Entry(screen, textvariable=TextVar).grid(row=2, column=1)
#
# Label(screen, text="Output Text").grid(row=2, column=2)
# OutputVar = StringVar()
# TextBox = Entry(screen, textvariable=OutputVar).grid(row=2, column=3)
#
# # Button for calling function
# B = Button(screen, text="Translate", command=Translate, relief=GROOVE).grid(row=3, column=1, columnspan=3)
#
# mainloop()


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  # pip install pillow
from googletrans import Translator  # pip install googletrans==3.1.0a0
from tkinter import messagebox

root = tk.Tk()
root.title('Langauge Translator')
root.geometry('530x380')
root.maxsize(530, 380)
root.minsize(530, 380)
translator = Translator()

def translate():
    language_1 = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()

    if language_1 == '':
        messagebox.showerror('Language Translator', 'please write something')
    else:
        t2.delete(1.0, 'end')
        output = translator.translate(language_1, dest=cl)
        t2.insert('end', output.text)


def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')


img = ImageTk.PhotoImage(Image.open('image.png'))
label = Label(image=img)
label.place(x=200, y=1)

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('verdana', 10, 'bold'), )

auto_detect['values'] = (
    'Auto Detect',
)

auto_detect.place(x=30, y=70)
auto_detect.current(0)

l = tk.StringVar()
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))

choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    ' Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    ' Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    ' Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=290, y=70)
choose_langauge.current(0)

t1 = Text(root, width=20, height=10, borderwidth=5, relief=RIDGE, font=("Helvetica", 16))
t1.place(x=10, y=100)

t2 = Text(root, width=20, height=10, borderwidth=5, relief=RIDGE, font=("Helvetica", 16))
t2.place(x=260, y=100)

button = Button(root, text="Translate", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2",
                command=translate)
button.place(x=150, y=330)

clear = Button(root, text="Clear", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor="hand2",
               command=clear)
clear.place(x=280, y=330)

root.mainloop()

