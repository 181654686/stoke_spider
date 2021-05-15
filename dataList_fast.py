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
        self.dayData = {}
        self.yearData = {}
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
        
        for d in range(0, len(params_json['date'])):
            price_in = 'price'
            if str(params_json['date'][d]) in self.dayData:
                self.dayData[str(params_json['date'][d])]['price'] = str(params_json[price_in][d])
            else:
                self.dayData[str(params_json['date'][d])] = {'price':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    def getPEAData(self):
        "https://eniu.com/chart/pea/sz000001/t/all"
        url = "https://eniu.com/chart/pea/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return

        for d in range(0, len(params_json['date'])):
            price_in = 'pe_ttm'
            if str(params_json['date'][d]) in self.dayData:
                self.dayData[str(params_json['date'][d])]['pea'] = str(params_json[price_in][d])
            else:
                self.dayData[str(params_json['date'][d])] = {'pea':str(params_json[price_in][d]),'stock_id':str(self.storkid)}



    def getPbData(self):
        "https://eniu.com/chart/pba/sz000001/t/all"
        url = "https://eniu.com/chart/pba/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return

        for d in range(0, len(params_json['date'])):
            price_in = 'pb'
            if str(params_json['date'][d]) in self.dayData:
                self.dayData[str(params_json['date'][d])]['pb'] = str(params_json[price_in][d])
            else:
                self.dayData[str(params_json['date'][d])] = {'pb':str(params_json[price_in][d]),'stock_id':str(self.storkid)}


    def getguxiData(self):
        "https://eniu.com/chart/dva/sz000001/t/all"
        url = "https://eniu.com/chart/dva/{}/t/all".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        
        for d in range(0, len(params_json['date'])):
            price_in = 'dv'
            if str(params_json['date'][d]) in self.dayData:
                self.dayData[str(params_json['date'][d])]['guxi'] = str(params_json[price_in][d])
            else:
                self.dayData[str(params_json['date'][d])] = {'guxi':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    
    def getvalueData(self):
        "https://eniu.com/chart/marketvaluea/sz000001"
        url = "https://eniu.com/chart/marketvaluea/{}".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        for d in range(0, len(params_json['date'])):
            price_in = 'market_value'
            if str(params_json['date'][d]) in self.dayData:
                self.dayData[str(params_json['date'][d])]['value'] = str(params_json[price_in][d])
            else:
                self.dayData[str(params_json['date'][d])] = {'value':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    def getRoeaData(self):
        "https://eniu.com/chart/roea/sz000001/q/4"
        url = "https://eniu.com/chart/roea/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        for d in range(0, len(params_json['date'])):
            price_in = 'roe'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['roe'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'roe':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

            price_in = 'roa'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['roa'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'roa':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    
    def getProfitData(self):
        "https://eniu.com/chart/profita/sz000001/q/4"
        url = "https://eniu.com/chart/profita/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return

        for d in range(0, len(params_json['date'])):
            price_in = 'profit'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['profit'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'profit':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    def getIncomeData(self):
        "https://eniu.com/chart/incomea/sz000001/q/4"
        url = "https://eniu.com/chart/incomea/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
 
        for d in range(0, len(params_json['date'])):
            price_in = 'income'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['income'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'income':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    def getprofitkfData(self):
        "https://eniu.com/chart/profitkfa/sz000001/q/4"
        url = "https://eniu.com/chart/profitkfa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        for d in range(0, len(params_json['date'])):
            price_in = 'profit_kf'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['profit_kf'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'profit_kf':str(params_json[price_in][d]),'stock_id':str(self.storkid)}


    def getdebtratioData(self):
        "https://eniu.com/chart/debtratioa/sz000001/q/4"
        url = "https://eniu.com/chart/debtratioa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        for d in range(0, len(params_json['date'])):
            price_in = 'asset'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['debtratio'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'debtratio':str(params_json[price_in][d]),'stock_id':str(self.storkid)}


    def getcashflowData(self):
        "https://eniu.com/chart/cashflowa/sz000001/q/4"
        url = "https://eniu.com/chart/cashflowa/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return
        for d in range(0, len(params_json['date'])):
            price_in = 'cash_flow'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['cashflow'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'cashflow':str(params_json[price_in][d]),'stock_id':str(self.storkid)}

    def getgrossprofitData(self):
        "https://eniu.com/chart/grossprofitmargina/sz000001/q/4"
        url = "https://eniu.com/chart/grossprofitmargina/{}/q/4".format(self.storkid)
        strhtml = requests.get(url)        #Get方式获取网页数据
        params_json = json.loads(strhtml.text)
        if len(params_json) == 0:
            return

        for d in range(0, len(params_json['date'])):
            price_in = 'net_profit_margin'
            if str(params_json['date'][d]) in self.yearData:
                self.yearData[str(params_json['date'][d])]['grossprofit'] = str(params_json[price_in][d])
            else:
                self.yearData[str(params_json['date'][d])] = {'grossprofit':str(params_json[price_in][d]),'stock_id':str(self.storkid)}



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

                data.append({'id':0 , 'date':str(k),
                        'value':str(v_temp),
                        'stokeid':str(self.storkid),
                        'caiwutype':str(p['keyName'])})

        db.bulk_query("insert stoke_caiwu_history(id,date, value,stokeid,caiwutype) values(:id, :date, :value,:stokeid,:caiwutype)", data)

# CREATE TABLE `gupiao`.`stoke_day_history` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `day` VARCHAR(45) NULL,
#   `guxi` VARCHAR(45) NULL,
#   `pea` VARCHAR(45) NULL,
#   `price` VARCHAR(45) NULL,
#   `value` VARCHAR(45) NULL,
#   `pb` VARCHAR(45) NULL,
#   PRIMARY KEY (`id`));

    def insertDayData(self):
        data = []
        for k,v in self.dayData.items():
            guxi=''
            pea=''
            price=''
            value=''
            pb=''

            if 'guxi' in v:
                guxi = v['guxi']
            if 'pea'in v:
                pea = v['pea']
            if 'price' in v:
                price = v['price']
            if 'value' in v:
                value = v['value']
            if 'pb' in v:
                pb = v['pb']

            data.append({'id':0,'day':k, 'guxi':guxi,'pea':pea,
            'price':price,'value':value,'pb':pb,'stoke_id':self.storkid})
        db.bulk_query("insert stoke_day_history(id,day, guxi,pea,price,value,pb,stoke_id) \
            values(:id, :day, :guxi,:pea,:price,:value,:pb,:stoke_id)", data)
        pass

# CREATE TABLE `gupiao`.`stoke_year_history` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `years` VARCHAR(45) NULL,
#   `cashflow` VARCHAR(45) NULL,
#   `debtratio` VARCHAR(45) NULL,
#   `grossprofit` VARCHAR(45) NULL,
#   `income` VARCHAR(45) NULL,
#   `profit` VARCHAR(45) NULL,
#   `profit_kf` VARCHAR(45) NULL,
#   `roa` VARCHAR(45) NULL,
#   `roe` VARCHAR(45) NULL,
#   PRIMARY KEY (`id`));

    def insertYearData(self):
        data = []
        for k,v in self.yearData.items():
            cashflow=''
            debtratio=''
            grossprofit=''
            income=''
            profit=''
            profit_kf =''
            roa=''
            roe = ''
            if 'cashflow' in v:
                cashflow = v['cashflow']
            if 'debtratio' in v:
                debtratio = v['debtratio']
            if 'grossprofit' in v:
                grossprofit = v['grossprofit']
            if 'income' in v:
                income = v['income']
            if 'profit' in v:
                profit = v['profit']
            if 'profit_kf' in v:
                profit_kf = v['profit_kf']
            if 'roa' in v:
                roa = v['roa']            
            if 'roe' in v:
                roe = v['roe']

            data.append({'id':0,'years':k, 'cashflow':cashflow,'debtratio':debtratio,
            'grossprofit':grossprofit,'income':income,'profit':profit,
            'profit_kf':profit_kf,'roa':roa,'roe':roe,'stoke_id':self.storkid})
        db.bulk_query("insert stoke_year_history(id,years, cashflow,debtratio,grossprofit,income,profit,profit_kf,roa,roe,stoke_id) \
            values(:id,:years,:cashflow,:debtratio,:grossprofit,:income,:profit,:profit_kf,:roa,:roe,:stoke_id)", data) 

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

    s.insertDayData()
    s.insertYearData()

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

getStoke()
# getAlldata('sh600000')