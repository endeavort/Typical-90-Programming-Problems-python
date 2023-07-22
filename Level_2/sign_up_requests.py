# 入力、変数等の作成
N = int(input())
name_list = set() # ユーザー名のset型

# ユーザ名がname_listにあるか調べる(set型の方が圧倒的に速い)
for i in range(1,N+1):
    S = input()
    # 登録されていない場合出力して登録
    if not(S in name_list):
        print(i)
        name_list.add(S)