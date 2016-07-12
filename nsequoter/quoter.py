# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:59:47 2016

@author: adi
"""

from nsequoter import utils

utils=utils.Utils()

def get_equity_quote(eq):
    return utils.get_quote(eq)
    
def get_futures_quote(u, mon):
    return utils.get_quote(u, 'FUTSTK', mon)
        


    
