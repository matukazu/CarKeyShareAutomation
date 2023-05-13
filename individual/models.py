import numpy as np

from const import KEYS_AMOUNT, INDIV_ROW_NUM, INDIV_COLUMN_NUM, INDIV_ARR_SIZE
from individual.utils import count_ones_by_column, count_ones_by_row

def arr_to_mats(indiv_arr):
    """
    個体用の1次元numpy配列を元に「カギ分配表」「乗車時間帯表」を表す2次元numpy配列にそれぞれ変換し返す
    """
    tmp_mat = indiv_arr.reshape((INDIV_ROW_NUM, INDIV_COLUMN_NUM)) # ユーザー × その他 の2次元配列に変換
    keys_mat, time_slots_mat = np.split(tmp_mat, [KEYS_AMOUNT], axis=1) # カギ、時間帯の境目で列方向に分割
    return (keys_mat, time_slots_mat)

# カギ分配表から値を抽出する
def count_each_keys(keys_mat):
    """それぞれのカギの個数を配列で返す

    Returns: 1次元 numpy配列
        indexs: カギ
        values: それぞれのカギの個数
    """
    return count_ones_by_column(keys_mat)

def count_one_user_have_keys(keys_mat):
    """一人当たりのカギ所持量を配列で返す

    Returns: 1次元 numpy配列
        indexs: ユーザー
        values: それぞれのカギの所持量
    """
    return count_ones_by_row(keys_mat)

# 乗車時間帯表から値を抽出する
def count_users_in_same_time(time_slots_mat):
    """同じ時間帯に乗車する人数を配列で返す

    Returns: 1次元 numpy配列
        indexs: 時間帯
        values: その時間帯に乗車する人数合計
    """
    return count_ones_by_column(time_slots_mat)

def count_each_users(time_slots_mat):
    """表中に存在する同一ユーザーの数を配列で返す

    Returns: 1次元 numpy配列
        indexs: ユーザー
        values: 別々の時間帯に存在する同一ユーザーの合計
    """
    return count_ones_by_row(time_slots_mat)

def make_sample_indiv_arr():
    # 個体用1次元配列 要素は0か1がランダム
    return np.random.randint(low=0, high=2, size=INDIV_ARR_SIZE)
