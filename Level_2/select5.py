# 入力、変数等の作成
N, P, Q = map(int,input().split())

# 組み合わせの全探索
# Nの最大値が100のため、計算量が100**5=10億となりそうだが、
# 組み合わせのため実際の計算量は最大で10億/5!=10億/120≒1千万となり、ゆうに計算できる
from itertools import combinations
A = list(map(int,input().split()))
ans = 0
for a, b, c, d, e in combinations(A, 5):
    # a * b * c * d * e % P == Q と同じだが、こちらの場合整数が2**63を超えてしまい、
    # 計算が途端に遅くなるためTLEとなる
    if a % P * b % P * c % P * d % P * e % P == Q: 
        ans += 1

print(ans)