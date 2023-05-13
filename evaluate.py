
# 評価関数を作る

import numpy as np

from const import KEYS_AMOUNT, USER_AMOUNT
import individual.models as md







def evaluate(individual):

    keys_mat, time_slots_mat = md.arr_to_mats(individual)

    # 優先度 高い
    # [ ] ユーザーの希望乗車時間帯と同じ

    # 優先度 低い
    # [ ] カギは1人2つ以上持たない
    # [ ] 同じ時間帯を希望する人が、その時間帯に使う車の予備カギを持つ

    return 0


