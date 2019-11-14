import sys

from PySide2.QtCore import QUrl, QStringListModel
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

import KillTheOld as KTO

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    model = QStringListModel()

    isoList = KTO.checkDirs()

    model.setStringList(isoList)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("myModel", model)
    engine.load(QUrl.fromLocalFile('view.qml'))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())