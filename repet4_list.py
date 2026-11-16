# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df_users = pd.read_csv("users.csv")
# df_orders = pd.read_csv("orders.csv")
# df_events = pd.read_csv("events.csv")
#
# df_users['reg_date'] = pd.to_datetime(df_users['reg_date'])
# df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
# df_events['timestamp'] = pd.to_datetime(df_events['timestamp'])
#
# df_orders_clean = df_orders[df_orders['status'] == 'Delivered'].copy()
#
# total_revenue = df_orders['amount'].sum()
# clean_revenue = df_orders_clean['amount'].sum()
# lost_revenue = total_revenue - clean_revenue
#
# print(f"Общая сумма заказов (включая отмены): {total_revenue:,.2f} руб.")
# print(f"Реальная очищенная выручка компании: {clean_revenue:,.2f} руб.")
# print(f"Отсеяно из-за отмен и возвратов: {lost_revenue:,.2f} руб.")
#
# canceled_revenue = df_orders[df_orders['status'] == 'Canceled']['amount'].sum()
# refunded_revenue = df_orders[df_orders['status'] == 'Refunded']['amount'].sum()
#
# steps = [
#     'Все заказы\n(Грязные данные)',
#     'Отмена\n(Canceled)',
#     'Возвраты\n(Refunded)',
#     'Реальная выручка\n(Чистые деньги)'
# ]
#
# amounts = [total_revenue, -canceled_revenue, -refunded_revenue, clean_revenue]
#
# cumulative = np.zeros(len(amounts))
# cumulative[0] = amounts[0]
# for i in range(1, len(amounts)):
#     if i == len(amounts) - 1:
#         cumulative[i] = clean_revenue
#     else:
#         cumulative[i] = cumulative[i - 1] + amounts[i]
#
# sns.set_theme(style="whitegrid")
# fig, ax = plt.subplots(figsize=(13, 7), dpi=100)
#
# for i in range(len(steps)):
#     if i == 0 or i == len(steps) - 1:
#         color = "#1565c0" if i == 0 else "#2e7d32"
#         ax.bar(steps[i], cumulative[i], color=color, width=0.5, edgecolor="black", linewidth=0.8)
#         display_text = f"{cumulative[i]:,.0f} ₽"
#         y_pos = cumulative[i] + total_revenue * 0.02
#         text_color = "black"
#     else:
#         color = "#c62828"
#         start_val = cumulative[i - 1]
#         ax.bar(steps[i], amounts[i], bottom=start_val, color=color, width=0.5, edgecolor="black", linewidth=0.8)
#         display_text = f"{amounts[i]:+,.0f} ₽"
#         y_pos = start_val + amounts[i] / 2
#         text_color = "white"
#
# plt.show()
#
#
#
#
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df_users = pd.read_csv("users.csv")
# df_orders = pd.read_csv("orders.csv")
# df_events = pd.read_csv("events.csv")
#
# df_users['reg_date'] = pd.to_datetime(df_users['reg_date'])
# df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])
# df_events['timestamp'] = pd.to_datetime(df_events['timestamp'])
#
# df_orders_clean = df_orders[df_orders['status'] == 'Delivered'].copy()
#
# total_revenue = df_orders['amount'].sum()
# clean_revenue = df_orders_clean['amount'].sum()
# lost_revenue = total_revenue - clean_revenue
#
# print(f"Общая сумма заказов (включая отмены): {total_revenue:,.2f} руб.")
# print(f"Реальная очищенная выручка компании: {clean_revenue:,.2f} руб.")
# print(f"Отсеяно из-за отмен и возвратов: {lost_revenue:,.2f} руб.")
#
# sns.set_theme(style="white")
# fig, axes = plt.subplots(1, 3, figsize=(14, 3.5), dpi=100)
# fig.patch.set_facecolor('#f8f9fa')
#
# kpis = [
#     {"title": "ОБЩИЙ ОБЪЕМ ЗАКАЗОВ\n(Грязные данные)", "value": f"{total_revenue:,.0f} ₽", "color": "#1565c0",
#      "bg": "#e3f2fd"},
#     {"title": "РЕАЛЬНАЯ ВЫРУЧКА\n(Чистые деньги)", "value": f"{clean_revenue:,.0f} ₽", "color": "#2e7d32",
#      "bg": "#e8f5e9"},
#     {"title": "ОТСЕЯНО ПРИ ОЧИСТКЕ\n(Отмены и возвраты)", "value": f"{lost_revenue:,.0f} ₽", "color": "#c62828",
#      "bg": "#ffebee"},
# ]
#
# for i, kpi in enumerate(kpis):
#     ax = axes[i]
#     ax.set_facecolor(kpi["bg"])
#
#     for spine in ax.spines.values():
#         spine.set_color(kpi["color"])
#         spine.set_linewidth(1.5)
#
#     ax.text(0.5, 0.75, kpi["title"], ha="center", va="center", fontsize=11, fontweight="bold", color="#37474f")
#     ax.text(0.5, 0.35, kpi["value"], ha="center", va="center", fontsize=24, fontweight="bold", color=kpi["color"])
#
#     ax.set_xticks([])
#     ax.set_yticks([])
#
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

# 1. Данные и названия
cars = list(('Москвич 3', 'JAC JS4'))
labels = list(('Длина (мм)', 'Ширина (мм)', 'Высота (мм)', 'База (мм)', 'Клиренс (мм)',
               'Багажник (л)', 'Бак (л)', 'Мощность (л.с.)', 'Момент (Н·м)', 'Масса (кг)'))

moskvich = list((4410, 1800, 1660, 2620, 170, 520, 50, 150, 210, 1440))
jac = list((4410, 1800, 1660, 2620, 150, 520, 50, 147, 210, 1365))

# 2. Собираем строки с цифрами и строки с названиями цветов
rows = []
colors = []

for i in range(10):
    rows.append([moskvich[i], jac[i]])

    if moskvich[i] == jac[i]:
        colors.append(['lightgreen', 'lightgreen'])  # Одинаково -> оба зелёные
    else:
        colors.append(['lightgreen', 'yellow'])  # Отличие -> второй жёлтый

# 3. Рисуем цветную таблицу по центру экрана
plt.axis('off')  # Убираем лишние координатные оси
table = plt.table(
    cellText=rows,
    rowLabels=labels,
    colLabels=cars,
    cellColours=colors,
    cellLoc='center',
    loc='center'
)

table.scale(0.8, 1.5)  # Делаем клетки чуть крупнее и удобнее для чтения
plt.title('Москвич 3 vs JAC JS4')
plt.show()



# ОБНОВЛЕННЫЙ

# import matplotlib.pyplot as plt
#
# # 1. Данные и названия (простые списки)
# cars = ['Москвич 3', 'JAC JS4']
# labels = [
#     'Длина кузова (мм)', 'Ширина кузова (мм)', 'Высота кузова (мм)',
#     'Колёсная база (мм)', 'Клиренс (мм)', 'Объём багажника (л)',
#     'Объём бака (л)', 'Мощность (л.с.)', 'Крутящий момент (Н·м)', 'Масса (кг)'
# ]
#
# moskvich = list((4410, 1800, 1660, 2620, 170, 520, 50, 150, 210, 1440))
# jac = list((4410, 1800, 1660, 2620, 150, 520, 50, 147, 210, 1365))
#
# # 2. Собираем строки и цвета (обычный цикл)
# rows = []
# colors = []
#
# for i in range(10):
#     rows.append([moskvich[i], jac[i]])
#
#     if moskvich[i] == jac[i]:
#         colors.append(['#e8f5e9', '#e8f5e9'])  # зелёный (одинаково)
#     else:
#         colors.append(['#e8f5e9', '#fff9c4'])  # жёлтый (отличается)
#
# # 3. Рисуем таблицу (одна понятная команда)
# plt.figure(figsize=(8, 6))
# plt.axis('off')
#
# table = plt.table(
#     cellText=rows,
#     rowLabels=labels,
#     colLabels=cars,
#     cellColours=colors,
#     colColours=['#cfd8dc', '#cfd8dc'],
#     rowColours=['#f5f5f5'] * 10,
#     cellLoc='center',
#     loc='center'
# )
#
# # 4. Делаем клетки крупными и красивыми (всего 3 строчки)
# table.set_fontsize(11)
# table.scale(0.7, 1.8)
# plt.title('Сравнение характеристик: Москвич 3 vs JAC JS4', fontsize=14, fontweight='bold')
#
# plt.show()







# Импортируем модуль pyplot из библиотеки matplotlib и даём ему короткое имя plt
import matplotlib.pyplot as plt

# Создаём список с названиями автомобилей для заголовков столбцов таблицы
cars = ['Москвич 3', 'JAC JS4']
# Создаём список с названиями характеристик для заголовков строк таблицы
labels = [
    'Длина кузова (мм)',
    'Ширина кузова (мм)',
    'Высота кузова (мм)',
    'Колёсная база (мм)',
    'Клиренс (мм)',
    'Объём багажника (л)',
    'Объём бака (л)',
    'Мощность (л.с.)',
    'Крутящий момент (Н·м)',
    'Масса (кг)',
]

# Создаём список числовых характеристик для первого автомобиля (Москвич 3)
moskvich = list((4410, 1800, 1660, 2620, 170, 520, 50, 150, 210, 1440))
# Создаём список числовых характеристик для второго автомобиля (JAC JS4)
jac = list((4410, 1800, 1660, 2620, 150, 520, 50, 147, 210, 1365))

# Создаём пустой список для хранения пар значений (будущих строк таблицы)
rows = []
# Создаём пустой список для хранения цветов каждой ячейки таблицы
colors = []

# Запускаем цикл от 0 до 9 (всего 10 итераций по количеству характеристик)
for i in range(10):
  # Добавляем в список строк пару значений: характеристику Москвича и JAC под индексом i
  rows.append([moskvich[i], jac[i]])

  # Проверяем, равны ли значения текущей характеристики у обоих автомобилей
  if moskvich[i] == jac[i]:
    # Если значения одинаковые, красим обе ячейки в светло-зелёный цвет
    colors.append(['#e8f5e9', '#e8f5e9'])
  # В противном случае (если значения различаются)
  else:
    # Красим первую ячейку в светло-зелёный, а вторую — в светло-жёлтый цвет
    colors.append(['#e8f5e9', '#fff9c4'])

# Создаём новое окно (фигуру) для графика размером 8 на 6 дюймов
plt.figure(figsize=(8, 6))
# Отключаем стандартные оси координат (рамку, деления и числа), так как рисуем только таблицу
plt.axis('off')

# Создаём саму таблицу и сохраняем её объект в переменную table для дальнейшей настройки
table = plt.table(
    # Передаём двумерный список с данными для ячеек таблицы
    cellText=rows,
    # Передаём список названий для левого столбца (заголовки строк)
    rowLabels=labels,
    # Передаём список названий для верхнего ряда (заголовки столбцов)
    colLabels=cars,
    # Передаём матрицу цветов для окрашивания ячеек с данными
    cellColours=colors,
    # Задаём серо-голубой цвет фона для заголовков столбцов
    colColours=['#cfd8dc', '#cfd8dc'],
    # Задаём светло-серый цвет фона для всех 10 заголовков строк
    rowColours=['#f5f5f5'] * 10,
    # Выравниваем текст внутри ячеек ровно по центру
    cellLoc='center',
    # Размещаем саму таблицу по центру области рисования
    loc='center',
)

# Устанавливаем размер шрифта для текста в таблице равным 11 пунктам
table.set_fontsize(11)
# Масштабируем размеры ячеек: сжимаем по ширине (0.7) и растягиваем по высоте (1.8)
table.scale(0.7, 1.8)
# Добавляем заголовок над таблицей с размером шрифта 14 и жирным начертанием
plt.title(
    'Сравнение характеристик: Москвич 3 vs JAC JS4',
    fontsize=14,
    fontweight='bold',
)

# Отображаем готовое окно с таблицей на экране
plt.show()
