# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from werkzeug.routing import BaseConverter
from flask import g,session,jsonify
from ihome.utils.response_code import RET
import functools


class ReConvert(BaseConverter):
    """自定义转换器"""
    def __init__(self,url_map,regex):

        super(ReConvert,self).__init__(url_map)

        self.regex = regex


# 定义的验证登录状态的装饰器
def login_required(view_func):
    # wraps函数的作用是将wrapper内层函数的属性设置为被装饰函数view_func的属性
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户的登录状态
        user_id = session.get("user_id")

        # 如果用户是登录的， 执行视图函数
        if user_id is not None:
            # 将user_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录的信息
            return jsonify(errno=RET.SESSIONERR, errmsg="用户未登录")

    return wrapper