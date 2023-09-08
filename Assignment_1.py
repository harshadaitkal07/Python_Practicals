# # Task 2
# #         integer greater than 50
# #         Define the numbers
# integers = [75,85,50,35,49,48,95]
#
#         # loop trough the list
# for num in integers:
#         if num > 50:
#                 print("The numbers greater than 50 are {}".format(num))

# Task 3
#
# # import arcpy
# # arcpy.env.workspace = r"E:\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
# #
# # arcpy.analysis.Buffer("wilson_schools", "wilson_500m", "500 meters")
# #
# # print("process completed")

# task 3.1
# import arcpy
# arcpy.env.workspace = r"E:\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
# # specify the feature class
# input_feature_class="Wilson_schools"
# output_feature_class="Wilson_Schools_MultiRingBuffer_non_dissolve"
#
# # buffer
# buffer_distance=[1000,1200, 1400]
# arcpy.analysis.MultipleRingBuffer(input_feature_class,output_feature_class,buffer_distance,"Feet","","NONE")
#
# print("process completed")

# # Task 4
# import arcpy
# arcpy.env.workspace = r"E:\programming_3\ProProject_Practical_One\ProProject_Practical_One\ProProject_Practical_One\Practical_One.gdb"
# input_layer="Wilson_Zoning"
# output_layer="Wilson_zoning_feature_to_points"

# arcpy.management.FeatureToPoint(input_layer,output_layer,"CENTROID")
#
# print("process completed")