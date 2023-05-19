


import random
# TODO: Jsonデータ渡せば良いだけなので、将来的にAPI化もいけるか
def make_individual():
    """"作成したい1次元表を元に、ランダムな個体を生成する関数"""

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
            "elem_max": 2,
            "can_duplicate": True
        }
    }

    result = []

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

        result.extend(arr)

    return result


if __name__ == "__main__":
    result = make_individual()
    print(result)