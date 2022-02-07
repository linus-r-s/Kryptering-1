from cracker import crack

dictionary = open('dict-small.txt', 'r').read().split('\n')
hashes = open('user_hashes.txt', 'r').readlines()

crack(hashes, dictionary, numbers=False)