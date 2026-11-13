import matplotlib.pyplot as plt


cars = ['Москвич 3', 'JAC JS4']
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

moskvich = list((4410, 1800, 1660, 2620, 170, 520, 50, 150, 210, 1440))
jac = list((4410, 1800, 1660, 2620, 150, 520, 50, 147, 210, 1365))

rows = []
colors = []

for i in range(10):
  rows.append([moskvich[i], jac[i]])

  if moskvich[i] == jac[i]:
    colors.append(['#e8f5e9', '#e8f5e9'])
  else:
    colors.append(['#e8f5e9', '#fff9c4'])

plt.figure(figsize=(8, 6))
plt.axis('off')

table = plt.table(
    cellText=rows,
    rowLabels=labels,
    colLabels=cars,
    cellColours=colors,
    colColours=['#cfd8dc', '#cfd8dc'],
    rowColours=['#f5f5f5'] * 10,
    cellLoc='center',
    loc='center',
)

table.set_fontsize(14)
table.scale(0.7, 1.8)
plt.title(
    'Сравнение характеристик: "Москвич 3" и JAC JS4',
    fontsize=15,
    fontweight='bold',
)
plt.tight_layout()
plt.show()
