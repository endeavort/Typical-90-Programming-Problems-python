# 入力、変数等の作成
n = int(input()) # 生徒の数
c, score = [0] * n, [0] * n
for i in range(n):
    c[i], score[i] = map(int,input().split())

one = [0] * (n + 1) # １組の累積和
two = [0] * (n + 1) # ２組の累積和

# 累積和を取っていく
# 各クラスのscore[i]までの和がone[i+1]に入っているようにする
for i in range(n):
    one[i + 1] += one[i]
    two[i + 1] += two[i]

    if c[i] == 1:
        one[i + 1] += score[i]
    else:
        two[i + 1] += score[i]
    
# print(f"1組:{one}")
# print(f"2組:{two}")

# 出力
q = int(input())
for i in range(q):
    l, r = map(int,input().split())
    print(one[r] - one[l - 1], two[r] - two[l - 1])