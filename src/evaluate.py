
# 評価関数を作る

import numpy as np

from .const import KEYS_AMOUNT, USER_AMOUNT
from .individual import models as md
from .MyClass import CarUser





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

# 希望乗車時間にアサインできなかった人の割合
# FIX: 希望時間以外にアサインした場合は計算できているが、希望時間にアサインできていない場合が計算出来ていない
#   userの希望時間から、理想の乗車時間表を作って、値が一致しなかった要素数を計算する形に変更すべき
def calc_ratio_not_assign_hope_time(times_mat):

    not_equal_hope_time_list = [0] * len(CarUser.user_list)
    # [x]時間帯表を掃いて、どのユーザーがどの時間帯にアサインしたのか調べる → (ユーザーID、アサイン時間)のリスト取得
    ut_list = md.create_user_time_index_list(times_mat)
    # print("---utlist---")
    # print(ut_list)

    # [ ](ユーザーID、アサイン時間)のリストをForで回す

    for ut in ut_list:
        u_id = ut[0] + 1
        t_ind = ut[1]

        user = CarUser.get_user_instance(u_id) # ユーザーIDに一致するユーザーインスタンスを取得する
        hope_time = user.get_use_time_hope() # 取得したユーザーインスタンスから希望時間インスタンスを取得する

        ht_list_ind = hope_time.get_id() - 1 # 希望時間IDは1始まりだが、アサイン時間はリストであり0始まりなので調整
        print(f"user:{u_id} \t htlistid:{ht_list_ind} \t tind:{t_ind}")

        # [ ] あるユーザーがアサイン時間IDと希望時間IDが一致しなかった回数を一覧として算出
        if (t_ind != ht_list_ind):
            not_equal_hope_time_list[u_id - 1] += 1 # ユーザーIDは1始まり 配列は0始まりなので調整

    print(not_equal_hope_time_list)
    # [ ] 希望時間と一致しなかった回数合計 ÷ 全部希望から外れた場合(＝時間帯表の要素数) ※全員希望と外れていたら1、全員希望通りで0。
    ratio_not_assign_hope_time = sum(not_equal_hope_time_list) / times_mat.size
    return ratio_not_assign_hope_time