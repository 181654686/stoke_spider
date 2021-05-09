import requests        #导入requests包
import json
import records
import configparser
import time

url = 'https://eniu.com/static/data/stock_list.json'
strhtml = requests.get(url)        #Get方式获取网页数据
# print(strhtml.text)
db = records.Database("mysql://root:123456@localhost:3306/gupiao?charset=utf8")

params_json = json.loads(strhtml.text)

data = []
for value in params_json:
    # time.sleep(1)
    # insertSql = "INSERT INTO `main_list`(`stock_abbr`, `stock_id`, `stock_name`, `stock_number`, `stock_pinyin`,`dt`,`done`) VALUES ('" + \
    #             str(value['stock_abbr']) + "','" + str(value['stock_id']) + "','" + str(value['stock_name']) + "','"  \
    #             +str(value['stock_number']) + "','" + str(value['stock_pinyin']) + "','"  \
    #              + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +  + "','" + 'nok' +"');" 
    # db.query(insertSql)

    data.append({'stock_abbr':str(value['stock_abbr']),'stock_id': str(value['stock_id']),\
                'stock_name':str(value['stock_name']),'stock_number':str(value['stock_number']),'stock_pinyin':str(value['stock_pinyin'])
                ,'dt':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),'done':'no'})

db.bulk_query("insert main_list(stock_abbr, stock_id,stock_name,stock_number,stock_pinyin,dt,done)\
                values( :stock_abbr, :stock_id,:stock_name,:stock_number,:stock_pinyin,:dt,:done)", data)
