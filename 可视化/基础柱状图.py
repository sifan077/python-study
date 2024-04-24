from pyecharts.charts import Bar
from pyecharts.options import *

bar = Bar()

bar.add_xaxis(['中国', '美国', '日本'])
# bar.add_yaxis('GDP', [25, 20, 10])
bar.add_yaxis('GDP', [25, 20, 10], label_opts=LabelOpts(position='right'))

# 反转坐标轴
bar.reversal_axis()

bar.render()
