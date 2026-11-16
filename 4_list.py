import pandas as pd
import matplotlib.pyplot as plt

# 1. Загружаем данные
df_jac = pd.read_csv(r"D:\moskvich-jac-analytics\jac_key .csv")
df_moskvich = pd.read_csv(r"D:\moskvich-jac-analytics\moskvich_key.csv")

# 2. Оставляем только нужные колонки
df_jac = df_jac[['ID_Периода', 'Продажи', 'Бренд']].copy()
df_moskvich = df_moskvich[['Period_Date', 'Sales_Volume_Units', 'Brand_Model']].copy()

# 3. Удаляем пустые строки и сбрасываем индекс
df_jac = df_jac.dropna().reset_index(drop=True)
df_moskvich = df_moskvich.dropna().reset_index(drop=True)

# 4. Заменяем опечатку 999999 на среднее значение по столбцу и приводим к целым числам
srednee = round(df_jac[df_jac['Продажи'] != 999999]['Продажи'].mean())
df_jac['Продажи'] = df_jac['Продажи'].replace(999999, srednee).astype(int)
df_moskvich['Sales_Volume_Units'] = df_moskvich['Sales_Volume_Units'].astype(int)

# 5. Выводим очищенные таблицы
print("--- Данные JAC ---")
print(df_jac.to_string())
print("\n--- Данные Москвич ---")
print(df_moskvich.to_string())

# 6. Группируем данные по полугодиям и считаем общую сумму продаж
jac_half = df_jac.groupby(df_jac.index // 6)['Продажи'].sum()
moskvich_half = df_moskvich.groupby(df_moskvich.index // 6)['Sales_Volume_Units'].sum()

print("\nВсего продано Москвич:", int(moskvich_half.sum()))
print("Всего продано JAC:", int(jac_half.sum()))

# 7. Строим график динамики продаж
periods = [
    '1-ое полугодие\n2023 г.', '2-ое полугодие\n2023 г.',
    '1-ое полугодие\n2024 г.', '2-ое полугодие\n2024 г.',
    '1-ое полугодие\n2025 г.', '2-ое полугодие\n2025 г.',
    '1-ое полугодие\n2026 г.', '2-ое полугодие\n2026 г.'
]

plt.figure(figsize=(11, 5))
plt.plot(periods[:len(moskvich_half)], moskvich_half, label='Москвич', color='#1565c0', marker='o', linewidth=2.5)
plt.plot(periods[:len(jac_half)], jac_half, label='JAC', color='#2e7d32', marker='s', linewidth=2.5)

plt.title("Динамика продаж модельного ряда «Москвич» и JAC в РФ (2023–2026 гг.)", fontsize=13, fontweight='bold', pad=20)
plt.ylabel("Продажи, шт.")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()

