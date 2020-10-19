# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:04:34 2020

@author: User
"""
import sys
from num2words import num2words
first=1
second=2
third=3
word=input('the word? ')
letter=input('letter to find? ')
if letter in word:
    for i in range(len(word)):
        if word[i]==letter:
            position=i+1
            print('the letter:', letter, 'is found in word at the', num2words(position, ordinal=True), 'position')
else: print('the letter:', letter, 'is not in word')
input('Press to quit')
sys.exit()