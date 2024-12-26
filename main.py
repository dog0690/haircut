import time
import os
def main():
    i = 0
    k = 0
    j = 0
    l = 0
    while i <= 52:
        if i%3 == 0:
            k += 25
        if i%4 ==0:
            j +=30
        if i%4 ==0:
            l += 25
        difference = k-j
        difference2 = k-l
        os.system('cls')
        print(f"normal fade every 3 weeks: week({i}) cost({k})\n")
        print(f"skin fade every 4 weeks: week({i}) cost({j})\n")
        print(f"normal fade every 4 weeks: week({i}) cost({l})\n")
        print(f"difference for normal fade(3) and skin fade(3) ({difference})")
        print(f"difference for normal fade(3) and normal fade (4) ({difference2})")
        i += 1

main()