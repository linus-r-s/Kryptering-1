def gen_dict():
  d = []
  i = 0
  with open('svenska-ord/svenska-ord.txt', 'r') as f:
    for line in f.readlines():
      if i % 250 == 0:
        d.append(line)
      i = i + 1
  with open('dict-small.txt', 'w') as f:
    for word in d:
      f.write(word)