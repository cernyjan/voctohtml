# -*- coding: utf-8 -*-
# čžřě+áýčíáý+í
"""
name: voctohtml -- vocabulary HTML generator in Python 
autor: Černý Jan
email: cerny.jan@hotmail.com
version: 0.1
"""
#import - own packages
#import - system packages
import ctypes
from time import sleep
#import - others packages


def main():
    """
    Main process of the voctohtml
    """
    print "\r"
    print "*********************************************"
    print "voctohtml v0.1 \t autor: Černý Jan \t 2015"
    print "*********************************************"
    print "\r"

if __name__ == '__main__':
    #change name of running process
    LIBC = ctypes.CDLL('libc.so.6')
    PROC_NAME = "voctohtml"
    LIBC.prctl(15, '%s\0' %PROC_NAME, 0, 0, 0)
    #sleep for 1s
    sleep(1)
    
    #main thread
    main()