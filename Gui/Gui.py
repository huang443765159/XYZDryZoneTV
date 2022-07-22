import cv2
import numpy as np
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtGui import QImage, QPixmap

from XYZDryZoneTV.Tv import TV
from .UI.UI import Ui_MainWindow


class _Const:
    SALE_INFO = 1
    SHOP_INFO = 2
    USER_INFO = 3


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._tv = TV()
        # SIGNAL
        self._sign = self._tv.sign
        self._sign.frame.connect(self._signal_frame)
        self._sign.user_info.connect(self._signal_user_info)
        self._sign.shop_info.connect(self._signal_shop_info)
        self._sign.sale_info.connect(self._signal_sale_info)
        self._sign.pay_succeed.connect(self._signal_pay_succeed)
        # BTN
        self._ui.btn_clear.clicked.connect(self._clear)
        self._ui.btn_qr_info.clicked.connect(self._qr_info)
        self._ui.btn_sale_info.clicked.connect(self._sale_info)
        self._ui.btn_shop_info.clicked.connect(self._shop_info)
        self._ui.btn_user_info.clicked.connect(self._user_info)
        self._ui.btn_car_frame.clicked.connect(self._car_frame)
        # ITEMS
        self._items = {_Const.SHOP_INFO: self._ui.shop_info,
                       _Const.SALE_INFO: self._ui.sale_info,
                       _Const.USER_INFO: self._ui.user_info}

    # SIGNAL
    def _signal_frame(self, frame: np.array):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        new_frame = cv2.resize(frame, (640, 480))
        image = QImage(new_frame.data, new_frame.shape[1], new_frame.shape[0], QImage.Format_RGB888)
        self._ui.car_frame.setPixmap(QPixmap.fromImage(image))
        # 显示QR
        self._qr_info()

    def _signal_user_info(self, user_info: str):
        self._set_text(text_id=_Const.USER_INFO, text=user_info, color=[0, 0, 0])

    def _signal_shop_info(self, shop_info: str):
        self._set_text(text_id=_Const.SHOP_INFO, text=shop_info, color=[0, 0, 0])

    def _signal_sale_info(self, sale_info: str):
        self._set_text(text_id=_Const.SALE_INFO, text=sale_info, color=[255, 0, 0])

    def _signal_pay_succeed(self, is_succeed: bool):
        if is_succeed:
            self._ui.qr_info.clear()

    def _set_text(self, text_id: int, text: str, color: list):
        self._items.get(text_id).setText(text)
        self._items.get(text_id).setStyleSheet(f'color: rgb({color[0]:d}, {color[1]:d}, {color[2]:d});')
        self._refresh_font_size(text_id=text_id)

    def _refresh_font_size(self, text_id: int):
        lb = self._items.get(text_id)
        if not lb.text():
            return
        l_width = lb.width()
        l_height = lb.height()
        font = lb.font()
        size_min = 1
        size_max = int(max(l_width, l_height))
        while size_min < size_max:
            size = int((size_min + size_max) / 2)
            font.setPixelSize(size)
            rect = QFontMetrics(font).boundingRect(lb.text())
            c_width = rect.width()
            c_height = rect.height()
            if c_width <= l_width and c_height <= l_height:
                size_min = size + 1
            else:
                size_max = size - 1
        font.setPixelSize(size_max - 10)
        lb.setFont(font)

    # API
    def _qr_info(self):
        frame = cv2.imread('./_IMAGES/qr.png')
        new_frame = cv2.resize(frame, (480, 480))
        image = QImage(new_frame.data, new_frame.shape[1], new_frame.shape[0], QImage.Format_RGB888)
        self._ui.qr_info.setPixmap(QPixmap.fromImage(image))

    def _sale_info(self):
        self._set_text(text_id=_Const.SALE_INFO, text='999元/年\n\n399元/年', color=[255, 0, 0])

    def _shop_info(self):
        self._set_text(text_id=_Const.SHOP_INFO, text='您前方还有1位\n 大约等待10分钟', color=[0, 0, 0])

    def _user_info(self):
        self._set_text(text_id=_Const.USER_INFO, text='京A12345\n 欢迎使用小象洗车', color=[0, 0, 0])

    def _car_frame(self):
        frame = cv2.imread('./_IMAGES/car.jpg')
        self._signal_frame(frame=frame)

    def _clear(self):
        for one_lb in self._items.values():
            one_lb.clear()
        self._ui.qr_info.clear()
        self._ui.car_frame.clear()
