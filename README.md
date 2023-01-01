# week-07

-   2022.12.26 ~ 2023.01.01

# Docs

_[Python Blog](https://ejaee.github.io/Python-coding-test/)_

## 1. 01_2346.py

_[풍선 터뜨리기](https://www.acmicpc.net/problem/2346)_

**Approach**

- Input value && save Circular Data Structure

- Stored data have to change the order freely

    : `depue`

- Stored data's initial location index must be maintained

    : `enumerate()`

- Only the contents should be printed out

    : `' '.join(map())`

I studied ...

- how to casting
- enumerate()
- depue()
- init list
- split()
- join()
- map()

## 2. 02_13335.py

_[트럭](https://www.acmicpc.net/problem/13335)_

**Approach**

- Input value && save an ordered list
    
    : `list`

- A set situation and conditions

    : `simulation / implamentation`

I studied ...

- sum()
- how to get list value

## 3. 03_17479.py

_[정식당](https://www.acmicpc.net/problem/17479)_

**Approach**

- Input fixed value(menu list) && This is standard {menu_name: price}

    : `dict`

- Input time over issue

    : `sys.stdin.readline ... `

I studied ...

- dict
  - init -> `dict = {} or dict = dict()`
  - save -> dict[arr[0]] = arr[1]
- readline
- rstrip()
- `&` != `and`

## 4. 04_16562.py

_[친구비](https://www.acmicpc.net/problem/16562)_

**Approach**

- Input consecutive integer ...

    : `list`

 - Check connectivity between nodes

    : `union - find Algorithms`

I studied ...

- union - find Algorithms

## 🤓 mandatory part

-   [풍선 터뜨리기](https://www.acmicpc.net/problem/2346)
-   [트럭](https://www.acmicpc.net/problem/13335)
-   [정식당](https://www.acmicpc.net/problem/17479)
-   [친구비](https://www.acmicpc.net/problem/16562)
-   [뒤집기 3](https://www.acmicpc.net/problem/1464)

이번주는 가장 기초적인 문제들만 뽑았습니다. 그래서 DFS & BFS는 다음주까지 할 예정입니다.

## 🧐 bonus part

한번 도전해볼만 한 문제 -> 저번 주에 했던거 복습 + 심화

-   [brainf*ck](https://www.acmicpc.net/problem/2733)
-   [소수의 곱](https://www.acmicpc.net/problem/2014)
