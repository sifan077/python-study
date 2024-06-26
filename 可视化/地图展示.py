from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

namemap = {'黑龙江省': '黑龙江', '吉林省': '吉林', '辽宁省': '辽宁', '北京市': '北京', '天津市': '天津',
           '河北省': '河北', '山西省': '山西', '内蒙古自治区': '内蒙古', '上海市': '上海', '江苏省': '江苏',
           '山东省': '山东', '浙江省': '浙江', '安徽省': '安徽', '江西省': '江西',
           '福建省': '福建', '广东省': '广东', '澳门特别行政区': '澳门', '台湾省': '台湾', '香港特别行政区': '香港', '西藏自治区': '西藏',
           '广西壮族自治区': '广西', '海南省': '海南', '河南省': '河南', '湖北省': '湖北', '湖南省': '湖南', '陕西省': '陕西', '新疆维吾尔自治区': '新疆',
           '宁夏回族自治区': '宁夏', '甘肃省': '甘肃', '青海省': '青海', '重庆市': '重庆', '四川省': '四川', '贵州省': '贵州', '云南省': '云南'}

data = [
    ("北京市", 100),
    ("天津市", 200),
    ("河北省", 300),
    ("山西省", 400),
    ("内蒙古自治区", 500),
    ("辽宁省", 600),
    ("吉林省", 700),
    ("黑龙江省", 800),
    ("上海市", 900),
    ("江苏省", 1000),
    ("浙江省", 1100),
    ("安徽省", 1200),
    ("福建省", 1300),
    ("江西省", 1400),
    ("山东省", 1500),
    ("河南省", 1600),
    ("湖北省", 1700),
    ("湖南省", 1800),
    ("广东省", 1900),
]
map.add("中国", data, "china")

# map.set_global_opts(
#     title_opts={"title": "中国地图展示"},
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#
#     ),
# )

map.render()
