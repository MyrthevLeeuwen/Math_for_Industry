import numpy as np

points_per_frame = 3

num_of_frames = 5


testinput = np.random.random((num_of_frames, points_per_frame, 2))

print(testinput)

# implement cost function MCF

# implement maximization of cost function w.r.t. drift

# implement algoritmm

    # initialize

    # loop:
    # for each new layer maximize the cost function w.r.t. the collection of layers
    # add the current layer to all previous layers with drift correction

    # output the total stack
