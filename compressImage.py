import sys
import os
from scipy import misc
import Image
from cluster import Cluster,kmeans,compress,createClusters

if __name__ == '__main__':

    if len(sys.argv) != 5 :
        print "Usage: compressImage.py <numero_de_clusters> <threshold> <num_iteraciones> <nombre_imagen_con_extension> "
        exit(1)

    k = int(sys.argv[1])
    threshold = float(sys.argv[2])
    max_iter = int(sys.argv[3])
    file_name = sys.argv[4]
    number_attributes = 3

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
    out_file = os.path.basename(file_name)[:-4]
    out_file += "_" + str(k) + ".png"
    im.show()
    im.save(out_file)