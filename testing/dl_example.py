from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Conv2D, LSTM, GRU
from keras.optimizers import Adam
from keras.losses import categorical_crossentropy

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10)))
model.add(Dense(125, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))

optimizer = Adam(lr=0.01)

model.compile(loss=categorical_crossentropy, optimizer=optimizer, metrics=['accuracy'])

# model.fit(X_train, Y_train, batch_size=32, epochs=5, verbose=1)

print(model.input_shape)
print(model.output_shape)

#
# output = activation(dot(input, kernel) + bias)
#
# model.fit_generator(train_generator,
#                     batch_size=32, nb_epoch=10, verbose=1)
#
# model.save(filepath)
#
# keras.models.load_model(filepath)
#
# model.predict(X_test, batch_size=32, verbose=1)
