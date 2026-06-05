import argparse
import os
import zipfile
from pathlib import Path
import ast
import json

def main():
    with open('main.py') as f:
        s = f.read()
        print(ast.dump(ast.parse(s), indent=4))
    # parser = argparse.ArgumentParser(
        # prog="scrython",
        # description="a simple python to scratch transpiler",
        # epilog="made by soul with love"
    # )

    # parser.add_argument('folder')
    # parser.add_argument('output')

    # args = parser.parse_args()
    
    # files = [f for r, d, files in os.walk(args.folder) for f in files if f.endswith('.py')]
    
    # for file in files:
        # print(ast.dump(ast.parse()))

    # targets = []
    # monitors = []
    # extensions = []
    # meta = {
    #     "semver": "3.0.0",
    #     "vm": "14.1.0",
    #     "agent": "Scrython Compiler v1.0.0"
    # }

    # project_json = json.dump({
    #     "targets": targets,
    #     "monitors": monitors,
    #     "extensions": extensions,
    #     "meta": meta
    # })

    # filename = args.output
    # if not '.sb3' in filename:
    #     filename += '.sb3'

    # with zipfile.ZipFile(filename, 'w') as zip:
    #     zip.write(project_json)

if __name__ == '__main__':
    main()