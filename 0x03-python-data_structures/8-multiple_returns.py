#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
        if sentence:
            sen_len = len(sentence)
            first = sentence if not sentence else sentence[:1]
            second = sentence if not sentence else sentence[1:2]
            return (sen_len, first, second)
