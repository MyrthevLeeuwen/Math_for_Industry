import numpy as np

points_per_frame = 1

num_of_frames = 2


testinput = np.random.random((num_of_frames, points_per_frame, 2))

# implement cost function MCF

# implement maximization of cost function w.r.t. drift


# function takes an array of frames each containing an array coordinates
# there may be drift between the different frames
# returns a single frame which is the union of the original frames, corrected for drift.
def gold_standard(input):
    # initialize
    ref = input[0].tolist() #convert to list because we are going to do a lot of concatenation

    # loop:
    # for each new layer maximize the cost function w.r.t. the collection of layers
    # add the current layer to all previous layers with drift correction

    for i in range(1, len(input)):
        frame = input[i]
        drift = estimate_drift(frame, ref)
        # correct the frame by subtracting the drift from all points
        corrected_frame = frame - np.full(frame.shape, drift)
        # merge the frames
        ref += corrected_frame.tolist()

    #output the total stack
    return np.array(ref)
