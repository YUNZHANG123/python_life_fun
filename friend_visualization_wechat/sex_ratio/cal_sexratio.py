# Question: get the sex of each friend and present the ratio of male and female on a pie chart
# Purpose: practise the Python IO
# Sophia  20190914
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser
from pyecharts import Pie

sex = []
with open('friends_info.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        sex.append(row.split(',')[2]) #get the sex of friends from the file that contains friends information

attr = ['male', 'female', 'unknown']
value = [sex.count('1'), sex.count('2'), sex.count('0')] #male is 1, female is 2, unknown is 0

pie = Pie('sex ratio of friends', 'total number of friends：%d' % len(sex), title_pos='center')
pie.add('', attr, value, radius=[30, 75], rosetype='area', is_label_show=True,
        is_legend_show=True, legend_top='bottom')

pie.render('ratio.html') #present in chart

webbrowser.open('ratio.html', new=2) #open it in website