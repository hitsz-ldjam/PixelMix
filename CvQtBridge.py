import numpy as np
from PySide2.QtGui import QImage


# This class can only handle RGB32 QImages and relevant matrices
class CvQtBridge:
    @staticmethod
    def sharedMatToCvMat(src: np.ndarray):
        return np.delete(src, 3, 2).copy()

    @staticmethod
    def qImageToSharedMat(image: QImage) -> np.ndarray:
        return np.ndarray(shape=(image.height(), image.width(), image.depth() // 8),
                          dtype=np.uint8,
                          buffer=image.bits())

    @staticmethod
    def cvMatToQImage(mat: np.ndarray) -> QImage:
        mat32 = mat.astype(np.uint32)
        # assuming sys.byteorder == "little"
        data = (255 << 24 | mat32[:, :, 2] << 16 | mat32[:, :, 1] << 8 | mat32[:, :, 0]).flatten()
        image = QImage(data, mat.shape[1], mat.shape[0], QImage.Format_RGB32)
        return image.copy()
