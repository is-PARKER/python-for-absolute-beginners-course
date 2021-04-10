d = {
    'Sam': 0,
    'rolls': [],
    'done': False,
}

def main():
    sam_raise()
    get_rolls()
    bool_flip()
    give_n()
    print_all()


def get_rolls():
    if d['rolls'] == []:
        n = ['rock', 'paper', 'scissors']
        return n

def give_n():
    add_n = get_rolls()
    d['rolls'] = add_n

def sam_raise():
    while not d['Sam'] == 7:
        d['Sam'] += 1

def bool_flip():
    if d['done'] == False:
        d['done'] = True


def print_all():
    print(d["Sam"])
    print(d['rolls'])
    print(d.get('Sarah'))
    print(d.get('Jeff', -1))
    print(d['done'])

if __name__ == '__main__':
    main()



