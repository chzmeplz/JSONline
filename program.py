current_json = {}


def main():
    print_header()
    do_stuff()
    print_json()


def print_header():
    print('|-------------------------|')
    print('| JSON Commandline Editor |')
    print('|-------------------------|')


def print_json():
    for key in current_json:
        print(key)


def do_stuff():
    current_json['test'] = 'value'


main()
