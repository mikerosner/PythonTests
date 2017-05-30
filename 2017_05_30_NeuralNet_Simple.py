

###########################Data Structures################################
#{
#  "neuralNet": {
#    "inputs" : [0, 1],
#    "outputs" : [2],
#    "weights" : [(0,2) : 0.1, (1,2) : 0.1]
#  }
#}
learningRate = 0.2

neuralNet = {
    "inputs" : [0, 1],
    "outputs" : [2],
    "weights" : {(0,2) : 0.1, (1,2) : 0.1}
  }

trainingSet = [(1,1,0)]

def evaluateAdjust(nn, train, lR):
  pred = train[0][0] * nn['weights'][(0,2)] + train[0][1] * nn['weights'][1,2]
  error = (train[0][2] - pred)**2
  print "prediction: ", pred, train[0][2]
  print "error: ", error
  #updateWeights (-1 * lR * (train[0][0] * nn['weights'][(0,2)]) * 
  #DELTA(i,j) = -1 * learningRate(lR) * Oi * (Oj - Tj) * Oj * (1-Oj) ; if j is an output neuron
  #DELTA(i,j) =           -1 * lR * Oi                                   * (Oj - Tj)            * Oj   * (1 - Oj) ; if j is an output neuron
  nn['weights'][(0,2)] += -1 * lR * (train[0][0] * nn['weights'][(0,2)]) * (pred - train[0][2]) * pred * (1 - pred)
  nn['weights'][(1,2)] += -1 * lR * (train[0][1] * nn['weights'][(1,2)]) * (pred - train[0][2]) * pred * (1 - pred)
  print "NeuralNet: ", nn

for x in range(0,100):
  evaluateAdjust(neuralNet, trainingSet, learningRate)
  

#To update the weight {\displaystyle w_{ij}} w_{ij} using gradient descent, one must choose a learning rate, 
#{\displaystyle \eta } \eta . The change in weight, which is added to the old weight, 
#is equal to the product of the learning rate and the gradient, multiplied by {\displaystyle -1} -1:

#def adjustWeights(nn, error, lR):
  #DELTA(i,j) = -1 * learningRate * Oi * (Oj - Tj) * Oj * (1-Oj) ; if j is an output neuron
  #Tj is the actual output for node j from the teacher set
  #Oj is the predicted output from the model
  
  
  
###########################Data Structures################################


#####Backpropogation######
#  initialize network weights (often small random values)
#  do
#     forEach training example named ex
#        prediction = neural-net-output(network, ex)  // forward pass
#        actual = teacher-output(ex)
#        compute error (prediction - actual) at the output units
#       compute {\displaystyle \Delta w_{h}} \Delta w_h for all weights from hidden layer to output layer  // backward pass
#        compute {\displaystyle \Delta w_{i}} \Delta w_i for all weights from input layer to hidden layer   // backward pass continued
#        update network weights // input layer not modified by error estimate
#  until all examples classified correctly or another stopping criterion satisfied
#  return the network
#####Backpropogation######
