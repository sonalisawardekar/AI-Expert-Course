import tensorflow as tf

import matplotlib.pyplot as plt
import random

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test)

# Display the first image and prediction
print("\nFirst 10 Predictions:")
for i in range(10):
    predicted = predictions[i].argmax()
    actual = y_test[i]
    print(f"Image {i}: Predicted = {predicted}, Actual = {actual}")

# Show a random test image
index = random.randint(0, len(x_test) - 1)





plt.imshow(x_test[index], cmap='gray')
plt.title(f"Predicted: {predictions[index].argmax()} | Actual: {y_test[index]}")
plt.axis('off')
plt.show()