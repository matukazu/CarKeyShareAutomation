from MyClass import CarUser, Car, CarUseTime
from individual import convert_to_tables_dict

from individual import make_individual

# 評価関数の重みづけ
weights = (-10.0,
           -1.0,
           -10.0)

# 評価関数の本体
def evaluate(individual):
    tables = convert_to_tables_dict(individual)

    ct_table = tables["car-time"]
    ku_table = tables["key-user"]
    ut_table = tables["user-time"]

    eval1 = find_total_user_cant_drive_have_driving_key(ku_table) # 最小化 優先度大
    eval2 = calc_ratio_not_assign_hope_time(ut_table) # 最小化 優先度中
    eval3 = find_user_amount_over_car_capacity(ut_table, ct_table) # 最小化 優先度大

    eval_list = [eval1, eval2, eval3]

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

# ある時間帯に乗るユーザーの総数とその時間帯に使用する車の定員合計を比べる
# 時間帯ごとの車の定員オーバーした数の合計を返す
# TODO: めっちゃソースが汚いので可読性良くしたいとは思う
def find_user_amount_over_car_capacity(ut_arr, ct_arr):

    # 時間帯IDの数だけ下記のような辞書を作る
    # {時間帯ID：{その時間に乗る合計人数: 値}, {その時間帯に使う車の定員合計: 値}}
    dict_to_calc_over_capa = {}
    USER_AMOUNT = "user_amount"
    TOTAL_CAR_CAPACITY = "total_car_capacity"
    for t_ind in range(len(CarUseTime.car_use_time_list)):
        if f"{t_ind}" not in dict_to_calc_over_capa:
            dict_to_calc_over_capa[f"{t_ind}"] = {}

        dict_to_calc_over_capa[f"{t_ind}"] = {
            USER_AMOUNT       : 0,
            TOTAL_CAR_CAPACITY: 0
        }

    # ut_arrからある時間帯に乗る人数合計を取得する
    for t_ind in list(set(ut_arr)): # ut_arrの要素は時間帯ID → 重複要素を削除してから繰り返す
        user_amount = count_occurrences(ut_arr, t_ind)

        dict_to_calc_over_capa[f"{t_ind}"][USER_AMOUNT] = user_amount

    # ct_arrからある時間帯に使う車一覧を取得し、各時間帯毎の定員合計を取得
    for c_ind, t_ind in enumerate(ct_arr):
        car = Car.get_car_instance(car_id=c_ind)

        dict_to_calc_over_capa[f"{t_ind}"][TOTAL_CAR_CAPACITY] += car.get_capacity()

    # 時間帯IDごとに 合計人数 - 定員合計を計算 値が0より大きいとき定員オーバーしたとして記録 → 時間帯ID：オーバー人数
    sum_over_num = 0  # すべての時間帯のオーバー人数合計
    for key, dict in dict_to_calc_over_capa.items():
        over_num = 0
        hoge = dict[USER_AMOUNT] - dict[TOTAL_CAR_CAPACITY]
        if hoge > 0:
            over_num = hoge

        dict_to_calc_over_capa[key]["over_num"] = over_num
        sum_over_num += over_num

    return sum_over_num

# ユーザーのリスト、カギのリストを元にユーザーが希望する理想の乗車時間体表を作成する
def make_hope_time_table():
    ret_arr = []

    for user in CarUser.user_list:
        hope_time = user.get_use_time_hope()
        if hope_time is not None:
            time_id = hope_time.get_id()
            ret_arr.append(time_id)

    return ret_arr

# 引数で与えられた値が、引数で与えられた配列中に何個含まれるか探して返す
def count_occurrences(arr, value):
    count = 0
    for item in arr:
        if item == value:
            count += 1
    return count

# テスト用に使ってた
# if __name__ == "__main__":

#     indiv = make_individual()
#     tables = convert_to_tables_dict(indiv)

#     ct_arr = tables["car-time"]
#     ku_arr = tables["key-user"]
#     ut_arr = tables["user-time"]

#     # print(indiv)
#     print("-car-time-")
#     print(ct_arr)
#     # print(ku_arr)
#     print("-user-time-")
#     print(ut_arr)

#     result = find_user_amount_over_car_capacity(ut_arr, ct_arr)
#     print(result)