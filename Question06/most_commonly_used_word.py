'''find the most
commonly used word of each txt file
in a directory'''

import re
import os
from collections import Counter


def wc(filename):
    with open(filename, 'r') as f:
        wordlist = []
        for line in f:
            content = re.sub('\W+',' ',line)
            wordlist.extend(content.lower().strip().split(' '))
    return Counter(wordlist).most_common(1)


def most_comm(aim_dir):
    dir_name = r'{}'.format(aim_dir)
    txt_list = os.walk(dir_name)
    print 'most common:'
    for root, dirs, files in txt_list:
        for file in files:
            print '{}:'.format(file)
            txt = os.path.join(dir_name,file)
            most_common=wc(txt)
            for letter, count in most_common:
                print '%s: %7d' % (letter,count)















