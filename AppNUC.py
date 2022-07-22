import sys
from PyQt5.QtCore import QObject, QCoreApplication

from XYZDryZoneTV.TvNUC import TvNUC


class AppNUC(QObject):

    def __init__(self):
        super(AppNUC, self).__init__()
        self._tv = TvNUC()


if __name__ == '__main__':
    app = QCoreApplication(sys.argv)
    nuc = AppNUC()
    sys.exit(app.exec_())
