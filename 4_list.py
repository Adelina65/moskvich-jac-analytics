import pandas as pd
import matplotlib.pyplot as plt


df_jac = pd.read_csv(r"D:\moskvich-jac-analytics\jac_sales.csv")
df_moskvich = pd.read_csv(r"D:\moskvich-jac-analytics\moskvich_sales.csv")

df_jac = df_jac[['ID_Периода', 'Продажи', 'Бренд']].copy()
df_moskvich = df_moskvich[['Period_Date', 'Sales_Volume_Units', 'Brand_Model']].copy()

srednee = round(df_jac[df_jac['Продажи'] != 999999]['Продажи'].mean())

df_jac['Продажи'] = df_jac['Продажи'].fillna(srednee).replace(999999, srednee).astype(int)
df_moskvich = df_moskvich.dropna().reset_index(drop=True)
df_moskvich['Sales_Volume_Units'] = df_moskvich['Sales_Volume_Units'].astype(int)

print("--- Данные JAC ---")
print(df_jac.to_string())
print("\n--- Данные Москвич ---")
print(df_moskvich.to_string())


jac_half = df_jac.groupby(df_jac.index // 6)['Продажи'].sum()
moskvich_half = df_moskvich.groupby(df_moskvich.index // 6)['Sales_Volume_Units'].sum()

print("\nВсего продано Москвич:", int(moskvich_half.sum()))
print("Всего продано JAC:", int(jac_half.sum()))


periods = [
    '1-е полугодие\n2023 г.', '2-е полугодие\n2023 г.',
    '1-е полугодие\n2024 г.', '2-е полугодие\n2024 г.',
    '1-е полугодие\n2025 г.', '2-е полугодие\n2025 г.',
    '1-е полугодие\n2026 г.', '2-е полугодие\n2026 г.'
]

plt.figure(figsize=(11, 5))
plt.plot(periods[:len(moskvich_half)], moskvich_half, label='Москвич', color='#1565c0', marker='o', linewidth=2.5)
plt.plot(periods[:len(jac_half)], jac_half, label='JAC', color='#2e7d32', marker='s', linewidth=2.5)

plt.title(
    "Динамика продаж автомобилей «Москвич» и JAC (2023–2026 гг.)",
    fontsize=14, fontweight='bold', pad=20
)
plt.ylabel("Продажи, шт.", fontsize=11)
plt.ylim(0, max(moskvich_half) * 1.15)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()
