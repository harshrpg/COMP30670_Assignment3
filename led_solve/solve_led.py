import argparse
from Lights import Lights
import re
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", "-i", help="Parameter required to provide input to the program", action="store_true")
    parser.add_argument("filename", help="Complete path for the file")
    args = parser.parse_args()
    filePath = args.filename
    if args.input:
        count = ""
        if filePath.startswith("http:"):
            response = requests.get(filePath)
            with open('input.txt', 'w') as fout:
                fout.writelines(response.text)
            fout.close()
            filePath = 'input.txt'
        with open(filePath) as fin:
            L = int(fin.readline())
            if L > 0:
                _lights = Lights(L)
            regex = re.compile(
                ".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
            for i in fin.readlines():
                result = regex.search(i)
                if result != None:
                    method = str(result.group(1))
                    # print(method.strip())
                    l1 = int(result.group(2))
                    l2 = int(result.group(3))
                    l3 = int(result.group(4))
                    l4 = int(result.group(5))
                    if l1 < 0:
                        l1 = 0
                    if l3 < 0:
                        l3 = 0
                    if l2 > L:
                        l2 = L-1
                    if l4 > L:
                        l4 = L-1
                    _lights.runCmd(method, l1, l2, l3, l4)

        count = _lights.counts()
        print(count)


if __name__ == "__main__":
    main()
