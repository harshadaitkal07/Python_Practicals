import arcpy
import os

gdb_path = r"E:\programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
fc_name ="MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "HISTORIC"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        establishment_year = row[1]

        if establishment_year < 1960:
            row[2] = "YES"
        else:
            row[2] = "NO"

        u_cursor.updateRow(row)

print("Process Completed")

# import arcpy
# import os
#
# gdb_path = r"E:\programming_3\ProProject_Cursors\ProProject_Cursors.gdb"
# fc_name ="MajorAttractions"
#
# fc_path = os.path.join(gdb_path, fc_name)
#
# fields_list = ["NAME", "ESTAB", "ADDR", "CITYNM", "ZIP", "EMP", "ACRES"]
#
# record = ("New Town Restaurant", 2021, "841 STREET","SAN DIEGO", 92101, 150, 10)
#
# i_cursor = arcpy.da.InsertCursor(fc_path, fields_list)
# i_cursor.insertRow(record)
#
# print("Process Completed")