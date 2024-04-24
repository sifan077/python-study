from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

from random import randint


def get_bar_chart():
    bar = Bar()

    bar.add_xaxis(['中国', '美国', '日本'])
    # bar.add_yaxis('GDP', [25, 20, 10])
    bar.add_yaxis('GDP', [randint(10, 100), randint(10, 100), randint(5, 35)], label_opts=LabelOpts(position='right'))

    # 反转坐标轴
    bar.reversal_axis()
    return bar


timeLine = Timeline()

timeLine.add(get_bar_chart(), '点1')
timeLine.add(get_bar_chart(), '点2')
timeLine.add(get_bar_chart(), '点3')
timeLine.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_timeline_show=True,
    is_loop_play=True,
)

timeLine.render('时间线柱状图.html')
