
import random
from deap import base
from deap import creator
from deap import tools

# 車の利用者クラス
# クラスメンバ
#   - ユーザーID
#   - 名前
#   - 運転可能か
#   - 今日の利用時間帯ID ※時間帯リスト内のIDのみ許す
#   - 明日車を利用するか
#   - 昨日カギをもらったか
#   - 毎日乗る予定か
class CarUser(object):
    def __init__(self,
                id                :int,
                name              :str,
                can_drive         :bool,
                use_time_id       :int,
                is_use_tommorow   :bool = True,
                had_key_yesterday :bool = False ,
                is_use_everyday   :bool = True ) -> None:

        self.id                = id
        self.name              = name
        self.can_drive         = can_drive
        self.use_time_id       = use_time_id
        self.is_use_tommorow   = is_use_tommorow
        self.had_key_yesterday = had_key_yesterday
        self.is_use_everyday   = is_use_everyday
    
    # TODO:ユーザーが選択している利用時間帯が、利用時間帯リスト内に含まれているかチェックする処理




# 車クラス
# - ID
# - 名前
# - 最大収容人数
class Car(object):
    def __init__(self, id, name, ride_capacity) -> None:
        self.id = id
        self.name = name
        self.ride_capacity = ride_capacity


# 車に乗る時間クラス
# - ID  (自動連番)
# - 表示名
class CarUseTimeChoice(object):
    __id_counter = 0

    def __init__(self, display_name: str) -> None:
        self.id           = CarUseTimeChoice.__id_counter
        self.display_name = display_name

        CarUseTimeChoice.__id_counter += 1


# カギの分担表を表すクラス
# 個体を表す1次元配列をカギの分担表を表す2次元配列に変換する
# ユーザー数 × カギ個数
class KeyShift(object):

    def 



# 評価関数クラス
class Eval():
    def __init__(self) -> None:
        pass

    def main() -> None:
        pass

    




# 遺伝的アルゴリズム個体クラス

def main():



    return 0


