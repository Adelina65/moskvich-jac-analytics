import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='white')

models = ['Москвич 6\nи JAC J7', 'Москвич 8\nи JAC JS6']
moskvich = [6910, 1645]
jac = [7609, 4565]

df = pd.DataFrame({
    'Модель': models * 2,
    'Бренд': ['Москвич', 'Москвич', 'JAC', 'JAC'],
    'Сумма': moskvich + jac,
})

df['Процент'] = (
    df['Сумма'] / df.groupby('Модель')['Сумма'].transform('sum') * 100
).round(1)

df['Текст'] = (
    df['Сумма'].apply(lambda x: f'{x:,}'.replace(',', ' '))
    + ' шт.\n('
    + df['Процент'].astype(str)
    + '%)'
)

colors = {'Москвич': '#004d40', 'JAC': '#80cbc4'}

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
)
ax.bar_label(
    c_moskvich,
    labels=df['Текст'].iloc[:2],
    label_type='center',
    color='white',
    weight='bold',
)

plt.title(
    'Продажи по модельным группам, где «Москвич» уступает JAC',
    fontsize=14,
    weight='bold',
    pad=15,
)
plt.xlabel('Модели')
plt.ylabel('Доля (%)')

plt.ylim(0, 110)
plt.tight_layout()
plt.show()
