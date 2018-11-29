import sys
import random

if len(sys.argv) < 3:
#    print '注意:'
    print ('gen_passwd.py [文字数] [行数]')
    exit()

if int(sys.argv[1]) > 30:
    print ('文字数が多すぎます(´・ω・`)')
    exit()
elif int(sys.argv[1]) <= 3:
    print('文字数が少なすぎます(´・ω・`)')
    exit()

if int(sys.argv[2]) > 10:
    print ('生成数が多すぎます(´・ω・`)')
    exit()
elif int(sys.argv[2]) <= 1:
    print('生成数が少なすぎます(´・ω・`)')

passlen = int(sys.argv[1])
count = int(sys.argv[2])
s = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789'
for i in range(count):
    password = ''
    for j in range(passlen):
        password += random.choice(s)
    print (password)
