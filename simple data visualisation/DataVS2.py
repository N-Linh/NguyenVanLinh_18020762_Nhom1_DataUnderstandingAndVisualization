import pandas as pd
import matplotlib.pyplot as plt

pf = pd.read_json('file_read\websosanh.json')
categories = pf['category']
category_count = categories.value_counts()

list = [(k, v) for k, v in category_count.items()]
cat_count_table = pd.DataFrame(list, columns = ['category', 'count'])
category = cat_count_table['category']
count = cat_count_table['count']

explode = (0.1, 0.1, 0, 0, 0)
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue']

plt.figure(figsize=(7,8))

plt.pie(count, explode=explode, labels=category, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.legend(title = 'list of category', loc='lower center')
plt.axis('equal')
plt.suptitle('statistics category articles', fontsize=18, ha='center', va='top')
plt.tight_layout()
plt.show()
