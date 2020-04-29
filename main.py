#!/usr/bin/env python3
import pathlib
from string import Template
import shutil
import sys
from typing import Dict, Union

from num2words import num2words


def create_viewmodel(number: int, previous_number: int, previous_version: str) -> Dict[str, str]:
    number_str = str(number)
    value_name = num2words(number)
    previous_value_name = num2words(previous_number)
    return {
        'module_name': 'is-eq-' + value_name,
        'function_name': 'is' + number_str,
        'value': number_str,
        'value_name': value_name,
        'previous_package': 'is-eq-' + previous_value_name,
        'previous_package_version': previous_version,
        'previous_function_name': 'is' + str(previous_number)
    }


def render_template(template: str, viewmodel: Dict[str, str]) -> str:
    tpl = Template(template)
    return tpl.substitute(viewmodel)


def parse_template_package(path: pathlib.Path) -> Dict[str, str]:
    res = {}
    for file in path.glob('*.tpl'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        res['.'.join(file.name.split('.')[:-1])] = content
    return res


def render_template_package(template_package: Dict[str, str], viewmodel: Dict[str, str]) -> Dict[str, str]:
    res = {}
    for file_name, template in template_package.items():
        res[file_name] = render_template(template, viewmodel)
    return res


def create_package_dir(path: pathlib.Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_package(package: Dict[str, str], path: pathlib.Path) -> None:
    for file_name, content in package.items():
        with open(path.joinpath(file_name), 'w', encoding='utf-8') as f:
            f.write(content)


def remove_package(path: pathlib.Path) -> None:
    shutil.rmtree(str(path.resolve()).encode('utf-8'), True)


def main():
    if len(sys.argv) != 3:
        print('Usage: {} <start_number> <stop_number>'.format(sys.argv[0]))
        sys.exit(1)

    start, stop = map(int, sys.argv[1:])

    for i in range(start, stop):
        viewmodel = create_viewmodel(i, (i - 1) if i != 0 else 0, '1.1.0')
        package_name = viewmodel['module_name']
        package_path = pathlib.Path('./packages/').joinpath(package_name)
        remove_package(package_path)
        create_package_dir(package_path)

        if i % 10 == 0:
            template_path = pathlib.Path('.').joinpath('package-template-base')
        else:
            template_path = pathlib.Path('.').joinpath('package-template-recurrent')

        template = parse_template_package(template_path)
        package = render_template_package(template, viewmodel)
        write_package(package, package_path)


if __name__ == '__main__':
    main()
