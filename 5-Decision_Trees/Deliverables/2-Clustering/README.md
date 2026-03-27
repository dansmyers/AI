# Clustering

<img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg" width="300px" />

*Iris versicolor* (via Wikipedia)

## Overview

Recall that clustering is a form of *unsupervised learning* - searching for patterns and structure in data without relying on class labels.

The goal of a clustering algorithm is to divide the input data set into subgroups - the clusters - such that points within a cluster are more similar to each other than they are to points in the other cluster.

There are a wide variety of clustering algorithms that differ in how they define what a "cluster" represents and how they assign points to clusters. Some can determine the number of clusters automatically, some require choosing the number of clusters in advance as a key hyperparameter.


## K-Means

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/K-means_convergence.gif/500px-K-means_convergence.gif" width="300px"/>

*Example run of k-means clustering with three clusters, from Wikipedia*

K-means is the grandaddy of clustering algorithms, re-invented several times by researchers in different fields. It isn't "the best" clustering algorithm, but it is popular and widely used. One of my teachers said to always try k-means first, because if it doesn't work then nothing else will work either.

The method chooses *k* points, called *centroids*, at random. It then repeatedly:

- Assigns every point to its nearest centroid
- Moves each centroid to the average of its assigned points

The centroids are assumed to be centers of the *k* clusters. As the image above shows, the assignment and averaging process tends to move centers towards distinct blobs of points.

K-means works well when the centers are *globular* (that is, ball-shaped within their dimensional space) and well-separated. The two basic problems with k-means are:

- It isn't guaranteed to converge to the actual best cluster groupings. K-means is sensitive to its initialization conditions; small changes in initialization may yield substantial differences in the final clustering. There are more sophisticated initialization methods that often outperform random choice.
 
- The user has to choose a good value for *k*.

### Fisher's Irises

R.A. Fisher was a British statistician of the early 20th Century who made a huge number of contributions to the practice of statistics, including formulating the concept of statistical significance and establishing the *p* < .05 guideline for hypothesis testing. In 1936, Fisher published a paper on a technique called linear disciminant analysis that used a set of measurements from iris flowers as its example. The iris data set has gone on to become probably the most famous example data set in machine learning.

The data set contains 150 examples divided equally between three species of iris flowers: *iris setosa*, *iris virginica*, and *iris versicolor*. The data record four measurements for each flower: petal length, petal width, sepal length, and sepal width. The sepals are the outer part of the flower that protect and support it while it's developing.

Create a program that

- Loads the iris data set (it's built in to scikit-learn)

- Creates a scatter plot of the data set by projecting into the two most important dimensions. This should show that one class is clearly separated from the other two, but the remaining two classes overlap somewhat in feature space.

- Performs a k-means clustering using three clusters, then visualizes the results on your scatter plot.

- Create one more scatter plot using only petal width and petal length as the variables. Is it possible to separate one class from the other two using only petal measurements?

### Silhouette plot

One method of choosing the value of *k* is to create a **silhouette plot**. Intuitively, if a clustering is good, then points within a given cluster should be simliar to each other, but *dissimilar* from points in other cluster. The silhouette score quantifies this idea.

Do some research on the silhouette plot. How is the score calculated and how is the plot structured? Then create a silhouette plot showing scores for values of *k* from 2 to 10 for the iris data.

What is the best number of clusters for the iris data set according to the silhouette plot? What does that suggest to you about the challenges of performing cluster analysis?


## Hierarchical clustering

<img src="https://upload.wikimedia.org/wikipedia/commons/1/12/Iris_dendrogram.png" width="300px" />

*Hierarchical clustering dendrogram for the iris dataset using R* (via Wikipedia)

Hierarchical clustering, also called *agglomerative clustering*, avoids the issue of picking cluster centers by building clusters from the bottom-up. The basic algorithm is simple:

- Start with each point as its own cluster
- Repeatedly identify the two nearest clusters and merge them to create a new, larger cluster.
- Continue until all points have been merged into one top-level cluster

It's typical to visualize the results of the clustering process by creating a **dendrogram** like the one above. It shows the sequence of cluster mergings from individual points up to the top-level supercluster. You can choose a desired number of final clusters by cutting the dendrogram to select the last *k* groups that were merged.

Hierarchical clustering does require choosing a rule for calculating the similarity of clusters to control the merging process. Distances between cluster centers are one choice. Another option is *Ward's linkage*, which merges the pair of clusters that yield a new cluster with minimal within-cluster variance; that is, it tries to merge clusters that result in similar items being grouped together. 

Use scikit-learn to construct a dendrogram like the one above with Ward's linkage as the merging criterion.


## Mixture models

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/MultivariateNormal.png/500px-MultivariateNormal.png" width="300px" />

*Example two-dimensional normal distribution* (via Wikipedia, again)

Did either clustering algorithm work well on the iris data set? What is it about the structure of the data that makes cleanly separating *iris versicolor* and *iris virginica* difficult?

Here's an idea: maybe a *probabilistic* approach could perform better? Instead of drawing hard boundaries, we could think of the data points as samples drawn from statistical distributions, which might be overlapping. A point could then have a *probability* of being assigned to each cluster. This would allow us to assign each point to its most likely cluster, but also capture the idea of uncertainty for points that are genuinely between clusters and hard to place.

The **Gaussian mixture model** method uses this approach. It assumes that the data are drawn from multivariate normal (Gaussian) distributions and finds the means and covariances of those distributions that best fit the observations.

Intuitively, you can think of a multivariate normal distribution as having each of its features drawn from a one-dimensional normal distribution. A sample from such a distribution looks like a "blob" in space, where the means of the distributions determine the center of the blob and the covariances determine the shape and orientation.

Try performing one more clustering using the GMM approach. How do its cluster assignments compare to the real data?

If you want to do more research, you can read about the expectation-maximization (EM) algorithm that's used to solve the distribution-fitting problem.

## Submission

Submit your plots (as .png images) and code.

