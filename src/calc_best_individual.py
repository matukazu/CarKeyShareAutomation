
import random #個体の各遺伝子を決めるために使用

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

from individual import make_individual
from evaluate import evaluate


# 最適な個体を計算して返す
def calc_best_individual():

    #最小化問題として設定(-1.0で最小化、1.0で最大化問題)
    creator.create("FitnessMin", base.Fitness, weights=(-10.0, -1.0))

    #個体の定義（list型と指定しただけで、中身の遺伝子は後で入れる）
    creator.create("Individual", list, fitness=creator.FitnessMin)

    #各種関数の設定
    #交叉、選択、突然変異などには、DEAPのToolbox内にある関数を利用
    toolbox = base.Toolbox()
    # # ランダムな個体の生成
    # toolbox.register("attribute", make_individual, creator.Individual)
    # #individualという関数を設定。それぞれの個体に含まれる2個の遺伝子をattributeにより決める
    # toolbox.register("individual", make_individual)
    toolbox.register("individual", tools.initIterate, creator.Individual, make_individual)
    #集団の個体数を設定するための関数を準備
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    #トーナメント方式で次世代に子を残す親を選択（tornsizeは各トーナメントに参加する個体の数）
    toolbox.register("select", tools.selTournament, tournsize=5)
    #交叉関数の設定。
    toolbox.register("mate", tools.cxTwoPoint)
    #突然変異関数の設定。indpbは各遺伝子が突然変異を起こす確率。
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    #評価したい関数の設定（目的関数のこと）
    toolbox.register("evaluate", evaluate)

    #乱数を固定
    random.seed(64)
    #何世代まで行うか
    NGEN = 50
    #集団の個体数
    POP = 80
    #交叉確率
    CXPB = 0.9
    #個体が突然変異を起こす確率
    MUTPB = 0.1

    #集団は80個体という情報の設定
    pop = toolbox.population(n=POP)
    #集団内の個体それぞれの適応度（目的関数の値）を計算
    for individual in pop:
        individual.fitness.values = toolbox.evaluate(individual)
    #パレート曲線上の個体(つまり、良い結果の個体)をhofという変数に格納
    hof = tools.ParetoFront()

    #今回は最も単純なSimple GAという進化戦略を採用
    algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=NGEN, halloffame=hof)

    #最終的な集団(pop)からベストな個体を1体選出する関数
    best_ind = tools.selBest(pop, 1)[0]

    return(best_ind, best_ind.fitness.values)


if __name__ == "__main__":
    best_ind, fitness_vals = calc_best_individual()
    
    #結果表示
    print(f"最も良い個体は{best_ind}で、そのときの目的関数の値は{fitness_vals}")



