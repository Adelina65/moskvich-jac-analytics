import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='white')

models = ['Москвич 3\nи JAC JS3/4', 'Москвич М70/М90/5\nи JAC RF8']
moskvich = [52975, 1317]
jac = [3652, 913]

df = pd.DataFrame({
    'Модель': models * 2,
    'Бренд': ['Москвич', 'Москвич', 'JAC', 'JAC'],
    'Сумма': moskvich + jac,
})

df['Процент'] = (
    df['Сумма'] / df.groupby('Модель')['Сумма'].transform('sum') * 100
).round(1)


def format_label(row):
  num_str = f"{int(row['Сумма']):,}".replace(',', ' ')
  sep = ' ' if row['Процент'] < 12 else '\n'
  return f"{num_str} шт.{sep}({row['Процент']}%)"


df['Текст'] = df.apply(format_label, axis=1)

colors = {'Москвич': '#455a64', 'JAC': '#d32f2f'}

ax = sns.histplot(
    data=df,
    x='Модель',
    weights='Процент',
    hue='Бренд',
    multiple='stack',
    shrink=0.55,
    palette=colors,
    edgecolor='white',
    linewidth=1.5,
)

ax.set_axisbelow(True)
ax.grid(axis='y', linestyle='--', linewidth=0.8, color='#CBD5E1', alpha=0.8)
sns.despine(top=True, right=True, left=True)

c_jac = ax.containers[0]
c_moskvich = ax.containers[1]

ax.bar_label(
    c_jac,
    labels=df['Текст'].iloc[2:],
    label_type='center',
    color='white',
    weight='bold',
    fontsize=9.5,
)
ax.bar_label(
    c_moskvich,
    labels=df['Текст'].iloc[:2],
    label_type='center',
    color='white',
    weight='bold',
    fontsize=10,
)

plt.title(
    'Продажи по модельным группам, где «Москвич» опережает JAC',
    fontsize=14,
    weight='bold',
    pad=15,
)
plt.xlabel('Модели')
plt.ylabel('Доля (%)')
plt.ylim(0, 110)
plt.tight_layout()
plt.show()
