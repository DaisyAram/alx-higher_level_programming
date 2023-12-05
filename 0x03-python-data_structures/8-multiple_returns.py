#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first_char = sentence[0] if leng > 0 else "None"
    tup = leng,first_char
    return (tup)
