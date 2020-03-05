import os
import numpy as np
import math
import argparse

MAX_ITERATIONS = 500


def main():
    # build argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', dest='k_input', nargs='?', default=None)
    parser.add_argument('-i', dest='input_file', nargs='?', default=None)
    args = parser.parse_args()

    if not args.k_input:
        print("k wasn't provided, try again!")
        return 0
    else:
        k_input = int(args.k_input)
        if k_input <= 1:
            print("k must be > 1, try again!")
            return 0

    if not args.input_file:
        print('no input file entered, try again!')
        return 0
    else:
        input = args.input_file
        inputFiles = os.listdir("./data")
        if input not in inputFiles:
            print(input + " is not an input file, try again!")
            return 0
        # delete output file
        output = "./output/" + input.replace("input", "output")
        if os.path.exists(output):
            os.remove(output)

    k = k_input
    DATA_SET = []
    centroids = []

    DATA_SET = read_data(input)
    output_file = open(output, "a")

    # pick K points as the initial centroids
    for x in range(k):
        centroids.append(DATA_SET[x])

    output_file.write('k = ' + str(k) + "\n")

    # begin k-mean clustering
    for n in range(MAX_ITERATIONS):
        classes = {}
        for i in range(k):
            classes[i] = []

        # find the distance between the points and the centroids
        for point in DATA_SET:
            distances = []

            for c in centroids:
                distances.append(euclidean_distance(point, c))

            # find which cluster the datapoint belongs to by finding the minimum
            cluster_index = distances.index(min(distances))
            classes[cluster_index].append(point)

            if n == MAX_ITERATIONS-1:
                # write to file
                output_file.write("{0}\t{1}\t{2}\n".format(point[0], point[1], cluster_index+1))

        # find new centroid by taking the centroid of the points in the cluster class
        for cluster_index in classes:
            centroids[cluster_index] = np.average(classes[cluster_index], axis=0)

    print("output written to '" + output + "' successfully")
    output_file.close()


def read_data(fname):
    """
    read data from input file
    :param fname: name of input file
    :return: array of data points
    """
    dataset = []

    input = open('./data/' + fname, 'r')

    for line in input:
        line = line.strip()
        items = line.split("\t")
        for n in range(len(items)):
            if n == 0:
                x = int(items[n])
            else:
                y = int(items[n])

        dataset.append([x,y])

    return dataset


def euclidean_distance(point1, point2):
    """
    calculate euclidean distance between two points
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


if __name__ == "__main__":
    main()
