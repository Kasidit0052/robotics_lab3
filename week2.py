# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 11:51:45 2020

@author: User
"""

import re
pin='12345'

def validate_pin(pin):
    pat = re.compile("^[0-9]{4}([0-9]{2})?$")
    if isinstance(pin,str):
        if pat.match(pin):
            return True
    return False
print(validate_pin(pin))
