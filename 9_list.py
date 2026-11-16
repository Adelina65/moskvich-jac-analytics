import matplotlib.pyplot as plt

labels = ['Москвич 3е\n(2 961 шт.)', 'JAC T9 / T8 / T6\n(13 698 шт.)']
values = [2961, 13698]
colors = ['#2A9D8F', '#F4A261']

plt.figure(figsize=(7, 5))
plt.pie(
    values,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    wedgeprops={'width': 0.5, 'edgecolor': 'white', 'linewidth': 2}, 
    textprops={'fontsize': 11}
)
plt.title('Соотношение продаж моделей без прямых аналогов (2023–2026 гг.)', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.show()

