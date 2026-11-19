import matplotlib.pyplot as plt

labels = ['Физические лица', 'Юридические лица', 'Государственные структуры']
colors = ['#457B9D', '#A8DADC', '#E63946']

moskvich = [35536, 23691, 6581]
jac = [15675, 14458, 304]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5.5))

fig.suptitle(
    'Структура продаж «Москвич» и JAC по категориям покупателей (2023–2026 гг.)',
    fontsize=13,
    fontweight='bold'
)

ax1.pie(moskvich, autopct='%1.1f%%', colors=colors, pctdistance=0.75)
ax1.set_title('Бренд «Москвич» (65 808 ед.)', fontweight='bold')

ax2.pie(jac, autopct='%1.1f%%', colors=colors, pctdistance=0.75)
ax2.set_title('Бренд JAC (30 437 ед.)', fontweight='bold')

fig.legend(labels, loc='upper center', bbox_to_anchor=(0.5, 0.93), ncol=3, frameon=False)

plt.tight_layout(rect=[0, 0, 1, 0.85])
plt.show()
