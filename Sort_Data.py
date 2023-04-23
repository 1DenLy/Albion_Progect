
import json
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup



#import Main_Code, List_item


Item_sort_list = []
City_dict = {}
sell_price_min_dict = {}
sell_price_max_dict = {}
buy_price_min_dict = {}
buy_price_max_dict = {}
locations = ['Caerleon','Fort Sterling','Lymhurst','Thetford','Martlock','Bridgewatch']

class Item():
    def __init__(self, item_id, city, 
                 sell_price_min=None, sell_price_min_date=None, 
                 sell_price_max=None, sell_price_max_date=None, 
                 buy_price_min=None, buy_price_min_date=None, 
                 buy_price_max=None, buy_price_max_date=None):
        
        # устанавливаем значения атрибутов при создании экземпляра класса
        self.item_id = item_id
        self.city = city

        # обрабатываем переменные с припиской "date"
        sell_price_min_date = self.format_datetime(sell_price_min_date)
        sell_price_max_date = self.format_datetime(sell_price_max_date)
        buy_price_min_date = self.format_datetime(buy_price_min_date)
        buy_price_max_date = self.format_datetime(buy_price_max_date)
        
        # используем условное выражение одной строкой для проверки на None
        self.sell_price_min = str(sell_price_min) if sell_price_min is not None else '------'
        self.sell_price_min_date = sell_price_min_date if sell_price_min_date is not None else '------'
        self.sell_price_max = str(sell_price_max) if sell_price_max is not None else '------'
        self.sell_price_max_date = sell_price_max_date if sell_price_max_date is not None else '------'
        self.buy_price_min = str(buy_price_min) if buy_price_min is not None else '------'
        self.buy_price_min_date = buy_price_min_date if buy_price_min_date is not None else '------'
        self.buy_price_max = str(buy_price_max) if buy_price_max is not None else '------'
        self.buy_price_max_date = buy_price_max_date if buy_price_max_date is not None else '------'


    def format_datetime(self, dt):
        today = datetime.now()

        if dt is not None:
            # Преобразуем строку dt в объект datetime.datetime
            dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')

            if dt.year == today.year:
                
                end = dt.strftime("%m-%dT%H:%M")
            
                if dt.month == today.month:

                    end = dt.strftime("%dT%H:%M")

                    if dt.day == today.day:

                        end = dt.strftime("%H:%M")
            else:
                end = str(dt)
        else:
            end = None

        return end

    def AddItem(self, Add_list: list):
        Add_list.append(self)


    def Item_in_listes(path: str):
        global Item_sort_list
        # Очищаем список перед добавлением новых элементов
        Item_sort_list.clear()

        try:
            # Открываем JSON файл и загружаем данные
            with open(path, 'r') as opened_file:
                datas = json.load(opened_file)

                for i in range(len(datas['item_id'])):
                    i = str(i)

                    # Создаем экземпляр Item для каждого элемента в файле
                    Generated_item = Item(datas['item_id'][i], 
                                datas['city'][i], 
                                datas['sell_price_min'][i], 
                                datas['sell_price_min_date'][i], 
                                datas['sell_price_max'][i], 
                                datas['sell_price_max_date'][i], 
                                datas['buy_price_min'][i], 
                                datas['buy_price_min_date'][i], 
                                datas['buy_price_max'][i], 
                                datas['buy_price_max_date'][i])
                    # Добавляем элемент в список
                    Generated_item.AddItem(Item_sort_list)
        
        except (IOError, ValueError, KeyError) as element:
            print(f'An error occured while reading the JSON file: {element}')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_List = QtWidgets.QListWidget(self.centralwidget)
        self.Main_List.setGeometry(QtCore.QRect(10, 10, 230, 480))
        self.Main_List.setObjectName("Main_List")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 500, 230, 140))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_Quality_S = QtWidgets.QComboBox(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Quality_S.setFont(font)
        self.comboBox_Quality_S.setObjectName("comboBox_Quality_S")
        self.comboBox_Quality_S.addItem("")
        self.comboBox_Quality_S.addItem("")
        self.comboBox_Quality_S.addItem("")
        self.comboBox_Quality_S.addItem("")
        self.comboBox_Quality_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Quality_S, 1, 2, 1, 1)
        self.Text_lable = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Text_lable.setFont(font)
        self.Text_lable.setObjectName("Text_lable")
        self.gridLayout_2.addWidget(self.Text_lable, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.comboBox_Tier_S = QtWidgets.QComboBox(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Tier_S.setFont(font)
        self.comboBox_Tier_S.setObjectName("comboBox_Tier_S")
        self.comboBox_Tier_S.addItem("")
        self.comboBox_Tier_S.addItem("")
        self.comboBox_Tier_S.addItem("")
        self.comboBox_Tier_S.addItem("")
        self.comboBox_Tier_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Tier_S, 1, 0, 1, 1)
        self.comboBox_Rarity_S = QtWidgets.QComboBox(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_Rarity_S.setFont(font)
        self.comboBox_Rarity_S.setObjectName("comboBox_Rarity_S")
        self.comboBox_Rarity_S.addItem("")
        self.comboBox_Rarity_S.addItem("")
        self.comboBox_Rarity_S.addItem("")
        self.comboBox_Rarity_S.addItem("")
        self.comboBox_Rarity_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Rarity_S, 1, 1, 1, 1)
        self.radioButtonArmo = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonArmo.setFont(font)
        self.radioButtonArmo.setObjectName("radioButtonArmo")
        self.gridLayout_2.addWidget(self.radioButtonArmo, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.radioButton_Resurses = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_Resurses.setFont(font)
        self.radioButton_Resurses.setObjectName("radioButton_Resurses")
        self.gridLayout_2.addWidget(self.radioButton_Resurses, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.radioButton_Thinks = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_Thinks.setFont(font)
        self.radioButton_Thinks.setObjectName("radioButton_Thinks")
        self.gridLayout_2.addWidget(self.radioButton_Thinks, 2, 1, 1, 1)
        self.comboBox_S = QtWidgets.QComboBox(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_S.setFont(font)
        self.comboBox_S.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.comboBox_S.setObjectName("comboBox_S")
        self.comboBox_S.addItem("")
        self.comboBox_S.addItem("")
        self.comboBox_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_S, 3, 0, 1, 3)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setGeometry(QtCore.QRect(250, 10, 840, 630))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_0 = QtWidgets.QLabel(self.verticalFrame)
        self.label_0.setMaximumSize(QtCore.QSize(65, 65))
        self.label_0.setText("")
        self.label_0.setObjectName("label_0")
        self.horizontalLayout.addWidget(self.label_0)
        self.label_Black_Market = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Black_Market.setFont(font)
        self.label_Black_Market.setObjectName("label_Black_Market")
        self.horizontalLayout.addWidget(self.label_Black_Market, 0, QtCore.Qt.AlignHCenter)
        self.label_Carleon = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Carleon.setFont(font)
        self.label_Carleon.setObjectName("label_Carleon")
        self.horizontalLayout.addWidget(self.label_Carleon, 0, QtCore.Qt.AlignHCenter)
        self.label_Fort_Stearling = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Fort_Stearling.setFont(font)
        self.label_Fort_Stearling.setObjectName("label_Fort_Stearling")
        self.horizontalLayout.addWidget(self.label_Fort_Stearling, 0, QtCore.Qt.AlignHCenter)
        self.label_Lymhyrst = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Lymhyrst.setFont(font)
        self.label_Lymhyrst.setObjectName("label_Lymhyrst")
        self.horizontalLayout.addWidget(self.label_Lymhyrst, 0, QtCore.Qt.AlignHCenter)
        self.label_Thetford = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Thetford.setFont(font)
        self.label_Thetford.setObjectName("label_Thetford")
        self.horizontalLayout.addWidget(self.label_Thetford, 0, QtCore.Qt.AlignHCenter)
        self.label_Martlock = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Martlock.setFont(font)
        self.label_Martlock.setObjectName("label_Martlock")
        self.horizontalLayout.addWidget(self.label_Martlock, 0, QtCore.Qt.AlignHCenter)
        self.label_Bridgewatch = QtWidgets.QLabel(self.verticalFrame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Bridgewatch.setFont(font)
        self.label_Bridgewatch.setObjectName("label_Bridgewatch")
        self.horizontalLayout.addWidget(self.label_Bridgewatch, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_Min_Sell = QtWidgets.QLabel(self.verticalFrame)
        self.label_Min_Sell.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_Min_Sell.setFont(font)
        self.label_Min_Sell.setTabletTracking(False)
        self.label_Min_Sell.setObjectName("label_Min_Sell")
        self.verticalLayout.addWidget(self.label_Min_Sell)
        self.label_Min_Sell_D = QtWidgets.QLabel(self.verticalFrame)
        self.label_Min_Sell_D.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Min_Sell_D.setFont(font)
        self.label_Min_Sell_D.setObjectName("label_Min_Sell_D")
        self.verticalLayout.addWidget(self.label_Min_Sell_D)
        self.label_Max_Sell = QtWidgets.QLabel(self.verticalFrame)
        self.label_Max_Sell.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Max_Sell.setFont(font)
        self.label_Max_Sell.setObjectName("label_Max_Sell")
        self.verticalLayout.addWidget(self.label_Max_Sell)
        self.label_Max_Sell_D = QtWidgets.QLabel(self.verticalFrame)
        self.label_Max_Sell_D.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Max_Sell_D.setFont(font)
        self.label_Max_Sell_D.setObjectName("label_Max_Sell_D")
        self.verticalLayout.addWidget(self.label_Max_Sell_D)
        self.label_Min_Buy = QtWidgets.QLabel(self.verticalFrame)
        self.label_Min_Buy.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Min_Buy.setFont(font)
        self.label_Min_Buy.setObjectName("label_Min_Buy")
        self.verticalLayout.addWidget(self.label_Min_Buy)
        self.label_Min_Buy_D = QtWidgets.QLabel(self.verticalFrame)
        self.label_Min_Buy_D.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Min_Buy_D.setFont(font)
        self.label_Min_Buy_D.setObjectName("label_Min_Buy_D")
        self.verticalLayout.addWidget(self.label_Min_Buy_D)
        self.label_Max_Buy = QtWidgets.QLabel(self.verticalFrame)
        self.label_Max_Buy.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Max_Buy.setFont(font)
        self.label_Max_Buy.setObjectName("label_Max_Buy")
        self.verticalLayout.addWidget(self.label_Max_Buy)
        self.label_Max_Buy_D = QtWidgets.QLabel(self.verticalFrame)
        self.label_Max_Buy_D.setMaximumSize(QtCore.QSize(70, 65))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_Max_Buy_D.setFont(font)
        self.label_Max_Buy_D.setObjectName("label_Max_Buy_D")
        self.verticalLayout.addWidget(self.label_Max_Buy_D)
        self.gridFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame1.setGeometry(QtCore.QRect(327, 77, 761, 561))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.gridFrame1.setFont(font)
        self.gridFrame1.setMouseTracking(False)
        self.gridFrame1.setTabletTracking(False)
        self.gridFrame1.setLineWidth(1)
        self.gridFrame1.setObjectName("gridFrame1")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_23 = QtWidgets.QLabel(self.gridFrame1)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(self.gridFrame1)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(self.gridFrame1)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(self.gridFrame1)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridFrame1)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(self.gridFrame1)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_21 = QtWidgets.QLabel(self.gridFrame1)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(self.gridFrame1)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 2, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.gridFrame1)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.gridFrame1)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.gridFrame1)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.gridFrame1)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.gridFrame1)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_1 = QtWidgets.QLabel(self.gridFrame1)
        self.label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.gridFrame1)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.gridFrame1)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(self.gridFrame1)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.gridFrame1)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_29 = QtWidgets.QLabel(self.gridFrame1)
        self.label_29.setMinimumSize(QtCore.QSize(0, 0))
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_43 = QtWidgets.QLabel(self.gridFrame1)
        self.label_43.setMinimumSize(QtCore.QSize(0, 0))
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_50 = QtWidgets.QLabel(self.gridFrame1)
        self.label_50.setMinimumSize(QtCore.QSize(0, 0))
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_36 = QtWidgets.QLabel(self.gridFrame1)
        self.label_36.setMinimumSize(QtCore.QSize(0, 0))
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(self.gridFrame1)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.gridFrame1)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(self.gridFrame1)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.gridFrame1)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.gridFrame1)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_25 = QtWidgets.QLabel(self.gridFrame1)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 3, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_26 = QtWidgets.QLabel(self.gridFrame1)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_27 = QtWidgets.QLabel(self.gridFrame1)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(self.gridFrame1)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_30 = QtWidgets.QLabel(self.gridFrame1)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.gridFrame1)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 3, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_33 = QtWidgets.QLabel(self.gridFrame1)
        self.label_33.setMinimumSize(QtCore.QSize(0, 0))
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_31 = QtWidgets.QLabel(self.gridFrame1)
        self.label_31.setMinimumSize(QtCore.QSize(0, 0))
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_34 = QtWidgets.QLabel(self.gridFrame1)
        self.label_34.setMinimumSize(QtCore.QSize(0, 0))
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 4, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_35 = QtWidgets.QLabel(self.gridFrame1)
        self.label_35.setMinimumSize(QtCore.QSize(0, 0))
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 4, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_32 = QtWidgets.QLabel(self.gridFrame1)
        self.label_32.setMinimumSize(QtCore.QSize(0, 0))
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_37 = QtWidgets.QLabel(self.gridFrame1)
        self.label_37.setMinimumSize(QtCore.QSize(0, 0))
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_40 = QtWidgets.QLabel(self.gridFrame1)
        self.label_40.setMinimumSize(QtCore.QSize(0, 0))
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 5, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_38 = QtWidgets.QLabel(self.gridFrame1)
        self.label_38.setMinimumSize(QtCore.QSize(0, 0))
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_41 = QtWidgets.QLabel(self.gridFrame1)
        self.label_41.setMinimumSize(QtCore.QSize(0, 0))
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 5, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_39 = QtWidgets.QLabel(self.gridFrame1)
        self.label_39.setMinimumSize(QtCore.QSize(0, 0))
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_42 = QtWidgets.QLabel(self.gridFrame1)
        self.label_42.setMinimumSize(QtCore.QSize(0, 0))
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 5, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_45 = QtWidgets.QLabel(self.gridFrame1)
        self.label_45.setMinimumSize(QtCore.QSize(0, 0))
        self.label_45.setObjectName("label_45")
        self.gridLayout.addWidget(self.label_45, 6, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_44 = QtWidgets.QLabel(self.gridFrame1)
        self.label_44.setMinimumSize(QtCore.QSize(0, 0))
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_46 = QtWidgets.QLabel(self.gridFrame1)
        self.label_46.setMinimumSize(QtCore.QSize(0, 0))
        self.label_46.setObjectName("label_46")
        self.gridLayout.addWidget(self.label_46, 6, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_48 = QtWidgets.QLabel(self.gridFrame1)
        self.label_48.setMinimumSize(QtCore.QSize(0, 0))
        self.label_48.setObjectName("label_48")
        self.gridLayout.addWidget(self.label_48, 6, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_47 = QtWidgets.QLabel(self.gridFrame1)
        self.label_47.setMinimumSize(QtCore.QSize(0, 0))
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 6, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_49 = QtWidgets.QLabel(self.gridFrame1)
        self.label_49.setMinimumSize(QtCore.QSize(0, 0))
        self.label_49.setObjectName("label_49")
        self.gridLayout.addWidget(self.label_49, 6, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_51 = QtWidgets.QLabel(self.gridFrame1)
        self.label_51.setMinimumSize(QtCore.QSize(0, 0))
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_53 = QtWidgets.QLabel(self.gridFrame1)
        self.label_53.setMinimumSize(QtCore.QSize(0, 0))
        self.label_53.setObjectName("label_53")
        self.gridLayout.addWidget(self.label_53, 7, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_52 = QtWidgets.QLabel(self.gridFrame1)
        self.label_52.setMinimumSize(QtCore.QSize(0, 0))
        self.label_52.setObjectName("label_52")
        self.gridLayout.addWidget(self.label_52, 7, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_54 = QtWidgets.QLabel(self.gridFrame1)
        self.label_54.setMinimumSize(QtCore.QSize(0, 0))
        self.label_54.setObjectName("label_54")
        self.gridLayout.addWidget(self.label_54, 7, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_55 = QtWidgets.QLabel(self.gridFrame1)
        self.label_55.setMinimumSize(QtCore.QSize(0, 0))
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 7, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_56 = QtWidgets.QLabel(self.gridFrame1)
        self.label_56.setMinimumSize(QtCore.QSize(0, 0))
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 7, 6, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalFrame.raise_()
        self.Main_List.raise_()
        self.gridFrame.raise_()
        self.gridFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)


        self.Sell_prise_min_butt_group = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7]
        self.Sell_prise_min_date_butt_group = [self.label_8, self.label_9, self.label_10, self.label_11, self.label_12, self.label_13, self.label_14]
        self.Sell_prise_max_butt_group = [self.label_15, self.label_16, self.label_17, self.label_18, self.label_19, self.label_20, self.label_21]
        self.Sell_prise_max_date_butt_group = [self.label_22, self.label_23, self.label_24, self.label_25, self.label_26, self.label_27, self.label_28]
        self.Buy_prise_min_butt_group = [self.label_29, self.label_30, self.label_31, self.label_32, self.label_33, self.label_34, self.label_35]
        self.Buy_prise_min_date_butt_group = [self.label_36, self.label_37, self.label_38, self.label_39, self.label_40, self.label_41, self.label_42]
        self.Buy_prise_max_butt_group = [self.label_43, self.label_44, self.label_45, self.label_46, self.label_47, self.label_48, self.label_49]
        self.Buy_prise_max_date_butt_group = [self.label_50, self.label_51, self.label_52, self.label_53, self.label_54, self.label_55, self.label_56]


        self.MainUnder_Funk()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_Quality_S.setItemText(0, _translate("MainWindow", "Обычн"))
        self.comboBox_Quality_S.setItemText(1, _translate("MainWindow", "Хорош"))
        self.comboBox_Quality_S.setItemText(2, _translate("MainWindow", "Выдающ"))
        self.comboBox_Quality_S.setItemText(3, _translate("MainWindow", "Отличн"))
        self.comboBox_Quality_S.setItemText(4, _translate("MainWindow", "Шедевр"))
        self.Text_lable.setText(_translate("MainWindow", "Фильтр/Сортировка"))
        self.comboBox_Tier_S.setItemText(0, _translate("MainWindow", "4"))
        self.comboBox_Tier_S.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox_Tier_S.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox_Tier_S.setItemText(3, _translate("MainWindow", "7"))
        self.comboBox_Tier_S.setItemText(4, _translate("MainWindow", "8"))
        self.comboBox_Rarity_S.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_Rarity_S.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_Rarity_S.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_Rarity_S.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_Rarity_S.setItemText(4, _translate("MainWindow", "4"))
        self.radioButtonArmo.setText(_translate("MainWindow", "Броня"))
        self.radioButton_Resurses.setText(_translate("MainWindow", "Ресурсы"))
        self.radioButton_Thinks.setText(_translate("MainWindow", "Шмотки"))
        self.comboBox_S.setItemText(0, _translate("MainWindow", "Стандарт"))
        self.comboBox_S.setItemText(1, _translate("MainWindow", "Разница цен >"))
        self.comboBox_S.setItemText(2, _translate("MainWindow", "Разница цен <"))
        self.label_Black_Market.setText(_translate("MainWindow", "Black_Market"))
        self.label_Carleon.setText(_translate("MainWindow", "Carleon"))
        self.label_Fort_Stearling.setText(_translate("MainWindow", "Fort Stearling"))
        self.label_Lymhyrst.setText(_translate("MainWindow", "Lymhyrst"))
        self.label_Thetford.setText(_translate("MainWindow", "Thetford"))
        self.label_Martlock.setText(_translate("MainWindow", "Martlock"))
        self.label_Bridgewatch.setText(_translate("MainWindow", "Bridgewatch"))
        self.label_Min_Sell.setText(_translate("MainWindow", "Min_Sell"))
        self.label_Min_Sell_D.setText(_translate("MainWindow", "Min_Sell_D"))
        self.label_Max_Sell.setText(_translate("MainWindow", "Max_Sell"))
        self.label_Max_Sell_D.setText(_translate("MainWindow", "Max_Sell_D"))
        self.label_Min_Buy.setText(_translate("MainWindow", "Min_Buy"))
        self.label_Min_Buy_D.setText(_translate("MainWindow", "Min_Buy_D"))
        self.label_Max_Buy.setText(_translate("MainWindow", "Max_Buy"))
        self.label_Max_Buy_D.setText(_translate("MainWindow", "Max_Buy_D"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "TextLabel"))
        self.label_43.setText(_translate("MainWindow", "TextLabel"))
        self.label_50.setText(_translate("MainWindow", "TextLabel"))
        self.label_36.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_25.setText(_translate("MainWindow", "TextLabel"))
        self.label_26.setText(_translate("MainWindow", "TextLabel"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "TextLabel"))
        self.label_35.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "TextLabel"))
        self.label_37.setText(_translate("MainWindow", "TextLabel"))
        self.label_40.setText(_translate("MainWindow", "TextLabel"))
        self.label_38.setText(_translate("MainWindow", "TextLabel"))
        self.label_41.setText(_translate("MainWindow", "TextLabel"))
        self.label_39.setText(_translate("MainWindow", "TextLabel"))
        self.label_42.setText(_translate("MainWindow", "TextLabel"))
        self.label_45.setText(_translate("MainWindow", "TextLabel"))
        self.label_44.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "TextLabel"))
        self.label_48.setText(_translate("MainWindow", "TextLabel"))
        self.label_47.setText(_translate("MainWindow", "TextLabel"))
        self.label_49.setText(_translate("MainWindow", "TextLabel"))
        self.label_51.setText(_translate("MainWindow", "TextLabel"))
        self.label_53.setText(_translate("MainWindow", "TextLabel"))
        self.label_52.setText(_translate("MainWindow", "TextLabel"))
        self.label_54.setText(_translate("MainWindow", "TextLabel"))
        self.label_55.setText(_translate("MainWindow", "TextLabel"))
        self.label_56.setText(_translate("MainWindow", "TextLabel"))


    def MainUnder_Funk(self):
        
        Item.Item_in_listes('Prises.json')
        self.Add_item_in_QlistWidget()
       
        self.Main_List.itemClicked.connect(self.Update_info)


    def Add_item_in_QlistWidget(self):
        added_items = set()  # создаем пустое множество, которое будем использовать для проверки на дубликаты
        
        for it in Item_sort_list:  # итерируемся по списку элементов, которые нужно добавить
            if it.item_id not in added_items:  # если элемент не является дубликатом
                
                self.Main_List.addItem(it.item_id)  # добавляем элемент в QListWidget
                added_items.add(it.item_id)  # добавляем элемент в множество добавленных элементов


    def Sorting(self):
        global ik, sell_price_min_dict, sell_price_max_dict, buy_price_min_dict, buy_price_max_dict
        
        for fik in Item_sort_list:

            City_dict[ik] = fik.city

            if fik.sell_price_min == None: fik.sell_price_min = 0
            if fik.sell_price_max == None: fik.sell_price_max = 0
            if fik.buy_price_min == None: fik.buy_price_min = 0
            if fik.buy_price_max == None: fik.buy_price_max = 0
            
            sell_price_min_dict[ik] = fik.sell_price_min
            sell_price_max_dict[ik] = fik.sell_price_max
            buy_price_min_dict[ik] = fik.buy_price_min
            buy_price_max_dict[ik] = fik.buy_price_max

            ik += 1

        def get_key(dict: dict, value):
            for key, val in dict.items():
                if val == value:
                    return key

        def Sort_dict(dict: dict):
            Sorted_dict = {}
            sort_list = sorted(dict.values(), reverse=True)

            for i in dict.values():
                for i in sort_list:
                    Sorted_dict[get_key(dict, i)] = i

            dict = Sorted_dict
            return dict
            
        sell_price_min_dict = Sort_dict(sell_price_min_dict)
        sell_price_max_dict = Sort_dict(sell_price_max_dict)
        buy_price_min_dict = Sort_dict(buy_price_min_dict)
        buy_price_max_dict = Sort_dict(buy_price_max_dict)


    def Update_info(self):
        # получаем выделенный элемент из списка
        selected_item = self.Main_List.currentItem()
        
        # проверяем, что элемент есть
        if selected_item:
            # получаем текст выделенного элемента
            selected_name = selected_item.text()
            
            # перебираем все товары из отсортированного списка Item_sort_list
            for item in Item_sort_list:
                # если нашли товар, у которого item_id совпадает с выбранным текстом, переходим к обновлению информации по нему
                if item.item_id == selected_name:
                    # определяем id города товара
                    id = locations.index(item.city) + 1
                    # обновляем информацию о ценах продажи и покупки для соответствующих кнопок в интерфейсе
                    self.Sell_prise_min_butt_group[id].setText(str(item.sell_price_min))
                    self.Sell_prise_min_date_butt_group[id].setText(item.sell_price_min_date)
                    self.Sell_prise_max_butt_group[id].setText(str(item.sell_price_max))
                    self.Sell_prise_max_date_butt_group[id].setText(item.sell_price_max_date)
                    self.Buy_prise_min_butt_group[id].setText(str(item.buy_price_min))
                    self.Buy_prise_min_date_butt_group[id].setText(item.buy_price_min_date)
                    self.Buy_prise_max_butt_group[id].setText(str(item.buy_price_max))
                    self.Buy_prise_max_date_butt_group[id].setText(item.buy_price_max_date)



    # def setText(self, group_lable, dict: dict):
    #     dict_item_id = list(dict.keys())
    #     print(dict_item_id)

    #     for id in range(len(group_lable)):
    #         group_lable[id].setText(str(dict[dict_item_id[id]]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
