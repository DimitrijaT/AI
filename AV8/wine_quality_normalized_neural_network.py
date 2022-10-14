from wine_quality_neural_network import read_dataset, divide_set
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_set(dataset)

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    scaler = StandardScaler()
    scaler.fit(train_x)

    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    classifier = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x, train_y)
    classifier2.fit(scaler.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions = classifier.predict(val_x)
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc1 += 1
    val_acc1 /= len(val_set)

    print(f'Bez normalizacija tochnost na validacisko mnozestvo: {val_acc1}')

    val_acc2 = 0
    val_predictions = classifier2.predict(scaler.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc2 += 1
    val_acc2 /= len(val_set)

    print(f'So StandardScaler tochnost na validacisko mnozestvo: {val_acc2}')

    val_acc3 = 0
    val_predictions = classifier3.predict(scaler2.transform(val_x))
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc3 += 1
    val_acc3 /= len(val_set)

    print(f'So MinMaxScaler tochnost na validacisko mnozestvo: {val_acc3}')

    # точност = (TP + TN) / (TP + FP + TN + FN)
    # прецизност = TP / (TP + FP)
    # одзив = TP / (TP + FN)

    tp, tn, fp, fn = 0, 0, 0, 0
    predictions = classifier3.predict(scaler2.transform(test_x))
    for true, pred in zip(test_y, predictions):
        if true == "good":
            if pred == true:
                tp += 1
            else:
                fn += 1
        else:
            if pred == true:
                tn += 1
            else:
                fp += 1


        # accuracy
    tocnost = (tp + tn) / (tp + fp + tn + fn)

    # precision
    preciznost = tp / (tp + fp)

    # recall
    odziv = tp / (tp + fn)

    print("Evaluacija:")
    print(f'Tocnost: {tocnost}')
    print(f'Preciznost: {preciznost}')
    print(f'Odziv: {odziv}')
