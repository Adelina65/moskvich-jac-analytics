import matplotlib.pyplot as plt

stages = ('Факт (2023–2026)', 'Прогноз (рост в 2 раза)')
fiz = (35536, 35536)
ur = (23691, 23691)
gos = (6581, 13162)
bottom_gos = (59227, 59227)

p1 = plt.bar(stages, fiz, width=0.45, label='Физлица', color='#CBD5E1')
p2 = plt.bar(stages, ur, width=0.45, bottom=fiz, label='Бизнес', color='#64748B')
p3 = plt.bar(stages, gos, width=0.45, bottom=bottom_gos, label='Госструктуры (Рост)', color='#E11D48')

plt.bar_label(p1, labels=['35 536 шт.', '35 536 шт.'], label_type='center')
plt.bar_label(p2, labels=['23 691 шт.', '23 691 шт.'], label_type='center', color='white')
plt.bar_label(p3, labels=['6 581 шт.', '13 162 шт.'], label_type='center', color='white')

plt.title('Рост продаж «Москвича» за счет госзаказа')
plt.yticks([])
plt.box(False)
plt.ylim(0, 95000)
plt.legend(frameon=False)
plt.show()
