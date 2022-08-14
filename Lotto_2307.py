#2307 양혜원
import random
import string

def func_lotto():
    str1 = ""
    for i in range(0,6):
        str1 += (str(random.randint(1, 46)))+" "
    print("당첨번호 : ", str1)

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