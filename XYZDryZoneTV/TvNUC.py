import numpy as np

from XYZNetwork3.Utils.CONST import CONST
from XYZNetwork3.MixSERVER import MixSERVER
from XYZNetwork3.MixINVITER import MixINVITER

from XYZDryZoneTV.Utils.CODEC import CODEC, encode


class TvNUC:

    def __init__(self):
        # NETWORK
        self._network = MixSERVER(tcp_port=CODEC.TCP.TV_PORT, event_cb=self._event)
        self._inviter = MixINVITER()
        self._inviter.set_machine_sn(machine_sn=CODEC.TCP.TV_MACHINE_SN)
        self._inviter.add_network(self._network)

    def _event(self, module: str, code: str, value: tuple):
        if module == CONST.PROTOCOL.TCP and code == CONST.EVENT.CONNECTION:
            is_online, (ip, port) = value
            print(f'TCP_IS_ONLINE={ip, port, is_online}')

    # API
    def set_qr_info(self, qr_link: str):
        data = encode(head=CODEC.QR_LINK, qr_link=qr_link)
        self._network.tcp.send(data)

    def set_welcome(self):
        data = encode(head=CODEC.WELCOME)
        self._network.tcp.send(data)

    def set_car_in(self, car_plate: str):
        data = encode(head=CODEC.CAR_IN, car_plate=car_plate)
        self._network.tcp.send(data)

    def set_car_plate(self, car_plate: str):
        data = encode(head=CODEC.CAR_PLATE, car_plate=car_plate)
        self._network.tcp.send(data)

    def set_car_frame(self, frame: np.array):
        data = encode(head=CODEC.FRAME, frame=frame)
        self._network.tcp.send(data)

    def set_pay_succeed(self, succeed: bool, car_plate: str):
        data = encode(head=CODEC.PAY_SUCCEED, succeed=succeed, car_plate=car_plate)
        self._network.tcp.send(data)
