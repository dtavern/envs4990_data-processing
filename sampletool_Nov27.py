# Raster Sampling Tool  November 27, 2015
# Written by: David Tavernini (david.tavernini@uleth.ca)
# For ENVS4990 assignment
# This tool runs the ArcGIS spatial analyst Sample tool to extract values
# for raster cells and outputs them to a .dbf table in columns ID, X, Y, Value.
# It will run for all rasters in a given folder and output the files with the
# same filename in a specified folder.

import arcpy, os, re
from arcpy import env
from arcpy.sa import *

in_folder = r'C:\scratch\int' # input folder pathway for multi-raster processing 
out_folder = r'C:\scratch\Sample_SLP7911_SeaExtcsv' # output folder

arcpy.env.mask = 'C:\scratch\ProcessingExtent\NA_Coast_ext.shp' #Set the raster mask to limit processing extent

arcpy.CheckOutExtension("Spatial")                              #check for extension reqd for analysis
for raster in os.listdir(in_folder):                            #selects band for copy
    if raster.endswith(".tif"):                                 #check if input file is TIFF format
        print("Input file: " + raster)                          # Print output file
        outputprefix = os.path.splitext(raster)[0]              #Retrieve filename without extension for output name
        outputname = os.path.join(out_folder, outputprefix + ".csv") #generete output path
        inputname = os.path.join(in_folder, raster)             #Genereate input path
        sampMethod = "NEAREST"                                  #Sampling method used for analysis
        Sample(inputname, inputname, outputname, sampMethod)    #run Sample tool
        print "Ouput complete. file: " + outputname             #Completion confirmation
	 
