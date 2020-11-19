import pandas as pd
import io
import math
 
df = pd.read_csv('sd.csv')
print (df)

dfcount = df.numbers.count()
print ( dfcount )

dfsum = df.numbers.sum()
print ( dfsum )

dfaverage = dfsum / dfcount
print ( dfaverage )

squaredsum = 0
temp = 0
 
for x in range ( dfcount ):
    print ( df.numbers[x] )
    temp = ( df.numbers[x] - dfaverage )
    print ( temp )
    temp *= temp
    print ( temp )
    squaredsum += temp

print ( squaredsum )

deviation = squaredsum / dfcount 
deviation = math.sqrt( deviation )
print ( deviation )
