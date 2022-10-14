from sklearn.tree import DecisionTreeClassifier

dataset = [[6.3, 2.3, 4.4, 1.3, 2],
           [6.4, 2.8, 5.6, 2.1, 0],
           [5.1, 3.3, 1.7, 0.5, 1],
           [5.1, 3.5, 1.4, 0.2, 1],
           [4.6, 3.1, 1.5, 0.2, 1],
           [5.8, 2.7, 5.1, 1.9, 0],
           [5.5, 3.5, 1.3, 0.2, 1],
           [5.7, 2.6, 3.5, 1.0, 2],
           [5.0, 3.5, 1.3, 0.3, 1],
           [6.3, 2.5, 5.0, 1.9, 0],
           [6.2, 2.2, 4.5, 1.5, 2],
           [5.0, 3.4, 1.6, 0.4, 1],
           [5.7, 4.4, 1.5, 0.4, 1],
           [4.9, 2.4, 3.3, 1.0, 2],
           [4.4, 2.9, 1.4, 0.2, 1],
           [5.5, 2.4, 3.7, 1.0, 2],
           [5.6, 2.5, 3.9, 1.1, 2],
           [5.6, 2.8, 4.9, 2.0, 0],
           [4.8, 3.4, 1.6, 0.2, 1],
           [5.6, 3.0, 4.5, 1.5, 2],
           [6.0, 3.0, 4.8, 1.8, 0],
           [6.3, 3.3, 4.7, 1.6, 2],
           [4.8, 3.0, 1.4, 0.1, 1],
           [7.9, 3.8, 6.4, 2.0, 0],
           [4.9, 3.0, 1.4, 0.2, 1],
           [4.3, 3.0, 1.1, 0.1, 1],
           [6.8, 3.2, 5.9, 2.3, 0],
           [5.6, 2.7, 4.2, 1.3, 2],
           [5.2, 4.1, 1.5, 0.1, 1],
           [6.2, 2.9, 4.3, 1.3, 2],
           [6.5, 2.8, 4.6, 1.5, 2],
           [5.4, 3.9, 1.3, 0.4, 1],
           [5.8, 2.6, 4.0, 1.2, 2],
           [5.4, 3.7, 1.5, 0.2, 1],
           [4.5, 2.3, 1.3, 0.3, 1],
           [6.3, 3.4, 5.6, 2.4, 0],
           [6.2, 3.4, 5.4, 2.3, 0],
           [5.7, 2.5, 5.0, 2.0, 0],
           [5.8, 2.7, 3.9, 1.2, 2],
           [6.4, 2.7, 5.3, 1.9, 0],
           [5.1, 3.8, 1.6, 0.2, 1],
           [6.3, 2.5, 4.9, 1.5, 2],
           [7.7, 2.8, 6.7, 2.0, 0],
           [5.1, 3.5, 1.4, 0.3, 1],
           [6.8, 2.8, 4.8, 1.4, 2],
           [6.1, 3.0, 4.6, 1.4, 2],
           [5.5, 4.2, 1.4, 0.2, 1],
           [5.0, 2.0, 3.5, 1.0, 2],
           [7.7, 3.0, 6.1, 2.3, 0],
           [5.1, 2.5, 3.0, 1.1, 2],
           [5.9, 3.0, 5.1, 1.8, 0],
           [7.2, 3.2, 6.0, 1.8, 0],
           [4.9, 3.1, 1.5, 0.2, 1],
           [5.7, 3.0, 4.2, 1.2, 2],
           [6.1, 2.9, 4.7, 1.4, 2],
           [5.0, 3.2, 1.2, 0.2, 1],
           [4.4, 3.2, 1.3, 0.2, 1],
           [6.7, 3.1, 5.6, 2.4, 0],
           [4.6, 3.6, 1.0, 0.2, 1],
           [5.1, 3.4, 1.5, 0.2, 1],
           [5.2, 2.7, 3.9, 1.4, 2],
           [6.4, 3.1, 5.5, 1.8, 0],
           [7.4, 2.8, 6.1, 1.9, 0],
           [4.9, 3.1, 1.5, 0.1, 1],
           [5.0, 3.5, 1.6, 0.6, 1],
           [6.7, 3.1, 4.7, 1.5, 2],
           [6.4, 3.2, 5.3, 2.3, 0],
           [6.3, 2.7, 4.9, 1.8, 0],
           [5.8, 4.0, 1.2, 0.2, 1],
           [6.9, 3.1, 5.4, 2.1, 0],
           [5.9, 3.2, 4.8, 1.8, 2],
           [6.6, 2.9, 4.6, 1.3, 2],
           [6.1, 2.8, 4.0, 1.3, 2],
           [7.7, 2.6, 6.9, 2.3, 0],
           [5.5, 2.6, 4.4, 1.2, 2],
           [6.3, 2.9, 5.6, 1.8, 0],
           [7.2, 3.0, 5.8, 1.6, 0],
           [6.5, 3.0, 5.8, 2.2, 0],
           [5.4, 3.9, 1.7, 0.4, 1],
           [6.5, 3.2, 5.1, 2.0, 0],
           [5.9, 3.0, 4.2, 1.5, 2],
           [5.1, 3.7, 1.5, 0.4, 1],
           [5.7, 2.8, 4.5, 1.3, 2],
           [5.4, 3.4, 1.5, 0.4, 1],
           [4.6, 3.4, 1.4, 0.3, 1],
           [4.9, 3.6, 1.4, 0.1, 1],
           [6.7, 2.5, 5.8, 1.8, 0],
           [5.0, 3.6, 1.4, 0.2, 1],
           [6.7, 3.3, 5.7, 2.5, 0],
           [4.4, 3.0, 1.3, 0.2, 1],
           [6.0, 2.2, 5.0, 1.5, 0],
           [6.0, 2.2, 4.0, 1.0, 2],
           [5.0, 3.4, 1.5, 0.2, 1],
           [5.7, 2.8, 4.1, 1.3, 2],
           [5.5, 2.4, 3.8, 1.1, 2],
           [5.1, 3.8, 1.9, 0.4, 1],
           [6.9, 3.1, 5.1, 2.3, 0],
           [5.6, 2.9, 3.6, 1.3, 2],
           [6.1, 2.8, 4.7, 1.2, 2],
           [5.5, 2.5, 4.0, 1.3, 2],
           [5.5, 2.3, 4.0, 1.3, 2],
           [6.0, 2.9, 4.5, 1.5, 2],
           [5.1, 3.8, 1.5, 0.3, 1],
           [5.7, 3.8, 1.7, 0.3, 1],
           [6.7, 3.3, 5.7, 2.1, 0],
           [4.8, 3.1, 1.6, 0.2, 1],
           [5.4, 3.0, 4.5, 1.5, 2],
           [6.5, 3.0, 5.2, 2.0, 0],
           [6.8, 3.0, 5.5, 2.1, 0],
           [7.6, 3.0, 6.6, 2.1, 0],
           [5.0, 3.0, 1.6, 0.2, 1],
           [6.7, 3.0, 5.0, 1.7, 2],
           [4.8, 3.4, 1.9, 0.2, 1],
           [5.8, 2.8, 5.1, 2.4, 0],
           [5.0, 2.3, 3.3, 1.0, 2],
           [4.8, 3.0, 1.4, 0.3, 1],
           [5.2, 3.5, 1.5, 0.2, 1],
           [6.1, 2.6, 5.6, 1.4, 0],
           [5.8, 2.7, 4.1, 1.0, 2],
           [6.9, 3.2, 5.7, 2.3, 0],
           [6.4, 2.9, 4.3, 1.3, 2],
           [7.3, 2.9, 6.3, 1.8, 0],
           [6.3, 2.8, 5.1, 1.5, 0],
           [6.2, 2.8, 4.8, 1.8, 0],
           [6.7, 3.1, 4.4, 1.4, 2],
           [6.0, 2.7, 5.1, 1.6, 2],
           [6.5, 3.0, 5.5, 1.8, 0],
           [6.1, 3.0, 4.9, 1.8, 0],
           [5.6, 3.0, 4.1, 1.3, 2],
           [4.7, 3.2, 1.6, 0.2, 1],
           [6.6, 3.0, 4.4, 1.4, 2]]


def divide_data():
    train_set1 = dataset[:int(len(dataset) * 0.3)]
    train_set2 = dataset[int(len(dataset) * 0.3):int(len(dataset) * 0.6)]
    train_set3 = dataset[int(len(dataset) * 0.6):]
    return train_set1, train_set2, train_set3


def get_x_and_y(given_set):
    set_x = [row[:-1] for row in given_set]
    set_y = [row[-1] for row in given_set]
    return set_x, set_y


if __name__ == '__main__':

    # Divide the data:
    first_train_set, second_train_set, third_train_set = divide_data()

    # Get the x and y for all three datasets:
    first_train_set_x, first_train_set_y = get_x_and_y(first_train_set)
    second_train_set_x, second_train_set_y = get_x_and_y(second_train_set)
    third_train_set_x, third_train_set_y = get_x_and_y(third_train_set)

    # Declare model:
    first_classifier = DecisionTreeClassifier(random_state=0)
    second_classifier = DecisionTreeClassifier(random_state=0)
    third_classifier = DecisionTreeClassifier(random_state=0)

    # Train model:
    first_classifier.fit(first_train_set_x, first_train_set_y)
    second_classifier.fit(second_train_set_x, second_train_set_y)
    third_classifier.fit(third_train_set_x, third_train_set_y)

    # User input:
    user_input_entry_x = [float(element) for element in input().split(", ")][:-1]

    # Make prediction with the three classifiers
    first_prediction = int(first_classifier.predict([user_input_entry_x]))
    second_prediction = int(second_classifier.predict([user_input_entry_x]))
    third_prediction = int(third_classifier.predict([user_input_entry_x]))

    votes = [0, 0, 0]

    votes[first_prediction] += 1
    votes[second_prediction] += 1
    votes[third_prediction] += 1

    votes = {0: votes[0], 1: votes[1], 2: votes[2]}

    print(f"Glasovi: {votes}")

    most_votes = -1
    highest_vote = votes.get(0)

    if votes[0] == votes[1] and votes[1] == votes[2]:
        print("unknown")
    else:
        for key in votes.keys():
            if votes.get(key) >= highest_vote:
                highest_vote = votes.get(key)
                most_votes = key

        print(f"Predvidena klasa: {most_votes}")
