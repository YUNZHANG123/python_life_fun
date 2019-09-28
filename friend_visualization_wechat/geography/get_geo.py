# Question: get the feographic location of each friend and present the locations on a pie chart
# Purpose: practise the Python IO
# Sophia  20190914

from pyecharts import Map
import webbrowser

province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
    '四川': 0, '贵州': 0, '云南': 0,
    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
    '香港': 0, '澳门': 0, '国外及未知': 0} #A dictionary of the names of some main Chinese geographic locations

provinces = []
with open('ma.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        provinces.append(row.split(',')[3]) #To get the locations from the friends information file into rows.

for province in provinces:
    if province in province_dict.keys():
        province_dict[province] += 1
    else:
        province_dict['国外及未知'] += 1 #apply the locations in the rows to the dictionary, and as the location fits the names in the dictionary, the number will add 1.


# 创建一个地图对象
map = Map("地域分布")
# 添加数据(是否使用视觉映射组件)
map.add("地域分布",province_dict.keys(),province_dict.values(),is_visualmap=True)
# 生成html文件
map.render("geo.html") #apply the dictionary on hte map.

webbrowser.open("geo.html")
