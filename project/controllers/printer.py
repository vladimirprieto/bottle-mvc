# -*- coding: utf-8 -*-
from bottle import template, request

def index(something=''):
    return template('printer/index', message='')


def printer(something=''):
    if request.method == 'POST':
        from project.models.Printer import Printer
        printer = Printer()
        message = printer.show_string(request.forms.get('text'))
        return template('printer/index', message=message)
    return template('printer/print', message='')

