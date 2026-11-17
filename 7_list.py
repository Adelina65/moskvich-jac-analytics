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
  pct_str = str(row['Процент']).replace('.', ',')
  sep = ' ' if row['Процент'] < 12 else '\n'
  return f"{num_str} шт.{sep}({pct_str}%)"


df['Текст'] = df.apply(format_label, axis=1)

colors = {'Москвич': '#455a64', 'JAC': '#d32f2f'}

plt.figure(figsize=(7.5, 5.5))

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

sns.despine(top=True, right=True, left=True)

c_jac = ax.containers[0]
c_moskvich = ax.containers[1]

ax.bar_label(
    c_jac,
    labels=df['Текст'].iloc[2:],
    label_type='center',
    color='white',
    weight='bold',
    fontsize=10,
)
ax.bar_label(
    c_moskvich,
    labels=df['Текст'].iloc[:2],
    label_type='center',
    color='white',
    weight='bold',
    fontsize=11,
)

plt.title(
    'Продажи по модельным группам, где «Москвич» опережает JAC',
    fontsize=13,
    weight='bold',
    pad=35,
)
plt.xlabel('')
plt.ylabel('')
plt.yticks([])
plt.ylim(0, 105)

sns.move_legend(
    ax,
    'upper center',
    bbox_to_anchor=(0.5, 1.07),
    ncol=2,
    title=None,
    frameon=False,
    fontsize=11,
)

plt.tight_layout()
plt.show()
