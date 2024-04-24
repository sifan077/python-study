import json

from pyecharts.charts import *
from pyecharts.options import *

import pandas as pd

data = pd.read_csv('./1960-2019全球GDP数据.csv', encoding='utf-8')

data_dict = {}

for index, row in data.iterrows():
    year = row['year']
    if year not in data_dict:
        data_dict[year] = []
    data_dict[year].append((row['GDP'], float(row['rate'])))

# print(data_dict)

for year in data_dict:
    data_dict[year].sort(key=lambda x: x[1], reverse=True)
    data_dict[year] = data_dict[year][:8]


# print(data_dict)


def get_bar_chart(bar_data):
    bar = Bar()
    bar.add_xaxis(list(map(lambda x: x[0], bar_data)))
    bar.add_yaxis('GDP', list(map(lambda x: x[1], bar_data)), label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    return bar


timeLine = Timeline()

for year in data_dict:
    bar = get_bar_chart(data_dict[year])
    bar.set_global_opts(
        title_opts=TitleOpts(
            title=f'{year}年全球GDP前八国家',
            subtitle='单位：亿美元')
    )
    timeLine.add(bar, f'{year}年')

timeLine.render("世界GDP前八国家.html")
