# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from werkzeug.routing import BaseConverter


class ReConvert(BaseConverter):
    """自定义转换器"""
    def __init__(self,url_map,regex):

        super(ReConvert,self).__init__(url_map)

        self.regex = regex