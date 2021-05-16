
#Using numpy to represent only one neuron
import numpy as np
inputs=[1,2,3,3.5]
weights=[0.5,0.8,0.9,0.3]
bias=2
output=np.dot(weights,inputs)+bias
print(output)
#Using numpy to represent only multiple neurons

inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1]
,[0.5,-0.91,-0.26,-0.5],
[-0.26,-0.27,0.17,0.87]]
biases=[2,3,0.5]

output1=np.dot(weights,inputs)+bias
print(output1)
