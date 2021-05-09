import requests        #导入requests包
import json
import records
import configparser
import time
from lxml import etree
import xml.sax 
import time
# sz000001

db = records.Database("mysql://root:123456@localhost:3306/gupiao?charset=utf8")

# data = [
#     {'name': 'Jiji', 'age': 23},
#     {'name': 'Mini', 'age': 22}
# ]

# db.bulk_query("insert names(name, age) values(:name, :age)", data)

class myXmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentName = ""
        self.CurrentData = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentName = tag

    # 元素结束调用
    def endElement(self, tag):
        pass

    # 读取字符时调用
    def characters(self, content):
        self.CurrentData = content



class stork():
    def __init__(self,storkid):
        self.storkid = storkid
        self._dataList = {}
        self._dataList["价格"] = "//*[@id='changyong']/p[1]/a"
        self._dataList["市盈率"] = "//*[@id='changyong']/p[2]/a"
        self._dataList["市净率"]= "//*[@id='changyong']/p[3]/a"
        self._dataList["股息率"]= "//*[@id='changyong']/p[4]/a"
        self._dataList["市值"]= "//*[@id='changyong']/p[5]/a"
        self._dataList["roe"] ="//*[@id='changyong']/p[6]/a"
        self._dataList["净利润"] ="//*[@id='caiwu']/p[2]/a"
        self._dataList["营收"] ="//*[@id='caiwu']/p[3]/a"
        self._dataList["利润扣非"] ="//*[@id='caiwu']/p[4]/a"
        self._dataList["负债率"] ="//*[@id='caiwu']/p[5]/a"
        self._dataList["现金流"] ="//*[@id='caiwu']/p[6]/a"
        self._dataList["毛利率"] ="//*[@id='caiwu']/p[7]/a"
        self._dataList["每股收益"] ="//*[@id='caiwu']/p[8]/a"

    def getData(self):

        url = 'https://eniu.com/gu/'+self.storkid
        strhtml = requests.get(url)        #Get方式获取网页数据
        html = etree.HTML(strhtml.text)
        for key,value in self._dataList.items():
            html_data = html.xpath(value)
            print(key+":"+html_data[0].text)
        pass

    def getPriceData(self):
        "https://eniu.com/chart/pricea/sz000001/t/all"
        url = "https://eniu.com/chart/pricea/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'price'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_price_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)


    def getPEAData(self):
        "https://eniu.com/chart/pea/sz000001/t/all"
        url = "https://eniu.com/chart/pea/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'pe_ttm'
        #     insertSql = "INSERT INTO stoke_pea_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'pe_ttm'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_pea_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)



    def getPbData(self):
        "https://eniu.com/chart/pba/sz000001/t/all"
        url = "https://eniu.com/chart/pba/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'pb'
        #     insertSql = "INSERT INTO stoke_pb_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'pb'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_pb_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)


    def getguxiData(self):
        "https://eniu.com/chart/dva/sz000001/t/all"
        url = "https://eniu.com/chart/dva/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'dv'
        #     insertSql = "INSERT INTO stoke_guxi_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'dv'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_guxi_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    
    def getvalueData(self):
        "https://eniu.com/chart/marketvaluea/sz000001"
        url = "https://eniu.com/chart/marketvaluea/{}".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'market_value'
        #     insertSql = "INSERT INTO stoke_value_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'market_value'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_value_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    def getRoeaData(self):
        "https://eniu.com/chart/roea/sz000001/q/4"
        url = "https://eniu.com/chart/roea/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'roe'
        #     insertSql = "INSERT INTO stoke_roe_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)

        #     price_in = 'roa'    
        #     insertSql = "INSERT INTO stoke_roa_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'roe'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_roa_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    
    def getProfitData(self):
        "https://eniu.com/chart/profita/sz000001/q/4"
        url = "https://eniu.com/chart/profita/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'profit'
        #     insertSql = "INSERT INTO stoke_profit_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'profit'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_profit_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    def getIncomeData(self):
        "https://eniu.com/chart/incomea/sz000001/q/4"
        url = "https://eniu.com/chart/incomea/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'income'
        #     insertSql = "INSERT INTO stoke_income_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'income'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_income_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    def getprofitkfData(self):
        "https://eniu.com/chart/profitkfa/sz000001/q/4"
        url = "https://eniu.com/chart/profitkfa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'profit_kf'
        #     insertSql = "INSERT INTO stoke_profit_kf_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'profit_kf'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_profit_kf_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)


    def getdebtratioData(self):
        "https://eniu.com/chart/debtratioa/sz000001/q/4"
        url = "https://eniu.com/chart/debtratioa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'asset'
        #     insertSql = "INSERT INTO stoke_debtratio_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'asset'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_debtratio_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)


    def getcashflowData(self):
        "https://eniu.com/chart/cashflowa/sz000001/q/4"
        url = "https://eniu.com/chart/cashflowa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'cash_flow'
        #     insertSql = "INSERT INTO stoke_cashflow_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'cash_flow'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_cashflow_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)

    def getgrossprofitData(self):
        "https://eniu.com/chart/grossprofitmargina/sz000001/q/4"
        url = "https://eniu.com/chart/grossprofitmargina/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        # for d in range(0, len(params_json['date'])):
        #     price_in = 'net_profit_margin'
        #     insertSql = "INSERT INTO stoke_grossprofit_history VALUES (0,'{}','{}','{}')"\
        #                 .format(str(params_json['date'][d]),str(params_json[price_in][d]),str(self.storkid))
        #     try:
        #         db.query(insertSql)
        #     except Exception as e:
        #         print(e)
        data = []
        for d in range(0, len(params_json['date'])):
            price_in = 'net_profit_margin'
            data.append({'id':0 , 'date':str(params_json['date'][d]),'value':str(params_json[price_in][d]),'stokeid':str(self.storkid)})
        db.bulk_query("insert stoke_grossprofit_history(id,date, value,stokeid) values(:id, :date, :value,:stokeid)", data)



    def getCawuData(self):
        "https://eniu.com/table/cwzba/sz000001/q/4"
        url = 'https://eniu.com/table/cwzba/'+self.storkid+"/q/4"
        strhtml = requests.get(url)        #Get方式获取网页数据
        # html = etree.HTML(strhtml.text)
        params_json = json.loads(strhtml.text)
        # with open("{}财务.txt".format(self.storkid),'w') as f:
        #     json.dump(strhtml.text,f)
        if len(params_json) == 0:
            return

        data = []
        for p in params_json:
            if p['keyName'].find('<')!=-1:
                continue
            for k,v in  p.items():
                if k == 'keyName':
                    continue
                v_temp = v
                if type(v) == type("str") and v.find('<')!=-1:
                    saxParse = xml.sax.make_parser()
                    saxParse.setFeature(xml.sax.handler.feature_namespaces, 0)  # 关闭命名解析
                    Handler = myXmlHandler()
                    xml.sax.parseString(v,Handler)
                    v_temp = Handler.CurrentData
                # insertSql = "INSERT INTO stoke_caiwu_history VALUES (0,'{}','{}','{}','{}')"\
                #             .format(str(k),str(v_temp),str(self.storkid)
                #             ,str(p['keyName']))
                data.append({'id':0 , 'date':str(k),
                        'value':str(v_temp),
                        'stokeid':str(self.storkid),
                        'caiwutype':str(p['keyName'])})
                # try:
                #     db.query(insertSql)
                # except Exception as e:
                #     print(e)

        db.bulk_query("insert stoke_caiwu_history(id,date, value,stokeid,caiwutype) values(:id, :date, :value,:stokeid,:caiwutype)", data)

    def done(self):
        insertSql = "UPDATE main_list set done = 'ok' where stock_id='{}'"\
        .format(str(self.storkid))
        try:
            db.query(insertSql)
        except Exception as e:
            print(e)
        pass

def getAlldata(stoke_id):
    s = stork(stoke_id)
    print('stoke_id:'+ stoke_id)
    s.getData()
    print('getPriceData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getPriceData()
    print('getPEAData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getPEAData()
    print('getPbData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getPbData()
    print('getguxiData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getguxiData()
    print('getvalueData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getvalueData()
    print('getRoeaData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getRoeaData()
    print('getProfitData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getProfitData()
    print('getIncomeData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getIncomeData()
    print('getprofitkfData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getprofitkfData()
    print('getdebtratioData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getdebtratioData()
    print('getcashflowData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getcashflowData()
    print('getgrossprofitData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getgrossprofitData()
    print('getCawuData:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.getCawuData()
    print('end:'+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    s.done()
    time.sleep(5)

def getStoke():
    Sql = "select * from main_list where done!='ok'"
    try:
        dataList = db.query(Sql)
    except Exception as e:
        print(e)
    # print(len(dataList))
    dd = dataList.as_dict()
    # print(dd[0])
    # {'id': None, 'stock_abbr': 'pfyh', 'stock_id': 'sh600000', 'stock_name': '浦发银行', 'stock_number': '600000', 
    # 'stock_pinyin': 'pufayinhang', 'dt': datetime.datetime(2021, 4, 23, 8, 21, 30)}
    for d in dd:
        getAlldata(d['stock_id'])

# getStoke()
getAlldata('sh600000')