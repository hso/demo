#! /usr/bin/env python
from petl.fluent import fromcsv


if __name__ == '__main__':
    # argument1|!1|!
    table = fromcsv('../input.csv', delimiter=';')

    for row in table.data():
        print 'yuhuu!'

