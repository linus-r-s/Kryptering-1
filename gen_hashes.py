import crypt

def gen_hashes():
  hashes = []
  with open('users_plain.txt', 'r') as f:
    for line in f.readlines():
      line = line.rstrip()
      hashes.append(f'{line.split(":")[0]}:{crypt.crypt(line.split(":")[1])}')
  with open('user_hashes.txt', 'w') as f:
    for line in hashes:
      f.write(line + '\n')