# Task 1
# import arcpy
# import os
#
# gdb_path = r"E:\programming_3\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
# Histdist_fc_name = "Wilson_Histdist"
#
# Histdist_fc_path = os.path.join(gdb_path, Histdist_fc_name)
# arcpy.management.MakeFeatureLayer(Histdist_fc_path, "Histdist_layer")
#
# feature_count = arcpy.GetCount_management("Histdist_layer")
# print("Count of the Histdist  is",feature_count)

# Task_2
import arcpy
# import os
# gdb_path = r"E:\programming_3\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
# restaurant_fc_name = "Wilson_Restaurants"
# crime_fc_name = "Wilson_Crimes96"
#
# restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
# crime_fc_name_path = os.path.join(gdb_path, crime_fc_name)
#
# # Converting a feature class to feature layer
# arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_layer")
# arcpy.management.MakeFeatureLayer(crime_fc_name_path, "crime_layer")
#
# arcpy.management.SelectLayerByLocation("crime_layer", "WITHIN_A_DISTANCE", "restaurant_layer", "500 meters")
#
# output_crime_restaurant = "crime_within_500meters"
# output_crime_restaurant_path = os.path.join(gdb_path, output_crime_restaurant)
#
# Crime_count = arcpy.GetCount_management("crime_layer")
# print("The Count of Crime within 500 meters of distance from all the restaurants is ", Crime_count)
# print("Process Complete")

# Task 3
import arcpy
import os

gdb_path = r"E:\programming_3\ProProject_Selections\ProProject_Selections\ProProject_Selections.gdb"
restaurant_fc_name = "Wilson_Restaurants"
hist_fc_name = "Wilson_Histdist"
crime_fc_name = "Wilson_Crimes96"

restaurant_fc_path = os.path.join(gdb_path, restaurant_fc_name)
hist_fc_path = os.path.join(gdb_path, hist_fc_name)
crime_fc_path = os.path.join(gdb_path, crime_fc_name)

# Converting a feature class into a feature layer
arcpy.management.MakeFeatureLayer(restaurant_fc_path, "restaurant_lyr")
arcpy.management.MakeFeatureLayer(hist_fc_path, "hist_dist_lyr")
arcpy.management.MakeFeatureLayer(crime_fc_path, "crime_lyr")

# Getting count of all the feature before applying selection
pre_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant before applying selection is {}".format(pre_count[0]))

arcpy.management.SelectLayerByAttribute("restaurant_lyr", "NEW_SELECTION", "ALCOHOL = 1")
post_count = arcpy.GetCount_management("restaurant_lyr")
print("The Count of restaurant serving Alcohol {}".format(post_count[0]))
arcpy.management.SelectLayerByLocation("restaurant_lyr", "WITHIN_A_DISTANCE", "hist_dist_lyr", "1000 feet", "SUBSET_SELECTION")
post_count = arcpy.GetCount_management("restaurant_lyr")
print("The Restaurant within 1000 feet of hist_dist  {}".format(post_count[0]))
arcpy.management.SelectLayerByLocation("crime_lyr", "WITHIN_A_DISTANCE", "restaurant_lyr", "500 feet", "SUBSET_SELECTION")
post_count = arcpy.GetCount_management("crime_lyr")
print("The crimes within 500 feet of selected restaurants {}".format(post_count[0]))
arcpy.management.SelectLayerByAttribute("crime_lyr", "SUBSET_SELECTION", "ALCOHOL > 0")
post_count = arcpy.GetCount_management("crime_lyr")
print("The Count of selected alcohol related crimes {}".format(post_count[0]))

print("Process Completed")




