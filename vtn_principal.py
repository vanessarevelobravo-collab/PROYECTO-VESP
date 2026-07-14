# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtn_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_vtn_principal(object):
    def setupUi(self, vtn_principal):
        if not vtn_principal.objectName():
            vtn_principal.setObjectName(u"vtn_principal")
        vtn_principal.resize(614, 300)
        self.lbl_codigo_2 = QLabel(vtn_principal)
        self.lbl_codigo_2.setObjectName(u"lbl_codigo_2")
        self.lbl_codigo_2.setGeometry(QRect(50, 40, 141, 21))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lbl_codigo_2.setFont(font)
        self.btn_agregar = QPushButton(vtn_principal)
        self.btn_agregar.setObjectName(u"btn_agregar")
        self.btn_agregar.setGeometry(QRect(70, 210, 75, 23))
        self.btn_buscar = QPushButton(vtn_principal)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(390, 40, 75, 23))
        self.lbl_fecha = QLabel(vtn_principal)
        self.lbl_fecha.setObjectName(u"lbl_fecha")
        self.lbl_fecha.setGeometry(QRect(100, 120, 61, 21))
        self.lbl_fecha.setFont(font)
        self.lbl_descripcion = QLabel(vtn_principal)
        self.lbl_descripcion.setObjectName(u"lbl_descripcion")
        self.lbl_descripcion.setGeometry(QRect(310, 110, 81, 21))
        self.lbl_descripcion.setFont(font)
        self.btn_limpiar = QPushButton(vtn_principal)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setGeometry(QRect(380, 210, 75, 23))
        self.text_fecha = QLineEdit(vtn_principal)
        self.text_fecha.setObjectName(u"text_fecha")
        self.text_fecha.setGeometry(QRect(160, 120, 113, 20))
        self.text_buscar_codigo = QLineEdit(vtn_principal)
        self.text_buscar_codigo.setObjectName(u"text_buscar_codigo")
        self.text_buscar_codigo.setGeometry(QRect(182, 40, 191, 20))
        self.btn_guardar = QPushButton(vtn_principal)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(190, 210, 75, 23))
        self.btn_eliminar = QPushButton(vtn_principal)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setGeometry(QRect(480, 210, 75, 23))
        self.text_codigo = QLineEdit(vtn_principal)
        self.text_codigo.setObjectName(u"text_codigo")
        self.text_codigo.setGeometry(QRect(160, 80, 113, 20))
        self.text_descripcion = QLineEdit(vtn_principal)
        self.text_descripcion.setObjectName(u"text_descripcion")
        self.text_descripcion.setGeometry(QRect(400, 110, 113, 20))
        self.lbl_codigo = QLabel(vtn_principal)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        self.lbl_codigo.setGeometry(QRect(100, 80, 61, 21))
        self.lbl_codigo.setFont(font)
        self.btn_actualizar = QPushButton(vtn_principal)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(290, 210, 75, 23))
        self.lbl_gmail = QLabel(vtn_principal)
        self.lbl_gmail.setObjectName(u"lbl_gmail")
        self.lbl_gmail.setGeometry(QRect(100, 160, 61, 21))
        self.lbl_gmail.setFont(font)
        self.text_gmail = QLineEdit(vtn_principal)
        self.text_gmail.setObjectName(u"text_gmail")
        self.text_gmail.setGeometry(QRect(160, 160, 281, 20))

        self.retranslateUi(vtn_principal)

        QMetaObject.connectSlotsByName(vtn_principal)
    # setupUi

    def retranslateUi(self, vtn_principal):
        vtn_principal.setWindowTitle(QCoreApplication.translate("vtn_principal", u"Dialog", None))
        self.lbl_codigo_2.setText(QCoreApplication.translate("vtn_principal", u"Buscar por codigo:", None))
        self.btn_agregar.setText(QCoreApplication.translate("vtn_principal", u"Agregar", None))
        self.btn_buscar.setText(QCoreApplication.translate("vtn_principal", u"BUSCAR", None))
        self.lbl_fecha.setText(QCoreApplication.translate("vtn_principal", u"Fecha:", None))
        self.lbl_descripcion.setText(QCoreApplication.translate("vtn_principal", u"Descripcion:", None))
        self.btn_limpiar.setText(QCoreApplication.translate("vtn_principal", u"Limpiar", None))
        self.btn_guardar.setText(QCoreApplication.translate("vtn_principal", u"Guardar", None))
        self.btn_eliminar.setText(QCoreApplication.translate("vtn_principal", u"Eliminar", None))
        self.lbl_codigo.setText(QCoreApplication.translate("vtn_principal", u"Codigo:", None))
        self.btn_actualizar.setText(QCoreApplication.translate("vtn_principal", u"Actualizar", None))
        self.lbl_gmail.setText(QCoreApplication.translate("vtn_principal", u"EMAIL:", None))
    # retranslateUi

