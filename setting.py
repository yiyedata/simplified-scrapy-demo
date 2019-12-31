#!/usr/bin/python
#coding=utf-8
import logging
logging.basicConfig(
  level=logging.DEBUG,
  filename='spider.log',
  filemode='a',
  format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
SETTINGFILE='setting.json'
