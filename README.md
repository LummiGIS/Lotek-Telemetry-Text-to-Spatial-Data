# Lotek-Telemetry-Text-to-Spatial-Data
Parses a Lotex  SRX800 output text file and converts the table to geo-spatial friendly data.  This script requires a Lotek text file as outputted from SRX800.  A user defined path to the text file is required prior to code execution.

Problem - The Lotek telemetry output file includes a heap of metadata followed by the actual telemetry tag data.  The telemetry tag data include extra spaces in table names and values, and non-ASCII character codes.  The inclusion of these text elements screws up any kind of drag-and-drop into a spreadsheet table.

This script reads each line of the telemetry file.  Once it finds the first line of the data table (a user defined input into the script) the script will parse those remaining data and convert to CSV.  The resulting CSV can be imported to a GIS.

USER DEFINED INPUTS:
1. The path to the telemetry text file (as a string).
2. The first line of the telemetry text file to collect data (as a string).
3. The power retun threshhold.  All power readings below this value will be discarded.
OUTPUT:
1. A CSV file in the same directory as the text file but with a csv suffex.
SCRIPT REQUIREMENTS:
1. The telemetry text file must be in a directory that the user has read and write permissions to.
