

import src.feasible as fsbl
from src.individual import models as md

# 個体データ作成 カギ分配・時間帯表の作成
indiv_arr = md.make_sample_indiv_arr()
keys_mat, time_slots_mat = md.arr_to_mats(indiv_arr)

def test():

    fsbl.hoge2(time_slots_mat)


    return



if __name__ == "__main__":
    test()

