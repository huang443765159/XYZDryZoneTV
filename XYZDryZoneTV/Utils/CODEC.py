import pickle

from XYZUtil4.tools.for_class import singleton


class _Tcp:
    TV_PORT = 10889
    TV_MACHINE_SN = 'XYZDryZoneTV'


@singleton
class _Codec:
    FRAME = b'\xe5'
    WELCOME = b'\xe6'
    CAR_IN = b'\xe7'
    QR_LINK = b'\xe8'
    CAR_PLATE = b'\xe9'
    PAY_SUCCEED = b'\xea'
    TCP = _Tcp()


def encode(head, **kwargs) -> bytes:
    return pickle.dumps((head, kwargs))


def decode(data:bytes) -> tuple:
    head, rx_msg = pickle.loads(data)
    return head, rx_msg


CODEC = _Codec()
