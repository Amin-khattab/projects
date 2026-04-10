import keras.layers
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.preprocessing.image import ImageDataGenerator


(x_train,y_train),(x_test , y_test) =mnist.load_data()

x_train = (x_train / 255.0 ).astype("float32")[...,None]
x_test = (x_test / 255.0).astype("float32")[...,None]

train_datagen = ImageDataGenerator(rotation_range=10,
                                   width_shift_range=0.1,
                                   height_shift_range=0.1,
                                   zoom_range=0.1,
                                   shear_range=0.1
                                   )

test_datagen = ImageDataGenerator()

train_generator = train_datagen.flow(x_train,y_train,batch_size=32)
test_generator = test_datagen.flow(x_test,y_test,batch_size=32)

cnn = keras.models.Sequential()

cnn.add(keras.layers.Conv2D(filters=32,activation="relu",kernel_size=3, input_shape=(28,28,1)))
cnn.add(keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(keras.layers.Conv2D(filters=32,activation="relu",kernel_size=3))
cnn.add(keras.layers.MaxPool2D(pool_size=2,strides=2))

cnn.add(keras.layers.Flatten())

cnn.add(keras.layers.Dense(units=128, activation="relu"))
cnn.add(keras.layers.Dense(units=10,activation="softmax"))

cnn.compile(optimizer = "adam", loss="sparse_categorical_crossentropy",metrics=['accuracy'])

cnn.fit(train_generator,validation_data = test_generator,epochs = 10)

test_loss,test_accuracy = cnn.evaluate(test_generator)
print(f"test loss {test_loss}")
print(f"test accuracy {test_accuracy}")

predictions = cnn.predict(x_test)

predicted_labels = predictions.argmax(axis=1)

print("sample predictions", predicted_labels[:20])
print("actual labels ",y_test[:20])

correct_predictions = (predicted_labels == y_test).sum()
wrong_predictions = len(y_test) - correct_predictions

print(f"correct predictions {correct_predictions}" )
print(f"wrong prdictions {wrong_predictions}")
