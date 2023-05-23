from MyClass import CarUser
from individual import convert_to_tables_dict

# 評価関数の重みづけ
weights = (-10.0,
           -1.0)


# 評価関数の本体
def evaluate(individual):
    tables = convert_to_tables_dict(individual)

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

# ある時間帯に乗るユーザーの総数とその時間帯に使用する車の定員合計を比べる
# 時間帯ごとの車の定員オーバーした数の合計を返す
def find_user_amount_over_car_capacity(ct_arr, ut_arr):

    # ut_arrからある時間帯に乗る人数を取得する 時間帯ID：合計人数
    
    # ct_arrからある時間帯に使う車一覧を取得 時間帯ID：[車一覧]
    # 車一覧を掃いて、車のインスタンスを取得 → 車の定員を取得 → 合計する → 時間帯ID：定員合計
    
    # 時間帯IDごとに 合計人数 - 定員合計を計算 値が0より大きいとき定員オーバーしたとして記録 → 時間帯ID：オーバー人数
    # すべての時間帯のオーバー人数を合計して返す

    return

# ユーザーのリスト、カギのリストを元にユーザーが希望する理想の乗車時間体表を作成する
def make_hope_time_table():
    ret_arr = []

    for user in CarUser.user_list:
        hope_time = user.get_use_time_hope()
        if hope_time is not None:
            time_id = hope_time.get_id()
            ret_arr.append(time_id)

    return ret_arr

