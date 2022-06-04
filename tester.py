import os
import subprocess
import sys
from pathlib import Path

import colorama
from colorama import Back
from colorama import Style

colorama.init()

d = {0: "git tests", 1: "plus tests", 2: "minus tests", 3: "mult tests", 4: "div tests", 5: "module tests",
     6: "sqrt tests", 7: "compare tests", 8: "random tests"}

count = 0
total = 0

for j in range(len(d)):
    print(Back.MAGENTA + f"{d[j]}\n")
    for i in range(len(list(Path(f"samples/{d[j]}/").iterdir()))):
        try:
            total += 1
            print(Back.CYAN + f"test {i}: ", end="")
            subprocess.call(["java", "-jar", "tester.jar", f"samples/{d[j]}/in{i}.txt", f"out_ref{i}.txt"])
            subprocess.run([sys.argv[1], f"samples/{d[j]}/in{i}.txt", f"out{i}.txt"])
            with open(f"out_ref{i}.txt") as first, open(f"out{i}.txt") as second:
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

            os.remove(f"out{i}.txt")
            os.remove(f"out_ref{i}.txt")
        except FileNotFoundError:
            print(Back.RED + "Выходной файл не создался, что скорее всего значит программа упала", end="")
            os.remove(f"out_ref{i}.txt")
    print()

print(Back.MAGENTA + f"Total count: {count}/{total}")

