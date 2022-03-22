#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Enter the word: ")
    n = len(word)
    print("The length of this word is:" + str(n))
    word = n * '*' + word + n * '*'
    print(word)
