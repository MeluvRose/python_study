# Data structure

데이터를 구조화 하고 싶을 때 사용 ( ex) list )

## Methods

- 어떤 것에도 결합되어 있지 않고, 기능을 구현(실행)할 수 있는 함수를 'function'
- 데이터(변수) 뒤에 결합/연결 되어 있는 특정 함수를 'method'라 한다.
- method는 결합되어 있는 데이터에 변화를 줄 수 있다.
  (update, delete)

## List

- `[..., ]`
- 같은 List 내에 서로 다른 type의 데이터를 보관할 수 있다.
  - List 내에 List가 있는 것도 가능
- mutable

## Tuple

- `(...,)`
- Immutable
  - 선언된 데이터의 변화를 줄 수 X

⭐ 순서(index)가 있는 데이터를 뒤에서 앞으로 접근하는 것도 가능하다.

## Dict(ionary)

- ```python
  dict = {
      'keyA' : value,
      'keyB' : value,
      ...
  }
  ```
- (key-value) pair Data

  - 각 Data는 key or value 에 대칭되어 있는 것에 접급

- mutable

## Loops

- for
  - `for ... in (data):`
  - 보통, 집합 데이터의 변수명은 '복수형'을 그리고 그 내부의 접근하는
    Placeholder 명은 '단수형'을 사용
    ex) `for movie in movies`, `for website in websites`, ...
    </br>

## Etc

- (String) formatting

  - `f"blah blah blah {(valuable)}"`
  - ...

- Pypi(pypi.org) : standard library에 포함되어 있지 않은 것들
