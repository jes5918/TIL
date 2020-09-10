"""
10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 
평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

10개의 수를 split로 입력받고,
sum함수를 이용해 다 더하고
max와 min 함수를 사용, sum에서 뺀다
len - 2로 나눠서 평균값 출력
"""
T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    print(f'#{tc} {round((sum(nums) - max(nums) - min(nums))/(len(nums)-2))}')
