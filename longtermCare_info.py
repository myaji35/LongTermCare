import urllib.request
# 매우 작은 브라우저로 웹사이트의 내용과 정보를 불러올 수 있습니다.
#import requests
# request로 가져온 웹사이트의 html 태그를 파싱하는데 사용합니다.
from bs4 import BeautifulSoup as bs

headers = {'headers':'value'}
url = 'httread'
#        서울   부산  대구  인천  광주  대전  울산  세종  경기  강원  충북  충남  전북  전남  경북  경남  제주
siDo_ = ['11','26','27','28','29','30','31','36','41','42','43','44','45','46','47','48','50']
params={'siDoCd':'11','excelCurrPage':'1'}
response = requests.post(url=url, data=params)

print(url)
page_no = 0
        
def fn_sido_info_page():
    for page_no in ++page_no :   
        params={'siDoCd':'11','excelCurrPage':page_no}
        response = requests.post(url=url, data=params)

        while response.status_code == 200:
            html = bs(response.text, 'html.parser')
            tags = html.select('#ltco_info_list > tbody > tr')
            
            num_ = 0
            info_list_group_no_ = 0
            info_list = []

            for tag in tags:
                num_ = num_ + 1
                #급여종류 0
                text_ = html.select('#ltco_info_list > tbody > tr:nth-child('+str(num_)+') > td:nth-child(2)' )[0]
                text_ = text_.text.replace("상세보기","").strip()     #좌우 공백제거
                info_list.append(text_)
                #평가결과 0
                text_ = html.select('#ltco_info_list > tbody > tr:nth-child('+str(num_)+') > td:nth-child(3)' )[0]
                text_ = text_.text.replace("상세보기","").strip()     #좌우 공백제거
                info_list.append(text_)
                #기관명 0
                text_ = html.select('#ltco_info_list > tbody > tr:nth-child('+str(num_)+') > td:nth-child(4)' )[0]
                text_ = text_.text.replace("상세보기","").strip()     #좌우 공백제거
                info_list.append(text_)
                #전화번호 0
                text_ = html.select('#ltco_info_list > tbody > tr:nth-child('+str(num_)+') > td:nth-child(9)' )[0]
                text_ = text_.text.replace("상세보기","").strip()     #좌우 공백제거
                info_list.append(text_)
                #주소 0
                text_ = html.select('#ltco_info_list > tbody > tr:nth-child('+str(num_)+') > td:nth-child(11)' )[0]
                text_ = text_.text.replace("상세보기","").strip()     #좌우 공백제거
                info_list.append(text_)
        print(page_no)
    info_list_group.append(info_list)
    
    print(info_list_group)

info_list_group = []
fn_sido_info_page()
