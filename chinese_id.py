# -*- coding: utf-8 -*-

import time
import datetime
import sys
import random


def date_to_unixtime(d):
    date_time_obj = datetime.strptime(d, "%Y-%m-%d %H:%M:%S")
    return time.mktime(date_time_obj.timetuple())


code_list = [110100, 110101, 110102, 110105, 110106, 110107, 110108, 110109, 110111, 110112, 110113, 110114, 110115, 110116, 110117, 110229]
start_time = date_to_unixtime('1968-01-01 00:00:00')
end_time = date_to_unixtime('2000-01-01 00:00:00')
rand_date = random.randrange(start_time, end_time)
rand_date = time.strftime('%Y%m%d', time.localtime(rand_date))
rand_order = random.randrange(1,999)
rand_order = rand_order.ljust(3, '0')
final = random.choice(code_list)+str(rand_date)+str(rand_order)
length = final.count()
add_up = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
add_up_first = 0
i = 0
while i < length:
    add_up_first += final[i] * add_up[i]
array = [1,0,'X',9,8,7,6,5,4,3,2]
print(final + array[add_up_first % 11])
