import requests

from XYZNetwork3.Utils.CONST import CONST
from XYZNetwork3.MixCLIENT import MixCLIENT

from XYZDryZoneTV.Utils.Signals import Signals
from XYZDryZoneTV.Utils.CODEC import CODEC, encode, decode

"""
要显示4部分东西
卖点 + 营销
二维码
用户信息 + 洗车店使用情况
是车辆的照片
"""


class TV:

    def __init__(self):
        # SIGNAL
        self.sign = Signals()
        # NETWORK
        self._network = MixCLIENT(tcp_port=CODEC.TCP.TV_PORT, event_cb=self._event, recv_cb=self._recv)
        self._network.set_machine_sn(machine_sn=CODEC.TCP.TV_MACHINE_SN)
        self._qr_is_show = False

    def _event(self, module: str, code: str, value: tuple):
        if module == CONST.PROTOCOL.TCP and code == CONST.EVENT.CONNECTION:
            is_online, (ip, port) = value
            print(f'TCP_ONLINE={ip, port, is_online}')

    def _recv(self, data: bytes, ip: str, pkt_id: int):
        head, rx_msg = decode(data=data)
        if head == CODEC.FRAME:  # 电视机上显示是车的画面, 并显示二维码
            self._qr_is_show = True
            self.sign.frame.emit(rx_msg['frame'])
        elif head == CODEC.SALE_INFO:
            self.sign.sale_info.emit(rx_msg['sale_info'])
        elif head == CODEC.QR_LINK:
            result = requests.get(rx_msg['qr_link'])
            with open('./_IMAGES/qr.png', 'wb') as f:
                f.write(result.content)
        elif head == CODEC.SHOP_INFO:
            self.sign.shop_info.emit(rx_msg['shop_info'])
        elif head == CODEC.USER_INFO:
            self.sign.user_info.emit(rx_msg['user_info'])
        elif head == CODEC.PAY_SUCCEED:  # 用户支付成功，关闭二维码
            self.sign.pay_succeed.emit(rx_msg['succeed'])
            self._qr_is_show = False

    def get_show_qr(self) -> bool:
        return self._qr_is_show
