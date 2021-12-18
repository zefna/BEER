import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

beer_df = pd.read_csv('beer.csv', sep='|')

# beer_dataset = sns.load_dataset('beer_df')

# beer_styles = beer_df['Стиль:'].value_counts().rename_axis('Стиль:').reset_index(name='Количество:')
# beer_styles.plot(x='Стиль:', y='Количество:', kind='bar')
# plt.show()
#
# beer_sorts = beer_df['Сорт:'].value_counts().rename_axis('Сорт:').reset_index(name='Количество:')
# beer_sorts.plot(x='Сорт:', y='Количество:', kind='bar', figsize=(15, 5))
# plt.show()
#
# beer_colors = beer_df['Цвет:'].value_counts().rename_axis('Цвет:').reset_index(name='Количество:')
# beer_colors.plot(x='Цвет:', y='Количество:', kind='bar')
# plt.show()
#
# beer_filtration = beer_df['Фильтрация:'].value_counts().rename_axis('Фильтрация:').reset_index(name='Количество:')
# beer_filtration.plot(x='Фильтрация:', y='Количество:', kind='bar')
# plt.show()
#
# beer_alcohol = beer_df['Алкоголь:'].value_counts().rename_axis('Алкоголь:').reset_index(name='Количество:')
# beer_alcohol.plot(x='Алкоголь:', y='Количество:', kind='bar', figsize=(15, 5))
# plt.show()
#
# beer_density = beer_df['Плотность:'].value_counts().rename_axis('Плотность:').reset_index(name='Количество:')
# beer_density.plot(x='Плотность:', y='Количество:', kind='bar', figsize=(15, 5))
# plt.show()

beer_df['Алкоголь:'] = beer_df['Алкоголь:'].str.rstrip('%').str.replace(',', '.').astype('float') / 100.0
beer_df['Плотность:'] = beer_df['Плотность:'].str.rstrip('%').str.replace(',', '.').astype('float') / 100.0

# beer_df['Алкоголь:'].hist(bins=50)
# beer_df['Плотность:'].hist(bins=50)
# xs = beer_df['Алкоголь:']
# ys = beer_df['Плотность:']
# pd.DataFrame(np.array([xs, ys]).T).plot.scatter(0, 1, s=12, c='green', grid=True)
# plt.xlabel('Алкоголь:')
# plt.ylabel('Плотность:')
# plt.show()
#
# beer_df['Алкоголь:'].cov(beer_df['Плотность:'])

# print('Выберите пиво (Светлое, Тёмное, Полутёмное)')
# color = input()

print('Введите крепость пива')
alc = float(int(input()) / 100)

#beer_df['Алкоголь:'] = beer_df['Алкоголь:'].astype(str)

result = beer_df[beer_df['Алкоголь:'] >= alc]

print(result)