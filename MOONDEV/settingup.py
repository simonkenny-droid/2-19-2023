# command B; side panel


# import packages

import pandas as pd # storing data like excel
import numpy as np # helps with maths
import onecall # connects to exchange to buy and sell
import time


#how t connect to an exchange
# get API KEYS and secret

# API KEY - Y4mPaPYPeqodVQkE9t1mPKoAMPiE6TATrPychFX9eZGN99yOjyacqvlZ0gaCagQM
# API SECRET - ZygPV8HtFyGqjMGcIglKAIg1k1vifUNL8v25JCtckC4VC7lfd6L5csJGVpXhZ3o8

onecall = onecall.phemex(
    key='dee161c5-4899-4b44-a334-5f4e3d75b108',
    secret='McSn1kKGdg8-PXn4EdWxM6BnUfRbIEehz4-JPSvPVXRjZGUxOWI3Ni1kZjIxLTQzZTUtYWIxNy04Y2QwOGI3YjAyMDM'
)

# check our balance 

#bal = onecall.get_balance()

#print (bal)

# get our position 
pos = onecall.get_positions('USD')
print (pos)


# positions

#pos = onecall.get_positions('ETHUSTD')

# get historical data 

