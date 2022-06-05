import os
import subprocess
import sys
from pathlib import Path

import colorama
from colorama import Back
from colorama import Style

colorama.init()

d = {0: "git tests", 1: "plus tests", 2: "minus tests", 3: "mult tests", 4: "div tests", 5: "module tests",
     6: "sqrt tests", 7: "compare tests", 8: "random tests", 9: "freaky tests"}

count = 0
total = 0

if len(sys.argv) == 2:
    for j in range(len(d)):
        print(Back.MAGENTA + f"{d[j]}\n")
        ls = os.listdir(f"samples/{d[j]}/")
        for i in range(len(ls)):
            try:
                total += 1
                print(Back.CYAN + f"test {ls[i]}: ", end="")
                st = str(ls[i])
                subprocess.call(["java", "-jar", "tester.jar", f"samples/{d[j]}/" + st, f"out_ref.txt"])
                subprocess.run([sys.argv[1], f"samples/{d[j]}/" + st, f"out.txt"])
                with open(f"out_ref.txt") as first, open(f"out.txt") as second:
                    fl = True
                    pairs = list(zip(first.readlines(), second.readlines()))
                    cnt = 1
                    for pair in pairs:
                        line1 = pair[0].rstrip()
                        line2 = pair[1].rstrip()
                        if line1 != line2:
                            fl = False
                            break
                        cnt += 1
                    if fl:
                        print(Back.GREEN + "Passed", end="")
                        print(Style.RESET_ALL)
                        count += 1
                    else:
                        print(Back.RED + "Failed", end="")
                        print(Style.RESET_ALL)

                os.remove(f"out.txt")
                os.remove(f"out_ref.txt")
            except FileNotFoundError:
                print(Back.RED + "Выходной файл не создался (программа упала)", end="")
                print(Style.RESET_ALL)
                os.remove(f"out_ref.txt")
        print()

    # print(Back.MAGENTA + f"Total count: {count}/{total}")

else:
    print(Back.MAGENTA + f"{sys.argv[2]}\n")
    ls = os.listdir(f"samples/{sys.argv[2]}/")
    for i in range(len(ls)):
        try:
            total += 1
            print(Back.CYAN + f"test {ls[i]}: ", end="")
            st = str(ls[i])
            subprocess.call(["java", "-jar", "tester.jar", f"samples/{sys.argv[2]}/" + st, f"out_ref.txt"])
            subprocess.run([sys.argv[1], f"samples/{sys.argv[2]}/" + st, f"out.txt"])
            with open(f"out_ref.txt") as first, open(f"out.txt") as second:
                fl = True
                pairs = list(zip(first.readlines(), second.readlines()))
                cnt = 1
                for pair in pairs:
                    line1 = pair[0].rstrip()
                    line2 = pair[1].rstrip()
                    if line1 != line2:
                        fl = False
                        break
                    cnt += 1
                if fl:
                    print(Back.GREEN + "Passed", end="")
                    print(Style.RESET_ALL)
                    count += 1
                else:
                    print(Back.RED + "Failed", end="")
                    print(Style.RESET_ALL)

            os.remove(f"out.txt")
            os.remove(f"out_ref.txt")
        except FileNotFoundError:
            print(Back.RED + "Выходной файл не создался (программа упала)", end="")
            print(Style.RESET_ALL)
            os.remove(f"out_ref.txt")
    print()

print(Back.MAGENTA + f"Total count: {count}/{total}")