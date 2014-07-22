'''
Created on 2014-7-22

@author: kongfy
'''

import sys
import string

allchars = string.maketrans('',  '')
keep = string.digits + string.whitespace + '.' 
delchars = allchars.translate(allchars, keep) + '\n'

def filter(s):
    return s.translate(allchars, delchars)

def main(argv):
    if len(argv) < 2:
        return
    
    inf = argv[1]
    f = open(inf)
    for line in f:
        index = line.find(':')
        title = line[:index]
        
        content = line[index + 1:]
        content = filter(content)
        
        output = title + content
        print ' '.join([x for x in output.split(' ') if x != ''])
    
    f.close()
    

if __name__ == '__main__':
    main(sys.argv)