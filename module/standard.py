import pandas as pd
import io
import math
 
## function to return standard deviation
## based on excel file of numbers

def standard(file_name):

# read file
    df = pd.read_csv(file_name)

# use measures of central tendency
    dfcount = df.numbers.count()
    dfsum = df.numbers.sum()
    dfaverage = dfsum / dfcount
    print ( dfaverage )

    squaredsum = 0
    temp = 0
 
#  summation for standard deviation
    for x in range ( dfcount ):
        print ( df.numbers[x] )
        temp = ( df.numbers[x] - dfaverage )
        print ( temp )
        temp *= temp
        print ( temp )
        squaredsum += temp

    deviation = squaredsum / dfcount 

# square root for deviation
    deviation = math.sqrt( deviation ) 

   
    return deviation
