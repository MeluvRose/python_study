# CONTROL FLOW

## IF/ELSE/ELIF

- IF
  - `if (Condition):`
    <br/>
    ex)
    ```python
    if 10 < 5:
      print("Correct")
    ```
- ELSE

  - ex)

    ```python
     correct = False

    if correct:
        print("Entered")
    else
        print("Wrong Password")
    ```

- ELIF

  - ex)

    ```python
      x = 10;

      if x > 10:
          print("X is greater than 10")
      elif x < 10:
          print("X is less than 10")
      else:
          print("X is 10")
    ```

## AND/OR

- AND(`and`)

  1. `True and True >> True`
  2. `True and False >> False`

- OR(`or`)
  1. `True or True >> True`
  2. `True or False >> True`
  3. `False or False >> False`

## WHILE

- `while (Condition):`
- ex)

  ```python
    distance = 0

    while distance < 20:
        print("I'm running:", distance, "Km")
        distance = distance + 1

    print("goal!!!")
  ```

## Etc.

- Standard Library
  - (거의) 모든 Programming Language에 존재
