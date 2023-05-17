
# 評価関数を作る

import numpy as np

from .const import KEYS_AMOUNT, USER_AMOUNT
from .individual import models as md
from .MyClass import CarUser, make_hope_time_table





# 評価関数の本体
# 値を小さくしたいものを計算
def evaluate(individual):

    keys_mat, time_slots_mat = md.arr_to_mats(individual)

    # 優先度 高い
    # [ ] ユーザーの希望乗車時間帯と同じ

    # 優先度 低い
    # カギは1人2つ以上持たない
    how_far_from_ideal_having_key = calc_distance_from_ideal_key_ave(keys_mat)

    # [ ] 同じ時間帯を希望する人が、その時間帯に使う車の予備カギを持つ

    return 0

def calc_distance_from_ideal_key_ave(keys_mat):
    """カギを持っている人たちを対象とした所持数の平均値から理想値である１までの差を算出する"""

    IDEAL_KEY_AVE = 1

    # 1を含む行だけ抜き出す = カギを持っている人を抜き出す
    user_have_keys_mat = keys_mat[np.any(keys_mat == 1, axis=1)]

    # 行ごとに合計し1次元配列にする = 1人ごとのカギの所持数合計を計算する
    user_key_amount_arr = np.sum(user_have_keys_mat, axis=1)

    # 1次元配列の平均を取る = カギを持っている人の平均所持数を計算する
    average_have_key = np.mean(user_key_amount_arr)

    # 理想値との差を取る

    return abs(average_have_key - IDEAL_KEY_AVE)

def calc_ratio_not_assign_hope_time(times_mat):
    """希望乗車時間にアサイン出来なかった人の割合を計算する。
    希望する乗車時間帯表と個体から生成した乗車時間帯表を比べて、異なっている割合を返す。"""
    hope_time_table = make_hope_time_table()

    total_elemets = times_mat.size
    different_elements = np.count_nonzero(times_mat != hope_time_table)
    different_ratio = different_elements / total_elemets

    return different_ratio







