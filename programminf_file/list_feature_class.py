# import arcpy
# arcpy.env.workspace=r""
#
# fc_list = arcpy.listFeatureClasses()
# for fc_name in fc_lists:
#     print(fc_name)
import arcpy

---------------
field_list= arcpy.ListFields("Freeways")

for field in field_list:
    print(field.name)
    print(field.type)
    print(field.length)
    print("------------------------")