from hoge import CarUseTimeChoice

# pythonのtest用ライブラリ使ってみたい


# TODO: 想定出力、実際の出力、結果がわかるような書き方に変更
def test_CarUseTimeChoice():
    
    obj0 = CarUseTimeChoice("乗らない")
    obj1 = CarUseTimeChoice("18時")
    obj2 = CarUseTimeChoice("19時")
    obj3 = CarUseTimeChoice("20時")

    obj_list = [obj0, obj1, obj2, obj3]

    for obj in obj_list:
        print(obj.id, obj.display_name)

    return 0


if __name__ == '__main__':
    test_CarUseTimeChoice()
