#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv
import os 
import re

def Excel2CSV(ExcelFile, CsvDir):
    workbook = xlrd.open_workbook(ExcelFile)
    worksheets = workbook.sheet_names() # Get All Sheets

    for worksheet_name in worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        csv_file = open(''.join([CsvDir, worksheet_name, '.csv']), 'w', newline='')
        wr = csv.writer(csv_file, quoting = csv.QUOTE_MINIMAL, escapechar='"')

        print("Save " + worksheet_name + "...")
        #print(worksheet.cell(2, 0).ctype, worksheet.cell(2, 1).ctype)

        for rownum in range(1, worksheet.nrows):
            #wr.writerow([entry for entry in worksheet.row_values(rownum)])
            row = worksheet.row_values(rownum)
            processed_row = []  #save processed Data
            for cell in row:
                if isinstance(cell, str):
                    strValue = cell            #convert cell to string
                else:
                    strValue = (str(cell))

                isInt = bool(re.match("^([0-9]+)\.0$", strValue))
              
                if isInt:
                    strValue = int(float(strValue))
                else:
                    isFloat = bool(re.match("^([0-9]+)\.([0-9]+)$", strValue))
                    isLong = bool(re.match("^([0-9]+)\.([0-9]+)e\+([0-9]+)$", strValue))

                    if isFloat:
                        strValue = float(strValue)
                    if isLong:
                        strValue = int(float(strValue))
                

                processed_row.append(strValue)
            #row = [int(cell.value) if isinstance(cell.value, int) else cell.value for cell in worksheet.row_values(rownum)]
            wr.writerow(processed_row)

        csv_file.close()
    

def getListFiles(path):
    FileList = []
    for root, dirs, files in os.walk(path): 
        for filespath in files:
            filetype = os.path.splitext(filespath)[-1]
            filename = os.path.splitext(filespath)[-2]
            if filetype == '.xlsx' and filename.find('~$') == -1 :
                FileList.append(os.path.join(root, filespath))
    return FileList

def Check_Dependence():
    f = os.popen("pip list")
    Installed_Lib = f.readlines()
    f.close()

    isFind = False
    for item in Installed_Lib:
        if(item.find('xlrd') !=  -1):
            isFind = True
            break
    
    if not isFind:
        if os.system('pip install xlrd') == 0:
            print('pip install xlrd dependence ready')
        else:
            raise Exception("Can't install xlrd")
    else:
        print("Check Dependence Alread!")
        
if __name__ == '__main__':
    #Check dependence
    Check_Dependence()
    xlrd = __import__('xlrd')
    FileList = getListFiles(r"./Excel_Data/.")
    
    CsvDir = r'./CSV_Data/'
    for file in FileList:
        print("Read " + file + "...")
        Excel2CSV(file, CsvDir)