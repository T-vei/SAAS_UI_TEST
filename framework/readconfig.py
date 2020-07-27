#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.ini')
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
FRAMEWORK_PATH = os.path.join(BASE_PATH, 'framework')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
PO_PATH = os.path.join(BASE_PATH, 'pageObject')
SCR_PATH = os.path.join(BASE_PATH, 'screenshot')
TOOL_PATH = os.path.join(BASE_PATH, 'tools')


class config():
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(CONFIG_FILE, encoding="UTF-8")

    def get(self,section,option):
        return self.conf.get(section,option)
    def sections(self):
        return self.conf.sections()

