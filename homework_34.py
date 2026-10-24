# Задача 1 Задача 3: Получение данных из базы данных
#
# Необходимо создать веб-приложение с использованием фреймворка Plotly Dash и библиотеки pandas, которое подключается к
# базе данных SQLite (или считывает локальный файл/таблицу с данными о продажах) и позволяет пользователю через
# выпадающий список (Dropdown) выбирать город, а на графике отображать динамику продаж по месяцам для выбранного города.
#
# Исходные данные (SQLite база sales.db)
# Таблица sales:
# • id (целое число)
# • city (текст: например, «Москва», «Санкт-Петербург», «Казань»)
# • month (текст: например, «Январь», «Февраль» и т. д.)
# • amount (вещественное число — сумма продаж)


import sqlite3
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html



def create_sample_db():
    conn = sqlite3.connect('sample_sales.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS sales (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    city TEXT, 
    month TEXT, 
    amount REAL)
    ''')

    sample_data = [
        ('Москва', 'Январь', 120000),
        ('Москва', 'Февраль', 150000),
        ('Москва', 'Март', 170000),
        ('Санкт-Петербург', 'Январь', 90000),
        ('Санкт-Петербург', 'Февраль', 95000),
        ('Санкт-Петербург', 'Март', 110000),
        ('Казань', 'Январь', 50000),
        ('Казань', 'Февраль', 60000),
        ('Казань', 'Март', 75000)
    ]

    cur.executemany('''INSERT INTO sales (city, month, amount) VALUES (?, ?, ?)''', sample_data)
    conn.commit()
    conn.close()

# create_sample_db()


def get_data_from_db():
    conn = sqlite3.connect('sample_sales.db')
    df = pd.read_sql_query('SELECT city, month, amount FROM sales', conn)
    conn.close()
    return df



df_sales = get_data_from_db()
cities = df_sales['city'].unique()
print(cities)

app = Dash()
app.layout = html.Div([
    html.H1('Динамика продаж по городам', style={'textAlign': 'center'}),

    html.Div([
        html.Label('Выберите город:'),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': city, 'value': city} for city in cities],
            value=cities[0],
            clearable=False
        )
    ], style={'width': '50%', 'margin': '0 auto'}),

    dcc.Graph(id='sales-graph')
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('city-dropdown', 'value')
)
def update_graph(selected_city):
    filtered_df = df_sales[df_sales['city'] == selected_city]
    fig = px.bar(
        filtered_df,
        x='month',
        y='amount',
        title=f'Динамика продаж — {selected_city}',
        labels={'month': 'Месяц', 'amount': 'Сумма продаж (руб.)'}
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)