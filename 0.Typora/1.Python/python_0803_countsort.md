### countsorting 방법

>SWEA 4834 카드정렬문제

- 0 ~ 9까지의 카드중 N개의 카드를 중복으로 뽑아 가장 많이 뽑아진 카드와 갯수를 출력

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    cnt = [0] * 10
    max_card = -1
    
    for i in range(N):
        cnt[cards[i]] += 1
    
    for i in range(9, -1, -1):
        if cnt[i] > max_card:
            res = i
            max_card = cnt[i]
    print(f'#{tc} {res} {cnt[res]}')
```

- cnt라는 크기 10인 리스트에 각각의 칸의 index를 카드숫자로 생각하고 주어진 카드리스트를 하나씩 받으며 값과 cnt의 주소가 같으면 cnt의 값에 +1을 추가한다





## 정렬 과정

다음과 같은 *수열 A*를 정렬 해야하는 상황을 생각해봅시다.



![img](python_0803_countsort.assets/2656634B56E7555108)



위 수열을 정렬하면 아래와 같은 *수열 B*를 얻습니다.



![img](python_0803_countsort.assets/2220E94156E7555111)



`Counting Sort`가 어떻게 *수열 A*를 정렬해서 *수열 B*를 얻는지 따라가 봅시다.

1. 첫번째로 각 숫자가 몇번 등장하는지 세어줍니다.

| 숫자      |  0   |  1   |  2   |  3   |  4   |  5   |
| :-------- | :--: | :--: | :--: | :--: | :--: | :--: |
| 등장 횟수 |  3   |  2   |  2   |  3   |  3   |  3   |

> 벌써 **Counting Sort**의 이름에 왜 **Counting**이 들어가있는지 알것 같지 않나요? 이렇게 각 숫자가 몇번 등장했는지 세어주기 때문입니다.
>
> cf) 이 예제만 보면 1번 과정만 하고 벌써 정렬을 다 한 것 같습니다. 각 숫자가 등장한 횟수만큼 작은 순서대로 찍어주면 되기 때문이죠. 그럼 왜 굳이 아래 과정을 할까요?
>
> ![img](python_0803_countsort.assets/2344644356E7555117) 같은 수열을 정렬하는 상황을 생각해보세요. 중간에 등장한 뜬금없이 큰 100이 있어서 3~99까지 무의미한 순회를 해야하죠. 따라서 방금 생각한 방법은 `숫자 크기`에 시간복잡도가 매우 큰 영향을 받으므로 `비효율적`이라는 것을 알 수 있습니다.



## 정리

`Counting Sort` 알고리즘의 시간복잡도는 O(n) 으로 `Quick Sort`보다 훨씬 유리해보입니다. 그러나 `Counting Sort`는 대부분의 상황에서 엄청난 `메모리 낭비`를 야기할 수 있습니다.

누적합 배열에 대한 접근을 O(1)에 달성하기 위해 정렬할 배열에 포함된 숫자의 최댓값 만큼의 메모리를 필요로 합니다. 아까 추가로 예시든 ![img](python_0803_countsort.assets/2626824156E755510D) 배열에 Counting Sort 알고리즘으로 정렬하기 위해서는 누적합 배열의 길이를 100으로 잡는 낭비를 해야합니다. 만약 배열에 최댓값으로 10억이 포함되어 있다면 엄청난 낭비가 되겠죠.

따라서 `Counting Sort`는 위에서든 예시처럼

![img](python_0803_countsort.assets/2554D94E56E7555107)

정렬하는 숫자가 `특정한 범위`(위 예시 : 0~5) 안에 있을 때 사용하게 됩니다.



`Counting Sort`를 대표적으로 활용하는 사례는 `26개의 알파벳`으로 이루어진 문자열에서 `Suffix Array`를 얻는 경우인데 이때 Counting Sort를 사용하기 때문에 일반적인 Sort를 사용해서 Suff



출처: https://bowbowbow.tistory.com/8 [멍멍멍]