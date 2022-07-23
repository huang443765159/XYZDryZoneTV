import numpy as np

from XYZUtil4.customclass.Signal import Signal
from XYZUtil4.tools.for_class import singleton


@singleton
class Signals:
    frame = Signal(np.array)  # frame
    car_in = Signal(str)  # car_plate
    welcome = Signal(bool)  # True
    car_plate = Signal(str)  # car_plate
    pay_succeed = Signal(bool, str)  # is_succeed, car_plate: str
