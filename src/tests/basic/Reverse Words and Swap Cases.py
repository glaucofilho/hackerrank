import math
import os
import random
import re
import sys


def reverse_words_order_and_swap_cases(sentence):
    sentence = sentence.swapcase()
    s_list = sentence.split(" ")
    s_list.reverse()
    s = " ".join(s_list)
    return s


a = reverse_words_order_and_swap_cases("aWESOME is cODING")
