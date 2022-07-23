import cv2
import os
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PIL import ImageFont, ImageDraw, Image

from XYZDryZoneTV.Tv import TV
from Gui.UI.UI import Ui_MainWindow


class _Const:
    SALE_INFO = 1
    SHOP_INFO = 2
    USER_INFO = 3


class Gui:

    def __init__(self, ui: Ui_MainWindow):
        self._ui = ui
        self._tv = TV()
        # DRAW
        font_path = './_FONT/1.ttf'
        self._font = ImageFont.truetype(font_path, 50)
        # SIGNAL
        self._sign = self._tv.sign
        self._sign.frame.connect(self._signal_frame)
        self._sign.car_plate.connect(self._signal_car_plate)
        self._sign.car_in.connect(self._signal_car_in)
        self._sign.welcome.connect(self._signal_welcome)
        self._sign.pay_succeed.connect(self._signal_pay_succeed)
        # BTN
        self._ui.btn_clear.clicked.connect(self._clear)
        self._ui.btn_welcome.clicked.connect(self._welcome)
        self._ui.btn_plate.clicked.connect(self._show_plate)
        self._ui.btn_car_frame.clicked.connect(self._car_frame)
        self._ui.btn_qr_info.clicked.connect(self._qr_info)
        self._ui.btn_pay_succeed.clicked.connect(self._pay_succeed)
        self._ui.btn_car_in.clicked.connect(self._car_in)
        self._signal_frame(frame=cv2.imread('_IMAGES/car.jpg'))

    # SIGNAL
    def _signal_frame(self, frame: np.array):  # 要同时显示二维码和车辆照片
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        new_frame = cv2.resize(frame, (int(640), int(480)))
        cv2.imwrite('./_IMAGES/car.jpg', new_frame)
        back_img = Image.open('./_IMAGES/ShowQr.jpg')
        car_img = Image.open('./_IMAGES/car.jpg')
        qr_img = Image.open('./_IMAGES/qr.png')
        back_img.paste(car_img, (1300, 50))
        back_img.paste(qr_img, (1400, 680))
        back_img.save('./_IMAGES/NewShowQr.jpg')
        self._signal_show_img(img_path='./_IMAGES/NewShowQr.jpg', size=(1900, 970),
                              text='前方无人洗车', draw_pos=(350, 550))

    def _signal_car_plate(self, car_plate: str):
        self._signal_show_img(img_path='./_IMAGES/ShowPlate.jpg', size=(1900, 970),
                              text=car_plate + ',欢迎使用小象洗车', draw_pos=(350, 550))

    def _signal_car_in(self, car_plate: str):
        self._signal_show_img(img_path='./_IMAGES/PlateAndIn.jpg', size=(1900, 970),
                              text=car_plate, draw_pos=(900, 700))

    def _signal_welcome(self, is_welcome: bool):
        self._welcome()

    def _signal_pay_succeed(self, is_succeed: bool, car_plate: str):
        if is_succeed:
            self._signal_show_img(img_path='./_IMAGES/PlatePaySucceed.jpg', size=(1900, 970),
                                  text=car_plate, draw_pos=(900, 700))

    # API
    def _welcome(self):
        self._show_img(img_path='./_IMAGES/Welcome.jpg', size=(1900, 970))

    def _show_plate(self):
        self._show_img(img_path='./_IMAGES/ShowPlate.jpg', size=(1900, 970))

    def _car_frame(self):
        self._show_img(img_path='./_IMAGES/car.jpg', size=(640, 480))

    def _qr_info(self):
        self._show_img(img_path='./_IMAGES/qr.png', size=(480, 480))

    def _pay_succeed(self):
        self._show_img(img_path='./_IMAGES/PlatePaySucceed.jpg', size=(1900, 970))

    def _car_in(self):
        self._show_img(img_path='./_IMAGES/PlateAndIn.jpg', size=(1900, 970))

    def _show_img(self, img_path: str, size: tuple):
        frame = cv2.imread(img_path)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        new_frame = cv2.resize(frame, size)
        image = QImage(new_frame.data, new_frame.shape[1], new_frame.shape[0], QImage.Format_RGB888)
        self._ui.img_info.setPixmap(QPixmap.fromImage(image))

    def _signal_show_img(self, img_path: str, size: tuple, text: str, draw_pos: tuple):
        img = cv2.imread(img_path)
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text(draw_pos, text, font=self._font, fill=(0, 0, 0))
        bk_img = np.array(img_pil)
        frame = cv2.cvtColor(bk_img, cv2.COLOR_BGR2RGB)
        new_frame = cv2.resize(frame, size)
        image = QImage(new_frame.data, new_frame.shape[1], new_frame.shape[0], QImage.Format_RGB888)
        self._ui.img_info.setPixmap(QPixmap.fromImage(image))

    def _clear(self):
        self._ui.img_info.clear()
