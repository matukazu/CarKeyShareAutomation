
# テンプレートクラス
# IDの自動連番機能有
class Base:
    __id_counter = 1

    def __init__(self, name):
        self.id = Base.__id_counter
        Base.__id_counter += 1
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

# 車の利用者クラス
class CarUser(Base):
    user_list = []

    def __init__(self, name, can_drive, use_time_hope):
        super().__init__(name)

        self.name                      = name
        self.can_drive                 = can_drive
        self.use_time_hope             = use_time_hope
        self.having_key_list                  = [] # 持っているカギリスト

        CarUser.user_list.append(self)

    @staticmethod
    def get_user_instance(user_id):
        ul = CarUser.user_list # ユーザーリストを掃く形で実装するとユーザーが増えたときに処理が重いのでやめた
        if len(ul) < user_id: # ex. 5人しかいないはずなのに6人目を指定した場合×
            return None

        list_ind = user_id - 1 # 配列番号は0始まりなので調整
        return ul[list_ind]

    def get_use_time_hope(self):
        return self.use_time_hope

class Car(Base):
    def __init__(self, name, capacity):
        super().__init__(name)

        self.capacity = capacity
        self.key_list = []

class CarKey(Base):
    key_list = [] # すべての車のカギリスト

    def __init__(self, name, car, can_use_drive):
        super().__init__(name)

        self.can_use_drive = can_use_drive # True: 運転用 / False: 予備カギ
        self.which_car = car # どの車のカギか

        CarKey.key_list.append(self)
        car.key_list.append(self) # 車クラス側のカギリストに追加


class CarUseTime(Base):
    def __init__(self, name):
        super().__init__(name) # 名前=時間帯の識別用 (例：18時、乗らない など)

        self.users_hope   = [] # この時間帯を希望するユーザー
        self.users_actual = [] # 実際この時間帯に使うユーザー

def test():
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


    print("車利用者リスト")
    for user in CarUser.user_list:
        print(user.name)

    print("---")

    print(f"車のカギリスト")
    for key in CarKey.key_list:
        print(key.name)

    print("---")

    print(f"車Ａのカギリスト")
    for key in car_A.key_list:
        print(key.name)

    print("---")

    print(f"車Ｂのカギリスト")
    for key in car_B.key_list:
        print(key.name)

    print("---")
    user = CarUser.get_user_instance(user_id=1)
    u_name = user.get_name()
    ht = user.get_use_time_hope()
    ht_id = ht.get_id()
    print(f"{u_name}の希望時間ID:{ht_id}")

    return

if __name__ == "__main__":
    test()

