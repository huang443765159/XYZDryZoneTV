import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Gui.Gui import Gui
from Gui.UI.UI import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._gui = Gui(ui=self._ui)
        QApplication.setStyle('Fusion')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
