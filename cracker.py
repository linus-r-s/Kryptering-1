import crypt
import time
from hmac import compare_digest as compare_hash

def crack(hashes, dictionary, numbers=False):
  start = time.time()
  total = len(hashes)
  cracked = 0
  print('*** Linus Lösenordsknäckare 1.0 ***')
  print('Knäcker lösenord, var vänlig vänta...')
  for user in hashes:
    user_cracked = False
    user_name, hash = user.split(':')
    hash = hash.rstrip()
    print(f'[*] Försöker knäcka {user_name}...')
    for word in dictionary:
      if compare_hash(hash, crypt.crypt(word, hash)):
        print(f'[+] Knäckte lösenord:\n\tanvändarnamn:\t{user_name}\n\tlösenord:\t\t{word}')
        cracked += 1
        user_cracked = True
        break
      if numbers:
        for i in range(1200, 1250):
          if compare_hash(hash, crypt.crypt(word+str(i), hash)):
            print(f'[+] Knäckte lösenord:\n\tanvändarnamn:\t{user_name}\n\tlösenord:\t\t{word+str(i)}')
            cracked += 1
            user_cracked = True
            break
    if not user_cracked:
      print(f'[-] Kunde inte knäcka lösenordet för {user_name}.')
    end = time.time()
    total_time = end - start

  print(f'[*] Färdig! Knäckte {cracked} av {total} lösenord på {round(total_time, 2)} s.')