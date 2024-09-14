#!/usr/bin/env python3
import sys
import importlib.util

if __name__ == "__main__":
    ''' Load the hidden_4.pyc module '''
    
    # Load the compiled module using importlib
    module_name = 'hidden_4'
    spec = importlib.util.spec_from_file_location(module_name, './hidden_4.pyc')
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    ''' Retrieve all names from the module '''
    names = dir(hidden_4)
    
    ''' Filter and print names that do not start with __ '''
    for name in sorted(names):
        if not name.startswith('__'):
            print(name)
