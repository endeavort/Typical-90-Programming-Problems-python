# 入力、変数等の作成
# 幅 A、奥行き B、高さ C
A, B, C = map(int,input().split()) 

# A, B, C の最大公約数rが長さrの立方体となる
# ユークリッドの互除法を用いて最大公約数を求める
import math
gcd_ab = math.gcd(A, B)
gcd_abc = math.gcd(gcd_ab, C)
# print(f"gcd_ab:{gcd_ab}, gcd_abd:{gcd_abc}")

# 出力
# 各辺の切断回数は最大公約数で割った数-1
ans = (A // gcd_abc - 1) + (B // gcd_abc -  1) + (C // gcd_abc - 1)
print(ans)