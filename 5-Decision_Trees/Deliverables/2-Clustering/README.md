# Clustering

## Overview

Recall that clustering is a form of *unsupervised learning* - searching for patterns and structure in data without relying on class labels.

The goal of a clustering algorithm is to divide the input data set into subgroups - the clusters - such that points within a cluster are more similar to each other than they are to points in the other cluster.

There are a wide variety of clustering algorithms that differ in how they define what a "cluster" represents and how they assign points to clusters. Some can determine the number of clusters automatically, some require choosing the number of clusters in advance as a key hyperparameter.


## K-Means

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/K-means_convergence.gif/500px-K-means_convergence.gif" width="400px"/>

*Example run of k-means clustering with three clusters, from Wikipedia*

K-means is the grandaddy of clustering algorithms, re-invented several times by researchers in different fields. It isn't "the best" clustering algorithm, but it is popular and widely used. One of my teachers said to always try k-means first, because if it doesn't work then nothing else will work either.

The method chooses *k* points, called *centroids*, at random. It then repeatedly:

- Assigns every point to its nearest centroid
- Moves each centroid to the average of its assigned points

The centroids are assumed to be centers of the *k* clusters. 
