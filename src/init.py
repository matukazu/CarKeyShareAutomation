
from MyClass import Car, CarUser, CarUseTime, CarKey

# クラスインスタンスの作成
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

# 個体データ配列作成用
initial_dict = {
    "car-time":{
        "arr_total": len(Car.car_list),
        "elem_min": 1,
        "elem_max": len(Car.car_list),
        "can_duplicate": False
    },

    "key-user":{
        "arr_total": len(CarKey.key_list),
        "elem_min": 1,
        "elem_max": len(CarKey.key_list),
        "can_duplicate": False
    },

    "user-time":{
        "arr_total": len(CarUser.user_list),
        "elem_min": 1,
        "elem_max": len(CarUser.user_list),
        "can_duplicate": True
    }
}