# TODO: クラスインスタンスリストを作成する機能が重複しているので、Baseクラスに統合する


# テンプレートクラス
# IDの自動連番機能有
class Base:
    _id_count = {}

    def __init__(self, name):
        # 継承したクラス毎に異なるIDで0始まりの自動連番
        cls = self.__class__
        if cls not in Base._id_count:
            Base._id_count[cls] = -1
        Base._id_count[cls] += 1
        self.id = Base._id_count[cls]

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
        return ul[int(list_ind)]

    def get_use_time_hope(self):
        return self.use_time_hope
    
    def get_can_drive(self):
        return self.can_drive

class Car(Base):
    car_list = []

    def __init__(self, name, capacity):
        super().__init__(name)

        self.capacity = capacity
        self.key_list = []

        Car.car_list.append(self)

class CarKey(Base):
    key_list = [] # すべての車のカギリスト

    def __init__(self, name, car, can_use_drive):
        super().__init__(name)

        self.can_use_drive = can_use_drive # True: 運転用 / False: 予備カギ
        self.which_car = car # どの車のカギか

        CarKey.key_list.append(self)
        car.key_list.append(self) # 車クラス側のカギリストに追加


class CarUseTime(Base):
    car_use_time_list = []

    def __init__(self, name):
        super().__init__(name) # 名前=時間帯の識別用 (例：18時、乗らない など)

        self.users_hope   = [] # この時間帯を希望するユーザー
        self.users_actual = [] # 実際この時間帯に使うユーザー

        CarUseTime.car_use_time_list.append(self)
