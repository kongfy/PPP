# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import time

def configs():
    for root, dirs, files in os.walk('configs'):
        for filename in files:
            yield os.path.join(root, filename)

def main():
    config_filename = os.path.join(os.getcwd(), 'config.py')
    result_dir = os.path.join(os.getcwd(), 'results')
    for config in configs():
        shutil.copy(config, config_filename)
        time.sleep(3)
        
        if not os.path.exists(result_dir):
            os.mkdir(result_dir)
        
        output = os.path.basename(config)[:os.path.basename(config).rfind('.')] + '.out'
        cmd = 'python main.py > ' + os.path.join(result_dir, output)
        
        print cmd
        os.system(cmd)
        
        

if __name__ == '__main__':
    main()
        