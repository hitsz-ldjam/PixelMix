import cv2
import numpy as np


def brightness_contrast(src: np.ndarray, brightness, contrast, dst: np.ndarray = None):
        # print(hex(id(src)))
        if dst is None:
            dst = src
        cv2.addWeighted(src, contrast, src, 0, brightness, dst)
        src[:, :, 3] = 255
