import os

folder_path= r"E:\programming_3\Python_Practicals"
file_name= "readme.txt"
file_path = os.path.join(folder_path,file_name)
file_obj=open(file_path,'r')
# print(file_obj.readlines())

lines = file_obj.readlines()
count =1
for line in lines :
    print("{} -{}".format(count,line))
    count= count+ 1