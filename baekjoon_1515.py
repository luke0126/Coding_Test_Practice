# 백준 1515번 - 수 이어 쓰기

# 아이디어: 1부터 입력값의 0번째 위치의 값과 비교하면서 결과값을 찾는다.

answer = []
nums = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == '':
        print(i)
        break