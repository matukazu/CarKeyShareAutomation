
from calc_best_individual import calc_best_individual
from individual import convert_to_tables_dict
from MyClass import Car, CarKey, CarUser, CarUseTime

def view():
    best_ind, fitness_vals = calc_best_individual()
    tables = convert_to_tables_dict(indiv_arr=best_ind)

    ct_table = tables["car-time"]
    ku_table = tables["key-user"]
    ut_table = tables["user-time"]

    print(ct_table)
    print(ku_table)
    print(ut_table)

    print("===車使用時間===")
    for c_ind, t_ind in enumerate(ct_table):
        car = Car.get_car_instance(car_id=c_ind)
        time = CarUseTime.get_carusetime_instance(time_id=t_ind)
        print(f"・車「{car.get_name()}」は「{time.get_name()}」")

    print("===かぎ分担===")
    for k_ind, u_ind in enumerate(ku_table):
        key = CarKey.get_carkey_instance(key_id=k_ind)
        user = CarUser.get_user_instance(user_id=u_ind)
        print(f"・カギ「{key.get_name()}」は「{user.get_name()}」")

    print("===乗車時間===")
    for u_ind, t_ind in enumerate(ut_table):
        user = CarUser.get_user_instance(user_id=u_ind)
        time = CarUseTime.get_carusetime_instance(time_id=t_ind)

        print(f"・「{user.get_name()}」さんは「{time.get_name()}」に帰る")



if __name__ == "__main__":
    view()