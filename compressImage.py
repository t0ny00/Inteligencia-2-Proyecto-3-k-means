import sys
from scipy import misc
import Image
from cluster import Cluster,kmeans,compress,createClusters

if __name__ == '__main__':

    k = 128
    number_attributes = 3
    threshold = 0.1
    max_iter = 5
    file_name = 'flor.png'

    # Load image
    image = misc.imread(file_name)

    # Transform pixel matrix into a one dimensional vector
    x = image.reshape((image.shape[0] * image.shape[1], 3))

    clusters = createClusters(k, number_attributes, 0, 255)
    kmeans(clusters, x, threshold,max_iter)

    # Change each pixel color by that of its centroid
    compress(clusters, x)

    # Restore pixel matrix
    x = x.reshape(image.shape)

    im = Image.fromarray(x)
    out_file = file_name[:-4]
    out_file += "_" + str(k) + ".png"
    im.show()
    im.save(out_file)