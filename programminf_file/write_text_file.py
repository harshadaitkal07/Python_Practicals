import os
folder_path =r"E:\programming_3\Python_Practicals"
file_name="writeme.txt"
file_path =os.path.join(folder_path, file_name)
file_obj=open(file_path,'w')
input_text="Helllooo everyone,this is a text write ex."

file_obj.write(input_text)
file_obj.close()
print("Process completed")