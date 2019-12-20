#data.go.kr -> 비급여진료비정보서비스api를 crawling 후 저장. 100rows를 1126page 크롤링해야하기에, 10번에 나눠서 크롤링함

import requests
from bs4 import BeautifulSoup
import json



url_test = "http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemHospList2?serviceKey="+public_key

result = requests.get(url_test)

bs_obj = BeautifulSoup(result.content, "html.parser")
total = bs_obj.totalcount.text
hospital = []
numOfRows=100
total_range = int(int(int(total)/numOfRows)/10)
for cnt in range(10):
    for i in range(total_range):
        pageNo = (i+1)+(cnt*total_range)
        url = "http://apis.data.go.kr/B551182/nonPaymentDamtInfoService/getNonPaymentItemHospList2?" \
              "serviceKey="+public_key \
              "&numOfRows=100&pageNo="+str(pageNo)
        result = requests.get(url)

        bs_obj = BeautifulSoup(result.content, "html.parser")
        items = bs_obj.body.items

        for item in items:
            data = {'yadmnm': item.yadmnm.text, 'clcdnm': item.clcdnm.text, 'sidocdnm': item.sidocdnm.text,
                    'sggucdnm': item.sggucdnm.text,
                    'date': item.adtfrdd.text, 'maxprc': item.maxprc.text, 'minprc': item.minprc.text,
                    'url': item.urladdr.text, 'npaykornm': item.npaykornm.text}
            hospital.append(data)

    with open("hospital"+str((cnt+1))+".json", "w",encoding="utf-8") as json_file:
        json.dump(hospital, json_file)
        hospital=[]
