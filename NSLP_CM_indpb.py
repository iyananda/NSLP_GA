import pandas as pd
import numpy as np

input_table = pd.read_csv('input_sam.csv')  # 파일경로
logname = "test_ams.txt" # 로그파일

input_table = input_table.as_matrix()

link_num = len(input_table[0])
sample_num = len(input_table)


def vi_cal(input_sensor_location):
    # input_sensor_location = [1,2]  #센서 위치를 링크 번호 기준으로 넣어주면 됨. (첫번째 링크가 1임) 단, 오름차순으로 넣어야 함.
    ref_pair = []
    ref_pair_num = []
    result = []
    line_pair = []
    VI = 0
    for line in input_table:
        line_pair = [line[i] for i in input_sensor_location]
        if line_pair not in ref_pair:
            # 새로운 쌍이 들어온 경우 ref_pair에 추가해주고 덧셈을 위한 null array를 result에 추가해줌.
            ref_pair.append(line_pair)
            temp = [[0.0, 0.0] for _ in range(link_num)]
            temp = np.asarray(temp)
            result.append(temp)
            ref_pair_num.append(0)
        temp = np.append(line, line ** 2)
        t = ref_pair.index(line_pair)
        ref_pair_num[t] += 1
        result[t] += np.vstack((line, line ** 2)).T

    for k in range(len(result)):
        temp = result[k].T
        VI += np.sum(temp[1] / ref_pair_num[k] - (temp[0] / ref_pair_num[k]) ** 2) * ref_pair_num[k]

    VI = VI / sample_num
    return VI

import random


import numpy

from functools import partial

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import multiprocessing

import time

import json

from functions import selNSGA2RemoveSame

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)


toolbox = base.Toolbox()

def evalOneMin(individual):
    return vi_cal(individual),


## register

#링크수, 센서수 입력



def setlink_NSGA2(numberoflinks, sensored, crspb, mutpb):
    print("--%s sensored links of %s total links--" % (sensored, numberoflinks))
# 개체생성기
    gen_ind = partial(random.sample, range(numberoflinks), sensored)


# Structure initializers
    toolbox.register("individual", tools.initIterate, creator.Individual, gen_ind)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evalOneMin)
    toolbox.register("mate", tools.cxUniform, indpb=mutpb)
    toolbox.register("mutate", tools.mutUniformInt, low = 0, up = numberoflinks, indpb=(crspb))
    toolbox.register("select", selNSGA2RemoveSame)

    print("Selection = NSGA-Ⅱ")
    logf = open(logname, "a")
    logf.write("\n\nSelection = NSGA-Ⅱ\n\n")
    logf.write("--%s sensored links of %s total links--" % (sensored, numberoflinks))
    logf.write("\n\n")
    logf.close

    print("--- Crossover Indpb= %s, Mutation Indpb= %s ---" % (crspb, mutpb))
    logf = open(logname, "a")
    logf.write("--- Crossover Indpb= %s, Mutation Indpb= %s ---" % (crspb, mutpb))
    logf.close

def timeview(*args):
    tt = (time.time() - start_time)
    return tt

def main(sdn):

    pool = multiprocessing.Pool()
    toolbox.register("map", pool.map)

    random.seed(sdn)
    print("--- Seed Number = %s ---" % sdn)
    logf = open(logname, "a")
    logf.write("Seed Number = %s\n\n" % sdn)
    logf.close

    pop = toolbox.population(n=200)
    hof = tools.HallOfFame(100)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    stats.register("time", timeview)

    pop, log = algorithms.eaMuPlusLambda(pop, toolbox, mu=10, lambda_=200, cxpb=0.3, mutpb=0.7, ngen=50,
                                         stats=stats, halloffame=hof, verbose=True)
    print(hof)

    ctime = time.time() - start_time

    print("--- Total %s seconds ---" % (time.time() - start_time))


    logf = open(logname, "a")
    for k in log:
        logf.write(json.dumps(k))
        logf.write("\n")
    logf.write("\n")
    hof_e = ""
    for j in hof:
        hof_e = hof_e + str(j) + ","
    logf.write(hof_e)
    logf.write("\n\n")
    logf.write("Total calculation time = %s" % ctime)
    logf.write("\n\n")
    logf.close

    return pop, log, hof, ctime

for i in range(7,10,2):
    for j in range(65,66):
        if __name__ == "__main__":
            start_time = time.time()
            setlink_NSGA2(277, 3, 0.5, i/10)
            p_n, l_n, h_n, t_n = main(j)

for i in range(9,10,2):
    for j in range(61,66):
        if __name__ == "__main__":
            start_time = time.time()
            setlink_NSGA2(277, 3, 0.5, i/10)
            p_n, l_n, h_n, t_n = main(j)