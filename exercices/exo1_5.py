#! /usr/bin/env Python3

def au_carrer(num):
    return num*num

nums=[9,5,7,14]
carre= map(au_carrer,nums)
print(list(carre))