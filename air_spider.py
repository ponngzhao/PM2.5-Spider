import requests
import datetime
import urllib.parse
import csv
from bs4 import BeautifulSoup
import threading

class air_spider():
    def __init__(self,city,year):
        self.city = city
        self.year = year
        self.date = year+'-01-01'
        with open(city+'-'+year+'.csv','w',newline='') as csv_file:
            data_file = csv.writer(csv_file)
            data_file.writerow(['城市','日期','AQI指数','空气质量级别','首要污染物'])
    
    def get_url(self):
        url_city = urllib.parse.quote(self.city.encode('gb2312'))
        url1 = "http://datacenter.mep.gov.cn/report/air_daily/report_30days_city.jsp?city="+url_city+"&startdate="
        url2 = "&location=rq"
        url = url1+self.date+url2
        return url
    
    def get_content(self,url):
        response = requests.get(url)
        text = response.text
        return text
    
    def add_date(self):
        now_date = datetime.datetime.strptime(self.date,'%Y-%m-%d')
        delta = datetime.timedelta(days = 29)
        next_date = now_date + delta
        next_date_str = next_date.strftime('%Y-%m-%d')
        self.date = next_date_str

    def get_data(self,content):
        data_list = []
        soup = BeautifulSoup(content,'lxml')
        soup = soup.find_all('tr',style='height:25px;')
        for i in soup:
            temp_list = []
            soup_list = i.find_all('td')
            temp_list.append(soup_list[1].get_text())
            temp_list.append(soup_list[3].get_text())
            temp_list.append(soup_list[4].get_text())
            temp_list.append(soup_list[5].get_text())
            data_list.append(temp_list)
        data_list.pop(0)
        return data_list
    
    def save_csv(self,data_list):
        with open(self.city+'-'+self.year+'.csv','a',newline='') as csv_file:
            data_file = csv.writer(csv_file)
            for i in data_list:
                data_file.writerow([self.city,i[0],i[1],i[2],i[3]])

    def start(self):
        for i in range(13):
            print("*"*50)
            print("正在下载"+self.city+self.year+"年"+str(i+1)+"月数据")
            self.add_date()
            url = self.get_url()
            print("正在下载："+url)
            content = self.get_content(url)
            data = self.get_data(content)
            self.save_csv(data)
            print(self.city+self.year+"年"+str(i+1)+"月数据下載完成")
def start_spider(city,year):
    spider = air_spider(city,year)
    spider.start()
        
def main():
    start_spider("临汾市","2011")
    # threads = []
    # # t1 = threading.Thread(target=start_spider,args=("临汾市","2011"))
    # # threads.append(t1)
    # t2 = threading.Thread(target=start_spider,args=("临汾市","2012"))
    # threads.append(t2)
    # t3 = threading.Thread(target=start_spider,args=("衡水市","2017"))
    # threads.append(t3)
    # t4 = threading.Thread(target=start_spider,args=("衡水市","2012"))
    # threads.append(t4)
    # for i in threads:
    #     i.setDaemon(True)
    #     i.start()
    
    # for j in threads:
    #     j.join()

if __name__ == '__main__':
    main()