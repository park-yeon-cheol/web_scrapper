import requests #외부 라이브러리인 requests를 다운받는다.
from bs4 import BeautifulSoup   #BeautifulSoup를 import 해준다.
indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50")
#print(indeed_result)    #response [200]이라는 값이 나온다. ==okay
#print(indeed_result.text)   #html 전부를 출력한다.
indeed_soup= BeautifulSoup(indeed_result.text,"html.parser")
#print(indeed_soup)
pagination = indeed_soup.find("div",{"class":"pagination"}) #indeed 사이트 소스를 보니 pagination은 div, class이름은 pagination으로 설정되어 있어서 관련된 것들을 찾아주었다.
#print(pagination)
pages=pagination.find_all('a')  #pagination중 anchor에 해당하는 부분을 모두 찾는다.
#print(pages)
spans=[]
for page in pages:
    spans.append(page.find("span")) #찾은 page에서 이제 span을 찾는다.
#print(spans[:-1])
spans=spans[:-1]    #마지막에 next에 해당하는 버튼이 따라오기 때문에 마지막을 빼고 spans에 저장한다.
#가져온 html에서 정보를 추출해야 한다.
#beautiful soup을 사용하여 html에서 정보를 추출한다.
#외부 라이브러리 이기 때문에 설치해 준다.



