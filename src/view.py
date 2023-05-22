
from calc_best_individual import calc_best_individual
from individual import convert_to_tables_dict
from MyClass import Car

def view():
    best_ind, fitness_vals = calc_best_individual()
    tables = convert_to_tables_dict(indiv_arr=best_ind)

    ct_table = tables["car-time"]
    ku_table = tables["key-user"]
    ut_table = tables["user-time"]

    print(ct_table)
    print(ku_table)
    print(ut_table)

    for c_ind, t_ind in enumerate(ct_table):
        





if __name__ == "__main__":
    view()