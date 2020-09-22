#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 14:07:50 2020

@author: kadah98
"""
import string

shift = 3
message = "happy"
def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    shiftDic = {}
    for i in range(len(string.ascii_lowercase)):
        if (i + shift) < 26:
            shiftDic[string.ascii_lowercase[i]] = string.ascii_lowercase[i + shift]
            shiftDic[string.ascii_uppercase[i]] = string.ascii_uppercase[i + shift]
        else:
            shiftDic[string.ascii_lowercase[i]] = string.ascii_lowercase[i + shift - 26]
            shiftDic[string.ascii_uppercase[i]] = string.ascii_uppercase[i + shift - 26]
    return shiftDic        
        

def apply_shift(shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
    
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    encryptedMessage = ""
    shiftDict = build_shift_dict(shift)
    for char in message:
        if char in shiftDict:
            encryptedMessage += shiftDict[char]
        else:
            encryptedMessage += char
    return encryptedMessage