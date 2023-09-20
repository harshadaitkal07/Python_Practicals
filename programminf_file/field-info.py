import arcpy
import os

arcpy.env.workspace=
folder_path=r"E:\programming_3\Python_Practicals"
output_text_file="field_information.txt"
output_file_path=(os.path.join(folder_path,output_text_file)
                  
file_obj= open (output_file_path,"w")

fc_list=arcpy.ListfeatureClasses()

for name in fc_list:
    print(name)
    file_obj_write(name+"\n")

    field_list=arcpy.ListFields(name)
    for field in field_list:
        print("Name:{},Type:{},Length:{}".format(field.name,field.type,field.length))
        file_obj.write("Name :{},Type:{},Length:{}\n".format(field.name,field.type,field.length))

        print("---------------")
        file_obj.write("---------------\n")

file_obj.close()
print("Process completed")
