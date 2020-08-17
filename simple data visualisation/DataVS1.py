import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('file_read\dantri.json')# read dantri.json file
categories = df['Category']# take category series
category_count = dict(categories.value_counts())# count number of articles per each category

list = [(k, v) for k, v in category_count.items()]

cat_count_table = pd.DataFrame(list, columns=['category', 'count'])
category_lim = cat_count_table[cat_count_table['count'] > 200]
category = category_lim['category']
count = category_lim['count']

plt.figure(figsize=(15, 6))
plt.suptitle('statistics category articles', fontsize=18)
plt.grid(color=(1.0, 0.47, 0.42))
plt.barh(category, count, color=(1.0, 0.47, 0.42))
plt.xlabel('number of counts')
plt.ylabel('category')
plt.show()