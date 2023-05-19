
# TODO: とりあえず。後でフォルダ構成整理したら修正
from src.MyClass import CarUser, make_hope_time_table


import random



# TODO:現状決め打ち。作成されたクラスインスタンス内のインスタンスリストから取得予定
# 作成したい1次元表を
initial_dict = {
    "car-time":{
        "arr_total": 2,
        "elem_min": 1,
        "elem_max": 2,
        "can_duplicate": False
    },

    "key-user":{
        "arr_total": 4,
        "elem_min": 1,
        "elem_max": 4,
        "can_duplicate": False
    },

    "user-time":{
        "arr_total": 3,
        "elem_min": 1,
        "elem_max": 3,
        "can_duplicate": True
    }
}

# TODO: Jsonデータ渡せば良いだけなので、将来的にAPI化もいけるか
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


# 評価関数用の関数群
# TODO: デバッグしやすいのでとりあえずここに記述

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




if __name__ == "__main__":
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

