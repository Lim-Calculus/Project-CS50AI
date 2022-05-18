## Observation
The model structure of my Neural Network will be Total of 3 Convolution Neural Network Model (CNN) Block
and one hidden layers with 512 units ( 2^9 = 512 ) and one output layer with 43 units.

The model is sequential.

Each CNN Block consists of two Convolutional Layer, one with same padding(padding="same") and one without same padding, a max pooling layer(2x2) with dropout of 0.25.

I choose ReLU as activation function because CNN with ReLU can be trained faster.

The output layer has 43 units same as the number of categories ( 0 -42 ) 

I found out that this models can work well in this project as the final result with accuracy of 0.9858 and loss of 0.0509.

I found out if I increase the number of the hidden neurons from 512 (2^9) to 1024(2^10), the accuracy is dropped, maybe overfitting occured at this point. 

## Details of the Model (Sequential)
## First CNN :
1. First Convolutional Layer with (2^5=32) filters, kernel size of 3x3 with same padding
2. Second Convolutional Layer with 32 filters, kernel size of 3x3 without the same padding
3. Max pooling layer with the size of 2x2 and same padding
4. The Dropout is set to 0.25

## Second CNN :
1. First Convolutional Layer with (2^6=64) filters, kernel size of 3x3 with same padding
2. Second Convolutional Layer with 64 filters, kernel size of 3x3 without the same padding
3. Max pooling layer with the size of 2x2 and same padding
4. The Dropout is set to 0.25


## Third CNN :
1. First Convolutional Layer with (2^7=128) filters, kernel size of 3x3 with same padding
2. Second Convolutional Layer with 128 filters, kernel size of 3x3 without the same padding
3. Max pooling layer with the size of 2x2 and same padding
4. The Dropout is set to 0.25

## Hidden Layer :
2^9=512 neurons, activation function=ReLU, The Dropout is set to 0.25

## Output Layer:
43 neurons, activation function =softmax

