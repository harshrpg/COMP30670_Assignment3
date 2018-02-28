import argparse
from Lights import Lights
import re


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="Parameter required to provide input to the program", action="store_true")
    parser.add_argument("filename", help="Complete path for the file")
    args = parser.parse_args()
    if args.input:
        count = ""
        with open(args.filename, 'r') as fin:
            L = int(fin.readline())
            if L > 0:
                _lights = Lights(L)
            regex = re.compile(
                ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
            for i in fin.readlines():
                result = regex.search(i)
                if result != None:
                    method = str(result.group(1))
                    l1 = int(result.group(2))
                    l2 = int(result.group(3))
                    l3 = int(result.group(4))
                    l4 = int(result.group(5))
                    if l1 >= 0 and l2 >= 0 and l3 >= 0 and l4 >= 0 and l1 < L and l2 < L and l3 < L and l4 < L:
                        count = _lights.runCmd(method, l1, l2, l3, l4)
                    else:
                        continue

        print(count)


if __name__ == "__main__":
    main()
