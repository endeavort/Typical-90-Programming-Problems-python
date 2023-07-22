# 入力、変数等の作成
height, width = map(int,input().split()) # 縦の長さ, 横の長さ
num_list = [list(map(int,input().split())) for _ in range(height)] # 数字のリスト
ans_list = [[0] * width for _ in range(height)] # 答えのリスト

# 行ごとに合計を前計算する
row_sums_list = [0] * height
for i in range(height):
    cnt = 0
    for j in range(width):
        cnt += num_list[i][j]
    row_sums_list[i] = cnt
print("行ごとの合計:")
print("⎴")
for r in row_sums_list:
    print(r)
print("⎵")

# 列ごとに合計を前計算する
col_sums_list = [0] * width
for i in range(width):
    cnt = 0
    for j in range(height):
        cnt += num_list[j][i]
    col_sums_list[i] = cnt
print(f"列ごとの合計:{col_sums_list}")

# 同じ行、同じ列にある整数を合計した数を求める
for i in range(height):
    for j in range(width):
        ans_list[i][j] = (row_sums_list[i] + col_sums_list[j]) - num_list[i][j]

# 出力
for i in range(height):
    print(*ans_list[i])