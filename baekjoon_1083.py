# 백준 1083 - 소트

n = int(input())
nums = list(map(int, input().split()))
s = int(input())

# 사전 뒷순서로 나타내야한다. 즉, 배열 앞쪽의 숫자가 크게 하라는 뜻이다.
for i in range(n):
    if s > 0: # 바꿀 수 있는 기회가 남아있다면
        # 남아있는 기회 중에서 앞 쪽으로 가져올 수 있는 최대값을 찾아야한다. s번의 기회가 남았다면 현위치에서 s+1까지가 바꿀 수 있는 범위이다.
        # 이때, index를 넘어가는 일을 방지해야한다. s값을 다 쓸 필요가 없기 때문에 범위는 nums 배열의 최대 범위까지로 하면 된다.
        if i + s + 1 < n:
            maximum = max(nums[i:i + s + 1])
        else:
            maximum = max(nums[i:n])
        max_index = nums.index(maximum) # 가장 큰 값의 index를 찾는다.
        for j in range(max_index, i, -1): # 바꿀 수 있는 가장 큰 값을 앞으로 보내기 위해 교환을 계속 해준다.
            nums[j], nums[j-1] = nums[j-1], nums[j]
        s -= (max_index - i) # 바꾸려고 하는 큰 값을 i까지 오려면 (max_index - i)번 만큼 교환한다.
    else:
        break

print(*nums)
