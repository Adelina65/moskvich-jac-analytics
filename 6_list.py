import pandas as pd
import matplotlib.pyplot as plt

# 1. Загружаем файлы (укажите название вашей подпапки вместо data)
df_jac = pd.read_csv("D:\moskvich-jac-analytics\jac_key .csv")
df_moskvich = pd.read_csv("D:\moskvich-jac-analytics\moskvich_key.csv")

# 2. Чистим продажи JAC от выброса (999999) и пустого значения в начале
df_jac.loc[df_jac['Продажи'] > 50000, 'Продажи'] = None
df_jac['Продажи'] = df_jac['Продажи'].interpolate().bfill()

# 3. Создаем список подписей для 8 полугодий (2023–2026)
periods = [
    '1 полугодие\n2023 г.', '2 полугодие\n2023 г.',
    '1 полугодие\n2024 г.', '2 полугодие\n2024 г.',
    '1 полугодие\n2025 г.', '2 полугодие\n2025 г.',
    '1 полугодие\n2026 г.', '2 полугодие\n2026 г.'
]

# Делим 48 месяцев на группы по 6 штук
group_id = [i // 6 for i in range(48)]

jac_half = df_jac.groupby(group_id)['Продажи'].sum()
moskvich_half = df_moskvich.groupby(group_id)['Sales_Volume_Units'].sum()

# 4. Выводим общие итоги
print("Всего продано Москвич:", int(moskvich_half.sum()))
print("Всего продано JAC:", int(jac_half.sum()))

# 5. Рисуем график
plt.figure(figsize=(11, 5))

plt.plot(periods, moskvich_half, label='Москвич', color='#1565c0', marker='o', linewidth=2.5)
plt.plot(periods, jac_half, label='JAC', color='#2e7d32', marker='s', linewidth=2.5)

plt.title("Динамика продаж «Москвич 3» и JAC JS4 (2023–2026)", fontsize=13, fontweight='bold')
plt.ylabel("Продажи, шт.")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
