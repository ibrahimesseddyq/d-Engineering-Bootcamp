#################### Numpy array ######################
import numpy as np
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball)
print(type(np_baseball))

################### Baseball Player Height ############
import numpy as np



np_height_in = np.array(height_in)
print(np_height_in)

np_height_m = np_height_in * 0.0254

print(np_height_m)
#################### Baseball Player BMI ###############
import numpy as np

np_height_m = np.array(height_in) * 0.0254
np_weight_kg  = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
print(bmi)
#################### Lightweight baseball player ########
import numpy as np

np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2
light = bmi < 21
print(light)

################### Subsetting Numpy Array ##############
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)
print(np_weight_lb[50])
print(np_height_in[100:111])

################## Numpy 2D array ########################
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np
np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)

#################### Subsetting 2D arrays ###############
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])
np_weight_lb = np_baseball[:,1]
print(np_baseball[123,0])

###################### Average Versus Median ############
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np.array(np_baseball[:,0])

# Print out the mean of np_height_in
print(np.mean(np_height_in))
print(np.median(np_height_in))