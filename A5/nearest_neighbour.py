import numpy as np
import matplotlib.pyplot as plt

"""
Given a dataset of points which are collected into groups in 2D space. 
Implement the two functions nearest_neighbour and classify_point which determine, for a given point,
its nearest neigbour (i.e. point) and the group of this neighbour respectively. 
See the .png-file for a visual representation, note that the image
indicates a nearest neighbour for each group. 

NB: You are not allowed to import any additional libraries. 
"""

def distance(pointA, pointB):
    """
    This calculates the Euclidean distance between two points: https://en.wikipedia.org/wiki/Euclidean_distance
    This is a suggested, but optional, helper-function you can choose to implement (or not). 
 
    :param pointA: The first coordinate
    :type pointA: list[float] or np.ndarray[(2,), float]
    :param pointB: The second coordinate
    :type pointB: list[float] or np.ndarray[(2,), float]
    :return: The distance between the two points
    :rtype: float
    """
    return np.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2) 

def nearest_neighbour(data, point):
    """
    This function returns an element in "data" which is the closest element to the variable "point". 

    :param data: All the points (neighbours) that need to be compared to "point".
    :type data: np.ndarray[(n, 2), float]
    :param point: The point of which you want to find the closest neighbour.
    :type point: list[float] or np.ndarray[(2,), float]
    :return: The nearest neighbour and the distance to that neighbour.
    :rtype: tuple[np.ndarray[(2,), float], float]
    """
    min_distance = distance(data[0], point)
    nearest = data[0]
    for p in data[1:]:
        new_distance = distance(p, point)
        if new_distance < min_distance:
            min_distance = new_distance
            nearest = p
    
    return nearest, min_distance

def classify_point(data, point):
    """
    This function finds the nearest group based on the nearest neighbour of each group.
    Groups are indexed from 0. 
    
    HINT: Use `nearest_neighbour` in this function. 

    :param data: A list of groups, where each group consists of all the points (neighbours) that need to be compared to "point".
    :type data: list[np.ndarray[(Any, 2), float]]
    :param point: The point of which you want to find the closest group.
    :type point: list[float] or np.ndarray[(2,), float]
    :return: The nearest group (index) and the nearest neighbour.
    :rtype: tuple[int, np.ndarray[(Any, 2), float]]
    """
    k = 0
    nearest, min_distance = nearest_neighbour(data[0], point)
    for i in range(1, len(data)):
        new_nearest, new_distance = nearest_neighbour(data[i], point)
        
        if new_distance < min_distance:
            nearest = new_nearest
            min_distance = new_distance
            k = i  

    return k, nearest

# The following code generates a visualization of the problem. 
# To produce the image you must "Hand-in" the assignment, or run it in your local environment. 
if __name__ == "__main__":
    RNG = np.random.default_rng()

    plt.matplotlib.rcParams['figure.figsize'] = [5, 4]  # This controls the size of the plot
    centers = [(3, 8), (5, 3), (8, 6)]  # this controls the center of each group
    n_points = 20  # Number of points of each group
    new_point = (5, 5)  # Coordinate of the new point

    # It is not necessary to change the code below, except for educational purposes
    data = []
    for i, (x, y) in enumerate(centers):
        data.append(np.array(list(zip(RNG.normal(x, 1, n_points), RNG.normal(y, 1, n_points)))))
        plt.plot(data[-1][:,0], data[-1][:,1], 'o', label=f"group {i+1}")

    plt.plot(*nearest_neighbour(data[0], new_point)[0], 'k.', label="nearest point")
    plt.plot(*nearest_neighbour(data[1], new_point)[0], 'k.')
    plt.plot(*nearest_neighbour(data[2], new_point)[0], 'k.')

    nearest_group, nearest_point = classify_point(data, new_point)
    print(f"The nearest neighbour of point {new_point} is {tuple(nearest_point)} which belongs to group {nearest_group}.")

    plt.plot(*new_point, 'x', color='k')
    plt.legend()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.savefig("nearest_neighbour_plot.png")