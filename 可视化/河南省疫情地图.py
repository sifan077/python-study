import json

from pyecharts.charts import Map
from pyecharts.options import *

f = open('./疫情.txt', 'r', encoding='utf-8')
data = f.read()
f.close()

data = json.loads(data)
# print(data['areaTree'])
data = data['areaTree'][0]

province = data['children']

province = province[3]

data = []

for item in province['children']:
    # print(item['name'], item['total']['confirm'])
    if item['name'] == '济源示范区':
        data.append(("{}市".format('济源'), item['total']['confirm']))
        continue
    data.append(("{}市".format(item['name']), item['total']['confirm']))

# print(data)

map = Map()

map.add("河南疫情地图", data, "河南")

map.set_global_opts(
    title_opts=TitleOpts(title="中国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-49999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-99999", "color": "#FF6666"},
            {"min": 10000, "label": "100000+", "color": "#990033"},
        ]),
    legend_opts=LegendOpts(is_show=True)
)

map.render("河南疫情地图.html")
