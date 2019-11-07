# -*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
BROKER_URL = "redis://192.168.72.128:6379/1"
CELERY_RESULT_BACKEND = 'redis://192.168.72.128:6379/2'