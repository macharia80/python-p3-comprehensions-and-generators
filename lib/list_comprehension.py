#!/usr/bin/env python3
num_list = range(0,10)
def return_evens(num_list):
    num_list = [
        0,1,2,3,4,5,6,7,8,9
    ]
    return [num for num in num_list if num % 2 == 0]
pass


def make_exclamation(sentence_list):
    sentence_list = [
        "I like computers",
        "I require coffee",
        "Live long and prosper",
    ]
    return [sentence + '!' for sentence in sentence_list]
pass