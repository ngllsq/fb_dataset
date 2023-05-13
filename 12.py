import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import *
from idlelib.tooltip import Hovertip
from PIL import Image, ImageTk
class CSVViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.table = tk.Frame(self)
        self.table.grid(row=0, column=0, sticky='nsew')
        self.headers = []
        self.data = []

        self.load_button = tk.Button(self, text="Загрузить", command=self.load_data)
        self.load_button.grid(row=1, column=0)
        self.load_button1 = tk.Button(self, text="Предсказание", command=self.open_new_window)
        self.load_button1.grid(row=2, column=0)
        self.button2 = tk.Button(self, text="Сезонность", command=self.open_new_window2)
        self.button2.grid(row=3, column=0)



    def load_data(self):
        filename = filedialog.askopenfilename(title="Открыть файл", filetypes=[("CSV Files", "*.csv")])
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            self.headers = next(reader)
            for i, row in enumerate(reader):
                if i >= 15:
                    break
                self.data.append(row)
            self.update_table()

    def update_table(self):
        for widget in self.table.winfo_children():
            widget.destroy()
        for i, header in enumerate(self.headers):
            tk.Label(self.table, text=header, relief='solid', width=10).grid(row=0, column=i)
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                tk.Label(self.table, text=value, relief='solid', width=10).grid(row=i + 1, column=j)

    def open_new_window(self):
        self.new_window = tk.Toplevel(self.master)
        new_window = NewWindow(self.new_window)

    def open_new_window2(self):
        self.new_window = tk.Toplevel(self.master)
        new_window = NewWindow2(self.new_window)

class NewWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # self.label = tk.Label(self, text="Новое окно")
        # self.label.grid(row=0, column=0)
        self.image = Image.open("предсказание.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self, image=self.photo)
        self.label.pack()

class NewWindow2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.image1 = Image.open("winter.jpg")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.label1 = tk.Label(self, image=self.photo1)
        self.label1.grid(row=0, column=0)

        self.image2 = Image.open("spring.jpg")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.label2 = tk.Label(self, image=self.photo2)
        self.label2.grid(row=0, column=1)

        self.image3 = Image.open("summer.jpg")
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label3= tk.Label(self, image=self.photo3)
        self.label3.grid(row=1, column=0)

        self.image4 = Image.open("autumn.jpg")
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.label4 = tk.Label(self, image=self.photo4)
        self.label4.grid(row=1, column=1)



# Создаем главное окно приложения
root = tk.Tk()
root.title('CSV Viewer')
root.geometry('500x500')


# Создаем приложение
app = CSVViewer(master=root)
app.mainloop()

