# 2307 양혜원
import random


def func_lotto():
    result = []
    for i in range(0, 6):
        n = random.randint(1, 46)
        result.append(n)

    result.sort()
    print("당첨번호 : {} {} {} {} {} {}".format(
        result[0], result[1], result[2], result[3], result[4], result[5]))


func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
func_lotto()
