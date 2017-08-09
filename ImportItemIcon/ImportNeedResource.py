#!/usr/bin/env python 
#-*- coding:utf-8 -*-

import csv
import os
import re

def FindIndex(HeaderList, Elem):
    for i, j in enumerate(HeaderList):
        if j == Elem:
            return i
    return -1

def ImportNeedResource(CsvFileDir, SrcCsvFileName, AccordingFieldName, DstCsvFileName, FillFieldName, ResourceDir):
    csv_source_file = open(''.join([CsvFileDir, SrcCsvFileName, '.csv']), 'r', newline='', encoding = 'utf-8')
    csv_destion_file = open(''.join([CsvFileDir, DstCsvFileName, '.csv']), 'w', newline='', encoding = 'utf-8')
    reader = csv.reader(csv_source_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')

    #print(csv_source_file)
    #add Icon Field
    header = next(reader)
    
    index = FindIndex(header, FillFieldName)
    if index == -1:
        header.append(FillFieldName)


    #Write csv File Header
    writer = csv.writer(csv_destion_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')
    writer.writerow(header)

    KeyIndex = header.index(AccordingFieldName)
    IconIndex = header.index(FillFieldName)
    for line in reader:
        Id = line[KeyIndex]
        ResourceName = ResourceDir + Id + '.' + Id
        #line.append(IconName)
        if IconIndex >= len(line):
            line.insert(IconIndex, ResourceName)
        else:
            line[IconIndex] = ResourceName
        writer.writerow(line)


if __name__ == '__main__':

    CsvFileDir = r'./CSV_Data/'
    SrcCsvFileName = r'Item'
    AccordingFieldName = r'Key'

    DstCsvFileName = SrcCsvFileName + r'WithIcon'
    FillFieldName = r'Icon'
    ResourceDir = r'/Game/UI/Kitbag/icon/'
    
    print("Reading " + CsvFileDir + SrcCsvFileName + "...")
    ImportNeedResource(CsvFileDir, SrcCsvFileName, AccordingFieldName, DstCsvFileName, FillFieldName, ResourceDir)
    print("Save " + CsvFileDir + DstCsvFileName + '.csv')
    