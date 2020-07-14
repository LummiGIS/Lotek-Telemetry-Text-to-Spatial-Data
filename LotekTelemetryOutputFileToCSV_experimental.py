# -*- coding: utf-8 -*-

'''This tool takes a Lotek telemetery txt file, parces and formats the data, and writes those data to a new csv file in the same director
as the text file. 

USER DEFINED INPUTS:
1. The path to the telemetry text file (as a string).
2. The first line of the telemetry text file to collect data (as a string).
3. The power retun threshhold.  All power readings below this value will be discarded.
OUTPUT:
1. A CSV file in the same directory as the text file but with a csv suffex.

SCRIPT REQUIREMENTS:
1. The telemetry text file must be in a directory that the user has read and write permissions to.

'''
import sys
import traceback
import re
import io
try:
    ###############    USER DEFINED INPUT PARAMETERS...    ####################
    
    #The path to the input Lotek SRX800 data file...
    inTelemetryTextFile = r"Z:\GISpublic\GerryG\StockAssesment\Lotek\aeria_data\20190703.TXT"
    #The line from the text file.  All data below this line to the 'end of data' are writen to the csv.
    dataStartLine = ' Date   Time         Channel  Tag ID        Antenna   Power   Data  Sensor Type       Latitude      Longitude'
    #powerThreshold
    powerThreshold = 50
    ###########################################################################
    outCSV = inTelemetryTextFile.split(".")[0]
    outCSV = outCSV + '.csv'
     
     
    outCSV = open(outCSV, 'a')
    #inTelemetryTextFile = io.open(inTelemetryTextFile,'r')io.open('myfile.txt', encoding='latin-1')
    inTelemetryTextFile = io.open(inTelemetryTextFile, encoding='latin-1')
    record = 0
    for line in inTelemetryTextFile:
        
        if line == dataStartLine:
            #Lotek puts a space in one of the column headings, fix that.
            line = line.replace( 'Tag ID', 'TagID')
            line = line.replace('Sensor Type', 'SensorType')
            record = 1
        
        if 'End of Data' in line:
            record = 0
        if record == 1:
            try:
                line = line.replace(u"TEMP [°C]", u"TempC")
            except:
                print "failed"
                pass
            
            #The lines have spaces of different lengths between the column headings, convert those to single commas.
            line = re.sub('\s+', ',', line).strip()
            #some rows have a space at the beginning, this would get a comma so if there, remove it...
            if line[0] == ',':
                line = line[1:]
            #strip off the trailing comma if there is one but skip line of length zero to avoid a crash...
            if len(line) != 0:
                if line[-1] == ',':
                    #print line
                    line = line[:-1]
            #TagID 999 is junk data, and power values < powerThreshold are junk data, do not write these lines to the output CSV.
            #Check the row for 999 values but skip the header row
            splitLine = line.split(",")
            if len(line)==0:
                pass
            else:
                if splitLine[3] == '999' or (splitLine[5].isdigit() and int(splitLine[5])< powerThreshold):
                    pass
                #elif  splitLine[5].isdigit():
                #    if int(splitLine[5])< powerThreshold:
                #        pass
                else:
                    #remove the plus sign in the latitude column
                    if "+" in splitLine[8]:
                        splitLine[8] = splitLine[8].replace('+', '')
                        
                        
                    line = ','.join(map(str, splitLine))  +'\n'
                    outCSV.write(line)
            
    outCSV.close()
    print 'done'

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
