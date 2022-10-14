import os.path

import numpy as np
from keras.layers import Dense, Dropout, Conv2D, LSTM, GRU, Activation
from keras.losses import categorical_crossentropy
from keras.models import Sequential, Model
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.preprocessing import MinMaxScaler

from AV9_Keras.visualize import plot_graph_loss


def read_dataset(file_path):
    """ Read the dataset and return the features and encoded classes

    :param file_path: path to the file that contains the dataset
    :type file_path: str
    :return: features and encoded classes
    :rtype: np.array, np.array
    """
    features = []
    classes = []
    with open(file_path) as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            features.append(list(map(float, parts[:-1])))
            classes.append(one_hot_encoding(int(parts[-1])))
    return np.array(features), np.array(classes)


def one_hot_encoding(sample):
    """ Encodes the ranking into class (with one-hot encoding)
    bad quality -> [1, 0, 0]
    medium quality -> [0, 1, 0]
    good quality -> [0, 0, 1]

    :param sample: one ranking value
    :type sample: int
    :return: one-hot encoded class
    :rtype: list(int)
    """
    if sample < 6:
        return [1, 0, 0]
    elif sample == 6:
        return [0, 1, 0]
    else:
        return [0, 0, 1]

    # тренирање, валидација и тестирање во соодносот 70%:10%:20%


def data_splitter(features, classes):
    features_train = features[:int(len(features) * 0.7)]
    classes_train = classes[:int(len(features) * 0.7)]

    print(features_train)
    print(classes_train)

    features_val = features[int(len(features) * 0.7):int(len(features) * 0.8)]
    classes_val = classes[int(len(features) * 0.7):int(len(features) * 0.8)]

    features_test = features[int(len(features) * 0.8):]
    classes_test = classes[int(len(features) * 0.8):]

    return features_train, classes_train, features_val, classes_val, features_test, classes_test


if __name__ == '__main__':
    features, classes = read_dataset("winequality-white.csv")

    features_train, classes_train, features_val, classes_val, features_test, classes_test = data_splitter(features,
                                                                                                          classes)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit(features_train)
    features_train = scaler.transform(features_train)

    # Create the model's layers
    model = Sequential()
    model.add(Dense(64, activation='relu', input_shape=(11,)))
    model.add(Dense(125, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(3, activation='softmax'))

    model.summary()
    optimizer = Adam(lr=0.001)

    # Compile the model
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the data
    history = model.fit(x=features_train, y=classes_train, batch_size=10, epochs=10, shuffle=True, verbose=2)

    print(history.history)

    print(model.predict(scaler.transform(features_test), batch_size=32, verbose=1))
    print(np.argmax(model.predict(scaler.transform(features_test), batch_size=32, verbose=1), axis=1))

    if os.path.isfile("wine_model.h5") is False:
        model.save("wine_model.h5")
    if os.path.isfile("wine_model_weights.h5") is False:
        model.save("wine_model_weights.h5")

    prediction = model.predict(scaler.transform(features_test), batch_size=32, verbose=1)
    convertedPrediction = np.argmax(prediction, axis=1)

    print(f'Accuracy = {accuracy_score(np.argmax(classes_test, axis=1), convertedPrediction)}')
    print(f'Precision = {precision_score(np.argmax(classes_test, axis=1), convertedPrediction, average="micro")}')
    print(f'Recall = {recall_score(np.argmax(classes_test, axis=1), convertedPrediction, average="micro")}')
    print(f'F1 score = {f1_score(np.argmax(classes_test, axis=1), convertedPrediction, average="micro")}')

    plot_graph_loss("winequality-white.csv", "model")