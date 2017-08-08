#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import csv
import os
import re

def ImportItemIcon(CsvFileDir, CsvFileName, IconDir):
    csv_source_file = open(''.join([CsvFileDir, CsvFileName, '.csv']), 'r', newline='', encoding = 'utf-8')
    csv_destion_file = open(''.join([CsvFileDir, CsvFileName, 'WithIcon', '.csv']), 'w', newline='', encoding = 'utf-8')
    reader = csv.reader(csv_source_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')

    print(csv_source_file)
    #add Icon Field
    header = next(reader)
    
    header.append('Icon')
    print(header)

    #Write csv File Header
    writer = csv.writer(csv_destion_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')
    writer.writerow(header)

    index = header.index('Key')
    for line in reader:
        Id = line[index]
        IconName = IconDir + Id + '.' + Id
        line.append(IconName)
        writer.writerow(line)


if __name__ == '__main__':

    CsvFileDir = r'./CSV_Data/'
    CsvFileName = r'Item'
    IconDir = r'/Game/UI/Kitbag/icon/'

    ImportItemIcon(CsvFileDir, CsvFileName, IconDir)
    