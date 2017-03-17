import numpy as np
from collections import OrderedDict
from cluster import Cluster,kmeans,compress,createClusters
import os.path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import copy
import sys

colors = ['b','g','r','c','m']
file = open("iris-clean.txt",'r')



def splitData(data,percentage,output_num):
    cut_index = int(round((percentage/float(100))*data.shape[0]))
    data_range = int(round(cut_index/float(output_num)))
    tmp = data.shape[0]/output_num
    data_train,data_test = [],[]
    for i in range(output_num):
        tmp2 = data[i*(tmp):data_range+i*tmp]
        for j in tmp2:
            data_train.append((j.tolist()))
        tmp3 = data[data_range+i*tmp:(i+1)*tmp]
        for j in tmp3: data_test.append((j.tolist()))
    data_train = np.resize(data_train,(len(data_train),len(data_train[0])))
    data_test = np.resize(data_test,(len(data_test),len(data_train[0])))
    return data_train,data_test

if __name__ == '__main__':

    if len(sys.argv) != 4 :
        print "Usage: irisCluster.py <numero_de_clusters> <threshold> <num_iteraciones>"
        exit(1)

    k = int(sys.argv[1])
    threshold = float(sys.argv[2])
    max_iter = int(sys.argv[3])
    data = np.loadtxt("iris-clean.txt", delimiter=",")

    number_attributes = 4
    x, junk = splitData(data, 100, 1)

    ready = False
    # Repeat k means algorithm until each cluster has at least one point associated to it
    while(not ready):
        print "Starting k-means"
        ready = True
        clusters = createClusters(k, number_attributes, 0, 8)
        kmeans(clusters, x, threshold,max_iter)
        for elem in clusters:
            if elem.emptyIndex():
                ready = False
                print "Non Optimal Result \n"


    nclusters = len(clusters)

    # Print Plots
    print("\n Number of clusters " + str(nclusters))
    for j in range(2):
        patches = []
        names   = []
        legend_labeler = [True,True,True,True]
        plt.title("Cluster distribution for Iris with " + str(k) + " clusters part " + str(j+1))
        if j == 0:
            plt.xlabel('Sepal Length')
            plt.ylabel('Sepal Width')
        else:
            plt.xlabel('Petal Length')
            plt.ylabel('Petal Width')
        for i in range(nclusters):
            patches.append(mpatches.Patch(color=colors[i]))
            names.append('Cluster '+str(i+1))
        for i in range(nclusters):
            centroid = clusters[i].getCentroid()
            indexes = clusters[i].getPointsIndex()
            if legend_labeler[0]:
                centroid_object = plt.scatter(centroid[0+j*2],centroid[1+j*2],c=colors[i],marker='x')
                co_copy = copy.copy(centroid_object)
                co_copy.set_facecolor('k')
                patches.append(co_copy)
                names.append('Centroid')
                legend_labeler[0] = False
            else:
                plt.plot([centroid[0+j*2]],[centroid[1+j*2]],colors[i]+'x')
            for elem in indexes:
                marker = ''
                index_label = ''
                act = data[elem]
                if elem < 50:
                    marker = '*'
                    index_label = "iris setosa"
                    if legend_labeler[1]:
                        obj = plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                        obj_copy = copy.copy(obj)
                        obj_copy.set_facecolor('k')
                        patches.append(obj_copy)
                        names.append(index_label)
                        legend_labeler[1] = False
                    else:
                        plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                elif elem >= 50 and elem < 100:
                    marker = 'D'
                    index_label = "iris versicolor"
                    if legend_labeler[2]:
                        obj = plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                        obj_copy = copy.copy(obj)
                        obj_copy.set_facecolor('k')
                        patches.append(obj_copy)
                        names.append(index_label)
                        legend_labeler[2] = False
                    else:
                        plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                elif elem >= 100:
                    marker = '^'
                    index_label = "iris virginica"
                    if legend_labeler[3]:
                        obj = plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                        obj_copy = copy.copy(obj)
                        obj_copy.set_facecolor('k')
                        patches.append(obj_copy)
                        names.append(index_label)
                        legend_labeler[3] = False
                    else:
                        plt.scatter(act[0+j*2],act[1+j*2],c=colors[i],marker=marker)
                
                
                
        handles,labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(patches,names,loc="lower right",scatterpoints=1, fontsize=6)
        plt.savefig(os.path.splitext(os.path.basename("k" + str(k) + "-" + str(j+1)))[0] + '.png')
        plt.show()
        plt.clf()
