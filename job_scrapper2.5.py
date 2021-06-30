import requests  # 외부 라이브러리인 requests를 다운받는다.
from bs4 import BeautifulSoup  # BeautifulSoup를 import 해준다.

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def extract_indeed_pages():  # 그 전에 짰던 코드를 함수로 구현
    result = requests.get(URL)
    # print(result)    #response [200]이라는 값이 나온다. ==okay
    # print(result.text)   #html 전부를 출력한다.
    # beautifulSoup = html 추출하는 라이브러리
    soup = BeautifulSoup(result.text,
                         "html.parser")  # BeautifulSoup(html_doc, 'html.parser') -> parser의 종류가 html 이라는 것을 알려줌
    # print(soup)
    pagination = soup.find("div", {
        "class": "pagination"})  # indeed 사이트 소스를 보니 pagination은 div, class이름은 pagination으로 설정되어 있어서 관련된 것들을 찾아주었다. pagination = 숫자 있는 곳
    # print(pagination)
    links = pagination.find_all('a')  # pagination중 anchor에 해당하는 부분을 모두 찾는다.
    # print(pages)
    pages = []
    for link in links[:-1]:
        pages.append(
            int(link.string))  # 찾은 links에서 이제 span을 찾는다. + .string을 통해 span 안에 있는 string만 가져온다. -> link.find("span").string을 해도 되지만 link.string을 해도 된다.
    # print(links.find("span"))   span 가져오기
    # print(pages[:-1])
    # pages=pages[0:-1]    #마지막에 next에 해당하는 버튼이 따라오기 때문에 마지막을 빼고 pages에 저장한다.    =for link in links[:-1]
    # print(pages)    #다른거 다 빼고 페이지 숫자만 나오게 된다.
    # 가져온 html에서 정보를 추출해야 한다.
    # beautiful soup을 사용하여 html에서 정보를 추출한다.
    # 외부 라이브러리 이기 때문에 설치해 준다.
    max_page = pages[-1]  # 마지막 페이지를 출력한다.
    return max_page


def extract_indeed_jobs(
        last_page):  # indeed_pages를 입력받아서 request를 만드는 함수 작성(38~40)번째 줄 내용을 함수로 만들고 50을 LIMIT라는 변수를 만들어서 지정해 준 것
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        print(result.status_code)  # request 성공에 대한 대답이 200개 이기 때문에 200이 5개 나오면 성공적으로 응답한 것이다.
    return jobs


# range(max_page)     #range를 통해 페이지 범위를 찾고 이를 활용하여 for문을 만든다.
# for n in range(max_page):
#     print(f"start={n*50}")      #indeed 값 만큼 곱한다.

last_indeed_pages = extract_indeed_pages()

# print(last_indeed_pages)

indeed_jobs = extract_indeed_jobs(last_indeed_pages)  # request 만들 준비
