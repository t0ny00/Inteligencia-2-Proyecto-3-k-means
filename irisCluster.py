import numpy as np
from cluster import Cluster,kmeans,compress,createClusters
import os.path
import matplotlib.pyplot as plt

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
    k = 5
    number_attributes = 4
    data = np.loadtxt("iris-clean.txt", delimiter=",")
    x, junk = splitData(data, 100, 1)
    ready = False
    while(not ready):
        ready = True
        clusters = createClusters(k, number_attributes, 0, 8)
        kmeans(clusters, x, 0.001,8)
        for elem in clusters:
            if elem.emptyIndex():
                ready = False

    
    print("Number of clusters " + str(len(clusters)))
    for j in range(2):
        for i in range(len(clusters)):
            print("Cluster "+str(i+1))
            print(clusters[i])
            centroid = clusters[i].getCentroid()
            indexes = clusters[i].getPointsIndex()
            plt.plot([centroid[0+j*2]],[centroid[1+j*2]],colors[i]+'X')
            for elem in indexes:
                marker = ''
                if elem < 50:
                    marker = '*'
                elif elem >= 50 and elem < 100:
                    marker = 'D'
                elif elem >= 100:
                    marker = '^'
                act = data[elem]
                plt.plot([act[0+j*2]],[act[1+j*2]],colors[i]+marker)
        plt.savefig(os.path.splitext(os.path.basename("k" + str(k) + "-" + str(j+1)))[0] + '.png')
    #plt.show()