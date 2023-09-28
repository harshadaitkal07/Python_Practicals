# Task 1
# import os
#
# folder_path = r"E:\programming_3\Python_Practicals"
# file_name = "Harshada.txt"
# files_path = os.path.join(folder_path,file_name)
#
# # function to automate
# try:
#     with open (files_path,"r") as file:
#         for line in file:
#             print(line, end="")
# except FileNotFoundError:
#     print(f"The file '{files_path}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# Task 2
import arcpy
import os

arcpy.env.workspace = r"E:\Sem_3_Assingments\programming for GIS-3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

# Output folder path is where the txt file will get created
output_folder_path = r"E:\Sem_3_Assingments\programming for GIS-3"
# Output file name
# output_text_file = "MajorAttractions_info.txt"
#
# output_file_path = os.path.join(output_folder_path, output_text_file)
#
# print(output_file_path)
#
# file_obj = open(output_file_path, "w")
#
# # Listing feature class from the gdb
# fc_list = arcpy.ListFeatureClasses("MajorAttractions")
#
# for fc_name in fc_list:
#     print(fc_name)
#
# print("------------------------------------------------")
#
# # Listing fields and looping fields
# field_list = arcpy.ListFields("MajorAttractions")
# for field in field_list:
#     print("Field Name: {}, Type: {}, Length: {}".format(field.name, field.type, field.length))
#     file_obj.write("Name: {}, Type: {}, Length: {} \n".format(field.name, field.type, field.length))
#
#     print("------------------------------------------")
#     file_obj.write("---------------------------------------------\n")
# file_obj.close()
# print("Process Completed")




# Task 3
import arcpy

arcpy.env.workspace = r"E:\Sem_3_Assingments\programming for GIS-3\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists\ProProject_AutomatingUsingLists.gdb"

feature_class_list = arcpy.ListFeatureClasses()
print(feature_class_list)

for fc in feature_class_list:
    desc_obj = arcpy.Describe(fc)
    shape_type = desc_obj.shapeType


    # add buffer point: 500 ft, polyline: 1000 ft, polygon: 600 ft

    if shape_type == "Point":
        buffer_distance = "300 feet"
    elif shape_type == "Polyline":
        buffer_distance = "2000 feet"
    elif shape_type == "Polygon":
        buffer_distance = "500 feet"

    Output_buffer = fc + "_Buffer"
    arcpy.analysis.Buffer(fc, Output_buffer, buffer_distance)

print("process complete")