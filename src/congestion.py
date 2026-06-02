import numpy as np

def compute_congestion(image, vehicles, grid_size=(2,2)):
    h, w = image.shape[:2]
    gh, gw = grid_size

    frame_h, frame_w = h//gh, w//gw
    congestion = np.zeros((gh, gw))

    for (cx, cy, area) in vehicles:
        gx = cx // frame_w
        gy = cy // frame_h

        if gx < gw and gy < gh:
            congestion[gy][gx] += area

    return congestion