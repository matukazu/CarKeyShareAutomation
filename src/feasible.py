
# ペナルティ用の関数

import numpy as np

from src.const import KEYS_AMOUNT, USER_AMOUNT
from .individual import models as md
from .MyClass import CarUser

# TODO： 個体が理想からどれだけ離れているか、その距離を計算して返せるようになるとさらに精度UPするはず
# 例えば「それぞれカギは1つしか存在しない」を理想とすると、
# それぞれのカギの数が1より離れているほどペナルティが大きいような距離関数を作成すべきか
# 同様にそれぞれの理想からの距離を計算して重みづけして返すようにすると良いと思う
def feasible(individual):
    """個体の実現可能性を計算する。実現してよい条件の場合True、そうでなければFalseを返す"""

    keys_mat, time_slots_mat = md.arr_to_mats(individual)

    is_ideal_indiv = True

    while (is_ideal_indiv == True):
        # [ ] 運転手用のカギは運転可能者しか持てない

        # [ ] 時間帯ごとに乗車人数が利用する車の定員オーバーしない

        is_ideal_indiv = check_keys_are_only_one(keys_mat) # それぞれカギは1つだけになっているか
        is_ideal_indiv = check_users_are_only_one(time_slots_mat) # 同一人物の人数は1人になっているか
        break
    else:
        is_ideal_indiv = False

    return is_ideal_indiv

def check_keys_are_only_one(key_mat) -> bool:
    """個体から取得したそれぞれのカギの個数がすべて1であることを確認する
    """
    keys_counts = md.count_each_keys(key_mat)
    return keys_counts == np.ones(KEYS_AMOUNT)

def check_users_are_only_one(time_slots_mat) -> bool:
    """個体から取得したユーザーの数がそれぞれすべて1人であることを確認する
    """
    users_counts = md.count_users_in_same_time(time_slots_mat)
    return users_counts == np.ones(USER_AMOUNT)



# [ ] 時間帯ごとに乗車人数が利用する車の定員オーバーしない
def hoge(key_mat):
    return

# [ ] 運転手用のカギを運転可能者以外が持っている数
# def hoge2(key_mat):
def hoge2(key_mat):
    ret = 0
    # カギ振り分け表 [乗車ユーザー、カギ]インデックスをリストとして集めたリストを取得
    uk_ind_list = md.create_user_key_index_list(key_mat)

    print("カギ表")
    print(key_mat)

    print("ユーザー-カギインデックスリスト")
    print(uk_ind_list)



    # リストをForで回す
    for uk in uk_ind_list:
        u_ind = uk[0]
        k_ind = uk[1]

        # カギIndexが偶数のときのみ運転手用のカギ → カギIndex
        # カギIndexに対応するUserIDからユーザーインスタンス取得
        # ユーザーが運転できなかったら＋1
        if k_ind % 2 == 0 :
            u_id = u_ind + 1
            user = CarUser.get_user_instance(user_id= u_id)

            if user.get_can_drive() != True:
                ret += 1

    print("return")
    print(ret)

    return ret

