from deap import tools

def selTournamentRemoveSame(individuals, k, tournsize):
    temp_append = list()
    temp_init = tools.selTournament(individuals, k, tournsize=tournsize)

    # temp_init에서 duplicates 제거
    for sublist in temp_init:
        if sublist not in temp_append:
            temp_append.append(sublist)
    # k개보다 적을 때 추가로 add
    while len(temp_append) < k:
        temp_add = tools.selRandom(individuals, int((k - len(temp_append))))
        for adding in temp_add:
            if adding not in temp_append:
                temp_append.append(adding)
    temp_result = temp_append

    return temp_result

def selNSGA2RemoveSame(individuals, k, nd='standard'):
    temp_append = list()
    temp_init = tools.selNSGA2(individuals, k, nd=nd)

    # temp_init에서 duplicates 제거
    for sublist in temp_init:
        if sublist not in temp_append:
            temp_append.append(sublist)
    # k개보다 적을 때 추가로 add
    while len(temp_append) < k:
        temp_add = tools.selRandom(individuals, int((k - len(temp_append))))
        for adding in temp_add:
            if adding not in temp_append:
                temp_append.append(adding)
    temp_result = temp_append

    return temp_result

def selBestRemoveSame(individuals, k, fit_attr='fitness'):
    temp_append = list()
    temp_init = tools.selBest(individuals, k, fit_attr=fit_attr)

    # temp_init에서 duplicates 제거
    for sublist in temp_init:
        if sublist not in temp_append:
            temp_append.append(sublist)
    # k개보다 적을 때 추가로 add
    while len(temp_append) < k:
        temp_add = tools.selRandom(individuals, int((k - len(temp_append))))
        for adding in temp_add:
            if adding not in temp_append:
                temp_append.append(adding)
    temp_result = temp_append

    return temp_result

def selSPEA2RemoveSame(individuals, k):
    temp_append = list()
    temp_init = tools.selSPEA2(individuals, k)

    # temp_init에서 duplicates 제거
    for sublist in temp_init:
        if sublist not in temp_append:
            temp_append.append(sublist)
    # k개보다 적을 때 추가로 add
    while len(temp_append) < k:
        temp_add = tools.selRandom(individuals, int((k - len(temp_append))))
        for adding in temp_add:
            if adding not in temp_append:
                temp_append.append(adding)
    temp_result = temp_append

    return temp_result

def selRandomRemoveSame(individuals, k):
    temp_append = list()
    temp_init = tools.selRandom(individuals, k)

    # temp_init에서 duplicates 제거
    for sublist in temp_init:
        if sublist not in temp_append:
            temp_append.append(sublist)
    # k개보다 적을 때 추가로 add
    while len(temp_append) < k:
        temp_add = tools.selRandom(individuals, int((k - len(temp_append))))
        for adding in temp_add:
            if adding not in temp_append:
                temp_append.append(adding)
    temp_result = temp_append

    return temp_result