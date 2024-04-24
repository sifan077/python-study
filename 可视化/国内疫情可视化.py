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

# print(province)

data = []

for item in province:
    # print(item['name'], item['total']['confirm'])
    data.append((
        item['name'],
        item['total']['confirm']
    ))
print(data)

name_map = {'黑龙江省': '黑龙江', '吉林省': '吉林', '辽宁省': '辽宁', '北京市': '北京', '天津市': '天津',
            '河北省': '河北', '山西省': '山西', '内蒙古自治区': '内蒙古', '上海市': '上海', '江苏省': '江苏',
            '山东省': '山东', '浙江省': '浙江', '安徽省': '安徽', '江西省': '江西',
            '福建省': '福建', '广东省': '广东', '澳门特别行政区': '澳门', '台湾省': '台湾', '香港特别行政区': '香港', '西藏自治区': '西藏',
            '广西壮族自治区': '广西', '海南省': '海南', '河南省': '河南', '湖北省': '湖北', '湖南省': '湖南', '陕西省': '陕西', '新疆维吾尔自治区': '新疆',
            '宁夏回族自治区': '宁夏', '甘肃省': '甘肃', '青海省': '青海', '重庆市': '重庆', '四川省': '四川', '贵州省': '贵州', '云南省': '云南'}

map = Map()

map.add("中国", data, "china", name_map=name_map)

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

map.render("全国疫情地图.html")
