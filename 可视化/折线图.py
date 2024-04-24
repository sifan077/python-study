from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts

line = Line()

line.add_xaxis(["中国", "美国", "日本"])

line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(
        title="GDP展示",
        pos_left="center",
        pos_bottom="1%"
    ),
    legend_opts=LegendOpts(
        is_show=True,
    ),
)

line.render()
