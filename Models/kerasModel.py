"""
File    : kerasModel.py
purpose : 1.Train model on MNIST digit datset
"""

import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten
from keras.utils.np_utils import to_categorical
from keras.datasets import mnist
from keras.utils import np_utils

def train():

    # MNIST digit datset
    (X_train,Y_train),(X_test,Y_test) = mnist.load_data()
    X_train = X_train.reshape(60000,28,28,1)
    X_test = X_test.reshape(10000,28,28,1)
    X_train = X_train / 255
    X_test = X_test / 255
    Y_train = np_utils.to_categorical(Y_train)
    Y_test = np_utils.to_categorical(Y_test)
    num_classes = Y_test.shape[1]

    model = Sequential()
    # Add Convolutional layers
    model.add(Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same', input_shape=(28,28,1)))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same'))
    model.add(MaxPooling2D(pool_size=(2,2)))    
    model.add(Flatten())
    
    # Densely connected layers
    model.add(Dense(128, activation='relu'))
    
    # Output layer
    model.add(Dense(num_classes, activation='softmax'))
    
    # Compile with adam optimizer & categorical_crossentropy loss function
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(X_train, Y_train, validation_data=(X_test,Y_test), epochs = 10)
    model.save('digitRecogniser.h5')
    return model

model = train()