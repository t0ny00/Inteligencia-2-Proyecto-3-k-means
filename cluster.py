import numpy as np
import sys


class Cluster:


    def __init__(self,number_attributes,min,max):
        self.centroid = np.random.uniform(min,max,number_attributes) # Value of the centroid
        self.points = [] # List of elements associated to the centroid
        self.point_index = [] # List of index of each point in their original vector

    # Empties the contents of points and point_index
    def clearPoints(self):
        self.points = []
        self.point_index = []

    # Check if the poit_index is empty
    def emptyIndex(self):
        return self.point_index == []

    def getPointsIndex(self):
        return self.point_index

    def getCentroid(self):
        return self.centroid

    # Calculate the euclidean distance between a point and the centroid
    def calculateDistance(self,point):
        return np.linalg.norm(self.centroid-point)

    def addPoint(self,point,index):
        self.points.append(point)
        self.point_index.append(index)

    # Calculate the centroid value by averaging the value of its points
    def calculateCentroid(self):
        if (len(self.points)): self.centroid = np.average(self.points,axis=0)


    def __str__(self):
        return "Centroid: %s \n \n Index: %s" % (self.centroid,self.point_index)

# Create a list of k clusters with random values between min and max
def createClusters(k,number_attributes,min,max):
    cluster_list = []
    for i in range(k) : cluster_list.append(Cluster(number_attributes,min,max))
    return cluster_list

def kmeans(clusters, x, threshold,max_iter):

    number_iterations = 0
    convergence = False

    while (not convergence and number_iterations < max_iter):
        # For each iteration start with zero points associated with the centroid
        for cluster in clusters: cluster.clearPoints()

        # For each point in x, check which centroid is the closest
        for point_index in range(len(x)):
            index_of_cluster = 0
            min_dist = sys.maxint
            point = x[point_index]
            for cluster in clusters:
                dist = cluster.calculateDistance(point)
                if (dist < min_dist):
                    index_of_cluster = clusters.index(cluster)
                    min_dist = dist
            clusters[index_of_cluster].addPoint(point,point_index)
        old_centroids = []

        # Store old centroid values and calculate the new ones
        for cluster in clusters:
            old_centroids.append(cluster.centroid)
            cluster.calculateCentroid()

        # If the distance between the old centroid and the new one is less than the threshold, assume convergence
        for i in range(len(clusters)) :
            cluster = clusters[i]
            if (cluster.calculateDistance(old_centroids[i]) > threshold) : break
            convergence = True

        number_iterations+=1
        print "Number of iterations: " + str(number_iterations)

# Change the value of each point for that of the centroid
# Method used in activity 3
def compress(clusters,x):
    for cluster in clusters:
        for i in range(len(cluster.points)):
            x[cluster.point_index[i]] = cluster.centroid





