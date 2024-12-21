# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.topmenu_container = QWidget(self.centralwidget)
        self.topmenu_container.setObjectName(u"topmenu_container")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topmenu_container.sizePolicy().hasHeightForWidth())
        self.topmenu_container.setSizePolicy(sizePolicy)
        self.topmenu_container.setStyleSheet(u"background-color: rgb(181, 181, 181);")
        self.horizontalLayout_9 = QHBoxLayout(self.topmenu_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_4 = QWidget(self.topmenu_container)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/icons/floppy-disks.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon1 = QIcon()
        icon1.addFile(u":/icons/gear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(898, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon()
        icon2.addFile(u":/icons/people.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)
        self.pushButton_4.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.widget_4)

        self.tabWidget = QTabWidget(self.topmenu_container)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setIconSize(QSize(25, 20))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.Home_tab = QWidget()
        self.Home_tab.setObjectName(u"Home_tab")
        self.Home_Button = QPushButton(self.Home_tab)
        self.Home_Button.setObjectName(u"Home_Button")
        self.Home_Button.setGeometry(QRect(10, 10, 57, 58))
        icon3 = QIcon()
        icon3.addFile(u":/icons/home (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Home_Button.setIcon(icon3)
        self.Home_Button.setIconSize(QSize(45, 50))
        self.Home_Button.setCheckable(True)
        self.Home_Button.setAutoExclusive(True)
        self.Home_Button.setFlat(True)
        self.layoutWidget_2 = QWidget(self.Home_tab)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(90, 10, 78, 69))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.DB_Button = QPushButton(self.layoutWidget_2)
        self.DB_Button.setObjectName(u"DB_Button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/database.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DB_Button.setIcon(icon4)
        self.DB_Button.setIconSize(QSize(40, 35))
        self.DB_Button.setCheckable(True)
        self.DB_Button.setAutoExclusive(True)
        self.DB_Button.setFlat(True)

        self.verticalLayout_9.addWidget(self.DB_Button)

        self.comboBox = QComboBox(self.layoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_9.addWidget(self.comboBox)

        self.tabWidget.addTab(self.Home_tab, "")
        self.Mode_tab = QWidget()
        self.Mode_tab.setObjectName(u"Mode_tab")
        self.verticalLayout_2 = QVBoxLayout(self.Mode_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_view_Button = QPushButton(self.Mode_tab)
        self.table_view_Button.setObjectName(u"table_view_Button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.table_view_Button.setIcon(icon5)
        self.table_view_Button.setIconSize(QSize(45, 50))
        self.table_view_Button.setCheckable(True)
        self.table_view_Button.setAutoExclusive(True)
        self.table_view_Button.setFlat(True)

        self.horizontalLayout.addWidget(self.table_view_Button)

        self.horizontalSpacer = QSpacerItem(938, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.Mode_tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mode_tab), u"Mode")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout_9.addLayout(self.verticalLayout)


        self.verticalLayout_7.addWidget(self.topmenu_container)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setStyleSheet(u"background-color: rgb(181, 181, 181);")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.widget_3)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 116, 380))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer)

        self.horizontalSpacer_4 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setStyleSheet(u"background-color: rgb(181, 181, 181);")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setFlat(True)

        self.verticalLayout_4.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(17, 498, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_8.addWidget(self.widget_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.stackedWidget.addWidget(self.Dashboard)
        self.table_view_page = QWidget()
        self.table_view_page.setObjectName(u"table_view_page")
        self.horizontalLayout_7 = QHBoxLayout(self.table_view_page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(651, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.stackedWidget.addWidget(self.table_view_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.widget)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.toggled.connect(self.widget_3.setVisible)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.Home_Button.setText("")
        self.DB_Button.setText("")
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"DataBase", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CSV", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Excel", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home_tab), QCoreApplication.translate("MainWindow", u"Home ", None))
        self.table_view_Button.setText("")
        self.pushButton.setText("")
    # retranslateUi

