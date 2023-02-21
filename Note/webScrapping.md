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

-
