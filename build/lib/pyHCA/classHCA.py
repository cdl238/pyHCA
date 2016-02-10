#!/usr/bin/env python
""" The classHCA is an ensemble of class to describe hydrophobic clusters and
domain created through hydrophobic clusters.
"""

__author__ = "Tristan Bitard-Feildel"
__licence__= "MIT"
__version__ = 0.1
__email__ = "t.bitard.feildel [you know what] uni-muenster.de"
__institute__ = "Institute for Evolution and Biodiversity, Muenster Germany"
        
class HydroCluster(object):
    """ the class definning the amas of hydrophobic clusters
    """
    #__slots__  = ["__start", "__stop", "__hydro_cluster"]
    def __init__(self, start, stop, hydro_cluster):
        self.__start = start
        self.__stop = stop
        self.__hydro_cluster = hydro_cluster[:]

    @property
    def start(self):
        return self.__start
    
    @property
    def stop(self):
        return self.__stop
    
    @property
    def hydro_cluster(self):
        return self.__hydro_cluster
    
    def __str__(self):
        """ write position, indexes are inclusive and start from 1
        """
        return "cluster\t{}\t{}\t{}".format(self.__start+1, self.__stop, 
                                                           self.__hydro_cluster)
    def add_offset(self, offset):
        """ add an offset to the hydrophobic clusters
        """
        self.__start += offset
        self.__stop += offset
        
    def get(self, method):
        if method == "all":
            return self.__start, self.__stop, self.__hydro_cluster
        elif hasattr(self, method):
            return getattr(self, method)
        else:
            raise ValueError("Unknown argument for function "
                             "HydroCluster.get({}".format(method))

class DomHCA(object):
    """ the class definning the domain delineated by the HCA segmentation
    """
    __slots__ = ["__start", "__stop", "__clusters"]
    def __init__(self, start, stop): #, list_of_hcclusters):
        self.__start = start
        self.__stop = stop
        #self.__clusters = list_of_hcclusters[:]
    @property
    def start(self):
        return self.__start
    
    @property
    def stop(self):
        return self.__stop
    
    #@property
    #def clusters(self):
        #return self.__clusters

    def add_offset(self, offset):
        """ add an offset to start and stop and all hydrophobic clusters inside
        the domain
        """
        self.__start += offset
        self.__stop += offset
        #for hclust in self.__clusters:
            #hclust.add_offset(offset)

    #def __iter__(self):
        #return iter(self.__clusters)
            
    def __str__(self):
        domain = "domain\t{}\t{}".format(self.__start+1, self.__stop)
        #clusters = "\n".join(domain+"\t"+str(clust) for clust in self.__clusters)
        #if clusters:
            #return clusters
        return domain


