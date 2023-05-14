
# 個体データの扱いのテスト


import individual.models as md

def test():

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

if __name__ == "__main__":
    test()
