# 백준 1684 - 같은 나머지

# 나머지가 같다는 뜻은 숫자들의 차이에 대한 최대공약수를 구하는 것과 같다.
# 이 점을 활용하여 수식을 코드로 바꾸면 된다.
import math

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
sub = []
for i in range(0, len(nums)):
    sub.append(nums[i] - nums[i - 1])

temp = sub[0]
for i in range(1, len(sub)):
    temp = math.gcd(temp, sub[i])

answer = temp
print(answer)
