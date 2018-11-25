# coding=utf-8
"""
    Created by prakash on 25/11/18
"""
import time
from multiprocessing import Process

from short_id import short_id

__author__ = 'Prakash14'

id_list = []
dup_dict = []
dup_list = []


def check_key(range_=1000):
    global id_list
    global dup_dict
    global dup_list
    # print(id_list, dup_dict, dup_list)
    for i in range(0, range_):
        ran = short_id()

        if ran in id_list:
            dup_list.append(ran)
            dup_dict.setdefault(str(ran), {}).setdefault('pos', []).append(i)
            dup_dict[str(ran)]['count'] = dup_dict[str(ran)].get("count", 0) + 1
        id_list.append(ran)


for i in range(0, 20):
    def p_(_i):
        global dup_dict
        global random_list
        global dup_list
        dup_dict = {}
        random_list = []
        dup_list = []
        val = _i * 1000
        SEED = 0
        start = time.time()
        check_key(val)
        print(val, " Key LEN : ", dup_dict.keys().__len__(), "Total: ", dup_list.__len__(),
              "Execute Time : ", time.time() - start)


    p_(i)
    p = Process(target=p_, args=(i,))
    p.start()
