import json

Item_sort_list = []
City_dict = {}
sell_price_min_dict = {}
sell_price_max_dict = {}
buy_price_min_dict = {}
buy_price_max_dict = {}

class Item():
    def __init__(self, item_id, city, sell_price_min, sell_price_min_date, sell_price_max, sell_price_max_date, buy_price_min, buy_price_min_date, buy_price_max, buy_price_max_date):

        self.item_id = item_id
        self.city = city
        self.sell_price_min = str(sell_price_min)
        self.sell_price_min_date = sell_price_min_date
        self.sell_price_max = str(sell_price_max)
        self.sell_price_max_date = sell_price_max_date
        self.buy_price_min = str(buy_price_min)
        self.buy_price_min_date = buy_price_min_date
        self.buy_price_max = str(buy_price_max)
        self.buy_price_max_date = buy_price_max_date


def Item_in_list():
    global Item_sort_list
    Item_sort_list.clear()

    with open('Prises.json') as prises:
        datas = json.load(prises)

        for i in range(len(datas['item_id'])):
                Ites = Item(datas['item_id'][str(i)], 
                            datas['city'][str(i)], 
                            datas['sell_price_min'][str(i)], 
                            datas['sell_price_min_date'][str(i)], 
                            datas['sell_price_max'][str(i)], 
                            datas['sell_price_max_date'][str(i)], 
                            datas['buy_price_min'][str(i)], 
                            datas['buy_price_min_date'][str(i)], 
                            datas['buy_price_max'][str(i)], 
                            datas['buy_price_max_date'][str(i)])
                Item_sort_list.append(Ites)
        

def Sorting():
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

    def get_key(dict, value):
        for key, val in dict.items():
            if val == value:
                return key

    def Sort_dict(dict):
        Sorted_dict = {}
        sort_list = sorted(dict.values(), reverse=True)
        #print(sort_list)
        
        for i in dict.values():
            for i in sort_list:
                Sorted_dict[get_key(dict, i)] = i

        dict = Sorted_dict
        return dict
        
    sell_price_min_dict = Sort_dict(sell_price_min_dict)
    sell_price_max_dict = Sort_dict(sell_price_max_dict)
    buy_price_min_dict = Sort_dict(buy_price_min_dict)
    buy_price_max_dict = Sort_dict(buy_price_max_dict)







def setText(group_lable, dict):
    dict_item_id = list(dict.keys())
    print(dict_item_id)

    for id in range(len(group_lable)):
        group_lable[id].setText(str(dict[dict_item_id[id]]))