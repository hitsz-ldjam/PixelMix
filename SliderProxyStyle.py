from typing import Any

from PySide2.QtCore import *
from PySide2.QtWidgets import *


# todo need clean up
class SliderProxyStyle(QProxyStyle):
    def styleHint(self,
                  hint: Any,
                  option: QStyleOption = ...,
                  widget: QWidget = ...,
                  returnData: QStyleHintReturn = ...) -> int:
        if hint == QStyle.SH_Slider_AbsoluteSetButtons:
            return Qt.LeftButton | Qt.MidButton | Qt.RightButton
        return super(SliderProxyStyle, self).styleHint(hint, option, widget, returnData)
