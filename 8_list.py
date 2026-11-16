import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='white')

models = list(('Москвич 6\nи JAC J7', 'Москвич 8\nи JAC JS6'))
moskvich = list((6910, 1645))
jac = list((7609, 4565))

m_pct = list((47.9, 26.73))
j_pct = list((52.1, 73.27))

df = pd.DataFrame({
    'Модель': models * 2,
    'Бренд': list(('Москвич', 'Москвич', 'JAC', 'JAC')),
    'Сумма': moskvich + jac,
    'Процент': m_pct + j_pct,
})

df['Текст'] = df['Сумма'].astype(str) + ' ₽ (' + df['Процент'].astype(str) + '%)'
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

c_jac = ax.containers.__getitem__(0)
c_moskvich = ax.containers.__getitem__(1)

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
    'Выручка по модельным группам, где «Москвич» уступает JAC', fontsize=14, weight='bold', pad=15
)
plt.xlabel('Модели')
plt.ylabel('Доля (%)')

plt.ylim(0, 110)
plt.show()
