#!/home/snelliott/anaconda/bin/python

"""This is a python module that converts temperatures
"""

def f_to_k(temp):
    converted = ((temp - 32 ) * (5.0/9)) + 273.15 
    return converted


def k_to_c(temp):
    return (temp - 273.15)

def f_to_c(temp):
    return k_to_c( f_to_k(temp ))

print(f_to_c(32))
