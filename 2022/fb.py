# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 15:42:04 2022

@author: jrozmaryn
"""
from facebook_scraper import *

for post in get_posts('rozmarynfamily',verify=False):
    print(post['text'][:50])