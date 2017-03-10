import numpy as np
import sys
import random

class Cluster:


    def __init__(self,number_attributes,min,max):
        self.centroid = np.random.uniform(min,max,number_attributes)
        self.points = []


    def clearPoints(self):
        self.points = []

    def getCentroid(self):
        return self.centroid

    def calculateDistance(self,point):
        return np.linalg.norm(self.centroid-point)

    def addPoint(self,point):
        self.points.append(point)

    def calculateCentroid(self):
        if (len(self.points)): self.centroid = np.average(self.points,axis=0)


    def __str__(self):
        return "Centroid: %s \n Points: \n %s" % (self.centroid, self.points)

def createClusters(k,number_attributes,min,max):
    cluster_list = []
    for i in range(k) : cluster_list.append(Cluster(number_attributes,min,max))
    return cluster_list

def kmeans(clusters, x, threshold):
    number_iterations = 0
    convergence = False
    while (not convergence):
        for cluster in clusters: cluster.clearPoints()
        for point in x:
            min = 0
            min_dist = sys.maxint
            for cluster in clusters:
                dist = cluster.calculateDistance(point)
                if (dist < min_dist):
                    min = clusters.index(cluster)
                    min_dist = dist
            clusters[min].addPoint(point)
        old_centroids = []
        for cluster in clusters:
            old_centroids.append(cluster.centroid)
            cluster.calculateCentroid()
        for i in range(len(clusters)) :
            centroid = clusters[i].getCentroid()
            if (not np.array_equal(centroid,old_centroids[i])) : break
            convergence = True
        number_iterations+=1

if __name__ == '__main__':
    # np.random.seed(1)
    clusters = createClusters(3,2,0,5)
    for i in clusters: print i
    kmeans(clusters,[[1,2],[1,3],[7,6],[15,9]],0.01)
    print "------------------------------"
    for i in clusters: print i


