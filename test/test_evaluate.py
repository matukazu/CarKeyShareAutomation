# 評価関数のテスト
# 実行時コマンド注意： python -m test.test_evaluate

from unittest import TestCase

from src.MyClass import CarUseTime, CarUser, Car, CarKey
from src.individual import models as md
import src.evaluate as ev



# 個体データ作成 カギ分配・時間帯表の作成
indiv_arr = md.make_sample_indiv_arr()
keys_mat, time_slots_mat = md.arr_to_mats(indiv_arr)

def test():
    init()
    test_init_print_keymat()
    test_init_print_timesmat()

    test_calc_average_key_distance()
    test_calc_ratio_not_assign_hope_time()


    return

# TDOO: 冗長なので、init処理をどこかに作って呼び出すようにする。
def init():
    time_not_use = CarUseTime("乗らない")
    time_18h     = CarUseTime("18時")
    time_19h     = CarUseTime("19時")

    user_A = CarUser(name="Aさん", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
    user_B = CarUser(name="Bさん", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
    user_C = CarUser(name="Cさん", can_drive=True , use_time_hope=time_19h) # 19時希望 運転可
    user_D = CarUser(name="Dさん", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
    user_E = CarUser(name="Eさん", can_drive=False, use_time_hope=time_19h) # 19時希望 運転不可
    user_F = CarUser(name="Fさん", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
    user_G = CarUser(name="Gさん", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可

    car_A = Car(name="車A", capacity=3)
    car_B = Car(name="車B", capacity=5)

    car_key_A1 = CarKey("カギA1", car_A, can_use_drive=True)
    car_key_A2 = CarKey("カギA2", car_A, can_use_drive=True)
    car_key_B1 = CarKey("カギB1", car_B, can_use_drive=True)
    car_key_B2 = CarKey("カギB2", car_B, can_use_drive=True)


def test_init_print_keymat():
    print("--カギ分配表--")
    print(keys_mat)
    return

def test_init_print_timesmat():
    print("--時間帯表--")
    print(time_slots_mat)
    return


def test_calc_average_key_distance():

    distance_from_ideal_key_ave = ev.calc_distance_from_ideal_key_ave(keys_mat)

    print(f"カギ所持者の平均カギ所持数 理想値=1との距離 :{distance_from_ideal_key_ave}")

    return


def test_calc_ratio_not_assign_hope_time():
    ret = ev.calc_ratio_not_assign_hope_time(time_slots_mat)
    print(ret)


if __name__ == "__main__":
    test()
