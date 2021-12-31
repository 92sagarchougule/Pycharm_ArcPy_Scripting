import arcpy

class LicenseError(Exception):
    pass

try:
    if (arcpy.CheckExtension('3d')=='available'):
        arcpy.CheckOutExtension('3d')
    else:
        #rise costom exception
        raise LicenseError

        arcpy.env.workspace = r'D:\TmpGIS'
        arcpy.HillShade_3d(r'D:\TmpGIS\Ras_Data\DEM.tif','Hillshed',300)
        arcpy.Aspect_3d(r'D:\TmpGIS\Ras_Data\DEM.tif','Aspect')
        arcpy.CheckInExtension('3D')
except LicenseError:
    print('3D analysis tool is not avaible')
except arcpy.ExecuteError:
    print(arcpy.getmessages(2))
