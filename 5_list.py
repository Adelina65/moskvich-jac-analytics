import matplotlib.pyplot as plt

models = [
    '«Москвич 3»\nи JAC JS3/4',
    '«Москвич 6»\nи JAC J7',
    '«Москвич 8»\nи JAC JS6',
    '«Москвич 3е»',
    'JAC\nT9/T8/T6',
    '«Москвич\nМ70/М90/5»\nи JAC RF8'
]

moskvich = [52975, 6910, 1645, 2961, 0, 1317]
jac = [3652, 7609, 4565, 0, 13698, 913]


labels_moskvich = [f'{v:,}'.replace(',', ' ') if v > 0 else 'нет\nаналога' for v in moskvich]
labels_jac = [f'{v:,}'.replace(',', ' ') if v > 0 else 'нет\nаналога' for v in jac]

x = range(len(models))
width = 0.35

plt.figure(figsize=(10, 6))

bars1 = plt.bar([i - width/2 for i in x], moskvich, width, label='Москвич', color='#2A9D8F')
bars2 = plt.bar([i + width/2 for i in x], jac, width, label='JAC', color='#F4A261')

lbl1 = plt.bar_label(bars1, labels=labels_moskvich, padding=3, fontsize=9)
lbl2 = plt.bar_label(bars2, labels=labels_jac, padding=3, fontsize=9)


for label in lbl1 + lbl2:
    if label.get_text() == 'нет\nаналога':
        label.set_color('gray')
        label.set_style('italic')
        label.set_fontsize(8)

plt.title('Соотношение продаж по парам моделей (2023–2026 гг.)', fontsize=14, fontweight='bold')
plt.ylabel('Количество авто (шт.)', fontsize=11)
plt.xticks(x, models)
plt.ylim(0, 60000)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
