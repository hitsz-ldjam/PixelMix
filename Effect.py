import cv2
import numpy as np


def brightness_contrast(mat: np.ndarray, brightness, contrast, dst: np.ndarray = None):
        # print(hex(id(mat)))
        if dst is None:
            dst = mat
        cv2.addWeighted(mat, contrast, mat, 0, brightness, dst)
        mat[:, :, 3] = 255
