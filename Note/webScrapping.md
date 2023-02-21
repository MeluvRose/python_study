# WebScrapping

## BeautifulSoup

- pip install beautifulsoup4

- 웹 스크래핑은 웹사이트에서 데이터를 긁어오는 것이지만, 데이터에 접근하기를
  허용하지 않는 사이트들이 있다.

  1. 모든 사이트가 사용가능하지 X
  2. 스크랩한 데이터를 상업적으로 사용할 경우, 법적인 문제가 발생할 수도

- making 'soup' with parser

  `soup = BeautifulSoup(markup, "html.parser")`

- soup.find_all()

  `soup.find_all("a", attrs={"class": "sister"}) <Attrs>`

  `soup.find_all("a", class_="sister") <CSS Class>`
  `soup.find_all(class_=re.compile("itl"))`

- Transfer HTML Tag to 'Beautifulsoup' entity

- (Beautifulsoup element).string()

- find...() property 'recursive' (boolean)

  - `False`일 경우, 조건에 맞는 tag이더라도, 바로 다음 깊이의 tag까지만을 탐색

-

## Keyword Arguments

- ex)

  ```python
  def sayHello(name, age):
      print(f"Hello {name}, you are {age} years old")
  ```

  라는 함수가 있다면, 순서에 맞게

  `say_hello("nico", 12)`

  라고 불러올 수도 있지만

  `say_hello(age=12, name="nico")`

  Parameter에 맞게 argument를 직접 입력한다면, 순서에 신경쓰지 않을 수 O

## Selenium

- 코드를 사용해서 브라우저를 자동화 하고 제어할 수 있는 방법은 'Selenium'이라는 것을 사용하면 된다.

- request.get()을 이용한 호출의 상태코드 '403' 응답에 대한 대처법 중 1개 이기도 하다.
  (강의에선 'indeed'가 request를 이용한 접근을 차단)

- setting guide

  1. install chrome driver
  2. `pip i selenium` and install chromedriver (or `pip i webdriver_manager`)

  - IF, webdriver_manager를 받았다면,

    `chrome_driver = ChromeDriverManager().install()`

    위의 함수 실행으로, chromeDriver 설치 및 파일 경로를 받아올 수 있다.

  3.  (`DevToolsActivePort file doesn't exist`)과 같은 error를 피하기 위해,
      다음과 같이 option을 설정

          ```python
          options = Options()
          options.add_argument("--no-sandbox")
          options.add_argument("--disable-dev-shm-usage")

          chrome_driver = ChromeDriverManager().install()
          browser = webdriver.Chrome(
          service=Service(ChromeDriverManager().install()), options=options
          )
          ```

  4.  이후 `browser`를 request 라이브러리처럼 사용가능

- selenium의 webdriver 방식의 사용법은 공식 문서 참고
  (https://www.selenium.dev/documentation/webdriver/)

- 한글 깨짐 방지 : 한글 전용 폰트(ex) NanumFont)를 설치 및 적용할 것(mkdir + mv)
  - path : /usr/share/fonts/truetype

## Etc

- (크지 않은) 배열의 각 요소를 변수처럼 사용하고 싶을 때,

  ```python
    list_of_numbers = [1,2,3]

    // (1)
    first = list_of_numbers[0]
    second = list_of_numbers[1]
    third = list_of_numbers[2]

    // (2)
    first, second, third = list_of_numbers
  ```

- `None`
