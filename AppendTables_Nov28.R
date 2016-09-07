# Append tables tool
# David Tavernini (david.tavernini@uleth.ca)
# November 28, 2015
#
# R-code to append columns from each table in a directory to the
# back end of the first table

filetype<-"*.dbf" #Inclue extension WITHOUT leading period
ColumnNumberToAppend<-4
InputPath<-"G:/tables/"
OutputFile<-"G:/outputtest/Compiled.txt"
StarterTable<-read.dbf("G:/tables/Export_Output.dbf")
AppendedTable<-StarterTable
allfiles<-list.files(path = InputPath, pattern = ".dbf", all.files = FALSE, full.names=TRUE,  recursive=FALSE, ignore.case=FALSE)

RunForAll<- function(x)
  CurrentTable<-read.dbf(x)
  AppendedTable<-merge(StarterTable, CurrentTable)

Finished<-lapply(allfiles, FUN = RunForAll)
  
write(StarterTable, OutputFile, append = FALSE, sep = "\t")
####


allfiles<-list.files(path = InputPath, pattern = ".dbf", all.files = FALSE, full.names=TRUE,  recursive=FALSE, ignore.case=FALSE)
RunForAll<- function(x)
  CurrentTable<-read.dbf(x)
Finished<-lapply(allfiles, FUN = RunForAll)