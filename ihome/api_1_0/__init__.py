# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Blueprint
api = Blueprint('api_1_0',__name__)

from . import demo
from . import verify_code,passport,profile