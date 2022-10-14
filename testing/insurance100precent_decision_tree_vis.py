from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
import csv

# OVIE 2 NE SE DEL OD MATERIJALOT, ZA VIZUELIZACIJA SAMO!
from sklearn import tree
import matplotlib.pyplot as plt


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:]
        # print()
    return dataset


if __name__ == '__main__':
    dataset = read_file('insurance.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    # 100% mnozestvo ZA TRENIRANJE
    train_set = dataset[:]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x_pure = train_x
    train_x = encoder.transform(train_x)

    classifier = DecisionTreeClassifier(criterion='entropy', max_depth=500, max_leaf_nodes=500, random_state=0)
    classifier.fit(train_x, train_y)

    tree.plot_tree(classifier)
    fig = plt.figure(figsize=(50, 40))
    _ = tree.plot_tree(classifier,
                       feature_names=["Rabota", "Patnicko", "Pol", "Ponuda"],
                       class_names=["DA", "NE"],
                       filled=True)
    plt.show()
