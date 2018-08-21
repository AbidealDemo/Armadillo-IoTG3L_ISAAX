#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

if __name__ == '__main__':
    message = os.environ.get('MESSAGE', 'I am G3L.')
    while True:
        print('Hello World. {}'.format(message))
        time.sleep(10)
