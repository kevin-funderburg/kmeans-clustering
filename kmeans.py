import os
import numpy as np
import math
import argparse

MAX_ITERATIONS = 500


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', dest='k_input', nargs='?', default=None)
    parser.add_argument('-i', dest='input_file', nargs='?', default=None)
    args = parser.parse_args()

    # if not args.all:
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

    # pick K points as the initial centroids
    for x in range(k):
        centroids.append(DATA_SET[x])

    print('k = ' + str(k))

    # begin k-mean clustering
    for n in range(MAX_ITERATIONS):
        classes = {}
        for i in range(k):
            classes[i] = []

        # find the distance between the points and the centroids
        for point in DATA_SET:
            distances = []

            for index in centroids:
                distances.append(euclidean_distance(point, index))

            # find which cluster the datapoint belongs to by finding the minimum
            cluster_index = distances.index(min(distances))
            classes[cluster_index].append(point)

            if n == MAX_ITERATIONS-1:
                out_fname = input.replace("input", "output")
                output = open("./output/" + out_fname, "a")
                output.write("{0}\t{1}\t{2}\r".format(point[0], point[1], cluster_index+1))
                print("{0}\t{1}\t{2}".format(point[0], point[1], cluster_index+1))

        # now that we have classified the datapoints into clusters, we need to again
        # find new centroid by taking the centroid of the points in the cluster class
        for cluster_index in classes:
            centroids[cluster_index] = np.average(classes[cluster_index], axis=0)


def read_data(fname):
    k = None
    dataset = []

    input = open('./data/' + fname, 'r')

    # get the data from the input file
    for line in input:
        line = line.strip()
        if "k=" in line:
            k = int(line.split("=")[1])
        else:
            items = line.split("\t")
            for n in range(len(items)):
                if n == 0:
                    x = int(items[n])
                else:
                    y = int(items[n])

            dataset.append([x,y])

    return dataset


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


if __name__ == "__main__":
    main()
