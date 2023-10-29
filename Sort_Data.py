
import os, json, pandas

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QComboBox

from datetime import datetime
import List_item

Item_sort_list = []
City_dict = {}
sell_price_min_dict = {}
sell_price_max_dict = {}
buy_price_min_dict = {}
buy_price_max_dict = {}
locations = ['Black Market','Caerleon','Fort Sterling','Lymhurst','Thetford','Martlock','Bridgewatch']

List_name_check_Armo = ['ARM', 'HEA', 'SHO']
List_name_check_Thinks = ['BAG', 'CAP']



class Item():
    global Find_All_Filename

    def __init__(self, item_id, city, 
                sell_price_min=None, sell_price_min_date=None, 
                sell_price_max=None, sell_price_max_date=None, 
                buy_price_min=None, buy_price_min_date=None, 
                buy_price_max=None, buy_price_max_date=None):
        
        # устанавливаем значения атрибутов при создании экземпляра класса
        self.item_id = item_id
        self.city = city

        # обрабатываем переменные с припиской "date"
        sell_price_min_date = self.__format_datetime(sell_price_min_date)
        sell_price_max_date = self.__format_datetime(sell_price_max_date)
        buy_price_min_date = self.__format_datetime(buy_price_min_date)
        buy_price_max_date = self.__format_datetime(buy_price_max_date)
        
        # используем условное выражение одной строкой для проверки на None
        self.sell_price_min = str(sell_price_min) if sell_price_min is not None else '------'
        self.sell_price_min_date = sell_price_min_date if sell_price_min_date is not None else '------'
        
        self.sell_price_max = str(sell_price_max) if sell_price_max is not None else '------'
        self.sell_price_max_date = sell_price_max_date if sell_price_max_date is not None else '------'
        
        self.buy_price_min = str(buy_price_min) if buy_price_min is not None else '------'
        self.buy_price_min_date = buy_price_min_date if buy_price_min_date is not None else '------'
        
        self.buy_price_max = str(buy_price_max) if buy_price_max is not None else '------'
        self.buy_price_max_date = buy_price_max_date if buy_price_max_date is not None else '------'


    def __format_datetime(self, dt):
        today = datetime.now() # Получаем текущую дату и время

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


    def __AddItem(self, Add_list: list):
        Add_list.append(self)


    def Find_All_Filename(folder_path: str): # Получаем список файлов в директории с помощью функции os.listdir()
        # Она возвращает список строк с именами файлов и папок в указанной директории
        
        # Создаем список, в который будут добавляться имена файлов с расширением .json
        # Для каждого имени файла в списке files_in_folder проверяем, заканчивается ли оно на ".json"
        # Если имя файла заканчивается на ".json", добавляем его в список json_files
        file_names = [f for f in os.listdir(folder_path) if f.endswith('.json')]
        file_names.sort(reverse=True)
        return file_names


    def Item_in_lists(self, path: str, taken_name: str):
        global Item_sort_list
        # Очищаем список перед добавлением новых элементов
        Item_sort_list.clear()
        
        for file in os.listdir(path):
            if file == taken_name and file.endswith('.json'):
                file_n = os.path.join(path, file)

                try:
                    # Открываем JSON файл и загружаем данные
                    with open(file_n, 'r') as opened_file:
                        dates = json.load(opened_file)

                        for i in range(len(dates['item_id'])):
                            i = str(i)

                            # Создаем экземпляр Item для каждого элемента в файле
                            Generated_item = Item(dates['item_id'][i], 
                                        dates['city'][i], 
                                        dates['sell_price_min'][i], 
                                        dates['sell_price_min_date'][i], 
                                        dates['sell_price_max'][i], 
                                        dates['sell_price_max_date'][i], 
                                        dates['buy_price_min'][i], 
                                        dates['buy_price_min_date'][i], 
                                        dates['buy_price_max'][i], 
                                        dates['buy_price_max_date'][i])
                            # Добавляем элемент в список
                            Generated_item.__AddItem(Item_sort_list)

                except (IOError, ValueError, KeyError) as element:
                    print(f'An error occurred while reading the JSON file: {element}')


    def Quality_Check(self, path: str, need_quality: int):
        
        need_file =[]

        for file in os.listdir(path):
            file_n = os.path.join(path, file)

            if os.path.isfile(file_n) and file_n.endswith('.json'):
                with open(file_n, 'r') as opened_file:
                    dates = json.load(opened_file)
                    qua = dates['quality'].get('1')

                    if qua == need_quality:
                        need_file.append(file)

        return need_file


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main_List = QtWidgets.QListWidget(self.centralwidget)
        self.Main_List.setGeometry(QtCore.QRect(10, 40, 230, 350))
        self.Main_List.setObjectName("Main_List")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 385, 230, 145))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButtonArmo = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonArmo.setFont(font)
        self.radioButtonArmo.setObjectName("radioButtonArmo")
        self.gridLayout_2.addWidget(self.radioButtonArmo, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.radioButton_Thinks = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_Thinks.setFont(font)
        self.radioButton_Thinks.setObjectName("radioButton_Thinks")
        self.gridLayout_2.addWidget(self.radioButton_Thinks, 2, 1, 1, 1)
        self.radioButton_Resurses = QtWidgets.QRadioButton(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_Resurses.setFont(font)
        self.radioButton_Resurses.setObjectName("radioButton_Resurses")
        self.gridLayout_2.addWidget(self.radioButton_Resurses, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        # self.comboBox_S = QtWidgets.QComboBox(self.gridFrame)
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.comboBox_S.setFont(font)
        # self.comboBox_S.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        # self.comboBox_S.setObjectName("comboBox_S")
        # self.comboBox_S.addItem("")
        # self.comboBox_S.addItem("")
        # self.comboBox_S.addItem("")
        # self.gridLayout_2.addWidget(self.comboBox_S, 3, 0, 1, 3)
        self.Text_lable = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Text_lable.setFont(font)
        self.Text_lable.setObjectName("Text_lable")
        self.gridLayout_2.addWidget(self.Text_lable, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
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
        self.comboBox_Rarity_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Rarity_S, 1, 1, 1, 1)
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
        self.comboBox_Tier_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Tier_S, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 3, QtCore.Qt.AlignHCenter)
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
        self.comboBox_Quality_S.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_Quality_S, 1, 2, 1, 1)
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 230, 22))
        self.comboBox.setObjectName("comboBox")
        self.gridFrame2 = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame2.setGeometry(QtCore.QRect(10, 530, 230, 110))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gridFrame2.setFont(font)
        self.gridFrame2.setObjectName("gridFrame2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridFrame2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.gridFrame2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridFrame2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridFrame2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridFrame2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.verticalFrame.raise_()
        self.Main_List.raise_()
        self.gridFrame.raise_()
        self.gridFrame.raise_()
        self.comboBox.raise_()
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

        self.Butt_item_group = QButtonGroup()
        self.Butt_item_group.addButton(self.radioButton_Resurses)
        self.Butt_item_group.addButton(self.radioButton_Thinks)
        self.Butt_item_group.addButton(self.radioButtonArmo)


        self.MainUnder_Funk()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButtonArmo.setText(_translate("MainWindow", "Броня"))
        self.radioButton_Thinks.setText(_translate("MainWindow", "Речі"))
        self.radioButton_Resurses.setText(_translate("MainWindow", "Ресурси"))
        # self.comboBox_S.setItemText(0, _translate("MainWindow", "Стандарт"))
        # self.comboBox_S.setItemText(1, _translate("MainWindow", "Разница цен >"))
        # self.comboBox_S.setItemText(2, _translate("MainWindow", "Разница цен <"))
        self.Text_lable.setText(_translate("MainWindow", "Фільтр/Сортування"))
        self.comboBox_Rarity_S.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_Rarity_S.setItemText(1, _translate("MainWindow", "0"))
        self.comboBox_Rarity_S.setItemText(2, _translate("MainWindow", "1"))
        self.comboBox_Rarity_S.setItemText(3, _translate("MainWindow", "2"))
        self.comboBox_Rarity_S.setItemText(4, _translate("MainWindow", "3"))
        self.comboBox_Rarity_S.setItemText(5, _translate("MainWindow", "4"))
        self.comboBox_Tier_S.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_Tier_S.setItemText(1, _translate("MainWindow", "4"))
        self.comboBox_Tier_S.setItemText(2, _translate("MainWindow", "5"))
        self.comboBox_Tier_S.setItemText(3, _translate("MainWindow", "6"))
        self.comboBox_Tier_S.setItemText(4, _translate("MainWindow", "7"))
        self.comboBox_Tier_S.setItemText(5, _translate("MainWindow", "8"))
        self.label.setText(_translate("MainWindow", "Шаблони Обновлення"))
        self.comboBox_Quality_S.setItemText(0, _translate("MainWindow", "---"))
        self.comboBox_Quality_S.setItemText(1, _translate("MainWindow", "Обичн"))
        self.comboBox_Quality_S.setItemText(2, _translate("MainWindow", "Хорош"))
        self.comboBox_Quality_S.setItemText(3, _translate("MainWindow", "Видающ"))
        self.comboBox_Quality_S.setItemText(4, _translate("MainWindow", "Отлічн"))
        self.comboBox_Quality_S.setItemText(5, _translate("MainWindow", "Шедевр"))
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
        self.label_23.setText(_translate("MainWindow", "Prise"))
        self.label_14.setText(_translate("MainWindow", "Time"))
        self.label_16.setText(_translate("MainWindow", "Prise"))
        self.label_17.setText(_translate("MainWindow", "Prise"))
        self.label_18.setText(_translate("MainWindow", "Prise"))
        self.label_13.setText(_translate("MainWindow", "Time"))
        self.label_21.setText(_translate("MainWindow", "Prise"))
        self.label_20.setText(_translate("MainWindow", "Prise"))
        self.label_9.setText(_translate("MainWindow", "Time"))
        self.label_10.setText(_translate("MainWindow", "Time"))
        self.label_12.setText(_translate("MainWindow", "Time"))
        self.label_11.setText(_translate("MainWindow", "Time"))
        self.label_7.setText(_translate("MainWindow", "Prise"))
        self.label_1.setText(_translate("MainWindow", "Prise"))
        self.label_8.setText(_translate("MainWindow", "Time"))
        self.label_15.setText(_translate("MainWindow", "Prise"))
        self.label_22.setText(_translate("MainWindow", "Prise"))
        self.label_2.setText(_translate("MainWindow", "Prise"))
        self.label_29.setText(_translate("MainWindow", "Prise"))
        self.label_43.setText(_translate("MainWindow", "Prise"))
        self.label_50.setText(_translate("MainWindow", "Prise"))
        self.label_36.setText(_translate("MainWindow", "Prise"))
        self.label_4.setText(_translate("MainWindow", "Prise"))
        self.label_3.setText(_translate("MainWindow", "Prise"))
        self.label_19.setText(_translate("MainWindow", "Prise"))
        self.label_6.setText(_translate("MainWindow", "Prise"))
        self.label_5.setText(_translate("MainWindow", "Prise"))
        self.label_25.setText(_translate("MainWindow", "Prise"))
        self.label_26.setText(_translate("MainWindow", "Prise"))
        self.label_27.setText(_translate("MainWindow", "Prise"))
        self.label_24.setText(_translate("MainWindow", "Prise"))
        self.label_30.setText(_translate("MainWindow", "Prise"))
        self.label_28.setText(_translate("MainWindow", "Prise"))
        self.label_33.setText(_translate("MainWindow", "Prise"))
        self.label_31.setText(_translate("MainWindow", "Prise"))
        self.label_34.setText(_translate("MainWindow", "Prise"))
        self.label_35.setText(_translate("MainWindow", "Prise"))
        self.label_32.setText(_translate("MainWindow", "Prise"))
        self.label_37.setText(_translate("MainWindow", "Prise"))
        self.label_40.setText(_translate("MainWindow", "Prise"))
        self.label_38.setText(_translate("MainWindow", "Prise"))
        self.label_41.setText(_translate("MainWindow", "Prise"))
        self.label_39.setText(_translate("MainWindow", "Prise"))
        self.label_42.setText(_translate("MainWindow", "Prise"))
        self.label_45.setText(_translate("MainWindow", "Prise"))
        self.label_44.setText(_translate("MainWindow", "Prise"))
        self.label_46.setText(_translate("MainWindow", "Prise"))
        self.label_48.setText(_translate("MainWindow", "Prise"))
        self.label_47.setText(_translate("MainWindow", "Prise"))
        self.label_49.setText(_translate("MainWindow", "Prise"))
        self.label_51.setText(_translate("MainWindow", "Prise"))
        self.label_53.setText(_translate("MainWindow", "Prise"))
        self.label_52.setText(_translate("MainWindow", "Prise"))
        self.label_54.setText(_translate("MainWindow", "Prise"))
        self.label_55.setText(_translate("MainWindow", "Prise"))
        self.label_56.setText(_translate("MainWindow", "Prise"))
        self.pushButton.setText(_translate("MainWindow", "Броня Б/А"))
        self.pushButton_2.setText(_translate("MainWindow", "Речі"))
        self.pushButton_3.setText(_translate("MainWindow", "Ресурси"))
        self.pushButton_4.setText(_translate("MainWindow", "Вибраний Файл"))


    def MainUnder_Funk(self):

        if self.Butt_item_group.checkedButton():
            self.Add_item_in_QlistWidget
        

        # соединяем сигнал itemClicked из элемента управления Main_List с методом Update_info
        self.Main_List.itemClicked.connect(self.Update_info)

        self.comboBox_update()
        # соединяем сигнал activated элемента управления comboBox с методом Item_in_lists класса Item с передачей аргументов
        self.comboBox.activated[str].connect(lambda: Item.Item_in_lists(self, './Last_JSON_File', self.comboBox.currentText()))
        # соединяем сигнал activated элемента управления comboBox с методом Add_item_in_QlistWidget
        self.comboBox.activated[str].connect(lambda: self.Add_item_in_QlistWidget())
        # соединяем сигнал clicked элемента управления pushButton с методом Knew_num_Start с передачей аргумента 1 2 3 4
        self.pushButton.clicked.connect(lambda: self.List_Start(1))
        self.pushButton_2.clicked.connect(lambda: self.List_Start(2))
        self.pushButton_3.clicked.connect(lambda: self.List_Start(3))
        self.pushButton_4.clicked.connect(lambda: self.List_Start(4))


        self.comboBox_Tier_S.activated[str].connect(self.Sorting_Item)
        self.comboBox_Rarity_S.activated[str].connect(self.Sorting_Item)
        self.comboBox_Quality_S.activated[str].connect(self.Sorting_Item)


    def comboBox_update(self):
        self.comboBox.addItems(Find_All_Filename('./Last_JSON_File'))


    def Add_item_in_QlistWidget(self):
        global Start_list
        global get_list_widget_strings

        def get_list_widget_strings(list_widget):
            rows = []
            items = list_widget.findItems("*", QtCore.Qt.MatchWildcard)
            for item in items:
                rows.append(item.text())
            return rows


        added_items = set()  # создаем пустое множество, которое будем использовать для проверки на дубликаты
        self.Main_List.clear()

        self.comboBox_Tier_S.setCurrentIndex(0)
        self.comboBox_Rarity_S.setCurrentIndex(0)
        self.comboBox_Quality_S.setCurrentIndex(0)
        
        def add_to_list(list, check_name):
            for name in list:
                if name == check_name[3:6]:
                    if check_name not in added_items:  # если элемент не является дубликатом
                        self.Main_List.addItem(check_name)  # добавляем элемент в QListWidget
                        added_items.add(check_name)  # добавляем элемент в множество добавленных элементов

        for it in Item_sort_list:  # итерируемся по списку элементов, которые нужно добавить

            if self.radioButtonArmo.isChecked():
                add_to_list(List_name_check_Armo, it.item_id)
            elif self.radioButton_Thinks.isChecked():
                add_to_list(List_name_check_Thinks, it.item_id)
            elif self.radioButton_Resurses.isChecked():
                add_to_list(List_item.Resource, it.item_id)
            else:
                if it.item_id not in added_items:
                    self.Main_List.addItem(it.item_id)
                    added_items.add(it.item_id)


        Start_list = get_list_widget_strings(self.Main_List)


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
                    id = locations.index(item.city)
                    # обновляем информацию о ценах продажи и покупки для соответствующих кнопок в интерфейсе
                    self.Sell_prise_min_butt_group[id].setText(str(item.sell_price_min))
                    self.Sell_prise_min_date_butt_group[id].setText(item.sell_price_min_date)
                    self.Sell_prise_max_butt_group[id].setText(str(item.sell_price_max))
                    self.Sell_prise_max_date_butt_group[id].setText(item.sell_price_max_date)
                    self.Buy_prise_min_butt_group[id].setText(str(item.buy_price_min))
                    self.Buy_prise_min_date_butt_group[id].setText(item.buy_price_min_date)
                    self.Buy_prise_max_butt_group[id].setText(str(item.buy_price_max))
                    self.Buy_prise_max_date_butt_group[id].setText(item.buy_price_max_date)


    def Sorting_Item(self):
        
        def filter_strings(string_list: list, opsions: int, second_char, last_two_chars:str):
            filtered_list = []
            try:
                if opsions == 2: # фильтр по второму символу и последним двум символам
                    if last_two_chars != '@0':
                        for string in string_list:
                            if len(string) >= 3 and string[1] == str(second_char) and string[-2:] == str(last_two_chars):
                                filtered_list.append(string)
                        return filtered_list
                    else: 
                        for string in string_list:
                            if len(string) >= 3 and string[1] == str(second_char) and string[-2] != '@':
                                filtered_list.append(string)
                        return filtered_list

                elif opsions == 1: # фильтр по второму символу
                    for string in string_list:
                        if len(string) >= 3 and string[1] == str(second_char):
                            filtered_list.append(string)
                    return filtered_list
                
                elif opsions == -1: # фильтр по последним двум символам
                    
                    if last_two_chars != '@0':
                        for string in string_list:
                            if len(string) >= 3 and string[-2:] == str(last_two_chars):
                                filtered_list.append(string)
                        return filtered_list
                    else:
                        for string in string_list:
                            if len(string) >= 3 and string[-2] != '@':
                                filtered_list.append(string)
                        return filtered_list
            
            except Exception as e:
                print(f'Error in Sorting_Item function: {e}')

        try:

            # Очистка исходного списка, если оба комбо-бокса находятся на изначальных значениях
            if self.comboBox_Tier_S.currentIndex() == 0 and self.comboBox_Rarity_S.currentIndex() == 0:

                self.Main_List.clear()
                self.Main_List.addItems(Start_list)

            else:
                # Фильтрация списка в зависимости от выбора в комбо-боксах
                if self.comboBox_Tier_S.currentIndex() and self.comboBox_Rarity_S.currentIndex() > 0:
                    
                    self.Main_List.clear()
                    need_tier_index = (self.comboBox_Tier_S.currentIndex() + 3)
                    option_index = '@' + str(self.comboBox_Rarity_S.currentIndex() - 1)
                    self.Main_List.addItems(filter_strings(Start_list, 2, need_tier_index, option_index))

                elif self.comboBox_Tier_S.currentIndex() > 0 and self.comboBox_Rarity_S.currentIndex() == 0:
                    
                    self.Main_List.clear()
                    need_tier_index = (self.comboBox_Tier_S.currentIndex() + 3)
                    self.Main_List.addItems(filter_strings(Start_list, 1, need_tier_index, None))

                elif self.comboBox_Rarity_S.currentIndex() > 0 and self.comboBox_Tier_S.currentIndex() == 0:

                    self.Main_List.clear()
                    option_index = '@' + str(self.comboBox_Rarity_S.currentIndex() - 1)
                    self.Main_List.addItems(filter_strings(Start_list, -1, None, option_index))

            # Обновление комбо-бокса "Quality"
            if self.comboBox_Quality_S.currentIndex() in range(0, 6):
                if self.comboBox_Quality_S.currentIndex() == 0:
                    self.comboBox.clear()
                    self.comboBox_update()
                else:
                    self.comboBox.clear()
                    self.comboBox.addItems(Item.Quality_Check(self, './Last_JSON_File', self.comboBox_Quality_S.currentIndex()))
        
        except Exception as e:
            print(f'Error in Sorting_Item function: {e}')


    def end_list(self, item_list_f, tier_list, rarity_list):
        item_list_new = []
        Res_list = List_item.Resource

        #Делаем проверку на передачу пустых списков
        if not item_list_f or not tier_list or not rarity_list:
            return None

        # Пробегаем через список
        for item in item_list_f: #предметов 
            for tier in tier_list:  #уровня
                for rarity in rarity_list: #редкости

                    if item != 'STONEBLOCK':
                        item_list_new.append(tier + item + rarity)
                    else:
                        item_list_new.append(tier + item)

        # Создаём функцию для переименования предметов
        def rename(string:str):
            # Если последние два символа не подходят ни под одно из вышеперечисленных условий, оставляем строку без изменения
            if string[-2:] == "@1":
                return string[:-2] + "_LEVEL1@1"
            elif string[-2:] == "@2":
                return string[:-2] + "_LEVEL2@2"
            elif string[-2:] == "@3":
                return string[:-2] + "_LEVEL3@3"
            elif string[-2:] == "@4":
                return string[:-2] + "_LEVEL4@4"
            else:
                return string
        
        # Создаём функцию для удаления уровня из названия предмета    
        def trim_string(string:str):
            if string[-2] == "@":   # Если в строке последний символ перед "@", обрезаем эту часть
                return string[3:-2]
            else:   # Если в строке последний символ после "@", обрезаем строку начиная с 3-го символа
                return string[3:]


        for i in range(len(item_list_new)):
            item = item_list_new[i]
            if trim_string(item) in Res_list:
                item_list_new[i] = rename(item)
                
        return item_list_new


    def Save_Json_From_Url(self, url: str, parse_date_column: str, pretty_print=False):
        try:
            df = pandas.read_html(url, header=0, parse_dates=[parse_date_column])
        except Exception as e:
            print(f"Failed to read data from {url}: {e}")
            
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        
        file_name = f"Prices_{current_time}.json"

        path_to_save = './Last_JSON_File/'
        
        if os.path.isfile(file_name):   # Проверяем, существует ли уже файл
            print(f"File {file_name} already exists, will not overwrite")
            return
        
        try:    # Записываем данные в формате JSON в файл с указанным именем
            df[0].to_json(path_to_save + file_name, date_format="iso", indent=4 if pretty_print else None)
            print(f"Data saved to {file_name}")
        except Exception as e:  # Выводим сообщение об ошибке, если сохранение не удалось
            print(f"Failed to save data to {file_name}: {e}")


    def List_Start(self, num_file):
        name_file = ''
        if num_file == 1: 
            name_file = './Start_File/Last_Armo_Lists.json'
        elif num_file == 2: 
            name_file = './Start_File/Last_Bag_Lists.json'
        elif num_file == 3: 
            name_file = './Start_File/Last_Resours_Lists.json'
        elif num_file == 4: 
            name_file = './Last_Lists.json'
        else:
            return None
        
        try:
            with open(name_file, 'r') as file:
                data = json.load(file)
                item_list = self.end_list(data['items'], data['tiers'], data['rarities'])
                if not item_list:
                    return None
                URL = stock + ','.join(item_list) + location + ','.join(data['locations']) + qualities_url + str(data['qualities'])
                self.Save_Json_From_Url(URL, 'item_id', True)
                self.comboBox_update()

        except Exception as e:
            print("Error: ", e)
            return None

            # with open(name_file, 'r') as file:
            #     data = json.load(file)
            #     URL = stock + ','. join(self.end_list(data['items'], data['tiers'], data['rarities'])) + location + ','. join(data['locations']) + qualities_url + str(data['qualities'])

            #     self.Save_Json_From_Url(URL, 'item_id', True)
            #     self.comboBox_update()

stock = 'https://www.albion-online-data.com/api/v2/stats/view/'
location = '?locations='
qualities_url = '&qualities='

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

















    