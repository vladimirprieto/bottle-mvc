# -*- coding: utf-8 -*-
__version__ = '0.1'

from bottle import Bottle, TEMPLATE_PATH
import cgi
import re

app = Bottle()

TEMPLATE_PATH.append("./project/views/")
TEMPLATE_PATH.remove("./views/")

import routes

