# // Task 1 //
# import arcpy
# import os
#
# gdb_path = r"E:\programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
# fc_name = 'MajorAttractions'
# fc_path = os.path.join(gdb_path, fc_name)
#
# fields_list = ["NAME", "ADDR"]
#
# with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
#     for row in s_cursor:
#         print("{}, {}".format(row[0], row[1]))
#
#
# print("Process is complete")

# // Task 2 //
# import arcpy
# import os
#
# gdb_path = r"E:\programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
# fc_name = 'MajorAttractions'
# fc_path = os.path.join(gdb_path, fc_name)
#
# fields_list = ["ESTAB", "NAME"]
#
# # Create a list to store the names of Major Attractions established after 1970
# major_attractions_after_1970 = []
#
# with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
#     for row in s_cursor:
#         estab = row[0]
#         if estab > 1970:
#             major_attractions_after_1970.append(row[1])  # Append the name to the list
#
# # Print the names of Major Attractions established after 1970
# for name in major_attractions_after_1970:
#     print(name)
#
# print("Process is complete")


# // Task 3 //
import arcpy
import os

gdb_path = r"E:\programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name = 'MajorAttractions'
fc_path = os.path.join(gdb_path, fc_name)

# Define the field names for X and Y coordinates
fields_list = ["SHAPE@X", "SHAPE@Y"]

with arcpy.da.SearchCursor(fc_path, fields_list) as s_cursor:
    for row in s_cursor:
        x_coord = row[0]  # X coordinate
        y_coord = row[1]  # Y coordinate
        print("X: {}, Y: {}".format(x_coord, y_coord))

print("Process is complete")