import os
import re
import math

centroids = {}
classes1 = []
classes2 = []
DATA_SET = []
k = None


def main():
    read_data()

    # pick K points as the initial centroids
    for n in range(k):
        centroids.append(DATA_SET[n])

    print('k = ' + str(k))

    # find the distance between the points and the centroids
    for point in DATA_SET:
        distances = []

        for index in centroids:
            distances.append(euclidean_distance(point, index))

        # find which cluster the datapoint belongs to by finding the minimum
        cluster_index = distances.index(min(distances))
        if cluster_index == 0:
            classes1.append(point)
        else:
            classes2.append(point)
        # classes[cluster_index].append(point)
        print("{0}\t{1}\t{2}".format(point[0], point[1], cluster_index))

    print('done')


def read_data():
    global k
    input1 = open('input1.txt', 'r')

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