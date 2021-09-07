import string
import time
import random
import json
"""record = {
1001: {'Name':'Good-night',     'mall_price':59,        'Actual_price':69,      'Quantity':100,         'product_info':'machine+liquid',        'prod_exp':'10/23'},
1002: {'Name':'Horlics_s',      'mall_price':5,         'Actual_price':5,       'Quantity':100,         'product_info':'20g',                   'prod_exp':'09/23'},
1003: {'Name':'Boost-mini',     'mall_price':5,         'Actual_price':5,       'Quantity':100,         'product_info':'20g',                   'prod_exp':'08/22'},
1004: {'Name':'Horlics-B',      'mall_price':48,        'Actual_price':50,      'Quantity':100,         'product_info':'500g',                  'prod_exp':'07/23'},
1005: {'Name':'Boost-box',      'mall_price':47,        'Actual_price':50,      'Quantity':100,         'product_info':'500g',                  'prod_exp':'01/24'},
1006: {'Name':'Battery',        'mall_price':12,        'Actual_price':15,      'Quantity':100,         'product_info':'remote-battery',        'prod_exp':'04/24'},
1007: {'Name':'Ashirwad_atta',  'mall_price':56,        'Actual_price':60,      'Quantity':100,         'product_info':'500g',                  'prod_exp':'03/22'},
1008: {'Name':'Parle-G',        'mall_price':9,         'Actual_price':10,      'Quantity':100,         'product_info':'10rs-pack',             'prod_exp':'02/23'},
1009: {'Name':'Britania-Toast', 'mall_price':8.9,       'Actual_price':10,      'Quantity':100,         'product_info':'pack-of-6-Toast',       'prod_exp':'01/22'},
1010: {'Name':'Arokya-Milk',    'mall_price':13.4,      'Actual_price':15,      'Quantity':100,         'product_info':' 250ml',                'prod_exp':'09/22'},
1011: {'Name':'ThumpsUp',       'mall_price':50,        'Actual_price':55,      'Quantity':100,         'product_info':'1L',                    'prod_exp':'09/23'},
1012: {'Name':'Sprite-Cool',    'mall_price':67,        'Actual_price':70,      'Quantity':100,         'product_info':'1.25L',                 'prod_exp':'05/22'},
1013: {'Name':'Pepsi-pro',      'mall_price':38,        'Actual_price':40,      'Quantity':100,         'product_info':'750ml',                 'prod_exp':'06/24'},
1014: {'Name':'Coca-Cola',      'mall_price':95,        'Actual_price':100,     'Quantity':100,         'product_info':'2.5L',                  'prod_exp':'07/23'},
1015: {'Name':'Maggie-noodles', 'mall_price':9.6,       'Actual_price':10,      'Quantity':100,         'product_info':'100g',                  'prod_exp':'08/22'},
1016: {'Name':'Halke-Phulke',   'mall_price':30,        'Actual_price':36,      'Quantity':100,         'product_info':'100g',                  'prod_exp':'03/24'},
1017: {'Name':'USA-Lays',       'mall_price':65,        'Actual_price':69,      'Quantity':100,         'product_info':'200g',                  'prod_exp':'06/22'},
1018: {'Name':'Goodday',        'mall_price':19,        'Actual_price':20,      'Quantity':100,         'product_info':'20rs-pack',             'prod_exp':'11/22'},
1019: {'Name':'Kit-kat',        'mall_price':19,        'Actual_price':20,      'Quantity':100,         'product_info':'4-sticks',              'prod_exp':'12/21'},
1020: {'Name':'Diary-milk',     'mall_price':18.5,      'Actual_price':20,      'Quantity':100,         'product_info':'10-bars',               'prod_exp':'11/21'},
1021: {'Name':'premium-Rice',   'mall_price':105,       'Actual_price':110,     'Quantity':1000,        'product_info':'Basmathi',              'prod_exp':'00/00'},
1022: {'Name':'Moong-Dal',      'mall_price':100,       'Actual_price':115,     'Quantity':100,         'product_info':'1kg-pack',              'prod_exp':'04/22'},
1023: {'Name':'Mill-Maker',     'mall_price':9.6,       'Actual_price':10,      'Quantity':100,         'product_info':'50g-pack',              'prod_exp':'06/23'},
1024: {'Name':'Potato(Aloo)',   'mall_price':38,        'Actual_price':40,      'Quantity':100,         'product_info':'40kg-A1',               'prod_exp':'09/24'},
1025: {'Name':'Tooth-Brush',    'mall_price':19.5,      'Actual_price':22,      'Quantity':100,         'product_info':'Ajay-Hard',             'prod_exp':'04/25'},
1026: {'Name':'Close-Up',       'mall_price':19,        'Actual_price':20,      'Quantity':100,         'product_info':'100g',                  'prod_exp':'04/22'},
1027: {'Name':'Clinic-Plus',    'mall_price':0.95,      'Actual_price':1,       'Quantity':100,         'product_info':'1rs-pack',              'prod_exp':'05/23'},
1028: {'Name':'Ponds-Powder',   'mall_price':9.5,       'Actual_price':10,      'Quantity':100,         'product_info':'40g',                   'prod_exp':'02/22'},
1029: {'Name':'Glow-n-Lovely',  'mall_price':34,        'Actual_price':36,      'Quantity':100,         'product_info':'100gm',                 'prod_exp':'01/22'},
1030: {'Name':'Santoor_soap',   'mall_price':20,        'Actual_price':22,      'Quantity':100,         'product_info':'200g',                  'prod_exp':'07/23'}
}
sam = open('newjson.json','r')
sam.write(record)
sam.close()"""
fd = open('newjson.json')
data = fd.read()
fd.close()
recr = json.loads(data)
def Bill(a1,b1):
    n = len(a1)
    total = 0
    d = 0.0
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12)) # takes the random inputs for transac id
    print("\n************     SACHU's MINI D-Mart**********\n") #prints the mart name
    print("Time: ",time.ctime(),"      Transaction_id: ",ran) # prints time and transac id
    print('______________________________________________________________________')
    print('sl.no\t name\t\tprice\t\tqty\t\tsub-total')  
    for i in range (n):
        x = a1[i]
        d = recr[x]["mall_price"] * b1[i]
        total = total+d
        print(i,'\t',recr[x]['Name'],'\t',recr[x]['mall_price'],'\t\t',b1[i],'\t\t',d)
    print('_________                               _______________________')
    print('#Total                                          \t',total)
    print("$$$$---->Thank You <------$$$$$\nvisit again")
    return 0

bill = []
qtty = []
print("************this is customer's choice pgm*********")
opt = 'y'
s1 = 0
while opt =='y' or opt == 'Y':
    prod_id = input('enter the product id: ')
    qty = int(input("enter the quantity: "))
    if prod_id in recr.keys():     #we will iterate through each key 
        if recr[prod_id]['Quantity']<qty: #here we check whether entered product id exist in product keys
            print("@@@we do not have sufficient quantity:@@@")
        else:
            bill.append(prod_id)
            qtty.append(qty)
            recr[prod_id]['Quantity'] = recr[prod_id]['Quantity'] - qty
            s1 += 1
    else:
        print("xxxx------the enterd product id does not exist:------xxxxx")
    opt = input("would like to add more item\n click y/Y for yes\nn/N for no: ")

if s1 > 0:
    Bill(bill,qtty)
    data = json.dumps(recr)
    sd = open("newjson.json",'w')
    sd.write(data)
    sd.close()