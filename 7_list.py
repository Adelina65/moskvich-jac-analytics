import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style='white')

models = list(('Москвич 3 и JAC JS3/4', 'Москвич М70/М90/5 и JAC RF8'))
moskvich = list((52975, 1317))
jac = list((3652, 913))

m_pct = list((93.6, 59.4))
j_pct = list((6.4, 40.6))

df = pd.DataFrame({
    'Модель': models * 2,
    'Бренд': list(('Москвич', 'Москвич', 'JAC', 'JAC')),
    'Сумма': moskvich + jac,
    'Процент': m_pct + j_pct,
})

df['Текст'] = df['Сумма'].astype(str) + ' ₽ (' + df['Процент'].astype(str) + '%)'
colors = {'Москвич': '#455a64', 'JAC': '#d32f2f'}
# colors = {'Москвич': '#1E88E5', 'JAC': '#FF7043'}

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
    'Выручка по модельным группам, где «Москвич» опережает JAC', fontsize=14, weight='bold', pad=15
)
plt.xlabel('Модели')
plt.ylabel('Доля (%)')
plt.ylim(0, 110)
plt.show()
