# Raster band extraction tool  November 27, 2015
#
# Written by: David Tavernini (david.tavernini@uleth.ca)
# For ENVS 4990 assignment
#
# This tool runs the ArcGIS Copy Raster tool to extract individual TIFF files
# from a multiband raster and outputs them to a specified folder with a file
# name the same as the band number without the 'Band_' prefix and appends leading
# zeroes to appear in correct sequential order for further ArcGIS analysis
#
# It was developed for a multiband raster containing daily sea pressure for
# every day from Jan 1, 1979 to Dec 31, 2011.
#
# It is currently set to extract ONLY days in September, October, and November
# from the years 1979 to 2011

import arcpy, os, re
in_raster = r'' # input multiband raster  
out_folder = r'' # preferably an empty folder  
 
desc = arcpy.Describe(in_raster) 

def getNextFilePath(output_folder):	#defines function to create incrementing file number -INACTIVE
	highest_num = 0
	for f in os.listdir(output_folder):
		if os.path.isfile(os.path.join(output_folder, f)):
			file_name = os.path.splitext(f)[0]
			try:
				file_num = int(file_name)
				if file_num > highest_num:
					highest_num = file_num
			except ValueError:
				'The file name "%s" is not an integer. Skipping' % file_name
  
	newname = highest_num + 1	#adds leading zeros onto file name -ACTIVE
	if newname < 10:
		newname1 = '0000' + str(newname)
	elif newname < 100:
		newname1 = '000' + str(newname)
	elif newname < 1000:
		newname1 = '00' + str(newname)
	elif newname < 10000:
		newname1 = '0' + str(newname)
	else: newname1 = str(newname)
	
	output_file = os.path.join(output_folder, newname1)
	return output_file

for band in desc.children:  #selects band for copy
	bandName1 = band.name #calls filename for band
	bandName = int(re.search(r'\d+', bandName1).group()) #extracts the integer from band filename
	if bandName < 10: #adds leading zeros onto file
		filename = '0000' + str(bandName)
	elif bandName < 100:
		filename = '000' + str(bandName)
	elif bandName < 1000:
		filename = '00' + str(bandName)
	elif bandName < 10000:
		filename = '0' + str(bandName)
	else: filename = str(bandName)
	band_path = os.path.join(in_raster, bandName1) #creates output pathway and executes tool if band integer falls on julian day of interest
	if 244 <= bandName <= 334 or 610 <= bandName <= 700 or 975 <= bandName <= 1065 or 1340 <= bandName <= 1430 or 1705 <= bandName <= 1795 or 2071 <= bandName <= 2161 or 2436 <= bandName <= 2526 or 2801 <= bandName <= 2891 or 3166 <= bandName <= 3256 or 3532 <= bandName <= 3622 or 3897 <= bandName <= 3987 or 4262 <= bandName <= 4352 or 4627 <= bandName <= 4717 or 4993 <= bandName <= 5083 or 5358 <= bandName <= 5448 or 5723 <= bandName <= 5813 or 6088 <= bandName <= 6178 or 6454 <= bandName <= 6544 or 6819 <= bandName <= 6909 or 7184 <= bandName <= 7274 or 7549 <= bandName <= 7639 or 7915 <= bandName <= 8005 or 8280 <= bandName <= 8370 or 8645 <= bandName <= 8735 or 9010 <= bandName <= 9100 or 9376 <= bandName <= 9466 or 9741 <= bandName <= 9831 or 10106 <= bandName <= 10196 or 10471 <= bandName <= 10561 or 10837 <= bandName <= 10927 or 11202 <= bandName <= 11292 or 11567 <= bandName <= 11657 or 11932 <= bandName <= 12022:
		print 'input:' + band_path 
		dest_path = os.path.join(out_folder, str(filename) + '.tif')  
		print 'output:' + dest_path
		arcpy.CopyRaster_management(band_path, dest_path, "", "", "", "NONE", "NONE", "") # change parameters here
	else: print bandName1 + ' not of interest'
