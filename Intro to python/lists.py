################### Subset and conquer #####################
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

print(areas[1])
print(areas[-1])
print(areas[5])


################# Slicing and dicing ######################
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[0:6]
upstairs = areas[-4:]
print(downstairs)
print(upstairs)

##################### Replace list Element ############
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area

areas[-1]= 10.50
areas[4]="chill zone"
#################### Extends a list #########################
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]


areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage",15.45]
#################### Inner Working of alist ####################
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

areas_copy = areas[:]

areas_copy[0] = 5.0

