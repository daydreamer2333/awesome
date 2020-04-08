#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#默认配置文件，比如数据库的用户名，口令等
configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'mysql',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}