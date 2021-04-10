# Data Structures
#1. D

d = {
  'bob': 0,
  'sarah': 0,
  'defeated_by':{'paper', 'wolf'},
  'defeats':{'scissors', 'sponge'},
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['michael'] = 7
print(f"you are defeated by {d['defeated_by']}")