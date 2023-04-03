import itertools
from random import sample

from utils import stack


def combine(choosen_letter, n, k, s):
    print(f"===========================Combine Function===============================")
    combinations = []
    print(f"--------------------------situation----------------------------")
    middle_letters = choosen_letter[:n - k + s]
    middle_combinations = list(itertools.combinations(middle_letters, s))
    tail_letters = choosen_letter[n - k + s:]
    tail_combinations = list(itertools.combinations(tail_letters, k - s))
    print(middle_combinations, tail_combinations)
    for middle_combination in middle_combinations:
        for tail_combination in tail_combinations:
            temp = list(middle_combination) + list(tail_combination)
            print("temp" + str(temp))
            combinations.append(list(middle_combination) + list(tail_combination))
    print("---------------------------final combination-------------------------")
    for combination in combinations:
        print(combination)
    print(len(combinations))
    return combinations


def select(combinations,validation_sets):
    print(f"===========================Select Function===============================")

    valid_combinations = []

    while (len(validation_sets) != 0):
        combination = satistic(combinations,validation_sets)
        print(str(combinations))
        # print(combination)
        # combinations = combinations.remove(combination)
        print("combination:" + str(combination))
        for validation_set in validation_sets:
            print("validation_set:" + str(validation_set))
            if set(validation_set).issubset(set(combination)):
                print("-------------------------")
                flag = 1

        validation_sets = [s for s in validation_sets if not set(s).issubset(set(combination))]
        if flag == 1:
            valid_combinations.append(combination)
            combinations.remove(combination)
            print("^^^^^^^^^^^^")
            print("Add combination" + str(combination))
        print("num of combinations:" + str(len(combinations)))
        print("num of validation_sets:" + str(len(validation_sets)))
        print("num of valid_combinations:" + str(len(valid_combinations)))
    print("---------------------result--------------------------")
    print(valid_combinations)
    print(len(valid_combinations))
    return valid_combinations


def satistic(combinations,validation_sets):
    max_count = 0
    max_list = []
    # combinations.reverse()
    print("combinations_r:" + str(combinations))
    for combination in combinations:
        count = 0
        # for combination in combinations:
        for validation_set in validation_sets:
            if set(validation_set).issubset(set(combination)):
                # print("-------------------------")
                count += 1
        if count > max_count:
            max_count = count
            max_list = combination
        # weight.update({combination: count})
        if count != 0:
            print("combination:" + str(combination) + ",count:"+str(count))

    # weight = sorted(weight, key=lambda x:x[0])

    print("weight:" + str(max_count))
    return max_list

def satistic_reverse(combinations, validation_sets):
    max_count = 0
    max_list = []
    # combinations.reverse()
    # print("combinations_r:" + str(combinations))
    for validation_set in validation_sets:

        count = 0
        # for combination in combinations:
        for combination in combinations:
            if set(validation_set).issubset(set(combination)):
                # print("-------------------------")
                combinations.remove(combination)
                count += 1
        if count > max_count:
            max_count = count
            max_list = validation_set
        # weight.update({combination: count})
        # print("combination:" + str(combination) + ",count:"+str(count))

    # weight = sorted(weight, key=lambda x:x[0])
    # combinations.remove(max_list)
    # print("weight:" + str(max_count))
    return max_list

def remove_duplicate_rows(arr):
    unique_rows = []
    seen = set()

    for row in arr:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(list(row_tuple))

    return unique_rows



def search(m, n, k, j, s):

    validation_sets = []
    potential_letter = list(x for x in range(m))
    # choosen_letter = sample(potential_letter, n)
    # choosen_letter.sort()

    # choosen_letter = list(x for x in range(n)) # test
    choosen_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H", 'I', "J"]  # test
    print(choosen_letter)
    validation_sets = list(itertools.combinations(choosen_letter, s))

    print("--------combinations----")
    # combinations = combine(choosen_letter, n, k, s)
    combinations = list(itertools.combinations(choosen_letter, k))
    # combination_first = list(itertools.combinations(choosen_letter, j))
    # validation_sets = select(combination_first, validation_sets)

    print("-----------validation_sets----------")
    validation_sets = []
    tmp_sets = list(itertools.combinations(choosen_letter, j))
    print("first_validation_sets:" + str(tmp_sets))
    print("length:" + str(len(tmp_sets)))
    for tmp_set in tmp_sets:
        small = list((itertools.combinations(tmp_set, s)))
        print(small)
        small.sort()
        length = len(small) // 2
        d = satistic_reverse(tmp_sets, small)
        validation_sets.append(d)
    # print("final_validation_sets:" + str(validation_sets))
    # print("length:" + str(len(validation_sets)))
    validation_sets = remove_duplicate_rows(validation_sets)
    print("final_validation_sets:" + str(validation_sets))
    print("length:" + str(len(validation_sets)))

    select(combinations, validation_sets)


if __name__ == '__main__':
    # search(45, 10, 6, 6, 4)
    # search(45, 9, 6, 4, 4)
    search(45, 10, 6, 6, 4)
