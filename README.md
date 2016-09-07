# envs4990_data-processing

##Description
This series of python and R scripts takes a multiband raster and splits it into separate rasters, converts each new .tif file into an ASCII format. Notes are included in the script for customizing input/output directories and other settings.

##Author
Scripts compiled by: David Tavernini
email: david.tavernini@uleth.ca

##Original Usage
These scripts were developed to process multiband raster daily sea-level pressure data for an independent study at the University of Lethbridge. The objective was to take a multiband raster (each band representing one day sea-level pressure) and split the bands into individual .tif files. In doing this, we were able to then batch convert the .tif files into .dbf tables containing cell ID, X coordinate of cell, Y coordinate of cell, and SLP value. Finally, using R, we matched all the X/Y coordinates for each of the .dbf tables and appended the daily sea level pressure values, resulting in a final table with X/Y coordinates, and a column for each day's sea level pressure.

##Instructions for use
###Band Splitting
Open the `.py` script called `RasterBandExtraction_Nov27.py` and find notes to adjust you input folder, output folder, and file output names. Note the block of script:
```python
band_path = os.path.join(in_raster, bandName1) #creates output pathway and executes tool if band integer falls on julian day of interest
	if 244 <= bandName <= 334 or 610 <= bandName <= 700 or 975 <= bandName <= 1065 or 1340 <= bandName <= 1430 or 1705 <= bandName <= 1795 or 2071 <= bandName <= 2161 or 2436 <= bandName <= 2526 or 2801 <= bandName <= 2891 or 3166 <= bandName <= 3256 or 3532 <= bandName <= 3622 or 3897 <= bandName <= 3987 or 4262 <= bandName <= 4352 or 4627 <= bandName <= 4717 or 4993 <= bandName <= 5083 or 5358 <= bandName <= 5448 or 5723 <= bandName <= 5813 or 6088 <= bandName <= 6178 or 6454 <= bandName <= 6544 or 6819 <= bandName <= 6909 or 7184 <= bandName <= 7274 or 7549 <= bandName <= 7639 or 7915 <= bandName <= 8005 or 8280 <= bandName <= 8370 or 8645 <= bandName <= 8735 or 9010 <= bandName <= 9100 or 9376 <= bandName <= 9466 or 9741 <= bandName <= 9831 or 10106 <= bandName <= 10196 or 10471 <= bandName <= 10561 or 10837 <= bandName <= 10927 or 11202 <= bandName <= 11292 or 11567 <= bandName <= 11657 or 11932 <= bandName <= 12022
```
which will only process julian days between each of those ranges. Otherwise it will output a string saying it is not of interest:
```python
else: print bandName1 + ' not of interest'
```

###.dbf conversion
Once all bands have been split, use `sampletool_Nov27.py` to convert raster files to .dbf tables. Take note of the input/output directories as defined by the notes in the script. There is one section of the script which you can define a vector shapefile as a mask to limit processing extent:
```python
arcpy.env.mask = 'C:\scratch\ProcessingExtent\NA_Coast_ext.shp'
```

### Compiling all tables into one .dbf
Once all bands have been converted to .dbf, you may append all subsequent tables onto the first by running `AppendTables_Nov28.R`. Take note of the codeblock:
```R
filetype<-"*.dbf" #Inclue extension WITHOUT leading period
ColumnNumberToAppend<-4
InputPath<-"G:/tables/"
OutputFile<-"G:/outputtest/Compiled.txt"
StarterTable<-read.dbf("G:/tables/Export_Output.dbf")
```
which allows you to set the column number which to append to the main table, directory of input tables, the file which will be output, and the starting table. Once completed you should have a one master .dbf that has complied the selected columns of all you individual .dbf files.


