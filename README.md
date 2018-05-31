# MDS
Computing Distance Matrix based on Point Vectors (or coordinate matrix) and its reverse: Computing Point Vectors based on Distance Matrix

There are 2 functions:
1) computes the distance matrix D given vector of points V. (this is the easy part)
2) given distance matrix D, derives the relative points from the centroid (the reverse)

Note: (my observation only)
* DM = getDM(V)
* V' = getXY(DM)

Here, V and V' may not have the same points. V is V' when V is centered as the centroid, and probably rotated. in other words, V' = HV where H is a transform matrix (similarity, i.e, by location and rotation only)


Sources:
1) Teknomo's Multi Dimensional Scaling, Pdf file
2) https://en.wikipedia.org/wiki/Multidimensional_scaling

