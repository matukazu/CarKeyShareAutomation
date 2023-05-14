
# プロジェクト全体で使う固定値の定義


CAR_AMOUNT   = 2  # 車の台数
KEYS_PER_CAR = 2  # 車1台当たりのカギの個数
KEYS_AMOUNT  = CAR_AMOUNT * KEYS_PER_CAR  # カギの総数

USER_AMOUNT  = 7 # 車の利用人数

TIME_SLOT_AMOUNT = 3 # 時間帯候補の数



# 個体データ 1次元 → 2次元変換用
INDIV_ROW_NUM = USER_AMOUNT
INDIV_COLUMN_NUM = KEYS_AMOUNT + TIME_SLOT_AMOUNT

# 個体データ 1次元配列 要素数
INDIV_ARR_SIZE = INDIV_ROW_NUM * INDIV_COLUMN_NUM
