
# Calculating Distance Lab

### Introduction

In this lab, you will write methods to calculate the distance of various neighbors from each other.  Once again, let's assume that the $x$ coordinates represent avenues of a neighbor, the $y$ coordinates represent streets.  We will also assume that the distance between each street and the distance between each avenue is the same.

We will work up to a function called `nearest_neighbors` that given a neighbor, finds the other neighbors who are closest.

### Getting Started

Let's declare a variable `neighbors` and assign it to an array of dictionaries, each representing the location of a neighbor.


```python
neighbors = [{'name': 'Fred', 'avenue': 4, 'street': 8}, {'name': 'Suzie', 'avenue': 1, 'street': 11}, 
             {'name': 'Bob', 'avenue': 5, 'street': 8}, {'name': 'Edgar', 'avenue': 6, 'street': 13},
             {'name': 'Steven', 'avenue': 3, 'street': 6}, {'name': 'Natalie', 'avenue': 5, 'street': 4}]
```


```python
neighbors
```




    [{'avenue': 4, 'name': 'Fred', 'street': 8},
     {'avenue': 1, 'name': 'Suzie', 'street': 11},
     {'avenue': 5, 'name': 'Bob', 'street': 8},
     {'avenue': 6, 'name': 'Edgar', 'street': 13},
     {'avenue': 3, 'name': 'Steven', 'street': 6},
     {'avenue': 5, 'name': 'Natalie', 'street': 4}]




```python
fred = neighbors[0]
natalie = neighbors[5]
```

We'll also plot our neighbors, to get a sense of our data.


```python
import plotly

plotly.offline.init_notebook_mode(connected=True)
trace0 = dict(x=list(map(lambda neighbor: neighbor['avenue'],neighbors)), 
              y=list(map(lambda neighbor: neighbor['street'],neighbors)),
              text=list(map(lambda neighbor: neighbor['name'],neighbors)),
              mode='markers')
plotly.offline.iplot(dict(data=[trace0], layout={'xaxis': {'dtick': 1}, 'yaxis': {'dtick': 1}}))
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="faec61cb-e6b3-471e-91e1-536f62f6a78f" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("faec61cb-e6b3-471e-91e1-536f62f6a78f", [{"x": [4, 1, 5, 6, 3, 5], "y": [8, 11, 8, 13, 6, 4], "text": ["Fred", "Suzie", "Bob", "Edgar", "Steven", "Natalie"], "mode": "markers"}], {"xaxis": {"dtick": 1}, "yaxis": {"dtick": 1}}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


We'll start by focusing on the neigbors Fred and Natalie, and points (4, 8) and (5, 4) respectively.

### Calculating the sides of the triangle

Remember that to calculate the distance, we use the Pythagorean Theorem to calculate the two shorter sides of the right triangle, and from there can calculate the distance, that is the hypotenuse, of the triangle.  Let's start with calculating the shorter sides and then use that work to calculate the distance. 

Write a function called `street_distance` that calculates how far **in streets** two neighbors are from each other.  So for example, with Natalie at street 4, and Fred at street 8, our `street_distance` function should return the number 4.


```python
def street_distance(first_neighbor, second_neighbor):
    pass
```

Now we execute the code, and as you can see from the comment to the right, our expected returned street distance is $4$.


```python
street_distance(fred, natalie) # 4
```

Write a function called `avenue_distance` that calculates how far in avenues two neighbors are from each other.  The distance should always be positive.


```python
def avenue_distance(first_neighbor, second_neighbor):
    pass
```


```python
avenue_distance(fred, natalie) #  1
```

### Calculating the distance

Now let's begin writing functions involved with calculating that hypotenuse of our right triangle.  Using the Pythagorean Theorem, $a^2 + b^2 = c^2 $, write a function called `distance_between_neighbors_squared` that calculates $c^2$, the length of the hypotenuse squared.


```python
def distance_between_neighbors_squared(first_neighbor, second_neighbor):
    pass
```


```python
distance_between_neighbors_squared(fred, natalie) # 17
```

Now take the next step, and write a function called `distance`, that given two neigbors returns the distance between them.  


```python
import math
def distance(first_neighbor, second_neighbor):
    pass
```


```python
distance(fred, natalie) # 4.123105625617661
```

### Writing Our "Nearest Neighbors" Functions

This next section will work up to building a `nearest_neighbor` function.  This is a function that given one neigbor, will tell us which neigbors are closest.  How do we write something like this? Can we use our calculation of distance between two neighbors, to figure out the closest neighbors to an individual?

Sure, we first need to calculate the distances between one neigbor and all of the others.  Next, we sort those neighbors by their distance from the selected_neighbor.  Finally, we select a given number of the closest neighbors.  Let's work through it.   

Note that we already have a function that calculates the distance between two neighbors.  We may think we could simply use this function to loop through our neighbors, but that would just return an array of distances.  


```python
distances = []
for neighbor in neighbors:
    distance_between = distance(fred, neighbor)
    distances.append(distance_between)

distances
```




    [None, None, None, None, None, None]



The returned array from the above procedure isn't super helpful.  We need to know who each distance is associated with.  

So let's accomplish this by writing a function called `distance_with_neighbor` that works like our distance function but instead of returning an integer, returns a dictionary representing the `second_neighbor`, and also adds in the a key value pair indicating distance from the `first_neighbor`.


```python
import math
def distance_with_neighbor(first_neighbor, second_neighbor):
    pass
```


```python
distance_with_neighbor(fred, natalie)
# {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4}
```

Now write a function called `distance_all` that returns an array representing the distances between a `first_neighbor` and the rest of the neighhbors.  The array should not return the `first_neighbor` in its collection of neighbors. 


```python
def distance_all(first_neighbor, neighbors):
    pass
```


```python
distance_all(fred, neighbors)

# [{'avenue': 1, 'distance': 4.242640687119285, 'name': 'Suzie', 'street': 11},
#  {'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
#  {'avenue': 6, 'distance': 5.385164807134504, 'name': 'Edgar', 'street': 13},
#  {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6},
#  {'avenue': 5, 'distance': 4.123105625617661, 'name': 'Natalie', 'street': 4}]
```

Finally, write a function called `nearest_neighbors` given a neighbor, returns an array of neighbors, ordered from closest to furthest from the neighbor.  The function should take an optional third argument that specifies how many "nearest" neighbors are returned.


```python
def nearest_neighbors(first_neighbor, neighbors, number = None):
    pass
```


```python
nearest_neighbors(fred, neighbors, 2)
# [{'avenue': 5, 'distance': 1.0, 'name': 'Bob', 'street': 8},
#  {'avenue': 3, 'distance': 2.23606797749979, 'name': 'Steven', 'street': 6}]
```

### Summary

In this lab, you built out the nearest neighbors.  We'll review building out these functions in the next section.
