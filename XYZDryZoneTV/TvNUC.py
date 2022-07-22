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

    def set_sale_info(self, sale_info: str):
        data = encode(head=CODEC.SALE_INFO, sale_info=sale_info)
        self._network.tcp.send(data)

    def set_shop_info(self, shop_info: str):
        data = encode(head=CODEC.SHOP_INFO, shop_info=shop_info)
        self._network.tcp.send(data)

    def set_user_info(self, user_info: str):
        data = encode(head=CODEC.USER_INFO, user_info=user_info)
        self._network.tcp.send(data)

    def set_car_frame(self, frame: np.array):
        data = encode(head=CODEC.FRAME, frame=frame)
        self._network.tcp.send(data)

    def set_pay_succeed(self, succeed: bool):
        data = encode(head=CODEC.PAY_SUCCEED, succeed=succeed)
        self._network.tcp.send(data)
