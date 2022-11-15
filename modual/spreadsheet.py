import gspread
from oauth2client.service_account import ServiceAccountCredentials

import os
# django에서 추가한 모듈이 아닌 임의의 폴더에서 models을 사용하려고 하는 경우 6 - 10줄을 models import 위에 선언해야함
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myPet.settings")

import django

django.setup()

from hospital.models import Hospital

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
json_file_name = 'mypet-367204-ba6afc1bb3db.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1SngP4jSQHzu3PjNhoueg04ns8vl_U0IEZt5jrkgP7Xg/edit#gid=0'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('병원')

cell_data = worksheet.acell('B1').value
location1 = worksheet.col_values(1)[1:]
location2 = worksheet.col_values(2)[1:]
location = []
for i in range(0, len(location1)):
    data = location1[i] + ' ' + location2[i]
    location.append(data)
# for i in cell_data:
#     loca = i + location2[i]
name = worksheet.col_values(3)[1:]
hour = worksheet.col_values(4)[1:]
break_hour = worksheet.col_values(5)[1:]
animal = worksheet.col_values(6)[1:]
service = worksheet.col_values(7)[1:]
number = worksheet.col_values(8)[1:]
address = worksheet.col_values(9)[1:]
subway = worksheet.col_values(10)[1:]
website = worksheet.col_values(12)[1:]
# 현재 상황: 스프레드시트에서 칼럼별로 데이터를 list로 가져오고 있음
# 문제: 가져온 list의 길이가 일정하지 않음
# 원인: 없는 데이터를 ''로 가져오는게 아니라 뒷부분이 없으면 더 이상 가져오지 않음
# 결과: list index out of range 발생
# 해결 방법: 부족한 칼럼 list의 길이를 ''을 넣어서 채워줘야함
for i in range(0, len(name)):
    hos_id = str(i + 1) + "1"
    # 코드 4자리 채우기
    id = hos_id.zfill(4)
    hos = Hospital(hos_id=id, name=name[i], address=address[i], location=location[i], animal=animal[i],
                   break_time=break_hour[i], facilitly=service[i], link=website[i], open_time=hour[i], subway=subway[i],
                   number=number[i])
    hos.save()
print(len(break_hour))
print(len(service))
print(len(website))
print(len(hour))
print(len(subway))
print(cell_data)
print(location)
print(name)
print(hour)
print(break_hour)
print(animal)
print(service)
print(address)
print(subway)
print(website)
