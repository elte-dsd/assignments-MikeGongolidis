# -*- coding: utf-8 -*-
"""CountMinSketch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Ttxh683RoOgPDUrHZwxeBTw37Dxjm7Y
"""

!pip install mmh3

import numpy as np
import pandas as pd
import mmh3

"""Initialize width of table:"""

width = int(input("Enter width of table:" ))

"""Initialize hash functions:"""

nhash = int(input("Enter number of hash functions < 1000: "))
hash_seeds = np.random.randint(1, 1000, int(nhash))

"""Input stream:"""

stream = input("Gime stream u want to test ")
unique_items = len(set(stream))
unique_items

"""Character to test:"""

character = input("Gime character u want to test:  ")

"""Actual algorithm starts here"""

table = pd.DataFrame(np.zeros((nhash, width)))
  

for ch in stream:
  for h in range(nhash):
    temp = mmh3.hash(ch,hash_seeds[h]) % width
    table.loc[h,temp] += + 1 
    
print(table)

"""Now for selected character we can return its frequency"""

freq = 1000
for h in range(nhash):
  freq = min(   table.loc[h,mmh3.hash(character,hash_seeds[h])%width] , freq ) 
  
print(freq)