import numpy as np
from cluster import Cluster,kmeans,compress,createClusters

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
    k = 4
    number_attributes = 4
    data = np.loadtxt("iris-clean.txt", delimiter=",")
    x, junk = splitData(data, 100, 1)
    clusters = createClusters(k, number_attributes, 0, 8)
    kmeans(clusters, x, 0.001,8)