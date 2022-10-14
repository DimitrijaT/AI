import csv


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[:]
        data = [row[1:] for row in dataset]
        header = [row[0] for row in dataset]
        print()
    return data, header


if __name__ == '__main__':
    data, head = read_file("Finki-careers-transposed.csv")

    with open('test.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([" "] + head)

        counter = 0
        for r in range(len(data)):
            csv_row = [head[r]]
            for r_2 in range(len(data)):
                for element in data[r]:
                    if (element != " " and element != "") and element in data[r_2]:
                        counter += 1

                print(f'{head[r]} has {counter} similar subjects to {head[r_2]}')
                csv_row += [counter]
                counter = 0
            writer.writerow(csv_row)
        outfile.close()
