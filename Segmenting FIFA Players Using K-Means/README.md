## Table of content
* [Overview](Overview)
* [Dataset](Dataset)
* [Methodology](Methodology)
* [Feature Selection and Data Preparation](Feature Selection and Data Preparation)
* [Dropping Null Values](Dropping Null Values)
* [Data Scaling](Data Scaling)
* [Determining the Optimal Number of Clusters](Determining the Optimal Number of Clusters)
* [Clustering with K-Means](Clustering with K-Means)
* [Visualization](Visualization)
* [Results](Results)
* [Conclusion](Conclusion)

# Overview
This project performs clustering analysis on FIFA player data using the k-means algorithm. The aim is to segment players into distinct groups based on their performance and market value attributes

# Dataset 
The dataset used for this analysis is in csv file 'players_22.csv', which contains attributes of FIFA players.

# Methodology
### ***Data Loading and Exploration***
The dataset was loaded using pandas library, and an initial inspection was performed to review the available columns and examine the first few rows. This step helped in understanding the structure of the data.

### ***Feature Selection and Data Preparation***

Relevant features for clustering were identified: overall rating, potential, wage in euros, and age. These features were selected for their significance in evaluating player performance and market value. A new DataFrame was created containing only these selected features.

### ***Dropping Null Values*** 

Rows with missing values in any of these features were removed to ensure the integrity of the data used for clustering.

### ***Data Scaling***

To ensure that each feature contributed equally to the clustering process, the data was scaled. This step was crucial for normalizing the values of the features and avoiding bias towards features with larger ranges.

### ***Determining the Optimal Number of Clusters***

The Within-Cluster Sum of Squares (WCSS) method was employed to determine the optimal number of clusters. By calculating WCSS for different numbers of clusters and plotting the results, the 'elbow' method helped identify the most suitable number of clusters.

### ***Clustering with K-Means***

K-means clustering was applied to segment the players into clusters based on the chosen number of clusters. This algorithm partitions the data into distinct groups by minimizing the variance within each cluster.

### ***Visualization***

Principal Component Analysis (PCA) was used to reduce the dimensionality of the data to two components for visualization. This allowed for a clear and interpretable graphical representation of the clusters, highlighting the distribution of players across different clusters.

### ***Results***
The scatter plot shows the results of k-means clustering on a dataset with the features 'potential,' 'age,' 'income,' and 'overall.' The clusters are represented by three different colors: red, yellow, and green. Here is an interpretation of the clusters:

**Red Cluster**
Potential and Overall: Likely represents players with relatively lower potential and overall ratings.
Age: These players might be younger and early in their careers, reflecting their lower overall ratings and potential.
Income: Lower income might correlate with lower potential and overall ratings.

**Yellow Cluster:**
Potential and Overall: Represents players with moderate potential and overall ratings.
Age: These players could be in the mid-range of their career, not too young or too old.
Income: Income for this group might be moderate, aligning with their potential and overall ratings.

**Green Cluster:**
Potential and Overall: Indicates players with higher potential and overall ratings.
Age: Likely older or more experienced players who have reached higher overall ratings and potential.
Income: Higher income can be expected, correlating with their higher potential and overall ratings.

# Conclusion
The analysis effectively segmented FIFA players into meaningful clusters, revealing distinct player profiles based on performance metrics and market value. This segmentation can provide valuable insights for team management, scouting, and further data-driven decision-making.


