# 백준 1041 - 주사위

n = int(input())
nums = list(map(int, input().split()))
answer = 0
if n == 1: # 쌓은 주사위가 한 개라면 보이는 면은 주사위의 바닥면을 제외한 나머지다. 값을 최소화 하려면 가장 큰 수를 안 보이게 하면 된다.
    nums.sort()
    answer = sum(nums[:5])
    print(answer)

else:
    # 합이 최소가 되도록 쌓기 위해서 보이는 주사위의 작은 값들을 보일 수 있는 면을 선택한다.
    minSide = [min(nums[0], nums[5]), min(nums[1], nums[4]), min(nums[2], nums[3])]
    minSide.sort()

    # 면이 보이는 수들은 최대한 작은 수로 보여지게 하고 보여지는 면 수 만큼 곱해주면 보이는 주사위 면의 값들이 최소가 된다.
    # n X n X n인 정육면체에서 세 면이 보이는 주사위는 맨 윗층 꼭짓점 4개뿐이다.
    threeSide = sum(minSide) * 4
    # 두 면이 보이는 주사위는 맨 아랫층 꼭짓점에 있는 주사위 4개 + 가장 아랫층을 제외한 층에서의 꼭짓점을 제외한 모서리에 껴 있는 주사위 (n-2)*8개다.
    twoSide = sum(minSide[:2]) * 4 + sum(minSide[:2]) * (n-2) * 8
    # 한 면이 보이는 주사위는 쌓은 정육면체 각 면에 모서리에 해당하는 주사위를 제외한 주사위 (n-2)(n-2)*5개 + 가장 아랫층에 꼭짓점을 제외한 모서리에 껴 있는 주사위 (n-2)*4개다.
    oneSide = minSide[0]*(n-2)*4 + minSide[0]*(n-2)**2*5

    answer = threeSide + twoSide + oneSide
    print(answer)
