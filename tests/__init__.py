"""
Created by Purushot on 25/11/18
"""

import logging
import time
import unittest
from multiprocessing import Process

from short_id import generate_short_id

__author__ = "Purushot14"

id_list = []
dup_dict = {}
dup_list = []


def check_key(range_=1000):
    global id_list
    global dup_dict
    global dup_list
    # print(id_list, dup_dict, dup_list)
    for i in range(0, range_):
        ran = generate_short_id()

        if ran in id_list:
            dup_list.append(ran)
            dup_dict.setdefault(str(ran), {}).setdefault("pos", []).append(i)
            dup_dict[str(ran)]["count"] = dup_dict[str(ran)].get("count", 0) + 1
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
        start = time.time()
        check_key(val)
        print(
            val,
            " Key LEN : ",
            dup_dict.keys().__len__(),
            "Total: ",
            dup_list.__len__(),
            "Execute Time : ",
            time.time() - start,
        )

    p_(i)
    p = Process(target=p_, args=(i,))
    p.start()


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        if len(logger.handlers) == 0:
            format_str = (
                "%(processName)s %(threadName)s : %(asctime)s:%(levelname)s:"
                "[%(filename)s:%(funcName)s():%(lineno)d]: %(message)s"
            )

            # print 'process:',process
            # print 'thread:',thread
            # print 'levelname:',levelname
            # print  'Module:',(name portion of filename).

            # print 'obj:,'name of the object(Eg:obj),current function( Eg: get_configured_logger) called by'
            # print 'class name:(obj is instance of class)'
            formatter = logging.Formatter(fmt=format_str)
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            logger.addHandler(handler)
