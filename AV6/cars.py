import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:]
        print()
    return dataset


if __name__ == '__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    # 70% mnozestvo ZA TRENIRANJE
    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    # 30% mnozestvo za TESTIRANJE
    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    # PROBA ZA EDEN
    predicted_class = classifier.predict([test_x[0]])[0]
    true_class = test_y[0]

    # MERENJE PRECIZNOST
    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1
    accuracy /= len(test_set)
    print(accuracy)

    entry = [element for element in input().split(" ")]
    encoded_entry = encoder.transform([entry])
    predicted_class = classifier.predict(encoded_entry)[0]
    print(predicted_class)
