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

###########################initialization################################


###########################initialization################################
