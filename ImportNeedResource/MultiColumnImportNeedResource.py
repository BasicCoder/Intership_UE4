#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv
import os
import re

def FindIndex(HeaderList, Elem):
    for i, j  in enumerate(HeaderList):
        if j == Elem:
            return i
    return -1

def ImportNeedResourcePerRow(row, according_indexs, fill_indexs, ResourceDirs):
    for i in range(0, len(according_indexs)):
        according_name = row[according_indexs[i]]
        resource_name = ResourceDirs[i] + according_name

        row[fill_indexs[i]] = resource_name
    return row

def ImportNeedResource(CsvFileDir, SrcCsvFileName, AccordingFieldNames, DstCsvFileName, FillFieldNames, ResourceDirs):
    csv_source_file = open(''.join([CsvFileDir, SrcCsvFileName, '.csv']), 'r', newline = '', encoding = 'utf-8')
    csv_destion_file = open(''.join([CsvFileDir, DstCsvFileName, '.csv']), 'w', newline = '', encoding = 'utf-8')
    reader = csv.reader(csv_source_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')

    if len(AccordingFieldNames) != len(FillFieldNames) and len(FillFieldNames) != len(ResourceDirs):
        raise Exception('Paramater Length not equal!')

    header = next(reader)
    according_indexs = []
    fill_indexs = []

    for fieldname in AccordingFieldNames:
        index = FindIndex(header, fieldname)
        according_indexs.append(index)


    for fieldname in FillFieldNames:
        index = FindIndex(header, fieldname)
        fill_indexs.append(index)

    writer = csv.writer(csv_destion_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')
    writer.writerow(header)


    for row in reader:
        processed_row = ImportNeedResourcePerRow(row, according_indexs, fill_indexs, ResourceDirs)
        writer.writerow(processed_row)



if __name__ == '__main__':
    CsvFileDir = r'./CSV_Data/'
    SrcCsvFileName = r'Item'
    AccordingFieldNames = [r'Key']

    DstCsvFileName = SrcCsvFileName + r'Procssed'
    FillFieldNames = [r'Icon']
    ResourceDirs = [r'/Game/UI/Kitbag/icon/']

    print("Reading " + CsvFileDir + SrcCsvFileName + "...")
    ImportNeedResource(CsvFileDir, SrcCsvFileName, AccordingFieldNames, DstCsvFileName, FillFieldNames, ResourceDirs)
    print("Save " + CsvFileDir + DstCsvFileName + '.csv')


