import matplotlib.pyplot as plt

models = [
    'Москвич 3\nи JAC JS3/4',
    'Москвич 6\nи JAC J7',
    'Москвич 8\nи JAC JS6',
    'Москвич 3е',
    'JAC\nT9/T8/T6',
    'Москвич\nМ70/М90/5\nи JAC RF8'
]

moskvich = [52975, 6910, 1645, 2961, 0, 1317]
jac = [3652, 7609, 4565, 0, 13698, 913]

labels_moskvich = [f'{v:,}'.replace(',', ' ') if v > 0 else 'нет\nаналога' for v in moskvich]
labels_jac = [f'{v:,}'.replace(',', ' ') if v > 0 else 'нет\nаналога' for v in jac]

x = range(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar([i - width/2 for i in x], moskvich, width, label='Москвич', color='#2A9D8F')
bars2 = ax.bar([i + width/2 for i in x], jac, width, label='JAC', color='#F4A261')

lbl1 = ax.bar_label(bars1, labels=labels_moskvich, padding=3, fontsize=11)
lbl2 = ax.bar_label(bars2, labels=labels_jac, padding=3, fontsize=11)

for label in lbl1 + lbl2:
    if label.get_text() == 'нет\nаналога':
        label.set_color('black')
        label.set_weight('bold')
        label.set_style('normal')
        label.set_fontsize(8)

ax.set_title('Соотношение продаж по парам моделей (2023–2026 гг.)', fontsize=15, fontweight='bold')
ax.set_xticks(x, models)
ax.set_ylim(0, 60000)

ax.tick_params(axis='x', length=0)
ax.tick_params(axis='y', length=0, labelleft=False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.legend(fontsize=11, frameon=False)
plt.tight_layout()
plt.show()
