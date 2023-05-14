# 評価関数のテスト

from unittest import TestCase

from src.individual import models as md
import src.evaluate as ev



# 個体データ作成 カギ分配・時間帯表の作成
indiv_arr = md.make_sample_indiv_arr()
keys_mat, time_slots_mat = md.arr_to_mats(indiv_arr)

def test():
    test_calc_average_key_distance()

    return


def test_calc_average_key_distance():
    """実行時コマンド注意： python -m test.test_evaluate"""

    print("--カギ分配表--")
    print(keys_mat)

    distance_from_ideal_key_ave = ev.calc_distance_from_ideal_key_ave(keys_mat)

    print(f"カギ所持者の平均カギ所持数 理想値=1との距離 :{distance_from_ideal_key_ave}")

    return

if __name__ == "__main__":
    test()
