import arcpy

fc = r'D:\TmpGIS\shp_Data\CityOfOleander.mdb\Property Data\Blocks'


# Get the count from GetCount's Result object
feature_count = int(arcpy.GetCount_management(fc).getOutput(0))

if feature_count == 0:
    arcpy.AddError("{0} has no features.".format(fc))
else:
    arcpy.AddMessage("\n\n{0} has {1} features.".format(fc, feature_count))
