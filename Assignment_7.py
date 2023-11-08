# import arcpy
# import os
#
# x_delhi = 77.24270285484538
# y_delhi = 28.66340264879396
#
# # Point object
# pnt_obj = arcpy.Point(x_delhi, y_delhi)
#
# # spatial reference object
# spatial_ref = arcpy.SpatialReference("WGS 1984")
#
# #  Point geometry
# pnt_geom = arcpy.PointGeometry(pnt_obj, spatial_ref)
#
# gdb_path = r"E:\programming_3\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
# fc_name = "Delhi"
# fc_path = os.path.join(gdb_path, fc_name)
#
# arcpy.CopyFeatures_management(pnt_geom, fc_path)
#
# print("Process Completed")


# import arcpy
# import os
#
# gdb_path = r"E:\programming_3\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
# output_fc_name = "Mumbai_to_Pune"
# output_fc_path = os.path.join(gdb_path, output_fc_name)
#
# x_pune = 73.8555859597187
# y_pune = 18.523965380098787
#
# X_Mumbai = 72.8535870040652
# y_Mumbai = 19.100986206019183
#
# # point objects
# pnt_pune_obj = arcpy.Point(x_pune, y_pune)
# pnt_mumbai_obj = arcpy.Point(X_Mumbai, y_Mumbai)
#
# # Spatial reference object
# spatial_ref = arcpy.SpatialReference("WGS 1984")
#
# #Array object
# polyline_array = arcpy.Array()
#
# polyline_array.add(pnt_pune_obj)
# polyline_array.add(pnt_mumbai_obj)
#
# polyline_geom = arcpy.Polyline(polyline_array, spatial_ref)
#
# arcpy.CopyFeatures_management(polyline_geom, output_fc_path)
#
# print("Process completed")

import arcpy
import os

gdb_path = r"E:\programming_3\Practical_7_ProProject\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
output_fc_name = "Pune_to_Thane_to_Mumbai"
output_fc_path = os.path.join(gdb_path, output_fc_name)

x_pune = 73.8555859597187
y_pune = 18.523965380098787

x_thane = 72.90727867649676
y_thane = 19.105285611625437

X_Mumbai = 72.83301745259699
Y_Mumbai = 18.929366647248877

pnt_pune_obj = arcpy.Point(x_pune, y_pune)
pnt_thane_obj = arcpy.Point(x_thane, y_thane)
pnt_mumbai_obj = arcpy.Point(X_Mumbai, Y_Mumbai)

# Spatial reference object
spatial_ref = arcpy.SpatialReference("WGS 1984")

polygon_array = arcpy.Array()

polygon_array.add(pnt_pune_obj)
polygon_array.add(pnt_thane_obj)
polygon_array.add(pnt_mumbai_obj)

polygon_geom = arcpy.Polygon(polygon_array, spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, output_fc_path)

print("Process completed")