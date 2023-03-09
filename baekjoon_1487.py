# 백준 1487
# 문제
# 세준이는 오랜 연구기간 끝에 신상품을 내놓았다. 세준이는 오랜 시간이 걸린 만큼 이 상품을 최대 이익에 팔려고 한다.
# 세준이는 이 상품을 사려고 하는 사람들이 총 몇 명이나 되는지 알아봤다. 무려 N명이나 살 의향을 보였다. 각각의 사람은 자기가 지불할 생각이 있는 최대 한도가 있다. 따라서, 어떤 사람이 20원까지 지불할 생각이 있는데, 세준이가 가격을 30원으로 책정하면 이 사람은 절대 안 살 것이고, 15원으로 책정하면 이 사람은 이 상품을 15원에 살 것이다. (단, 세준이가 안 팔수도 있다.)
# 그리고, 세준이는 각각의 사람에게 배달하는 비용이 얼마나 걸리는 지 알고 있다.
# N명의 사람과, 각각의 사람이 지불할 용의가 있는 최대 금액과 배송비가 주어졌을 때, 세준이의 이익을 최대로 하는 가격을 출력하는 프로그램을 작성하시오.

num = int(input(''))
customer = []  # 손님이 제시한 가격 및 배송비
benefit = []  # 각 가격 당 얻을 수 있는 이익

for i in range(num):
    price, fee = map(int, input().split())
    info = [price, fee]
    customer.append(info)

customer.sort(key=lambda x: x[0])  # 이익이 최대인 가격이 여러 개면 가장 낮은 가격을 출력해야 하므로 제시한 가격을 오름차순으로 정렬함

for i in range(num):
    cost = customer[i][0]
    earn = 0
    for j in range(num):
        if cost <= customer[j][0]:
            if cost - customer[j][1] >= 0:
                earn = earn + cost - customer[j][1]
    benefit.append(earn)

if max(benefit) <= 0:  # 어떤 가격으로 팔아도 이익을 남길 수 없으면 0으로 출력해야 하므로 제시한 가격에 대한 이익들이 모두 0 이하이면 0으로 출력
    answer = 0
else:
    answer = customer[benefit.index(max(benefit))][0]
print(answer)
