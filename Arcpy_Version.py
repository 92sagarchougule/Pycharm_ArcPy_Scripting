import arcpy

d = arcpy.GetInstallInfo()

for key, value in list(d.items()):
    print("{:<13} : {}".format(key,value))
    

