import numpy as np
import sys


class Cluster:


    def __init__(self,number_attributes,min,max):
        self.centroid = np.random.uniform(min,max,number_attributes)
        self.points = []
        self.point_index = []


    def clearPoints(self):
        self.points = []
        self.point_index = []

    def getCentroid(self):
        return self.centroid

    def calculateDistance(self,point):
        return np.linalg.norm(self.centroid-point)

    def addPoint(self,point,index):
        self.points.append(point)
        self.point_index.append(index)

    def calculateCentroid(self):
        if (len(self.points)): self.centroid = np.average(self.points,axis=0)


    def __str__(self):
        return "Centroid: %s \n \n Index: %s" % (self.centroid,self.point_index)

def createClusters(k,number_attributes,min,max):
    cluster_list = []
    for i in range(k) : cluster_list.append(Cluster(number_attributes,min,max))
    return cluster_list

def kmeans(clusters, x, threshold,max_iter):

    number_iterations = 0
    convergence = False

    while (not convergence and number_iterations < max_iter):

        for cluster in clusters: cluster.clearPoints()

        for point_index in range(len(x)):
            min = 0
            min_dist = sys.maxint
            point = x[point_index]
            for cluster in clusters:
                dist = cluster.calculateDistance(point)
                if (dist < min_dist):
                    min = clusters.index(cluster)
                    min_dist = dist
            clusters[min].addPoint(point,point_index)
        old_centroids = []

        for cluster in clusters:
            old_centroids.append(cluster.centroid)
            cluster.calculateCentroid()

        for i in range(len(clusters)) :
            cluster = clusters[i]
            if (cluster.calculateDistance(old_centroids[i]) > threshold) : break
            convergence = True

        number_iterations+=1
        print "Number of iterations: " + str(number_iterations)

def compress(clusters,x):
    for cluster in clusters:
        for i in range(len(cluster.points)):
            x[cluster.point_index[i]] = cluster.centroid





