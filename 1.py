#coding: utf-8
'''
 字典的使用
'''

import sys

def collect(file):
    result = {}
    for line in file.readlines():
        left, right = line.split();
        if result.has_key(right):
            result[right].append(left)
        else:
            result[right] = [left]
    return result

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print 'ddd'
    else:
        result = collect(open(sys.argv[1],'r'))
        for (right, lefts) in result.items():
            print "%d  '%s' => %s" % (len(lefts), right, lefts)
            
