import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels. tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

df = pd.read_csv(r'C:\Users\nglls\OneDrive\Рабочий стол\revenue_data.csv')

class window:

    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x500")
        self.master.title("Faberlic")

        self.label = tk.Label(self.master, text="Мы собрали данные компании Faberlic c 2013 по 2021 год, проанализировали их и создали модель машинного обучения.\n Результаты нашей работы вы можете наблюдать в этом приложении")
        self.label.pack()

        self.button = tk.Button(self.master, text="Доход", command=self.new_window)
        self.button.pack()

    def new_window(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.geometry("1000x500")
        self.new_window.title("Доход")

        self.button1 = tk.Button(self.new_window, text="Тренд и Сезонность", command=self.window_trend_and_sesonal)
        self.button1.pack()

        self.button2 = tk.Button(self.new_window, text="Динамика дохода по сезонам", command = self.sesonal)
        self.button2.pack()

        self.button3 = tk.Button(self.new_window, text="Стационарность", command = self.stationarity)
        self.button3.pack()

        self.button4 = tk.Button(self.new_window, text="Прогнозирование", command = self.predictions)
        self.button4.pack()

    def window_trend_and_sesonal(self):
        plt.plot(df['weaks'], df['revenue'])
        plt.title('График доходов')
        plt.xlabel('Недели')
        plt.ylabel('Доход')
        plt.show()

    def sesonal(self):
        self.sesonal_window = tk.Toplevel(self.master)
        self.sesonal_window.geometry("1000x500")
        self.sesonal_window.title("Динамика дохода по сезонам")

        self.button5 = tk.Button(self.sesonal_window, text="Зима", command = self.winter)
        self.button5.pack()

        self.button6 = tk.Button(self.sesonal_window, text="Весна", command = self.spring)
        self.button6.pack()

        self.button7 = tk.Button(self.sesonal_window, text="Лето", command = self.summer)
        self.button7.pack()

        self.button8 = tk.Button(self.sesonal_window, text="Осень", command = self.autumn)
        self.button8.pack()

    def winter(self):
        z = 0
        w13 = []
        w14 = []
        w15 = []
        w16 = []
        w17 = []
        w18 = []
        w19 = []
        w20 = []
        w21 = []
        for i in df['revenue']:
            if z <=7 or 46 < z < 51:
                w13.append(i)
            elif 51 < z <= 59 or 99 < z <= 103:
                w14.append(i)
            elif 103 < z <= 111 or 151 < z <= 155:
                w15.append(i)
            elif 155 < z <= 164 or 203 < z < 207:
                w16.append(i)
            elif 207 < z <= 216 or 255 < z < 259:
                w17.append(i)
            elif 260 < z <= 268 or 307 < z < 312:
                w18.append(i)
            elif 312 < z <= 320 or 359 < z < 364:
                w19.append(i)
            elif 364 < z <= 372 or 412 < z <= 416:
                w20.append(i)
            elif 416 < z < 425 or z > 464:
                w21.append(i)
            z+= 1
        x = list(range(12))
        y1 = w13 
        y2 = w14
        y3 = w15
        y4 = w16
        y5 = w17
        y6 = w18
        y7 = w19
        y8 = w20
        y9 = w21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("WINTER")
        plt.show()

    def spring(self):
        z = 0
        s13 = []
        s14 = []
        s15 = []
        s16 = []
        s17 = []
        s18 = []
        s19 = []
        s20 = []
        s21 = []
        for i in df['revenue']:
            if 7 < z <= 20:
                s13.append(i)
            elif 59 < z <= 72:
                s14.append(i)
            elif 111 < z < 125:
                s15.append(i)
            elif 164 < z <= 177:
                s16.append(i)
            elif 216 < z <= 229:
                s17.append(i)
            elif 268 < z <= 281:
                s18.append(i)
            elif 320 < z <= 333:
                s19.append(i)
            elif 372 < z < 386:
                s20.append(i)
            elif 425 < z <= 438:
                s21.append(i)
            z+= 1
            x = list(range(13))
        y1 = s13 
        y2 = s14
        y3 = s15
        y4 = s16
        y5 = s17
        y6 = s18
        y7 = s19
        y8 = s20
        y9 = s21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("SPRING")
        plt.show()

    def summer(self):
        z = 0
        su13 = []
        su14 = []
        su15 = []
        su16 = []
        su17 = []
        su18 = []
        su19 = []
        su20 = []
        su21 = []
        for i in df['revenue']:
            if 20 < z <= 33:
                su13.append(i)
            elif 72 < z < 86:
                su14.append(i)
            elif 125 < z <= 138:
                su15.append(i)
            elif 177 < z <= 190:
                su16.append(i)
            elif 229 < z <= 242:
                su17.append(i)
            elif 281 < z <= 294:
                su18.append(i)
            elif 333 < z <= 346:
                su19.append(i)
            elif 386 < z <= 399:
                su20.append(i)
            elif 438 < z <= 451:
                su21.append(i)
            z+= 1
            x = list(range(13))
        y1 = su13 
        y2 = su14
        y3 = su15
        y4 = su16
        y5 = su17
        y6 = su18
        y7 = su19
        y8 = su20
        y9 = su21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("SUMMER")
        plt.show()

    def autumn(self):
        z = 0
        a13 = []
        a14 = []
        a15 = []
        a16 = []
        a17 = []
        a18 = []
        a19 = []
        a20 = []
        a21 = []
        for i in df['revenue']:
            if 33 < z <= 46:
                a13.append(i)
            elif 86 < z <= 99:
                a14.append(i)
            elif 138 < z <= 151:
                a15.append(i)
            elif 190 < z <= 203:
                a16.append(i)
            elif 242 < z <= 255:
                a17.append(i)
            elif 294 < z <= 307:
                a18.append(i)
            elif 346 < z <= 359:
                a19.append(i)
            elif 399 < z <= 412:
                a20.append(i)
            elif 451 < z <= 464:
                a21.append(i)
            z+= 1
            x = list(range(13))
        y1 = a13 
        y2 = a14
        y3 = a15
        y4 = a16
        y5 = a17
        y6 = a18
        y7 = a19
        y8 = a20
        y9 = a21


        plt.plot(x,y1, label = '2013')
        plt.plot(x,y2, label = '2014')
        plt.plot(x,y3, label = '2015')
        plt.plot(x,y4, label = '2016')
        plt.plot(x,y5, label = '2017')
        plt.plot(x,y6, label = '2018')
        plt.plot(x,y7, label = '2019')
        plt.plot(x,y8, label = '2020')
        plt.plot(x,y9, label = '2021')
        plt.legend()
        plt.title("AUTUMN")
        plt.show()

    def stationarity(self):
        self.stationarity_window = tk.Toplevel(self.master)
        self.stationarity_window.geometry("1000x500")
        self.stationarity_window.title("Стационарность")
        adf_result = adfuller(df['revenue'])
        adf_text = f"ADF Statistic: {adf_result[0]:.2f}\n"
        adf_text += f"p-value: {adf_result[1]:.2f}\n"
        adf_text += "Critical Values:\n"
        for key, value in adf_result[4].items():
            adf_text += f"\t{key}: {value:.2f}\n"
        label = tk.Label(self.stationarity_window, text=adf_text)
        label.pack()

    def predictions(self):
        self.predictions_window = tk.Toplevel(self.master)
        self.predictions_window.geometry("1000x500")
        self.predictions_window.title("Прогнозирование")
        self.label = tk.Label(self.predictions_window, text='Введите количество недель для прогнозирования:')
        self.label.pack()
        self.days_entry = tk.Entry(self.predictions_window)
        self.days_entry.pack()
        self.button_pred = tk.Button(self.predictions_window, text='Сделать прогноз', command=self.prediction)
        self.button_pred.pack()
        

    def prediction(self):
        days_entry_value = self.days_entry.get()
        if len(days_entry_value.strip()) == 0:
            self.label = tk.Label(self.predictions_window, text='Ошибка: Вы не вели количество недель!')
            self.label.pack()
        else:
            days = int(days_entry_value)
            if days == 0:
                self.label = tk.Label(self.predictions_window, text='Ошибка: количество недель должно быть больше нуля!')
                self.label.pack()
            else:
                df['weaks'] = pd.to_datetime(df['weaks'], infer_datetime_format=True)
                df.set_index('weaks', inplace = True)
                model = ExponentialSmoothing(df, trend='add', seasonal = 'add', seasonal_periods=108)
                fitted_model = model.fit()
                global pred
                pred = fitted_model.forecast(days)
                label = tk.Label(self.predictions_window, text=pred)
                label.pack()
                self.button_graphics = tk.Button(self.predictions_window, text='Посмотреть графическое представление спрогнозированных данных',
                                                command=self.prediction_graphics)
                self.button_graphics.pack()
            
    def prediction_graphics(self):
        plt.figure(figsize=(10, 6))
        plt.plot(pred)
        plt.title('График доходов')
        plt.xlabel('Недели')
        plt.ylabel('Доход')
        plt.show()



if __name__ == '__main__':
    root = tk.Tk()
    app = window(root)
    root.mainloop()

