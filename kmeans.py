import os
import re
import numpy as np
import math
import argparse

centroids = []
DATA_SET = []
k = None
MAX_ITERATIONS = 500


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', dest='k_input', nargs='?', default=None)
    args = parser.parse_args()

    if not args.k_input:
        print("k wasn't provided, try again!")
        return 0

    if args.k_input:
        k_input = int(args.k_input)
        if k_input <= 1:
            print("k must be > 1, try again!")
            return 0

    read_data()

    # pick K points as the initial centroids
    for n in range(k):
        centroids.append(DATA_SET[n])

    print('k = ' + str(k))

    # start k-mean clustering
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
                print("{0}\t{1}\t{2}".format(point[0], point[1], cluster_index+1))

        # now that we have classified the datapoints into clusters, we need to again
        # find new centroid by taking the centroid of the points in the cluster class
        for cluster_index in classes:
            centroids[cluster_index] = np.average(classes[cluster_index], axis=0)

    print('done')


def read_data():
    global k
    input1 = open('./data/input1.txt', 'r')

    # get the data from the input file
    for line in input1:
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

            DATA_SET.append([x,y])


def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


if __name__ == "__main__":
    main()