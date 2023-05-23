
from MyClass import Car, CarUser, CarUseTime, CarKey

# クラスインスタンスの作成
time_not_use = CarUseTime("乗らない")
time_18h     = CarUseTime("18時")
time_19h     = CarUseTime("19時")
time_20h     = CarUseTime("20時")

user_A = CarUser(name="A", can_drive=True , use_time_hope=time_20h) # 20時希望 運転可
user_B = CarUser(name="B", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
user_C = CarUser(name="C", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
user_D = CarUser(name="D", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
user_E = CarUser(name="E", can_drive=True , use_time_hope=time_18h) # 18時希望 運転可
user_F = CarUser(name="F", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_G = CarUser(name="G", can_drive=False, use_time_hope=time_20h) # 20時希望 運転不可
user_H = CarUser(name="H", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_I = CarUser(name="I", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_J = CarUser(name="J", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_K = CarUser(name="K", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_L = CarUser(name="L", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_M = CarUser(name="M", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可
user_N = CarUser(name="N", can_drive=False, use_time_hope=time_18h) # 18時希望 運転不可

car_A = Car(name="車A", capacity=7)
car_B = Car(name="車B", capacity=5)
car_C = Car(name="車C", capacity=5)

car_key_A1 = CarKey("カギA1", car_A, can_use_drive=True)
car_key_A2 = CarKey("カギA2", car_A, can_use_drive=False)
car_key_B1 = CarKey("カギB1", car_B, can_use_drive=True)
car_key_B2 = CarKey("カギB2", car_B, can_use_drive=False)
car_key_C1 = CarKey("カギC1", car_C, can_use_drive=True)
car_key_C2 = CarKey("カギC2", car_C, can_use_drive=False)

# 個体データ配列作成用
initial_dict = {
    "car-time":{
        "arr_total": len(Car.car_list), # 車の数だけ要素作る
        "elem_min": 1,
        "elem_max": len(CarUseTime.car_use_time_list) - 1, # 車をどの時間帯か振る → 最大時間帯ID＝リストIndex以下
        "can_duplicate": False
    },

    "key-user":{
        "arr_total": len(CarKey.key_list), # カギの個数分だけ要素作る
        "elem_min": 1,
        "elem_max": len(CarUser.user_list) - 1, # ユーザーに配る → ユーザーの最大ID＝リストIndex以下
        "can_duplicate": False
    },

    "user-time":{
        "arr_total": len(CarUser.user_list), # 利用者の人数分だけ要素作る
        "elem_min": 1,
        "elem_max": len(CarUseTime.car_use_time_list) - 1, # 誰がどの時間帯か振る → 最大時間帯ID＝リストIndex以下
        "can_duplicate": True
    }
}
