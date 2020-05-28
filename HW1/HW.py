import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(
    'https://github.com/anastasiarazb/skillbox_nlp_demo/blob/master/%D0%9C%D1%81%D0%BA_5%D0%BB%D0%B5%D1%82.xls?raw=true'
    , skiprows=6)  # Получаем датафрейм
df['Местное время в Москве (ВДНХ)'] = pd.to_datetime(df['Местное время в Москве (ВДНХ)'], dayfirst=True)  # Переводим str в timestamp

foo = pd.Timestamp(day=1, month=12, year=2017)  # Задаем нижнюю границу
bar = pd.Timestamp(day=1, month=1, year=2019)  # Задаем верхнюю границу

bar_df = df[df['Местное время в Москве (ВДНХ)'] <= bar]  # Обрезаем датафрейм сверху
foobar_df = bar_df[foo <= bar_df['Местное время в Москве (ВДНХ)']]  # Обрезаем датафрейм снизу

plt.plot(foobar_df['Местное время в Москве (ВДНХ)'], foobar_df['T'])  # Строим график
plt.show()  # Показываем график
