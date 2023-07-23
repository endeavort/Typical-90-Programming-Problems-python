# 入力、変数等の作成
Q = int(input())

# list型の場合、先頭要素の追加や削除を行うと
# それ以降の要素を全て移動する必要があるため大きなコストがかかる
# そのため双方向連結リストのcollections.dequeを使用する
# ※中央部分のアクセスが多い場合はlistの方が速い
import collections
cards = collections.deque() # 山札

for _ in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        # 先頭に追加
        cards.appendleft(x)
    elif t == 2:
        # 末尾に追加
        cards.append(x)
    else:
        # 要素の出力
        print(cards[x-1])

