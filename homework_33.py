# # Задача 2: Переключатель графиков (Радиокнопки)
# #
# # Цель: научиться динамически менять тип визуализации (Scatter vs Bar) для одного и того же набора данных.
# #
# # Задание:
# # Возьмите простой набор данных (например, продажи пяти вымышленных товаров). Добавьте радиокнопки с опциями:
# # «Столбчатая диаграмма» и «Линейный график». При переключении радиокнопки график ниже должен мгновенно менять свой вид.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

data = {
    "Товар": ["Товар А", "Товар Б", "Товар В", "Товар Г", "Товар Д"],
    "Продажи": [500, 700, 400, 900, 600]
}
df = pd.DataFrame(data)

app = Dash()

app.layout = html.Div(children=[
    html.H1("Переключатель графиков"),

    html.Div(children=[
        html.Label("Выберите вид графика:"),
        dcc.RadioItems(
            id='chart-type-radio',
            options=[
                {'label': 'Столбчатая диаграмма', 'value': 'Bar'},
                {'label': 'Линейный график', 'value': 'Line'}
            ],
            value='Bar',
            labelStyle={'display': 'inline-block', 'margin-right': '20px'}
        )
    ]),

    html.Div(children=[
        dcc.Graph(id="dynamic-chart")
    ])
])



@app.callback(
    Output("dynamic-chart", "figure"),
    Input("chart-type-radio", "value")
)
def update_chart(chart_type):

    if chart_type == 'Bar':
        fig = px.bar(
            df,
            x='Товар',
            y='Продажи',
            title='Продажи товаров (Столбчатая диаграмма)',
            color='Товар'
        )
    else:
        fig = px.line(
            df,
            x='Товар',
            y='Продажи',
            title='Продажи товаров (Линейный график)',
            markers=True
        )

    return fig


if __name__ == '__main__':
    app.run(debug=True)