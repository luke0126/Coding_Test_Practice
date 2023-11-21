# 백준 20310번 - 타노스

S = input()
z_count, o_count = S.count('0') // 2, S.count('1') // 2
check = [True] * len(S)

for i, char in enumerate(S):
    if o_count > 0 and char == '1':
        o_count -= 1
        check[i] = False

for i in range(len(S) - 1, -1, -1):
    if z_count > 0 and S[i] == '0':
        z_count -= 1
        check[i] = False

res = ''.join(S[i] for i, is_true in enumerate(check) if is_true)
print(res)
