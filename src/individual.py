
import random

from init import initial_dict # 個体データ作成・変換用の初期値格納用辞書


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
def convert_to_tables_dict(indiv_arr):
    """ 個体生成用辞書の値から
    例： 個体1次元配列を配列数3, 6, 14の三つの配列に分割するケース
    入力 : [4, 1, 2, 8, 5, 2, 3, 10, 1, 4, 4, 3, 2, 2, 2, 4, 3, 1, 1, 4, 1, 4, 1]

    出力
    ・[4, 1, 2]
    ・[8, 5, 2, 3, 10, 1]
    ・[4, 4, 3, 2, 2, 2, 4, 3, 1, 1, 4, 1, 4, 1]
    """

    ret_dict = {}

    arr_start_ind = 0
    for key, values in initial_dict.items():
        arr_total = values["arr_total"]

        # 配列の長さ分スライスで取り出す。繰り返し時は前回取り出した範囲の次の要素を先頭として取り出す。
        slice_arr = indiv_arr[arr_start_ind : arr_start_ind + arr_total]
        arr_start_ind += arr_total

        ret_dict[key] = slice_arr

    return ret_dict

