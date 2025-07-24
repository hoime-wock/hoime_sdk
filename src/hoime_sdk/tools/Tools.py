# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
----------------------------------------
@所属项目 : Process
----------------------------------------
@作者     : French<1109527533@hoime.cn>
@软件     : PyCharm
@文件名   : Tools.py
@创建时间 : 2025/7/17 - 09:53
@修改时间 : 2025/7/17 - 09:53
@文件说明 : 工具方法
"""
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from datetime import datetime, timedelta


# 参数效验
def args_verify(args_list, request_data):
    """
    @编写作者: French \n
    @创建时间: 2025-07-17 \n
    @修改时间: 2025-07-17 \n
    @功能描述: 参数效验 \n

    Args:
        args_list: 参数列表
        request_data: 请求数据

    Returns:
        bool
    """
    args_set = set(args_list)
    keys_set = set(request_data.keys())
    status = True
    # 判断参数是否为空
    if args_set.issubset(keys_set):
        for i in args_set:
            if request_data[i] is None or request_data[i] == "":
                status = False
    else:
        status = False
    return status

# 数据分页
def data_pager(data_list, page_number, quantity=10):
    """
    @编写作者: French \n
    @创建时间: 2025-07-17 \n
    @修改时间: 2025-07-17 \n
    @功能描述: 数据分页器 \n

    Args:
        data_list: 数据列表
        page_number(str): 页数
        quantity(int): 数量

    Returns:
        list
    """
    # 类型转换
    page_number = int(page_number)
    quantity = int(quantity)
    # 页数列表
    page_list = Paginator(data_list, quantity)
    try:
        page = page_list.page(page_number)
    except EmptyPage:
        page = page_list.page(page_list.num_pages)
    data = {
        "current_page": page_number,
        "page_data": page.object_list,
        "quantity": page_list.count,
        "total_pages": page_list.num_pages
    }
    return data

# 获取指定天数前的工作日(不好含当天, 排除周六末和休息日)
def get_workday_by_days(date, days, holiday=None):
    """
    @编写作者: French \n
    @创建时间: 2025-07-23 \n
    @修改时间: 2025-07-23 \n
    @功能描述: 数据分页器 \n

    Args:
        date(date): 数据列表
        days(int): 天数
        holiday(list): 数量

    Returns:
        list
    """
    if holiday is None:
        holiday = []

    # 存储工作日的列表
    work_days = []

    # 设置前一天会检查日期
    check_date = date - timedelta(days=1)

    # 循环收集指定数量的工作日
    while len(work_days) < days:
        # 检查是否为工作日(小于5为工作日)
        if check_date.weekday() < 5:
            # 获取为字符串
            date_str = check_date.strftime("%Y-%m-%d")
            # 判断是否存在节假日中
            if date_str not in holiday:
                work_days.append(date_str)
        # 往前推一天
        check_date -= timedelta(days=1)
    work_days.reverse()
    return work_days


if __name__ == '__main__':
    new_datas = datetime.now()

    ass = get_workday_by_days(new_datas, 0)
    print(ass)
    for i in ass:
        print(i)