import numpy as np
import random
import sys

file = open('predictions.txt')
i = random.randint(1,100)
output_file = sys.argv[1]
output = open(output_file, 'w')
for i in file.readlines():
    result = i.strip().split(',')
    if len(result) != 20:
        result = result[:20]
    result = [float(i) for i in result]
    result = str(np.argmax(result))+','
    output.write(result)
    

