import sys
from scipy import misc
import Image
from cluster import Cluster,kmeans,compress,createClusters

if __name__ == '__main__':

    k = 8
    number_attributes = 3
    file_name = 'flor.png'
    image = misc.imread(file_name)
    x = image.reshape((image.shape[0] * image.shape[1], 3))
    clusters = createClusters(k, number_attributes, 0, 255)
    kmeans(clusters, x, 0.001,8)
    compress(clusters, x)
    x = x.reshape(image.shape)
    im = Image.fromarray(x)
    out_file = file_name[:-4]
    out_file += "_" + str(k) + ".png"
    im.show()
    im.save(out_file)