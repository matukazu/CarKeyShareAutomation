# 汎用的に使える関数

import numpy as np

# 2次元numpy配列の行/列それぞれについて
# 各配列中の1の数を集計し1次元配列として返す
def count_ones_by_column(matrix):
    return np.sum(matrix, axis=0)

def count_ones_by_row(matrix):
    return np.sum(matrix, axis=1)

# 値が0/1の2次元numpy配列から、値が1だったときの行列インデックスを1次元配列として返す
def find_indices_of_ones(matrix):
    return np.argwhere(matrix == 1)