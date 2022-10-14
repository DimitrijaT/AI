from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
import graphviz
import csv

import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

# DEL ZA VIZUELIZACIJA SAMO!
from sklearn import tree
import matplotlib.pyplot as plt


def read_file(file_name, encoding="utf8"):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        set = list(csv_reader)
        heading = set[:1]
        data_set = set[1:]
        # print()
    return data_set


def divide_data_balanced(data_set, percent):
    yes_set = [row for row in data_set if row[-1] == 1]
    no_set = [row for row in data_set if row[-1] == 0]

    percent /= 100
    train_set = yes_set[:int(len(yes_set) * percent)] + no_set[:]
    test_set = yes_set[int(len(yes_set) * percent):] + no_set[int(len(no_set) * percent):]
    return train_set, test_set


def get_x_and_y(given_set):
    set_x = [row[:-1] for row in given_set]
    set_y = [row[-1] for row in given_set]
    return set_x, set_y


def remove_feature(train_x, test_x, featureToRemove, heading):
    train_x_2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i not in list(featureToRemove)]
        train_x_2.append(row)
    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i not in list(featureToRemove)]
        test_x_2.append(row)

    heading_2 = [heading[i] for i in range(len(heading)) if i not in featureToRemove]

    return train_x_2, test_x_2, heading_2


def stats_printer(classifier, test_set, test_x, test_y):
    print("##################################################")
    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of Leaves: {classifier.get_n_leaves()}')

    feature_importances = list(classifier.feature_importances_)
    print(f'Feature importances: {feature_importances}')

    most_important_feature = feature_importances.index(max(feature_importances))
    print(f'Most Important Feature: {most_important_feature}')

    least_important_feature = feature_importances.index(min(feature_importances))
    print(f'Least Important Feature: {least_important_feature}')

    accuracy(classifier, test_set, test_x, test_y)

    # точност = (TP + TN) / (TP + FP + TN + FN)
    # прецизност = TP / (TP + FP)
    # одзив = TP / (TP + FN)

    tp, tn, fp, fn = 0, 0, 0, 0
    predictions = classifier.predict(test_x)
    for true, pred in zip(test_y, predictions):
        if true == 1:
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
    tocnost = 0
    if (tp + fp + tn + fn) != 0:
        tocnost = (tp + tn) / (tp + fp + tn + fn)

    # precision
    preciznost = 0
    if (tp + fp) != 0:
        preciznost = tp / (tp + fp)

    # recall
    odziv = 0
    if (tp + fn) != 0:
        odziv = tp / (tp + fn)

    print("Evaluacija:")
    print(f'Tocnost: {tocnost}')
    print(f'Preciznost: {preciznost}')
    print(f'Odziv: {odziv}')

    print("##################################################")
    return most_important_feature, least_important_feature


def accuracy(classifier, test_set, test_x, test_y):
    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1
    accuracy /= len(test_set)
    print(f'Accuracy: {accuracy}')


def print_plot_tree(classifier):
    tree.plot_tree(classifier)
    fig = plt.figure(figsize=(30, 30))
    _ = tree.plot_tree(classifier,
                       feature_names=["Gender?", "Younger or Older?",
                                      "Are you physically active?",
                                      "Would you like to get notifications to exercise?",
                                      "Do you count calories?", "Do you have proper sleep schedule?",
                                      "Do you have negative effects from lack of sleep?",
                                      "Would you like to get notifications to help have a proper sleep schedule?",
                                      "Do you deal with stress on a daily basis?",
                                      "Do you already use an app to track your health?"],
                       class_names=["NO", "YES"],
                       filled=True,
                       rounded=True,
                       fontsize=24,
                       proportion=True,
                       label='all')
    plt.show()


# "Gender?", "Younger or Older?",
#                                       "Are you physically active?",
#                                       "Would you like to get notifications to exercise?",
#                                       "Do you count calories?", "Do you have proper sleep schedule?",
#                                       "Do you have negative effects from lack of sleep?",
#                                       "Would you like to get notifications to help have a proper sleep schedule?",
#                                       "Do you deal with stress on a daily basis?",
#                                       "Do you already use an app to track your health?"

def print_graphviz(classifier, heading):
    # DOT data
    dot_data = tree.export_graphviz(classifier, out_file=None,
                                    feature_names=list(heading),
                                    class_names=["No", "Yes"],
                                    filled=True,
                                    rounded=True,
                                    proportion=True,
                                    special_characters=True)

    # Draw graph
    graph = graphviz.Source(dot_data, format="png")
    graph.render("decision_tree_graphivz")


def dataset_to_binary_preprocessing(data_set):
    data_set_2 = []
    for row in data_set:
        row_2 = []
        for i in range(len(row)):
            if i == 0:
                if row[i] == 'Male':
                    row_2.append(1)  # Male = 1
                else:
                    row_2.append(0)  # Female = 0
                continue
            if i == 1:
                if row[i] == '18 - 24':
                    row_2.append(1)  # Young 1
                else:
                    row_2.append(0)  # Old 0
                continue
            elif i == 2:
                if row[i] == '0 - 1':
                    row_2.append(0)  # NO = 0
                else:
                    row_2.append(1)  # YES = 1
                continue
            elif i == 5:
                if row[i] == 'I always sleep at the same time':
                    row_2.append(1)  # YES = 1
                else:
                    row_2.append(0)  # NO = 0
                continue
            elif i == 8:
                if int(row[i]) >= 3:
                    row_2.append(1)
                else:
                    row_2.append(0)
                continue
            else:
                if row[i] == 'Yes':
                    row_2.append(1)
                else:
                    row_2.append(0)
                continue
        data_set_2.append(row_2)
    return data_set_2


if __name__ == '__main__':
    data_set = read_file("Questionnaire2.csv")
    heading = ["Gender?", "Younger or Older?",
               "Are you physically active?",
               "Would you like to get notifications to exercise?",
               "Do you count calories?", "Do you have proper sleep schedule?",
               "Do you have negative effects from lack of sleep?",
               "Would you like to get notifications to help have a proper sleep schedule?",
               "Do you deal with stress on a daily basis?",
               "Do you already use an app to track your health?"]
    data_set = dataset_to_binary_preprocessing(data_set)
    print()

    train_set, test_set = divide_data_balanced(data_set, 80)
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in data_set])

    train_x, train_y = get_x_and_y(train_set)
    test_x, test_y = get_x_and_y(test_set)

    train_x = encoder.transform(train_x)
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', max_depth=4, max_leaf_nodes=15)
    classifier.fit(train_x, train_y)

    most_important_feature, least_important_feature = stats_printer(classifier, test_set, test_x, test_y)
    train_x, test_x, heading = remove_feature(train_x, test_x, [0, 1, 3, 6, 7], heading)
    # train_x, test_x, heading = remove_feature(train_x, test_x, most_important_feature, heading)
    # train_x, test_x, heading = remove_feature(train_x, test_x, least_important_feature, heading)

    classifier2 = DecisionTreeClassifier(criterion='entropy', max_depth=4, max_leaf_nodes=15, random_state=1,
                                         ccp_alpha=0.02)
    classifier2.fit(train_x, train_y)

    most_important_feature, least_important_feature = stats_printer(classifier2, test_set, test_x, test_y)

    print(len(train_x[0]))
    print(len(heading))
    print(classifier2.classes_)
    print_graphviz(classifier2, heading)
