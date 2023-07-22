# 入力、変数等の作成
N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
diff = 0
check = False

# AとBの各インデックスごとの差の絶対値とKの偶奇が同じ and K >= diff ならばYes
for i in range(N):
    diff += abs(A[i] - B[i])
if K % 2 == diff % 2 and K >= diff :
    check = True

if check:
    print("Yes")
else:
    print("No")