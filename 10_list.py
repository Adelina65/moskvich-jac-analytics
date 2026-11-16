import matplotlib.pyplot as plt

labels = ['Физические лица', 'Юридические лица', 'Государственные\nструктуры']

moskvich = [35536, 23691, 6581]  # Итого: 65 808 ед.
jac = [15675, 14458, 304]        # Итого: 30 437 ед.

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5))

fig.suptitle(
    'Сводная таблица продаж «Москвич» и JAC по категориям покупателей (2023–2026 гг.)',
    fontsize=13,
    fontweight='bold'
)

ax1.pie(moskvich, labels=labels, autopct='%1.1f%%', colors=['#1B8A6B', '#52B788', '#95D5B2'])
ax1.set_title('Бренд «Москвич» (65 808 ед.)', fontweight='bold')

ax2.pie(jac, labels=labels, autopct='%1.1f%%', colors=['#EAB308', '#FACC15', '#FEF08A'])
ax2.set_title('Бренд JAC (30 437 ед.)', fontweight='bold')

plt.tight_layout()
plt.show()
