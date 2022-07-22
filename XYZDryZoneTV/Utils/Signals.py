import numpy as np

from XYZUtil4.customclass.Signal import Signal
from XYZUtil4.tools.for_class import singleton


@singleton
class Signals:
    frame = Signal(np.array)  # frame
    shop_info = Signal(str)  # shop_info
    sale_info = Signal(str)  # sale_info
    user_info = Signal(str)  # user_info
    pay_succeed = Signal(bool)  # is_succeed
