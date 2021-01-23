import requests #외부 라이브러리인 requests를 다운받는다.
indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50")
print(indeed_result)    #response [200]이라는 값이 나온다. ==okay
print(indeed_result.text)   #html 전부를 출력한다.

#가져온 html에서 정보를 추출해야 한다.
#beautiful soup을 사용하여 html에서 정보를 추출한다.
#외부 라이브러리 이기 때문에 설치해 준다.



