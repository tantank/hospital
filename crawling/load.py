# hospital1~10을 load해서 hospital_all이라는 하나의 json파일을 만듦. flatten까지 해봄
# 포트폴리오인 것을 감안해, 기존의 112500가량 되던 데이터 중, 2.3만개 가량만 사용하기로함
# 지역별로 json파일을 따로 생성
import json
import numpy as np
hospital = []
'''
for i in range(2):
    with open("hospital"+str(i+1)+".json", "r") as json_file:
        st_python = json.load(json_file)
    hospital.append(st_python)

with open("hospital_23000.json", "w", encoding="utf-8") as json_file:
    json.dump(hospital, json_file)
'''
with open("hospital_23000.json","r") as json_file:
    st_python = json.load(json_file)
    hospital.append(st_python)

hospital = np.array(hospital)
hospital = hospital.flatten()
hospital_list = hospital.item(0).keys()
print(hospital)
sidocdnm_list = np.array([])
#sggucdnm_list = np.array([])
city_list = ['강원','경기','경남','경북','광주','대구','대전','부산','서울','세종시','울산','인천','전남','전북',
'충남','충북']

city = []

for i in city_list:
    city.append([])

print(city)
for i in hospital:
    for right in city_list:
        if i.get('sidocdnm') == right:
            city[city_list.index(right)].append(i)
    #x=[]
    #x.append(i.get('sidocdnm'))
    #x.append(i.get('sggucdnm'))
    #sidocdnm_list = np.append(sidocdnm_list,i.get('sidocdnm'))
    #sggucdnm_list = np.append(sggucdnm_list,i.get('sggucdnm'))

# for i in city_list:
#     with open("hospital_"+str(i)+".json", "w", encoding="utf-8") as json_file:
#         json.dump(city[city_list.index(i)], json_file)

#print(np.unique(sidocdnm_list))
#print(np.unique(sggucdnm_list))
