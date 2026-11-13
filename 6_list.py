import pandas as pd
import matplotlib.pyplot as plt


df_jac = pd.read_csv("D:\moskvich-jac-analytics\jac_key .csv")
df_moskvich = pd.read_csv("D:\moskvich-jac-analytics\moskvich_key.csv")

sales = list(df_jac['Продажи'])
for i in range(len(sales)):
    if sales[i] > 50000:
        if i == 0:
            sales[i] = sales[i + 1]
        elif i == len(sales) - 1:
            sales[i] = sales[i - 1]
        else:
            sales[i] = (sales[i - 1] + sales[i + 1]) / 2
df_jac['Продажи'] = sales

periods = [
    '1-ое полугодие\n2023 г.', '2-ое полугодие\n2023 г.',
    '1-ое полугодие\n2024 г.', '2-ое полугодие\n2024 г.',
    '1-ое полугодие\n2025 г.', '2-ое полугодие\n2025 г.',
    '1-ое полугодие\n2026 г.', '2-ое полугодие\n2026 г.'
]

jac_half = df_jac.groupby(df_jac.index // 6)['Продажи'].sum()
moskvich_half = df_moskvich.groupby(df_moskvich.index // 6)['Sales_Volume_Units'].sum()


print("Всего продано Москвич:", int(moskvich_half.sum()))
print("Всего продано JAC:", int(jac_half.sum()))


plt.figure(figsize=(11, 5))
plt.plot(periods[:len(moskvich_half)], moskvich_half, label='Москвич', color='#1565c0', marker='o', linewidth=2.5)
plt.plot(periods[:len(jac_half)], jac_half, label='JAC', color='#2e7d32', marker='s', linewidth=2.5)

plt.title("Динамика продаж «Москвич 3» и JAC JS4 (2023–2026 гг.)",
          fontsize=13, fontweight='bold', pad=20)
plt.ylabel("Продажи, шт.")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
