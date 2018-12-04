#!/usr/bin/env python
# coding:utf-8 
# +------------------------------------------
# | author: guijianliang
# | date： 2018/11/18 13:19
# +------------------------------------------

from flask import Blueprint

api = Blueprint('api',__name__,url_prefix='/api')

# 下面的要写在后面
from . import view







































