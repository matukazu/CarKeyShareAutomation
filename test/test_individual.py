
# 個体データの扱いのテスト
# python -m test.test_individual

import numpy as np

from src.individual import models as md
# from src.individual import utils as ut

def test():
    # test_count_ones()
    test_find_indices_of_ones()

def test_count_ones():

    indiv_arr = md.make_sample_indiv_arr()
    keys_mat, time_slots_mat = md.arr_to_mats(indiv_arr)

    count_each_keys          = md.count_each_keys(keys_mat)
    count_one_user_have_keys = md.count_one_user_have_keys(keys_mat)

    count_users_in_same_time = md.count_users_in_same_time(time_slots_mat)
    count_each_users         = md.count_each_users(time_slots_mat)

    print("--カギ分配表--")
    print(keys_mat)

    print("--乗車時間帯表--")
    print(time_slots_mat)

    print(f"それぞれのカギの個数:{count_each_keys}")
    print(f"一人当たりのカギ所持量:{count_one_user_have_keys}")
    print(f"同じ時間帯に乗車予定の人数:{count_users_in_same_time}")
    print(f"それぞれのユーザーの数:{count_each_users}")

    return

def test_find_indices_of_ones():
    mat = np.array([[1, 0, 0],
                    [1, 0, 0],
                    [0, 1, 0]])

    ret = md.create_user_time_index_list(mat)
    print(ret)

    # 正解： [[0,0], [1,0], [2, 1]]

    return


if __name__ == "__main__":
    test()
