# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QDoubleSpinBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1410, 730)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1410, 730))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/static/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#images .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#images .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#images .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, "
                        "255, 255);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/static/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extra"
                        "Label { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ///////////////////"
                        "//////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS *"
                        "/\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, "
                        "249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121,"
                        " 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    mar"
                        "gin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
""
                        "    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* ////////////////////////////////////////////////"
                        "/////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/static/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid r"
                        "gb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/static/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/*"
                        " /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189"
                        ", 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px"
                        ";	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QMessageBox */\n"
"QMessageBox {\n"
"	background-color: #21252b; /* QMessageBox\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QMessageBox QLabel#qt_msgbox_label { /* textLabel */\n"
"	color: #298DFF;\n"
"	background-color: transparent;\n"
"	min-width: 240px; /* textLabel\u8bbe\u7f6e\u6700\u5c0f\u5bbd\u5ea6\u53ef\u4ee5\u76f8\u5e94\u7684\u6539\u53d8QMessageBox\u7684\u6700\u5c0f\u5bbd\u5ea6 */\n"
"	min-height: 40px; /* textLabel\u548ciconLabel\u9ad8\u5ea6\u4fdd\u6301\u4e00\u81f4 */\n"
"}\n"
"\n"
"QMessageBox QLabel#qt_msgboxex_icon_label { /* iconLabel */\n"
"	width: 40px;\n"
"	height: 40px; /* textLabel\u548c"
                        "iconLabel\u9ad8\u5ea6\u4fdd\u6301\u4e00\u81f4 */\n"
"}\n"
"\n"
"QMessageBox QPushButton { /* QMessageBox\u4e2d\u7684QPushButton\u6837\u5f0f */\n"
"	color: #298DFF;\n"
"	font-family: \"Microsoft YaHei\";\n"
"	font-size: 10pt;\n"
"	min-width: 70px;\n"
"	min-height: 25px;\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"QMessageBox QDialogButtonBox#qt_msgbox_buttonbox { /* buttonBox */\n"
"	button-layout: 0; /* \u8bbe\u7f6eQPushButton\u5e03\u5c40\u597d\u50cf\u6ca1\u5565\u4f5c\u7528 */\n"
"}\n"
"\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(64, 0))
        self.leftMenuBg.setMaximumSize(QSize(64, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_1 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/static/images/smartCamera.png);")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Plain)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_1.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftMenuFrame.sizePolicy().hasHeightForWidth())
        self.leftMenuFrame.setSizePolicy(sizePolicy1)
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy2)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/static/icons/menu.png);")
        self.toggleButton.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy1.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy1)
        self.topMenu.setLayoutDirection(Qt.LeftToRight)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topMenu)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.btn_camera = QPushButton(self.topMenu)
        self.btn_camera.setObjectName(u"btn_camera")
        sizePolicy2.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy2)
        self.btn_camera.setMinimumSize(QSize(0, 50))
        self.btn_camera.setFont(font)
        self.btn_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_camera.setLayoutDirection(Qt.LeftToRight)
        self.btn_camera.setStyleSheet(u"background-image: url(:/icons/static/icons/camera.png);")
        self.btn_camera.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_camera)

        self.btn_image = QPushButton(self.topMenu)
        self.btn_image.setObjectName(u"btn_image")
        sizePolicy2.setHeightForWidth(self.btn_image.sizePolicy().hasHeightForWidth())
        self.btn_image.setSizePolicy(sizePolicy2)
        self.btn_image.setMinimumSize(QSize(0, 50))
        self.btn_image.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_image.setStyleSheet(u"background-image: url(:/icons/static/icons/images.png);")

        self.verticalLayout_3.addWidget(self.btn_image)

        self.btn_liucheng = QPushButton(self.topMenu)
        self.btn_liucheng.setObjectName(u"btn_liucheng")
        sizePolicy2.setHeightForWidth(self.btn_liucheng.sizePolicy().hasHeightForWidth())
        self.btn_liucheng.setSizePolicy(sizePolicy2)
        self.btn_liucheng.setMinimumSize(QSize(0, 50))
        self.btn_liucheng.setMaximumSize(QSize(16777215, 16777215))
        self.btn_liucheng.setStyleSheet(u"background-image: url(:/icons/static/icons/liucheng.png);")

        self.verticalLayout_3.addWidget(self.btn_liucheng)

        self.btn_statistic = QPushButton(self.topMenu)
        self.btn_statistic.setObjectName(u"btn_statistic")
        sizePolicy2.setHeightForWidth(self.btn_statistic.sizePolicy().hasHeightForWidth())
        self.btn_statistic.setSizePolicy(sizePolicy2)
        self.btn_statistic.setMinimumSize(QSize(0, 50))
        self.btn_statistic.setStyleSheet(u"background-image: url(:/icons/static/icons/statistic.png);")

        self.verticalLayout_3.addWidget(self.btn_statistic)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy2.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy2)
        self.btn_exit.setMinimumSize(QSize(0, 50))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/static/icons/exit.png);")

        self.verticalLayout_3.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setStyleSheet(u"")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy2.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy2)
        self.toggleLeftBox.setMinimumSize(QSize(0, 48))
        self.toggleLeftBox.setMaximumSize(QSize(16777215, 16777215))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/static/icons/setting.png);")
        self.toggleLeftBox.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_1.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/static/icons/cil-chevron-double-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.extraContent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setStyleSheet(u"QSpinBox\n"
"{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QSpinBox::down-arrow {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/static/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QSpinBox::up-arrow {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/stat"
                        "ic/icons/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QDoubleSpinBox\n"
"{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/static/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QDoubleSpinBox::up-arrow {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	"
                        "border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/static/icons/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"	margin-left: 0px;\n"
"	margin-right:10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid gray;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #bd93f9;\n"
"}")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_save = QPushButton(self.extraTopMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy2.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy2)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-save.png);")

        self.verticalLayout_7.addWidget(self.btn_save)

        self.frame_save = QFrame(self.extraTopMenu)
        self.frame_save.setObjectName(u"frame_save")
        sizePolicy1.setHeightForWidth(self.frame_save.sizePolicy().hasHeightForWidth())
        self.frame_save.setSizePolicy(sizePolicy1)
        self.frame_save.setMinimumSize(QSize(0, 0))
        self.frame_save.setMaximumSize(QSize(16777215, 0))
        self.frame_save.setStyleSheet(u"background-color: rgb(64, 71, 84);\n"
"font: 9pt \"\u9ed1\u4f53\";")
        self.frame_save.setFrameShape(QFrame.StyledPanel)
        self.frame_save.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_save)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(16)
        self.gridLayout_3.setContentsMargins(30, 16, -1, 16)
        self.CBox_suffix = QCheckBox(self.frame_save)
        self.CBox_suffix.setObjectName(u"CBox_suffix")
        sizePolicy1.setHeightForWidth(self.CBox_suffix.sizePolicy().hasHeightForWidth())
        self.CBox_suffix.setSizePolicy(sizePolicy1)
        self.CBox_suffix.setStyleSheet(u"text-align: center")
        self.CBox_suffix.setIconSize(QSize(16, 16))

        self.gridLayout_3.addWidget(self.CBox_suffix, 0, 0, 1, 5)

        self.LEdit_savePath = QLineEdit(self.frame_save)
        self.LEdit_savePath.setObjectName(u"LEdit_savePath")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LEdit_savePath.sizePolicy().hasHeightForWidth())
        self.LEdit_savePath.setSizePolicy(sizePolicy3)
        self.LEdit_savePath.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_3.addWidget(self.LEdit_savePath, 3, 1, 1, 1)

        self.TButton_savePath = QToolButton(self.frame_save)
        self.TButton_savePath.setObjectName(u"TButton_savePath")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TButton_savePath.sizePolicy().hasHeightForWidth())
        self.TButton_savePath.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.TButton_savePath, 3, 2, 1, 1)

        self.label_savePath = QLabel(self.frame_save)
        self.label_savePath.setObjectName(u"label_savePath")
        sizePolicy1.setHeightForWidth(self.label_savePath.sizePolicy().hasHeightForWidth())
        self.label_savePath.setSizePolicy(sizePolicy1)
        self.label_savePath.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_savePath, 3, 0, 1, 1)

        self.label_11 = QLabel(self.frame_save)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.CBox_chooseSaveImage = QComboBox(self.frame_save)
        self.CBox_chooseSaveImage.addItem("")
        self.CBox_chooseSaveImage.addItem("")
        self.CBox_chooseSaveImage.addItem("")
        self.CBox_chooseSaveImage.addItem("")
        self.CBox_chooseSaveImage.addItem("")
        self.CBox_chooseSaveImage.setObjectName(u"CBox_chooseSaveImage")
        self.CBox_chooseSaveImage.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_3.addWidget(self.CBox_chooseSaveImage, 4, 1, 1, 2)


        self.verticalLayout_7.addWidget(self.frame_save)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy2.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy2)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-equalizer.png);")

        self.verticalLayout_7.addWidget(self.btn_adjustments)

        self.frame_algorithm = QFrame(self.extraTopMenu)
        self.frame_algorithm.setObjectName(u"frame_algorithm")
        sizePolicy1.setHeightForWidth(self.frame_algorithm.sizePolicy().hasHeightForWidth())
        self.frame_algorithm.setSizePolicy(sizePolicy1)
        self.frame_algorithm.setMinimumSize(QSize(0, 0))
        self.frame_algorithm.setMaximumSize(QSize(16777215, 0))
        self.frame_algorithm.setStyleSheet(u"background-color: rgb(64, 71, 84);\n"
"font: 9pt \"\u9ed1\u4f53\";")
        self.frame_algorithm.setFrameShape(QFrame.StyledPanel)
        self.frame_algorithm.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_algorithm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(16)
        self.gridLayout_2.setContentsMargins(30, 16, 30, 16)
        self.LEdit_V = QLineEdit(self.frame_algorithm)
        self.LEdit_V.setObjectName(u"LEdit_V")
        self.LEdit_V.setMinimumSize(QSize(0, 34))
        self.LEdit_V.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_2.addWidget(self.LEdit_V, 8, 1, 1, 1)

        self.label_feature = QLabel(self.frame_algorithm)
        self.label_feature.setObjectName(u"label_feature")
        sizePolicy4.setHeightForWidth(self.label_feature.sizePolicy().hasHeightForWidth())
        self.label_feature.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.label_feature, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_algorithm)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 9, 0, 1, 1)

        self.label_matchRatio = QLabel(self.frame_algorithm)
        self.label_matchRatio.setObjectName(u"label_matchRatio")
        sizePolicy1.setHeightForWidth(self.label_matchRatio.sizePolicy().hasHeightForWidth())
        self.label_matchRatio.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_matchRatio, 1, 0, 1, 1)

        self.LEdit_D = QLineEdit(self.frame_algorithm)
        self.LEdit_D.setObjectName(u"LEdit_D")
        self.LEdit_D.setMinimumSize(QSize(0, 34))
        self.LEdit_D.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_2.addWidget(self.LEdit_D, 9, 1, 1, 1)

        self.label_6 = QLabel(self.frame_algorithm)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_matchDeadline = QLabel(self.frame_algorithm)
        self.label_matchDeadline.setObjectName(u"label_matchDeadline")

        self.gridLayout_2.addWidget(self.label_matchDeadline, 2, 0, 1, 1)

        self.label_5 = QLabel(self.frame_algorithm)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 7, 0, 1, 1)

        self.LEdit_H = QLineEdit(self.frame_algorithm)
        self.LEdit_H.setObjectName(u"LEdit_H")
        self.LEdit_H.setMinimumSize(QSize(0, 34))
        self.LEdit_H.setMaximumSize(QSize(16777215, 16777215))
        self.LEdit_H.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_2.addWidget(self.LEdit_H, 7, 1, 1, 1)

        self.label_29 = QLabel(self.frame_algorithm)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 6, 0, 1, 1)

        self.label_28 = QLabel(self.frame_algorithm)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 3, 0, 1, 1)

        self.SBox_matchDeadline = QSpinBox(self.frame_algorithm)
        self.SBox_matchDeadline.setObjectName(u"SBox_matchDeadline")
        self.SBox_matchDeadline.setMinimumSize(QSize(0, 34))
        self.SBox_matchDeadline.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.SBox_matchDeadline.setMinimum(4)
        self.SBox_matchDeadline.setMaximum(200)
        self.SBox_matchDeadline.setValue(7)

        self.gridLayout_2.addWidget(self.SBox_matchDeadline, 2, 1, 1, 2)

        self.DSBox_matchRatio = QDoubleSpinBox(self.frame_algorithm)
        self.DSBox_matchRatio.setObjectName(u"DSBox_matchRatio")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.DSBox_matchRatio.sizePolicy().hasHeightForWidth())
        self.DSBox_matchRatio.setSizePolicy(sizePolicy5)
        self.DSBox_matchRatio.setMinimumSize(QSize(0, 34))
        self.DSBox_matchRatio.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.DSBox_matchRatio.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.DSBox_matchRatio.setMaximum(1.000000000000000)
        self.DSBox_matchRatio.setSingleStep(0.050000000000000)
        self.DSBox_matchRatio.setValue(0.700000000000000)

        self.gridLayout_2.addWidget(self.DSBox_matchRatio, 1, 1, 1, 2)

        self.CBox_feature = QComboBox(self.frame_algorithm)
        self.CBox_feature.addItem("")
        self.CBox_feature.addItem("")
        self.CBox_feature.addItem("")
        self.CBox_feature.addItem("")
        self.CBox_feature.addItem("")
        self.CBox_feature.setObjectName(u"CBox_feature")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.CBox_feature.sizePolicy().hasHeightForWidth())
        self.CBox_feature.setSizePolicy(sizePolicy6)
        self.CBox_feature.setMinimumSize(QSize(120, 0))
        self.CBox_feature.setStyleSheet(u"background-color: rgb(27, 29, 35);")

        self.gridLayout_2.addWidget(self.CBox_feature, 0, 1, 1, 2)

        self.DSBox_keypointThreshold = QDoubleSpinBox(self.frame_algorithm)
        self.DSBox_keypointThreshold.setObjectName(u"DSBox_keypointThreshold")
        self.DSBox_keypointThreshold.setMinimumSize(QSize(0, 34))
        self.DSBox_keypointThreshold.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.DSBox_keypointThreshold.setDecimals(3)
        self.DSBox_keypointThreshold.setMaximum(1.000000000000000)
        self.DSBox_keypointThreshold.setSingleStep(0.001000000000000)
        self.DSBox_keypointThreshold.setValue(0.006000000000000)

        self.gridLayout_2.addWidget(self.DSBox_keypointThreshold, 3, 1, 1, 1)

        self.DSBox_matchThreshold = QDoubleSpinBox(self.frame_algorithm)
        self.DSBox_matchThreshold.setObjectName(u"DSBox_matchThreshold")
        self.DSBox_matchThreshold.setMinimumSize(QSize(0, 34))
        self.DSBox_matchThreshold.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.DSBox_matchThreshold.setMaximum(1.000000000000000)
        self.DSBox_matchThreshold.setSingleStep(0.010000000000000)
        self.DSBox_matchThreshold.setValue(0.280000000000000)

        self.gridLayout_2.addWidget(self.DSBox_matchThreshold, 6, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_algorithm)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy2.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy2)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-layers.png);")

        self.verticalLayout_7.addWidget(self.btn_more)

        self.frame_more = QFrame(self.extraTopMenu)
        self.frame_more.setObjectName(u"frame_more")
        sizePolicy1.setHeightForWidth(self.frame_more.sizePolicy().hasHeightForWidth())
        self.frame_more.setSizePolicy(sizePolicy1)
        self.frame_more.setMinimumSize(QSize(0, 0))
        self.frame_more.setMaximumSize(QSize(16777215, 0))
        self.frame_more.setStyleSheet(u"background-color: rgb(64, 71, 84);")
        self.frame_more.setFrameShape(QFrame.StyledPanel)
        self.frame_more.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_more)
        self.verticalLayout_19.setSpacing(16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(30, 16, -1, 16)
        self.CBox_showImageFunction = QCheckBox(self.frame_more)
        self.CBox_showImageFunction.setObjectName(u"CBox_showImageFunction")

        self.verticalLayout_19.addWidget(self.CBox_showImageFunction)

        self.CBox_showDoubleImage = QCheckBox(self.frame_more)
        self.CBox_showDoubleImage.setObjectName(u"CBox_showDoubleImage")

        self.verticalLayout_19.addWidget(self.CBox_showDoubleImage)


        self.verticalLayout_7.addWidget(self.frame_more)


        self.verticalLayout_6.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.btn_saveOption = QPushButton(self.extraCenter)
        self.btn_saveOption.setObjectName(u"btn_saveOption")
        sizePolicy1.setHeightForWidth(self.btn_saveOption.sizePolicy().hasHeightForWidth())
        self.btn_saveOption.setSizePolicy(sizePolicy1)
        self.btn_saveOption.setStyleSheet(u"background-color: rgb(64, 71, 84);\n"
"margin: 0 15px;\n"
"padding: 8px 0;\n"
"border-radius: 12px;\n"
"text-align: center;\n"
"border-left: 0;")
        self.btn_saveOption.setIconSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.btn_saveOption)

        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        font3 = QFont()
        font3.setFamilies([u"\u65b9\u6b63\u8212\u4f53"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"background: transparent;\n"
"font: 14pt \"\u65b9\u6b63\u8212\u4f53\";")
        self.textEdit.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.textEdit.setFrameShape(QFrame.Box)
        self.textEdit.setFrameShadow(QFrame.Sunken)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.textEdit)


        self.verticalLayout_6.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.contentBox)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy7)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamilies([u"\u65b9\u6b63\u8212\u4f53"])
        font4.setPointSize(26)
        font4.setBold(False)
        font4.setItalic(False)
        self.titleRightInfo.setFont(font4)
        self.titleRightInfo.setStyleSheet(u"font: 26pt \"\u65b9\u6b63\u8212\u4f53\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(140, 0))
        self.rightButtons.setFrameShape(QFrame.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/icons/static/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/static/icons/Minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/static/icons/zhankai.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/static/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_9.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(0, 0))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setMinimumSize(QSize(0, 0))
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.stackedWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        sizePolicy1.setHeightForWidth(self.camera.sizePolicy().hasHeightForWidth())
        self.camera.setSizePolicy(sizePolicy1)
        self.camera.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.camera)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.cameraLabel = QLabel(self.camera)
        self.cameraLabel.setObjectName(u"cameraLabel")
        sizePolicy6.setHeightForWidth(self.cameraLabel.sizePolicy().hasHeightForWidth())
        self.cameraLabel.setSizePolicy(sizePolicy6)
        self.cameraLabel.setMinimumSize(QSize(640, 520))
        self.cameraLabel.setStyleSheet(u"background-color: rgb(33, 37, 43);border-radius: 16px;\n"
"font: 20pt \"\u6977\u4f53\";")
        self.cameraLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.cameraLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.cameraBtns = QFrame(self.camera)
        self.cameraBtns.setObjectName(u"cameraBtns")
        sizePolicy3.setHeightForWidth(self.cameraBtns.sizePolicy().hasHeightForWidth())
        self.cameraBtns.setSizePolicy(sizePolicy3)
        self.cameraBtns.setFrameShape(QFrame.StyledPanel)
        self.cameraBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.cameraBtns)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, -1, 10, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btn_biaoding = QPushButton(self.cameraBtns)
        self.btn_biaoding.setObjectName(u"btn_biaoding")
        icon5 = QIcon()
        icon5.addFile(u":/icons/static/icons/biaoding.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_biaoding.setIcon(icon5)
        self.btn_biaoding.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.btn_biaoding)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.cameraBtn = QPushButton(self.cameraBtns)
        self.cameraBtn.setObjectName(u"cameraBtn")
        sizePolicy6.setHeightForWidth(self.cameraBtn.sizePolicy().hasHeightForWidth())
        self.cameraBtn.setSizePolicy(sizePolicy6)
        icon6 = QIcon()
        icon6.addFile(u":/icons/static/icons/camera_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u":/icons/static/icons/camera_on.png", QSize(), QIcon.Normal, QIcon.On)
        self.cameraBtn.setIcon(icon6)
        self.cameraBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.cameraBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.shutterBtn = QPushButton(self.cameraBtns)
        self.shutterBtn.setObjectName(u"shutterBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.shutterBtn.sizePolicy().hasHeightForWidth())
        self.shutterBtn.setSizePolicy(sizePolicy8)
        icon7 = QIcon()
        icon7.addFile(u":/icons/static/icons/shutter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shutterBtn.setIcon(icon7)
        self.shutterBtn.setIconSize(QSize(64, 64))

        self.horizontalLayout_6.addWidget(self.shutterBtn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.changeCameraBtn = QPushButton(self.cameraBtns)
        self.changeCameraBtn.setObjectName(u"changeCameraBtn")
        sizePolicy8.setHeightForWidth(self.changeCameraBtn.sizePolicy().hasHeightForWidth())
        self.changeCameraBtn.setSizePolicy(sizePolicy8)
        icon8 = QIcon()
        icon8.addFile(u":/icons/static/icons/camera_change.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeCameraBtn.setIcon(icon8)
        self.changeCameraBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.changeCameraBtn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.videoMatchBtn = QPushButton(self.cameraBtns)
        self.videoMatchBtn.setObjectName(u"videoMatchBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/static/icons/dingwei.png", QSize(), QIcon.Normal, QIcon.Off)
        self.videoMatchBtn.setIcon(icon9)
        self.videoMatchBtn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.videoMatchBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_12.addWidget(self.cameraBtns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.camera)
        self.images = QWidget()
        self.images.setObjectName(u"images")
        self.images.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.horizontalLayout_7 = QHBoxLayout(self.images)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, -1, 10, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.imageSArea = QScrollArea(self.images)
        self.imageSArea.setObjectName(u"imageSArea")
        sizePolicy6.setHeightForWidth(self.imageSArea.sizePolicy().hasHeightForWidth())
        self.imageSArea.setSizePolicy(sizePolicy6)
        self.imageSArea.setMinimumSize(QSize(800, 600))
        self.imageSArea.setStyleSheet(u"font-family: url(:/fonts/static/fonts/IPix.ttf);font-size: 18px;background-color: rgb(33, 37, 43);border-radius: 16px;")
        self.imageSArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageSArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.imageSArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.imageSArea.setWidgetResizable(True)
        self.imageSArea.setAlignment(Qt.AlignCenter)
        self.imageSAreaContent = QWidget()
        self.imageSAreaContent.setObjectName(u"imageSAreaContent")
        self.imageSAreaContent.setGeometry(QRect(0, 0, 800, 600))
        sizePolicy1.setHeightForWidth(self.imageSAreaContent.sizePolicy().hasHeightForWidth())
        self.imageSAreaContent.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u":/fonts/static/fonts/IPix.ttf"])
        font5.setBold(False)
        font5.setItalic(False)
        self.imageSAreaContent.setFont(font5)
        self.verticalLayout = QVBoxLayout(self.imageSAreaContent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.resultLabel = QLabel(self.imageSAreaContent)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy9)
        self.resultLabel.setMinimumSize(QSize(800, 600))
        self.resultLabel.setStyleSheet(u"font: 20pt \"\u6977\u4f53\";")
        self.resultLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.resultLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.imageSArea.setWidget(self.imageSAreaContent)

        self.horizontalLayout_7.addWidget(self.imageSArea, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.imageMenu = QFrame(self.images)
        self.imageMenu.setObjectName(u"imageMenu")
        sizePolicy3.setHeightForWidth(self.imageMenu.sizePolicy().hasHeightForWidth())
        self.imageMenu.setSizePolicy(sizePolicy3)
        self.imageMenu.setStyleSheet(u"QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"};")
        self.imageMenu.setFrameShape(QFrame.StyledPanel)
        self.imageMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.imageMenu)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 0, 8, 0)
        self.addGloadImageBtn = QPushButton(self.imageMenu)
        self.addGloadImageBtn.setObjectName(u"addGloadImageBtn")
        sizePolicy8.setHeightForWidth(self.addGloadImageBtn.sizePolicy().hasHeightForWidth())
        self.addGloadImageBtn.setSizePolicy(sizePolicy8)
        self.addGloadImageBtn.setMinimumSize(QSize(0, 45))
        self.addGloadImageBtn.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-image-plus.png);")

        self.verticalLayout_13.addWidget(self.addGloadImageBtn)

        self.addLocalImageBtn = QPushButton(self.imageMenu)
        self.addLocalImageBtn.setObjectName(u"addLocalImageBtn")
        sizePolicy8.setHeightForWidth(self.addLocalImageBtn.sizePolicy().hasHeightForWidth())
        self.addLocalImageBtn.setSizePolicy(sizePolicy8)
        self.addLocalImageBtn.setMinimumSize(QSize(0, 45))
        self.addLocalImageBtn.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-image-plus.png);")

        self.verticalLayout_13.addWidget(self.addLocalImageBtn)

        self.matchImageBtn = QPushButton(self.imageMenu)
        self.matchImageBtn.setObjectName(u"matchImageBtn")
        sizePolicy8.setHeightForWidth(self.matchImageBtn.sizePolicy().hasHeightForWidth())
        self.matchImageBtn.setSizePolicy(sizePolicy8)
        self.matchImageBtn.setMinimumSize(QSize(0, 45))
        self.matchImageBtn.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-loop-circular.png);")

        self.verticalLayout_13.addWidget(self.matchImageBtn)

        self.angleImageBtn = QPushButton(self.imageMenu)
        self.angleImageBtn.setObjectName(u"angleImageBtn")
        sizePolicy8.setHeightForWidth(self.angleImageBtn.sizePolicy().hasHeightForWidth())
        self.angleImageBtn.setSizePolicy(sizePolicy8)
        self.angleImageBtn.setMinimumSize(QSize(0, 45))
        self.angleImageBtn.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-triangle.png);")

        self.verticalLayout_13.addWidget(self.angleImageBtn)

        self.calcHDistanceBtn = QPushButton(self.imageMenu)
        self.calcHDistanceBtn.setObjectName(u"calcHDistanceBtn")
        sizePolicy8.setHeightForWidth(self.calcHDistanceBtn.sizePolicy().hasHeightForWidth())
        self.calcHDistanceBtn.setSizePolicy(sizePolicy8)
        self.calcHDistanceBtn.setMinimumSize(QSize(0, 45))
        self.calcHDistanceBtn.setStyleSheet(u"background-image: url(:/icons/static/icons/cil-pen-alt.png);")

        self.verticalLayout_13.addWidget(self.calcHDistanceBtn)


        self.horizontalLayout_7.addWidget(self.imageMenu)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.stackedWidget.addWidget(self.images)
        self.liucheng = QWidget()
        self.liucheng.setObjectName(u"liucheng")
        self.verticalLayout_16 = QVBoxLayout(self.liucheng)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_liucheng = QLabel(self.liucheng)
        self.label_liucheng.setObjectName(u"label_liucheng")
        sizePolicy8.setHeightForWidth(self.label_liucheng.sizePolicy().hasHeightForWidth())
        self.label_liucheng.setSizePolicy(sizePolicy8)
        self.label_liucheng.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setFamilies([u"\u65b9\u6b63\u59da\u4f53"])
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_liucheng.setFont(font6)
        self.label_liucheng.setStyleSheet(u"font: 20pt \"\u65b9\u6b63\u59da\u4f53\";")
        self.label_liucheng.setFrameShape(QFrame.NoFrame)
        self.label_liucheng.setFrameShadow(QFrame.Plain)

        self.verticalLayout_16.addWidget(self.label_liucheng, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.GBox_show = QGroupBox(self.liucheng)
        self.GBox_show.setObjectName(u"GBox_show")
        sizePolicy7.setHeightForWidth(self.GBox_show.sizePolicy().hasHeightForWidth())
        self.GBox_show.setSizePolicy(sizePolicy7)
        self.GBox_show.setInputMethodHints(Qt.ImhNone)
        self.GBox_show.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.horizontalLayout_8 = QHBoxLayout(self.GBox_show)
        self.horizontalLayout_8.setSpacing(16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_btns = QFrame(self.GBox_show)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_btns)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_Setp1 = QPushButton(self.frame_btns)
        self.btn_Setp1.setObjectName(u"btn_Setp1")
        sizePolicy8.setHeightForWidth(self.btn_Setp1.sizePolicy().hasHeightForWidth())
        self.btn_Setp1.setSizePolicy(sizePolicy8)
        self.btn_Setp1.setMinimumSize(QSize(120, 40))
        self.btn_Setp1.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.btn_Setp1)

        self.line1 = QFrame(self.frame_btns)
        self.line1.setObjectName(u"line1")
        sizePolicy6.setHeightForWidth(self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy6)
        self.line1.setMaximumSize(QSize(16777215, 20))
        self.line1.setLayoutDirection(Qt.LeftToRight)
        self.line1.setStyleSheet(u"")
        self.line1.setFrameShadow(QFrame.Plain)
        self.line1.setLineWidth(10)
        self.line1.setMidLineWidth(0)
        self.line1.setFrameShape(QFrame.VLine)

        self.verticalLayout_17.addWidget(self.line1, 0, Qt.AlignHCenter)

        self.btn_Setp2 = QPushButton(self.frame_btns)
        self.btn_Setp2.setObjectName(u"btn_Setp2")
        sizePolicy8.setHeightForWidth(self.btn_Setp2.sizePolicy().hasHeightForWidth())
        self.btn_Setp2.setSizePolicy(sizePolicy8)
        self.btn_Setp2.setMinimumSize(QSize(120, 40))
        self.btn_Setp2.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.btn_Setp2)

        self.line2 = QFrame(self.frame_btns)
        self.line2.setObjectName(u"line2")
        sizePolicy6.setHeightForWidth(self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy6)
        self.line2.setMinimumSize(QSize(0, 20))
        self.line2.setFrameShadow(QFrame.Plain)
        self.line2.setLineWidth(10)
        self.line2.setFrameShape(QFrame.VLine)

        self.verticalLayout_17.addWidget(self.line2, 0, Qt.AlignHCenter)

        self.btn_Setp3 = QPushButton(self.frame_btns)
        self.btn_Setp3.setObjectName(u"btn_Setp3")
        sizePolicy8.setHeightForWidth(self.btn_Setp3.sizePolicy().hasHeightForWidth())
        self.btn_Setp3.setSizePolicy(sizePolicy8)
        self.btn_Setp3.setMinimumSize(QSize(120, 40))
        self.btn_Setp3.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.btn_Setp3)

        self.line3 = QFrame(self.frame_btns)
        self.line3.setObjectName(u"line3")
        sizePolicy6.setHeightForWidth(self.line3.sizePolicy().hasHeightForWidth())
        self.line3.setSizePolicy(sizePolicy6)
        self.line3.setMinimumSize(QSize(0, 20))
        self.line3.setFrameShadow(QFrame.Plain)
        self.line3.setLineWidth(10)
        self.line3.setFrameShape(QFrame.VLine)

        self.verticalLayout_17.addWidget(self.line3, 0, Qt.AlignHCenter)

        self.btn_Setp4 = QPushButton(self.frame_btns)
        self.btn_Setp4.setObjectName(u"btn_Setp4")
        sizePolicy8.setHeightForWidth(self.btn_Setp4.sizePolicy().hasHeightForWidth())
        self.btn_Setp4.setSizePolicy(sizePolicy8)
        self.btn_Setp4.setMinimumSize(QSize(120, 40))
        self.btn_Setp4.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.btn_Setp4)

        self.line4 = QFrame(self.frame_btns)
        self.line4.setObjectName(u"line4")
        sizePolicy6.setHeightForWidth(self.line4.sizePolicy().hasHeightForWidth())
        self.line4.setSizePolicy(sizePolicy6)
        self.line4.setMinimumSize(QSize(0, 20))
        self.line4.setFrameShadow(QFrame.Plain)
        self.line4.setLineWidth(10)
        self.line4.setFrameShape(QFrame.VLine)

        self.verticalLayout_17.addWidget(self.line4, 0, Qt.AlignHCenter)

        self.btn_Setp5 = QPushButton(self.frame_btns)
        self.btn_Setp5.setObjectName(u"btn_Setp5")
        self.btn_Setp5.setMinimumSize(QSize(120, 40))

        self.verticalLayout_17.addWidget(self.btn_Setp5)


        self.horizontalLayout_8.addWidget(self.frame_btns)

        self.frame_result = QFrame(self.GBox_show)
        self.frame_result.setObjectName(u"frame_result")
        sizePolicy1.setHeightForWidth(self.frame_result.sizePolicy().hasHeightForWidth())
        self.frame_result.setSizePolicy(sizePolicy1)
        self.frame_result.setFrameShape(QFrame.StyledPanel)
        self.frame_result.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_result)
        self.verticalLayout_18.setSpacing(20)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 9)
        self.frame = QFrame(self.frame_result)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(20)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(16, -1, -1, -1)
        self.label_globalImgSize = QLabel(self.frame_2)
        self.label_globalImgSize.setObjectName(u"label_globalImgSize")
        sizePolicy8.setHeightForWidth(self.label_globalImgSize.sizePolicy().hasHeightForWidth())
        self.label_globalImgSize.setSizePolicy(sizePolicy8)
        self.label_globalImgSize.setMinimumSize(QSize(0, 30))
        self.label_globalImgSize.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_globalImgSize, 1, 0, 1, 1)

        self.label_localImgSize = QLabel(self.frame_2)
        self.label_localImgSize.setObjectName(u"label_localImgSize")
        sizePolicy8.setHeightForWidth(self.label_localImgSize.sizePolicy().hasHeightForWidth())
        self.label_localImgSize.setSizePolicy(sizePolicy8)
        self.label_localImgSize.setMinimumSize(QSize(0, 30))
        self.label_localImgSize.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_localImgSize, 0, 0, 1, 1)

        self.label_featureExtraction = QLabel(self.frame_2)
        self.label_featureExtraction.setObjectName(u"label_featureExtraction")
        self.label_featureExtraction.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_featureExtraction, 0, 1, 1, 1)

        self.label_featureMatch = QLabel(self.frame_2)
        self.label_featureMatch.setObjectName(u"label_featureMatch")
        self.label_featureMatch.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_featureMatch, 1, 1, 1, 1)

        self.label_matchPoints = QLabel(self.frame_2)
        self.label_matchPoints.setObjectName(u"label_matchPoints")
        sizePolicy8.setHeightForWidth(self.label_matchPoints.sizePolicy().hasHeightForWidth())
        self.label_matchPoints.setSizePolicy(sizePolicy8)
        self.label_matchPoints.setMinimumSize(QSize(0, 30))
        self.label_matchPoints.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_matchPoints, 4, 0, 1, 1)

        self.label_timeCount = QLabel(self.frame_2)
        self.label_timeCount.setObjectName(u"label_timeCount")
        sizePolicy8.setHeightForWidth(self.label_timeCount.sizePolicy().hasHeightForWidth())
        self.label_timeCount.setSizePolicy(sizePolicy8)
        self.label_timeCount.setMinimumSize(QSize(0, 30))
        self.label_timeCount.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_6.addWidget(self.label_timeCount, 4, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setContentsMargins(16, -1, 9, -1)
        self.label_HDistanceError = QLabel(self.frame_3)
        self.label_HDistanceError.setObjectName(u"label_HDistanceError")
        self.label_HDistanceError.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_HDistanceError, 2, 4, 1, 1)

        self.TButton_HDistanceError = QToolButton(self.frame_3)
        self.TButton_HDistanceError.setObjectName(u"TButton_HDistanceError")
        self.TButton_HDistanceError.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_7.addWidget(self.TButton_HDistanceError, 2, 5, 1, 1)

        self.label_HOffset = QLabel(self.frame_3)
        self.label_HOffset.setObjectName(u"label_HOffset")
        sizePolicy6.setHeightForWidth(self.label_HOffset.sizePolicy().hasHeightForWidth())
        self.label_HOffset.setSizePolicy(sizePolicy6)
        self.label_HOffset.setMinimumSize(QSize(0, 60))
        self.label_HOffset.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_HOffset, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_3, 1, 3, 1, 1, Qt.AlignRight)

        self.label_VOffset = QLabel(self.frame_3)
        self.label_VOffset.setObjectName(u"label_VOffset")
        sizePolicy8.setHeightForWidth(self.label_VOffset.sizePolicy().hasHeightForWidth())
        self.label_VOffset.setSizePolicy(sizePolicy8)
        self.label_VOffset.setMinimumSize(QSize(0, 60))
        self.label_VOffset.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_VOffset, 1, 1, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label, 0, 3, 1, 1, Qt.AlignRight)

        self.label_66 = QLabel(self.frame_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_66, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_4, 2, 3, 1, 1, Qt.AlignRight)

        self.label_53 = QLabel(self.frame_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_53, 1, 0, 1, 1)

        self.label_VError = QLabel(self.frame_3)
        self.label_VError.setObjectName(u"label_VError")
        self.label_VError.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_VError, 1, 4, 1, 1)

        self.label_HError = QLabel(self.frame_3)
        self.label_HError.setObjectName(u"label_HError")
        self.label_HError.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_HError, 0, 4, 1, 1)

        self.label_52 = QLabel(self.frame_3)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_52, 0, 0, 1, 1)

        self.TButton_calcHError = QToolButton(self.frame_3)
        self.TButton_calcHError.setObjectName(u"TButton_calcHError")
        sizePolicy8.setHeightForWidth(self.TButton_calcHError.sizePolicy().hasHeightForWidth())
        self.TButton_calcHError.setSizePolicy(sizePolicy8)
        self.TButton_calcHError.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_7.addWidget(self.TButton_calcHError, 0, 5, 1, 1)

        self.TButton_HError = QToolButton(self.frame_3)
        self.TButton_HError.setObjectName(u"TButton_HError")
        self.TButton_HError.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_7.addWidget(self.TButton_HError, 1, 5, 1, 1)

        self.label_HDistance = QLabel(self.frame_3)
        self.label_HDistance.setObjectName(u"label_HDistance")
        sizePolicy8.setHeightForWidth(self.label_HDistance.sizePolicy().hasHeightForWidth())
        self.label_HDistance.setSizePolicy(sizePolicy8)
        self.label_HDistance.setMinimumSize(QSize(0, 60))
        self.label_HDistance.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_HDistance, 2, 1, 1, 1)

        self.label_67 = QLabel(self.frame_3)
        self.label_67.setObjectName(u"label_67")
        sizePolicy4.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy4)
        self.label_67.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_67, 0, 2, 1, 1)

        self.label_68 = QLabel(self.frame_3)
        self.label_68.setObjectName(u"label_68")
        sizePolicy4.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy4)
        self.label_68.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_68, 1, 2, 1, 1)

        self.label_69 = QLabel(self.frame_3)
        self.label_69.setObjectName(u"label_69")
        sizePolicy4.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy4)
        self.label_69.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";")

        self.gridLayout_7.addWidget(self.label_69, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 1, 0, 1, 2)


        self.verticalLayout_18.addWidget(self.frame)

        self.btn_runStep = QPushButton(self.frame_result)
        self.btn_runStep.setObjectName(u"btn_runStep")
        sizePolicy8.setHeightForWidth(self.btn_runStep.sizePolicy().hasHeightForWidth())
        self.btn_runStep.setSizePolicy(sizePolicy8)
        self.btn_runStep.setMinimumSize(QSize(0, 40))
        self.btn_runStep.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.verticalLayout_18.addWidget(self.btn_runStep)


        self.horizontalLayout_8.addWidget(self.frame_result)


        self.verticalLayout_16.addWidget(self.GBox_show)

        self.stackedWidget.addWidget(self.liucheng)
        self.statistic = QWidget()
        self.statistic.setObjectName(u"statistic")
        self.horizontalLayout_9 = QHBoxLayout(self.statistic)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(self.statistic)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(20, -1, 20, -1)
        self.label1_2_2 = QLabel(self.frame_4)
        self.label1_2_2.setObjectName(u"label1_2_2")
        self.label1_2_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_12.addWidget(self.label1_2_2, 1, 2, 1, 1, Qt.AlignHCenter)

        self.label1_1_2 = QLabel(self.frame_4)
        self.label1_1_2.setObjectName(u"label1_1_2")
        self.label1_1_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_12.addWidget(self.label1_1_2, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_12.addWidget(self.label_22, 2, 0, 1, 1)

        self.label1_3 = QLabel(self.frame_4)
        self.label1_3.setObjectName(u"label1_3")
        self.label1_3.setStyleSheet(u"font: 16pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_12.addWidget(self.label1_3, 2, 2, 1, 1, Qt.AlignHCenter)

        self.label1_2_1 = QLabel(self.frame_4)
        self.label1_2_1.setObjectName(u"label1_2_1")

        self.gridLayout_12.addWidget(self.label1_2_1, 1, 0, 1, 1)

        self.label1_1_1 = QLabel(self.frame_4)
        self.label1_1_1.setObjectName(u"label1_1_1")

        self.gridLayout_12.addWidget(self.label1_1_1, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.groupBox)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_13.addWidget(self.label_34, 1, 0, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 2, 3, 1, 1)

        self.label1_DError = QLabel(self.frame_9)
        self.label1_DError.setObjectName(u"label1_DError")

        self.gridLayout_13.addWidget(self.label1_DError, 2, 4, 1, 1)

        self.label_35 = QLabel(self.frame_9)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_13.addWidget(self.label_35, 2, 0, 1, 1)

        self.label1_H = QLabel(self.frame_9)
        self.label1_H.setObjectName(u"label1_H")
        sizePolicy4.setHeightForWidth(self.label1_H.sizePolicy().hasHeightForWidth())
        self.label1_H.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label1_H, 0, 1, 1, 1)

        self.label1_HError = QLabel(self.frame_9)
        self.label1_HError.setObjectName(u"label1_HError")

        self.gridLayout_13.addWidget(self.label1_HError, 0, 4, 1, 1)

        self.label1_D = QLabel(self.frame_9)
        self.label1_D.setObjectName(u"label1_D")
        sizePolicy4.setHeightForWidth(self.label1_D.sizePolicy().hasHeightForWidth())
        self.label1_D.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label1_D, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_13.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_13.addWidget(self.label_30, 0, 0, 1, 1)

        self.label1_VError = QLabel(self.frame_9)
        self.label1_VError.setObjectName(u"label1_VError")

        self.gridLayout_13.addWidget(self.label1_VError, 1, 4, 1, 1)

        self.label1_V = QLabel(self.frame_9)
        self.label1_V.setObjectName(u"label1_V")
        sizePolicy4.setHeightForWidth(self.label1_V.sizePolicy().hasHeightForWidth())
        self.label1_V.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label1_V, 1, 1, 1, 1)

        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        sizePolicy4.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label_39, 0, 2, 1, 1)

        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label_40, 1, 2, 1, 1)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        sizePolicy4.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy4)

        self.gridLayout_13.addWidget(self.label_41, 2, 2, 1, 1)

        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_13.addWidget(self.label_2, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 1, 0, 1, 1)

        self.btn_runStep1 = QPushButton(self.groupBox)
        self.btn_runStep1.setObjectName(u"btn_runStep1")
        self.btn_runStep1.setMinimumSize(QSize(0, 30))
        self.btn_runStep1.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_4.addWidget(self.btn_runStep1, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.statistic)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_5 = QFrame(self.groupBox_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(20, -1, 20, -1)
        self.label2_3 = QLabel(self.frame_5)
        self.label2_3.setObjectName(u"label2_3")
        self.label2_3.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_14.addWidget(self.label2_3, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_14.addWidget(self.label_23, 2, 0, 1, 1)

        self.label2_2_2 = QLabel(self.frame_5)
        self.label2_2_2.setObjectName(u"label2_2_2")
        self.label2_2_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_14.addWidget(self.label2_2_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label2_1_1 = QLabel(self.frame_5)
        self.label2_1_1.setObjectName(u"label2_1_1")

        self.gridLayout_14.addWidget(self.label2_1_1, 0, 0, 1, 1)

        self.label2_1_2 = QLabel(self.frame_5)
        self.label2_1_2.setObjectName(u"label2_1_2")
        self.label2_1_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_14.addWidget(self.label2_1_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label2_2_1 = QLabel(self.frame_5)
        self.label2_2_1.setObjectName(u"label2_2_1")

        self.gridLayout_14.addWidget(self.label2_2_1, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)

        self.btn_runStep2 = QPushButton(self.groupBox_2)
        self.btn_runStep2.setObjectName(u"btn_runStep2")
        self.btn_runStep2.setMinimumSize(QSize(0, 30))
        self.btn_runStep2.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_8.addWidget(self.btn_runStep2, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.groupBox_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_10)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label2_D = QLabel(self.frame_10)
        self.label2_D.setObjectName(u"label2_D")
        sizePolicy4.setHeightForWidth(self.label2_D.sizePolicy().hasHeightForWidth())
        self.label2_D.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.label2_D, 2, 1, 1, 1)

        self.label2_VError = QLabel(self.frame_10)
        self.label2_VError.setObjectName(u"label2_VError")

        self.gridLayout_15.addWidget(self.label2_VError, 1, 4, 1, 1)

        self.label_42 = QLabel(self.frame_10)
        self.label_42.setObjectName(u"label_42")
        sizePolicy4.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.label_42, 0, 2, 1, 1)

        self.label2_HError = QLabel(self.frame_10)
        self.label2_HError.setObjectName(u"label2_HError")

        self.gridLayout_15.addWidget(self.label2_HError, 0, 4, 1, 1)

        self.label_38 = QLabel(self.frame_10)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_15.addWidget(self.label_38, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_10)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_15.addWidget(self.label_10, 0, 3, 1, 1)

        self.label_44 = QLabel(self.frame_10)
        self.label_44.setObjectName(u"label_44")
        sizePolicy4.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.label_44, 2, 2, 1, 1)

        self.label_51 = QLabel(self.frame_10)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_15.addWidget(self.label_51, 2, 3, 1, 1)

        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_15.addWidget(self.label_36, 0, 0, 1, 1)

        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_15.addWidget(self.label_37, 1, 0, 1, 1)

        self.label2_H = QLabel(self.frame_10)
        self.label2_H.setObjectName(u"label2_H")
        sizePolicy4.setHeightForWidth(self.label2_H.sizePolicy().hasHeightForWidth())
        self.label2_H.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.label2_H, 0, 1, 1, 1)

        self.label2_V = QLabel(self.frame_10)
        self.label2_V.setObjectName(u"label2_V")

        self.gridLayout_15.addWidget(self.label2_V, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_15.addWidget(self.label_12, 1, 3, 1, 1)

        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        sizePolicy4.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy4)

        self.gridLayout_15.addWidget(self.label_43, 1, 2, 1, 1)

        self.label2_DError = QLabel(self.frame_10)
        self.label2_DError.setObjectName(u"label2_DError")

        self.gridLayout_15.addWidget(self.label2_DError, 2, 4, 1, 1)


        self.gridLayout_8.addWidget(self.frame_10, 1, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.statistic)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_6 = QFrame(self.groupBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(20, -1, 20, -1)
        self.label3_1_1 = QLabel(self.frame_6)
        self.label3_1_1.setObjectName(u"label3_1_1")

        self.gridLayout_19.addWidget(self.label3_1_1, 0, 0, 1, 1)

        self.label3_1_2 = QLabel(self.frame_6)
        self.label3_1_2.setObjectName(u"label3_1_2")
        self.label3_1_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_19.addWidget(self.label3_1_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label3_2_1 = QLabel(self.frame_6)
        self.label3_2_1.setObjectName(u"label3_2_1")

        self.gridLayout_19.addWidget(self.label3_2_1, 1, 0, 1, 1)

        self.label3_2_2 = QLabel(self.frame_6)
        self.label3_2_2.setObjectName(u"label3_2_2")
        self.label3_2_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_19.addWidget(self.label3_2_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label3_3 = QLabel(self.frame_6)
        self.label3_3.setObjectName(u"label3_3")
        self.label3_3.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_19.addWidget(self.label3_3, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_19.addWidget(self.label_24, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_6, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.groupBox_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_11)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_50 = QLabel(self.frame_11)
        self.label_50.setObjectName(u"label_50")
        sizePolicy4.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label_50, 2, 2, 1, 1)

        self.label3_D = QLabel(self.frame_11)
        self.label3_D.setObjectName(u"label3_D")
        sizePolicy4.setHeightForWidth(self.label3_D.sizePolicy().hasHeightForWidth())
        self.label3_D.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label3_D, 2, 1, 1, 1)

        self.label_46 = QLabel(self.frame_11)
        self.label_46.setObjectName(u"label_46")
        sizePolicy4.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label_46, 0, 2, 1, 1)

        self.label_47 = QLabel(self.frame_11)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_16.addWidget(self.label_47, 1, 0, 1, 1)

        self.label_45 = QLabel(self.frame_11)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_16.addWidget(self.label_45, 0, 0, 1, 1)

        self.label3_V = QLabel(self.frame_11)
        self.label3_V.setObjectName(u"label3_V")
        sizePolicy4.setHeightForWidth(self.label3_V.sizePolicy().hasHeightForWidth())
        self.label3_V.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label3_V, 1, 1, 1, 1)

        self.label3_H = QLabel(self.frame_11)
        self.label3_H.setObjectName(u"label3_H")
        sizePolicy4.setHeightForWidth(self.label3_H.sizePolicy().hasHeightForWidth())
        self.label3_H.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label3_H, 0, 1, 1, 1)

        self.label_49 = QLabel(self.frame_11)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_16.addWidget(self.label_49, 2, 0, 1, 1)

        self.label3_HError = QLabel(self.frame_11)
        self.label3_HError.setObjectName(u"label3_HError")

        self.gridLayout_16.addWidget(self.label3_HError, 0, 4, 1, 1)

        self.label3_VError = QLabel(self.frame_11)
        self.label3_VError.setObjectName(u"label3_VError")

        self.gridLayout_16.addWidget(self.label3_VError, 1, 4, 1, 1)

        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        sizePolicy4.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy4)

        self.gridLayout_16.addWidget(self.label_48, 1, 2, 1, 1)

        self.label3_DError = QLabel(self.frame_11)
        self.label3_DError.setObjectName(u"label3_DError")

        self.gridLayout_16.addWidget(self.label3_DError, 2, 4, 1, 1)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_16.addWidget(self.label_14, 0, 3, 1, 1)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_16.addWidget(self.label_15, 1, 3, 1, 1)

        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_16.addWidget(self.label_16, 2, 3, 1, 1)


        self.gridLayout_9.addWidget(self.frame_11, 1, 0, 1, 1)

        self.btn_runStep3 = QPushButton(self.groupBox_3)
        self.btn_runStep3.setObjectName(u"btn_runStep3")
        self.btn_runStep3.setMinimumSize(QSize(0, 30))
        self.btn_runStep3.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_9.addWidget(self.btn_runStep3, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.statistic)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_7 = QFrame(self.groupBox_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_7)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(20, -1, 20, -1)
        self.label4_1_1 = QLabel(self.frame_7)
        self.label4_1_1.setObjectName(u"label4_1_1")

        self.gridLayout_20.addWidget(self.label4_1_1, 0, 0, 1, 1)

        self.label4_1_2 = QLabel(self.frame_7)
        self.label4_1_2.setObjectName(u"label4_1_2")
        self.label4_1_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_20.addWidget(self.label4_1_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label4_2_1 = QLabel(self.frame_7)
        self.label4_2_1.setObjectName(u"label4_2_1")

        self.gridLayout_20.addWidget(self.label4_2_1, 1, 0, 1, 1)

        self.label4_2_2 = QLabel(self.frame_7)
        self.label4_2_2.setObjectName(u"label4_2_2")
        self.label4_2_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_20.addWidget(self.label4_2_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label4_3 = QLabel(self.frame_7)
        self.label4_3.setObjectName(u"label4_3")
        self.label4_3.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_20.addWidget(self.label4_3, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_20.addWidget(self.label_25, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.groupBox_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(20, -1, 20, -1)
        self.label_59 = QLabel(self.frame_12)
        self.label_59.setObjectName(u"label_59")
        sizePolicy4.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label_59, 2, 2, 1, 1)

        self.label4_VError = QLabel(self.frame_12)
        self.label4_VError.setObjectName(u"label4_VError")

        self.gridLayout_17.addWidget(self.label4_VError, 1, 4, 1, 1)

        self.label_58 = QLabel(self.frame_12)
        self.label_58.setObjectName(u"label_58")
        sizePolicy4.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label_58, 1, 2, 1, 1)

        self.label_54 = QLabel(self.frame_12)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_17.addWidget(self.label_54, 0, 0, 1, 1)

        self.label4_D = QLabel(self.frame_12)
        self.label4_D.setObjectName(u"label4_D")
        sizePolicy4.setHeightForWidth(self.label4_D.sizePolicy().hasHeightForWidth())
        self.label4_D.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label4_D, 2, 1, 1, 1)

        self.label_55 = QLabel(self.frame_12)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_17.addWidget(self.label_55, 1, 0, 1, 1)

        self.label4_H = QLabel(self.frame_12)
        self.label4_H.setObjectName(u"label4_H")
        sizePolicy4.setHeightForWidth(self.label4_H.sizePolicy().hasHeightForWidth())
        self.label4_H.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label4_H, 0, 1, 1, 1)

        self.label4_HError = QLabel(self.frame_12)
        self.label4_HError.setObjectName(u"label4_HError")

        self.gridLayout_17.addWidget(self.label4_HError, 0, 4, 1, 1)

        self.label4_V = QLabel(self.frame_12)
        self.label4_V.setObjectName(u"label4_V")
        sizePolicy4.setHeightForWidth(self.label4_V.sizePolicy().hasHeightForWidth())
        self.label4_V.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label4_V, 1, 1, 1, 1)

        self.label_56 = QLabel(self.frame_12)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_17.addWidget(self.label_56, 2, 0, 1, 1)

        self.label_57 = QLabel(self.frame_12)
        self.label_57.setObjectName(u"label_57")
        sizePolicy4.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy4)

        self.gridLayout_17.addWidget(self.label_57, 0, 2, 1, 1)

        self.label4_DError = QLabel(self.frame_12)
        self.label4_DError.setObjectName(u"label4_DError")

        self.gridLayout_17.addWidget(self.label4_DError, 2, 4, 1, 1)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_17.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_17.addWidget(self.label_17, 1, 3, 1, 1)

        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_17.addWidget(self.label_18, 2, 3, 1, 1)


        self.gridLayout_10.addWidget(self.frame_12, 1, 0, 1, 1)

        self.btn_runStep4 = QPushButton(self.groupBox_4)
        self.btn_runStep4.setObjectName(u"btn_runStep4")
        self.btn_runStep4.setMinimumSize(QSize(0, 30))
        self.btn_runStep4.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_10.addWidget(self.btn_runStep4, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.statistic)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_8 = QFrame(self.groupBox_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(64, 71, 84);border-radius: 16px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(20, -1, 20, -1)
        self.label5_1_1 = QLabel(self.frame_8)
        self.label5_1_1.setObjectName(u"label5_1_1")

        self.gridLayout_21.addWidget(self.label5_1_1, 0, 0, 1, 1)

        self.label5_1_2 = QLabel(self.frame_8)
        self.label5_1_2.setObjectName(u"label5_1_2")
        self.label5_1_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_21.addWidget(self.label5_1_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label5_2_1 = QLabel(self.frame_8)
        self.label5_2_1.setObjectName(u"label5_2_1")

        self.gridLayout_21.addWidget(self.label5_2_1, 1, 0, 1, 1)

        self.label5_2_2 = QLabel(self.frame_8)
        self.label5_2_2.setObjectName(u"label5_2_2")
        self.label5_2_2.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_21.addWidget(self.label5_2_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label5_3 = QLabel(self.frame_8)
        self.label5_3.setObjectName(u"label5_3")
        self.label5_3.setStyleSheet(u"font: 14pt \"\u6977\u4f53\";\n"
"text-decoration: underline;")

        self.gridLayout_21.addWidget(self.label5_3, 2, 1, 1, 1, Qt.AlignHCenter)

        self.label_26 = QLabel(self.frame_8)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_21.addWidget(self.label_26, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_8, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.groupBox_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_13)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_62 = QLabel(self.frame_13)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_18.addWidget(self.label_62, 2, 0, 1, 1)

        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_18.addWidget(self.label_19, 0, 3, 1, 1, Qt.AlignRight)

        self.label5_H = QLabel(self.frame_13)
        self.label5_H.setObjectName(u"label5_H")
        sizePolicy4.setHeightForWidth(self.label5_H.sizePolicy().hasHeightForWidth())
        self.label5_H.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label5_H, 0, 1, 1, 1)

        self.label5_VError = QLabel(self.frame_13)
        self.label5_VError.setObjectName(u"label5_VError")

        self.gridLayout_18.addWidget(self.label5_VError, 1, 4, 1, 1)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_18.addWidget(self.label_20, 1, 3, 1, 1, Qt.AlignRight)

        self.label5_DError = QLabel(self.frame_13)
        self.label5_DError.setObjectName(u"label5_DError")

        self.gridLayout_18.addWidget(self.label5_DError, 2, 4, 1, 1)

        self.label_61 = QLabel(self.frame_13)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_18.addWidget(self.label_61, 1, 0, 1, 1)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_18.addWidget(self.label_21, 2, 3, 1, 1, Qt.AlignRight)

        self.label5_V = QLabel(self.frame_13)
        self.label5_V.setObjectName(u"label5_V")
        sizePolicy4.setHeightForWidth(self.label5_V.sizePolicy().hasHeightForWidth())
        self.label5_V.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label5_V, 1, 1, 1, 1)

        self.label_60 = QLabel(self.frame_13)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_18.addWidget(self.label_60, 0, 0, 1, 1)

        self.label5_D = QLabel(self.frame_13)
        self.label5_D.setObjectName(u"label5_D")
        sizePolicy4.setHeightForWidth(self.label5_D.sizePolicy().hasHeightForWidth())
        self.label5_D.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label5_D, 2, 1, 1, 1)

        self.label5_HError = QLabel(self.frame_13)
        self.label5_HError.setObjectName(u"label5_HError")

        self.gridLayout_18.addWidget(self.label5_HError, 0, 4, 1, 1)

        self.label_63 = QLabel(self.frame_13)
        self.label_63.setObjectName(u"label_63")
        sizePolicy4.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label_63, 0, 2, 1, 1)

        self.label_64 = QLabel(self.frame_13)
        self.label_64.setObjectName(u"label_64")
        sizePolicy4.setHeightForWidth(self.label_64.sizePolicy().hasHeightForWidth())
        self.label_64.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label_64, 1, 2, 1, 1)

        self.label_65 = QLabel(self.frame_13)
        self.label_65.setObjectName(u"label_65")
        sizePolicy4.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.label_65, 2, 2, 1, 1)


        self.gridLayout_11.addWidget(self.frame_13, 1, 0, 1, 1)

        self.btn_runStep5 = QPushButton(self.groupBox_5)
        self.btn_runStep5.setObjectName(u"btn_runStep5")
        self.btn_runStep5.setMinimumSize(QSize(0, 30))
        self.btn_runStep5.setStyleSheet(u"background-color: rgb(64, 71, 84);")

        self.gridLayout_11.addWidget(self.btn_runStep5, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBox_5)

        self.stackedWidget.addWidget(self.statistic)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        sizePolicy7.setHeightForWidth(self.contentSettings.sizePolicy().hasHeightForWidth())
        self.contentSettings.setSizePolicy(sizePolicy7)
        self.contentSettings.setMinimumSize(QSize(0, 0))
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 20, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.topMenus.sizePolicy().hasHeightForWidth())
        self.topMenus.setSizePolicy(sizePolicy10)
        self.topMenus.setMinimumSize(QSize(0, 0))
        self.topMenus.setStyleSheet(u"QComboBox::down-arrow { color: white; }")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.topMenus)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(20, 10, 20, -1)
        self.setIPLEdit = QLineEdit(self.topMenus)
        self.setIPLEdit.setObjectName(u"setIPLEdit")
        sizePolicy8.setHeightForWidth(self.setIPLEdit.sizePolicy().hasHeightForWidth())
        self.setIPLEdit.setSizePolicy(sizePolicy8)
        self.setIPLEdit.setMinimumSize(QSize(0, 34))

        self.gridLayout.addWidget(self.setIPLEdit, 0, 1, 1, 2)

        self.setIPLabel = QLabel(self.topMenus)
        self.setIPLabel.setObjectName(u"setIPLabel")
        sizePolicy6.setHeightForWidth(self.setIPLabel.sizePolicy().hasHeightForWidth())
        self.setIPLabel.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.setIPLabel, 0, 0, 1, 1)

        self.resolutionBox = QComboBox(self.topMenus)
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.addItem("")
        self.resolutionBox.setObjectName(u"resolutionBox")
        sizePolicy8.setHeightForWidth(self.resolutionBox.sizePolicy().hasHeightForWidth())
        self.resolutionBox.setSizePolicy(sizePolicy8)
        self.resolutionBox.setStyleSheet(u"QComboBox::down-arrow {\n"
"	color: rgb(85, 255, 255);\n"
"}")

        self.gridLayout.addWidget(self.resolutionBox, 5, 1, 1, 3)

        self.CLinkBtn_Right = QCommandLinkButton(self.topMenus)
        self.CLinkBtn_Right.setObjectName(u"CLinkBtn_Right")
        sizePolicy8.setHeightForWidth(self.CLinkBtn_Right.sizePolicy().hasHeightForWidth())
        self.CLinkBtn_Right.setSizePolicy(sizePolicy8)
        self.CLinkBtn_Right.setStyleSheet(u"font: 10pt \"\u9ed1\u4f53\";")
        icon10 = QIcon()
        icon10.addFile(u":/icons/static/icons/cil-hand-point-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CLinkBtn_Right.setIcon(icon10)

        self.gridLayout.addWidget(self.CLinkBtn_Right, 7, 2, 1, 2)

        self.groupBox_6 = QGroupBox(self.topMenus)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy3.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy3)
        self.groupBox_6.setMinimumSize(QSize(0, 360))
        self.groupBox_6.setStyleSheet(u"background-color: rgb(33, 37, 43);border-radius:10px;")
        self.gridLayout_22 = QGridLayout(self.groupBox_6)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(16, -1, 16, -1)
        self.label_inputVoltage = QLabel(self.groupBox_6)
        self.label_inputVoltage.setObjectName(u"label_inputVoltage")
        self.label_inputVoltage.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_inputVoltage, 2, 1, 1, 1)

        self.label_27 = QLabel(self.groupBox_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_27, 1, 0, 1, 1)

        self.lcd_battery = QLCDNumber(self.groupBox_6)
        self.lcd_battery.setObjectName(u"lcd_battery")
        self.lcd_battery.setStyleSheet(u"background-color: rgb(44, 49, 58);")
        self.lcd_battery.setDigitCount(3)
        self.lcd_battery.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_battery.setProperty("intValue", 100)

        self.gridLayout_22.addWidget(self.lcd_battery, 0, 0, 1, 2)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_31, 4, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_6)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_32, 2, 0, 1, 1)

        self.label_chargeStatus = QLabel(self.groupBox_6)
        self.label_chargeStatus.setObjectName(u"label_chargeStatus")
        self.label_chargeStatus.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_chargeStatus, 4, 1, 1, 1)

        self.label_batteryVoltage = QLabel(self.groupBox_6)
        self.label_batteryVoltage.setObjectName(u"label_batteryVoltage")
        self.label_batteryVoltage.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_batteryVoltage, 1, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox_6)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_33, 5, 0, 1, 1)

        self.label_timeRemaining = QLabel(self.groupBox_6)
        self.label_timeRemaining.setObjectName(u"label_timeRemaining")
        self.label_timeRemaining.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";")

        self.gridLayout_22.addWidget(self.label_timeRemaining, 5, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 9, 0, 1, 4)

        self.resolutionLabel = QLabel(self.topMenus)
        self.resolutionLabel.setObjectName(u"resolutionLabel")
        sizePolicy6.setHeightForWidth(self.resolutionLabel.sizePolicy().hasHeightForWidth())
        self.resolutionLabel.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.resolutionLabel, 5, 0, 1, 1)

        self.CLinkBtn_Left = QCommandLinkButton(self.topMenus)
        self.CLinkBtn_Left.setObjectName(u"CLinkBtn_Left")
        sizePolicy8.setHeightForWidth(self.CLinkBtn_Left.sizePolicy().hasHeightForWidth())
        self.CLinkBtn_Left.setSizePolicy(sizePolicy8)
        self.CLinkBtn_Left.setStyleSheet(u"font: 10pt \"\u9ed1\u4f53\";")
        icon11 = QIcon()
        icon11.addFile(u":/icons/static/icons/cil-hand-point-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CLinkBtn_Left.setIcon(icon11)

        self.gridLayout.addWidget(self.CLinkBtn_Left, 7, 0, 1, 2)

        self.setIPBtn = QPushButton(self.topMenus)
        self.setIPBtn.setObjectName(u"setIPBtn")
        sizePolicy6.setHeightForWidth(self.setIPBtn.sizePolicy().hasHeightForWidth())
        self.setIPBtn.setSizePolicy(sizePolicy6)
        self.setIPBtn.setMinimumSize(QSize(0, 34))
        self.setIPBtn.setLayoutDirection(Qt.LeftToRight)
        self.setIPBtn.setStyleSheet(u"text-align: center; /* \u5c06\u6587\u672c\u5c45\u4e2d */\n"
"border: none; /* \u53bb\u9664\u8fb9\u6846 */\n"
"padding: 0px; /* \u53bb\u9664\u5185\u8fb9\u8ddd */\n"
"background-image: url(:/icons/static/icons/cil-paper-plane.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius: 6px;")
        self.setIPBtn.setIconSize(QSize(0, 0))

        self.gridLayout.addWidget(self.setIPBtn, 0, 3, 1, 1)


        self.verticalLayout_15.addWidget(self.topMenus)


        self.verticalLayout_14.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_10.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.statusLabel = QLabel(self.bottomBar)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMaximumSize(QSize(16777215, 16))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setBold(False)
        font7.setItalic(False)
        self.statusLabel.setFont(font7)
        self.statusLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.statusLabel)

        self.versionLabel = QLabel(self.bottomBar)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.versionLabel)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setCursor(QCursor(Qt.SizeFDiagCursor))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/icons/static/icons/size.png)")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_10.addWidget(self.bottomBar)


        self.verticalLayout_9.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"1900200327\u5434\u4f69\u94a6", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u89c9\u5b9a\u4f4d\u7cfb\u7edf(for\u6bd5\u8bbe)", None))
#if QT_CONFIG(tooltip)
        self.toggleButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u5c55\u5f00", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.toggleButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
#if QT_CONFIG(tooltip)
        self.btn_camera.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_camera.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
#if QT_CONFIG(tooltip)
        self.btn_image.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247", None))
#if QT_CONFIG(tooltip)
        self.btn_liucheng.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_liucheng.setText(QCoreApplication.translate("MainWindow", u"\u6d41\u7a0b", None))
#if QT_CONFIG(tooltip)
        self.btn_statistic.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_statistic.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1", None))
#if QT_CONFIG(tooltip)
        self.btn_exit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.toggleLeftBox.setText("")
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.CBox_suffix.setToolTip(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u5219\u4e3a\u4fdd\u5b58\u56fe\u50cf\u4e0d\u8986\u76d6", None))
#endif // QT_CONFIG(tooltip)
        self.CBox_suffix.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u8986\u76d6\u4e4b\u524d\u7684\u56fe\u7247", None))
        self.LEdit_savePath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./images", None))
#if QT_CONFIG(tooltip)
        self.TButton_savePath.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.TButton_savePath.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_savePath.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u4fdd\u5b58\u8def\u5f84", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u76f8\u673a\u56fe\u7247", None))
        self.CBox_chooseSaveImage.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u76f8\u673a\u56fe\u7247", None))
        self.CBox_chooseSaveImage.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4ec5\u5de6\u76f8\u673a\u56fe\u7247", None))
        self.CBox_chooseSaveImage.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4ec5\u53f3\u76f8\u673a\u56fe\u7247", None))
        self.CBox_chooseSaveImage.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5de6\u53f3\u5206\u4f53\u4fdd\u5b58", None))
        self.CBox_chooseSaveImage.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5de6\u53f3\u5408\u4f53\u4fdd\u5b58", None))

        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5", None))
        self.LEdit_V.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_feature.setToolTip(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
#endif // QT_CONFIG(tooltip)
        self.label_feature.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb", None))
        self.label_matchRatio.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u6bd4\u7387\u503c", None))
        self.LEdit_D.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2", None))
        self.label_matchDeadline.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c11\u5339\u914d\u70b9", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2", None))
        self.LEdit_H.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u9608\u503c", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u70b9\u63d0\u53d6\u9608\u503c", None))
#if QT_CONFIG(tooltip)
        self.DSBox_matchRatio.setToolTip(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u6bd4\u7387\u503c", None))
#endif // QT_CONFIG(tooltip)
        self.DSBox_matchRatio.setPrefix("")
        self.DSBox_matchRatio.setSuffix("")
        self.CBox_feature.setItemText(0, QCoreApplication.translate("MainWindow", u"SIFT\u7b97\u6cd5", None))
        self.CBox_feature.setItemText(1, QCoreApplication.translate("MainWindow", u"SURF\u7b97\u6cd5", None))
        self.CBox_feature.setItemText(2, QCoreApplication.translate("MainWindow", u"ORB\u7b97\u6cd5", None))
        self.CBox_feature.setItemText(3, QCoreApplication.translate("MainWindow", u"AKAZE\u7b97\u6cd5", None))
        self.CBox_feature.setItemText(4, QCoreApplication.translate("MainWindow", u"SuperGlue\u7b97\u6cd5(\u6df1\u5ea6\u5b66\u4e60)", None))

        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u591a", None))
        self.CBox_showImageFunction.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u56fe\u7247\u5916\u7f6e\u663e\u793a", None))
        self.CBox_showDoubleImage.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u76ee\u56fe\u50cf\u663e\u793a", None))
        self.btn_saveOption.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"## `\u57fa\u4e8e\u56fe\u50cf\u7279\u5f81\u7684\n"
"\u89c6\u89c9\u5b9a\u4f4d\u7cfb\u7edf`\n"
"\n"
"`- \u7279\u5f81\u63d0\u53d6\u7b97\u6cd5\uff1aSIFT\u7b97\u6cd5`\n"
"\n"
"`- \u7279\u5f81\u5339\u914d\u7b97\u6cd5\uff1aFLANN\u5339\u914d`\n"
"\n"
"`- \u89d2\u5ea6\u8ba1\u7b97\u7b97\u6cd5\uff1a\u5355\u5e94\u6027\u77e9\u9635\u8ba1\u7b97`\n"
"\n"
"`- \u8ddd\u79bb\u8ba1\u7b97\u7b97\u6cd5\uff1a\u6b27\u51e0\u91cc\u5f97\u8ddd\u79bb\u8ba1\u7b97`\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u65b9\u6b63\u8212\u4f53'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<h2 align=\"center\" style=\" margin-top:20px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u9ed1\u4f53'; font-size:10pt; font-weight:700; color:#bd93f9;\">\u57fa\u4e8e\u56fe\u50cf\u7279\u5f81\u7684<br />\u89c6\u89c9\u5b9a\u4f4d\u7cfb\u7edf</span></h2>\n"
"<p style=\" margin-top:20px; margin-bottom:12px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u9ed1\u4f53'; font-s"
                        "ize:10pt; font-weight:700; color:#ffffff;\">- \u7279\u5f81\u63d0\u53d6\u7b97\u6cd5\uff1aSIFT\u7b97\u6cd5</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:12px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u9ed1\u4f53'; font-size:10pt; font-weight:700; color:#ffffff;\">- \u7279\u5f81\u5339\u914d\u7b97\u6cd5\uff1aFLANN\u5339\u914d</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:12px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u9ed1\u4f53'; font-size:10pt; font-weight:700; color:#ffffff;\">- \u89d2\u5ea6\u8ba1\u7b97\u7b97\u6cd5\uff1a\u5355\u5e94\u6027\u77e9\u9635\u8ba1\u7b97</span></p>\n"
"<p style=\" margin-top:20px; margin-bottom:12px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'\u9ed1\u4f53'; font-size:10pt; font-weight:700; color:#ffffff;\">- \u8ddd\u79bb\u8ba1\u7b97\u7b97\u6cd5\uff1a\u6b27\u51e0\u91cc\u5f97\u8ddd\u79bb"
                        "\u8ba1\u7b97</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Smart Camera", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5c55\u5f00", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.cameraLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u6253\u5f00\u6444\u50cf\u5934", None))
#if QT_CONFIG(tooltip)
        self.btn_biaoding.setToolTip(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a", None))
#endif // QT_CONFIG(tooltip)
        self.btn_biaoding.setText("")
#if QT_CONFIG(tooltip)
        self.cameraBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934", None))
#endif // QT_CONFIG(tooltip)
        self.cameraBtn.setText("")
#if QT_CONFIG(tooltip)
        self.shutterBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u62cd\u7167", None))
#endif // QT_CONFIG(tooltip)
        self.shutterBtn.setText("")
#if QT_CONFIG(tooltip)
        self.changeCameraBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u6444\u50cf\u5934", None))
#endif // QT_CONFIG(tooltip)
        self.changeCameraBtn.setText("")
#if QT_CONFIG(tooltip)
        self.videoMatchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u8ffd\u8e2a", None))
#endif // QT_CONFIG(tooltip)
        self.videoMatchBtn.setText("")
        self.resultLabel.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u56fe\u7247", None))
        self.addGloadImageBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5168\u5c40\u56fe\u7247", None))
        self.addLocalImageBtn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5c40\u90e8\u56fe\u7247", None))
        self.matchImageBtn.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d", None))
        self.angleImageBtn.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u504f\u79fb\u89d2", None))
        self.calcHDistanceBtn.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u6c34\u5e73\u8ddd\u79bb", None))
        self.label_liucheng.setText(QCoreApplication.translate("MainWindow", u"\u7b97\u6cd5\u6d41\u7a0b\u5c55\u793a", None))
        self.GBox_show.setTitle(QCoreApplication.translate("MainWindow", u"SIFT\u7b97\u6cd5\u6d41\u7a0b", None))
        self.btn_Setp1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6", None))
        self.btn_Setp2.setText(QCoreApplication.translate("MainWindow", u"FLANN\u7279\u5f81\u5339\u914d", None))
        self.btn_Setp3.setText(QCoreApplication.translate("MainWindow", u"RANSAC\u63d0\u9ad8\u7cbe\u51c6", None))
        self.btn_Setp4.setText(QCoreApplication.translate("MainWindow", u"\u6839\u636e\u5355\u5e94\u6027\u77e9\u9635\u8ba1\u7b97\u504f\u79fb\u89d2", None))
        self.btn_Setp5.setText(QCoreApplication.translate("MainWindow", u"\u6839\u636e\u6df1\u5ea6\u56fe\u8ba1\u7b97\u6c34\u5e73\u76f4\u7ebf\u8ddd\u79bb", None))
        self.label_globalImgSize.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c40\u56fe\u50cf\u5c3a\u5bf8\uff1a640x480", None))
        self.label_localImgSize.setText(QCoreApplication.translate("MainWindow", u"\u5c40\u90e8\u56fe\u50cf\u5c3a\u5bf8\uff1a640x480", None))
        self.label_featureExtraction.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5\uff1aSIFT\u7b97\u6cd5", None))
        self.label_featureMatch.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u7b97\u6cd5\uff1aFLANN\u7b97\u6cd5", None))
        self.label_matchPoints.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label_timeCount.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.label_HDistanceError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
#if QT_CONFIG(tooltip)
        self.TButton_HDistanceError.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5b9e\u9645\u6c34\u5e73\u76f4\u7ebf\u8ddd\u79bb", None))
#endif // QT_CONFIG(tooltip)
        self.TButton_HDistanceError.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_HOffset.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_VOffset.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u76f4\u7ebf\u8ddd\u79bb\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2\u5ea6\uff1a", None))
        self.label_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2\u5ea6\uff1a", None))
#if QT_CONFIG(tooltip)
        self.TButton_calcHError.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5b9e\u9645\u6c34\u5e73\u504f\u79fb\u89d2\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.TButton_calcHError.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.TButton_HError.setToolTip(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u5b9e\u9645\u5782\u76f4\u504f\u79fb\u89d2\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.TButton_HError.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_HDistance.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.btn_runStep.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"SIFT\u7b97\u6cd5", None))
        self.label1_2_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label1_1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\uff1a", None))
        self.label1_3.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u597d", None))
        self.label1_2_1.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.label1_1_1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label1_DError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb:", None))
        self.label1_H.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label1_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label1_D.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2:", None))
        self.label1_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label1_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.btn_runStep1.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"SURF\u7b97\u6cd5", None))
        self.label2_3.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u597d", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\uff1a", None))
        self.label2_2_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label2_1_1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label2_1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label2_2_1.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.btn_runStep2.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.label2_D.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label2_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label2_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2:", None))
        self.label2_H.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label2_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label2_DError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"ORB\u7b97\u6cd5", None))
        self.label3_1_1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label3_1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label3_2_1.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.label3_2_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label3_3.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u597d", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\uff1a", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label3_D.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2:", None))
        self.label3_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label3_H.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb:", None))
        self.label3_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label3_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label3_DError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.btn_runStep3.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"AKAZE\u7b97\u6cd5", None))
        self.label4_1_1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label4_1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label4_2_1.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.label4_2_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label4_3.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u597d", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\uff1a", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.label4_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2:", None))
        self.label4_D.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2:", None))
        self.label4_H.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label4_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label4_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label4_DError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.btn_runStep4.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"SuperGlue\u7b97\u6cd5(\u6df1\u5ea6\u5b66\u4e60)", None))
        self.label5_1_1.setText(QCoreApplication.translate("MainWindow", u"\u7279\u5f81\u5339\u914d\u70b9\uff1a0/0", None))
        self.label5_1_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label5_2_1.setText(QCoreApplication.translate("MainWindow", u"\u8017\u65f6\uff1a0s", None))
        self.label5_2_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label5_3.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u597d", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\uff1a", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u7ebf\u8ddd\u79bb:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label5_H.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label5_VError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label5_DError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb\u89d2:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label5_V.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5e73\u504f\u79fb\u89d2:", None))
        self.label5_D.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label5_HError.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u00b0", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"px", None))
        self.btn_runStep5.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u6267\u884c", None))
        self.setIPLabel.setText(QCoreApplication.translate("MainWindow", u"\u6811\u8393\u6d3eIP", None))
        self.resolutionBox.setItemText(0, QCoreApplication.translate("MainWindow", u"640x480", None))
        self.resolutionBox.setItemText(1, QCoreApplication.translate("MainWindow", u"800x600", None))
        self.resolutionBox.setItemText(2, QCoreApplication.translate("MainWindow", u"1280*720", None))
        self.resolutionBox.setItemText(3, QCoreApplication.translate("MainWindow", u"1920*1080", None))

        self.CLinkBtn_Right.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u8bbf\u95ee", None))
        self.CLinkBtn_Right.setDescription(QCoreApplication.translate("MainWindow", u"\u53f3\u6444\u50cf\u5934", None))
        self.groupBox_6.setTitle("")
        self.label_inputVoltage.setText(QCoreApplication.translate("MainWindow", u"5V", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6c60\u7535\u538b\uff1a", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u5145\u7535\u72b6\u6001\uff1a", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7535\u538b\uff1a", None))
        self.label_chargeStatus.setText(QCoreApplication.translate("MainWindow", u"Charging Done", None))
        self.label_batteryVoltage.setText(QCoreApplication.translate("MainWindow", u"4.2V", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u9884\u8ba1\u5269\u4f59\uff1a", None))
        self.label_timeRemaining.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.resolutionLabel.setText(QCoreApplication.translate("MainWindow", u"\u5206\u8fa8\u7387", None))
        self.CLinkBtn_Left.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u8bbf\u95ee", None))
        self.CLinkBtn_Left.setDescription(QCoreApplication.translate("MainWindow", u"\u5de6\u6444\u50cf\u5934", None))
        self.setIPBtn.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"webCameraIP:192.168.0.1", None))
        self.versionLabel.setText(QCoreApplication.translate("MainWindow", u"by:1900200327\u5434\u4f69\u94a6     v1.9.0", None))
    # retranslateUi

