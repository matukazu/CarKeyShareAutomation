# TODO: とりあえず。後でフォルダ構成整理したら修正
# from src.MyClass import CarUser, make_hope_time_table
import random

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


# ユーザーのリスト、カギのリストを元にユーザーが希望する理想の乗車時間体表を作成する
def make_hope_time_table():
    ret_arr = []

    for user in CarUser.user_list:
        hope_time = user.get_use_time_hope()
        if hope_time is not None:
            time_id = hope_time.get_id()
            ret_arr.append(time_id)

    return ret_arr


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
    print("init 終わり")

    return


# 評価関数用の関数群
# TODO: デバッグしやすいのでとりあえずここに記述



def evaluate(individual):
    tables = individual_to_tables_dict(individual)

    ct_table = tables["car-time"]
    ku_table = tables["key-user"]
    ut_table = tables["user-time"]

    eval1 = find_total_user_cant_drive_have_driving_key(ku_table) # 最小化 優先度大
    eval2 = calc_ratio_not_assign_hope_time(ut_table) # 最小化 優先度中

    eval_list = [eval1, eval2]

    return eval_list





def find_total_user_cant_drive_have_driving_key(ku_arr):
    """カギ-カギ持ち担当者の1次元配列を元に、運転できないユーザーで運転用カギを持っている人数を返す"""
    result = 0 # 運転手用のカギを運転可能者以外が持っている数

    for k_id, u_id in enumerate(ku_arr):
        # カギIndexが偶数のときのみ運転手用のカギ → カギIndex
        # カギIndexに対応するUserIDからユーザーインスタンス取得
        if k_id % 2 == 0 :
            user = CarUser.get_user_instance(user_id=u_id)

            # ユーザーが運転できなかったら＋1
            if user.get_can_drive() != True:
                result += 1

    return result

def calc_ratio_not_assign_hope_time(ut_arr):
    """希望乗車時間にアサイン出来なかった人の割合を計算する。
    希望する乗車時間帯表と個体から生成した乗車時間帯表を比べて、異なっている割合を返す。"""
    
    ideal_ut_arr = make_hope_time_table()

    diff_count = 0
    for i, j in zip(ideal_ut_arr, ut_arr):
        if i is not j:
            diff_count += 1
    total_elements = len(ut_arr)

    different_ratio = diff_count / total_elements

    return different_ratio



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

# TODO:現状決め打ち。作成されたクラスインスタンス内のインスタンスリストから取得予定
# 作成したい1次元表を
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

# TODO: Jsonデータ渡せば良いだけなので、将来的にAPI化もいけるか
# TODO: 個体データ作る際に元々「運転できるユーザーにしかカギを渡さない」ロジックを組み込めないか → 精度up
def make_individual():
    """"作成したい1次元表を元に、ランダムな個体を生成する関数"""

    indiv_arr = []

    for key, values in initial_dict.items():
        arr_total = values["arr_total"]
        elem_min = values["elem_min"]
        elem_max = values["elem_max"]
        can_duplicate = values["can_duplicate"]

        arr = []
        if can_duplicate:
            # 重複を許可する場合
            arr = [random.randint(elem_min, elem_max) for _ in range(arr_total)]
        else:
            # 重複を許可しない場合
            arr_set = set()  # 既に使用された整数を記録するセット
            while len(arr) < arr_total:
                num = random.randint(elem_min, elem_max)
                if num not in arr_set:
                    arr.append(num)
                    arr_set.add(num)

        indiv_arr.extend(arr)

    return indiv_arr


# 個体データ配列を意味のある表に変換する
# また、評価関数で使うために表に関わる汎用的な処理を追加する

def individual_to_tables_dict(indiv_arr):

    ret_dict = {}

    for key, values in initial_dict.items():
        arr_total = values["arr_total"]
        slice_arr = indiv_arr[:arr_total]
        ret_dict[key] = slice_arr

    return ret_dict




if __name__ == "__main__":

    init()

    print(Car.car_list)

    indiv_arr = make_individual()
    print(indiv_arr)

    tables = individual_to_tables_dict(indiv_arr)

    ct_table = tables["car-time"]
    ku_table = tables["key-user"]
    ut_table = tables["user-time"]
    
    print(f"車-時間：{ct_table}")
    print(f"カギ-ユーザー：{ku_table}")
    print(f"ユーザー-時間：{ut_table}")

    # result = find_total_user_cant_drive_have_driving_key(ku_table)
    # print(f"運転できないユーザーでカギ持っている数:{result}")

