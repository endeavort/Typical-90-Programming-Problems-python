# 実行時間測定プログラム
import time

# 測定対象プログラム
def func():
    pass

# 処理の開始時刻を取得
start_time = time.time()

# 実行時間を測定したい関数を呼び出す
func()

# 処理の終了時刻を取得
end_time = time.time()

# 実行時間を計算
execution_time = end_time - start_time

# 出力
print(f"実行時間: {execution_time:.5f}秒")
