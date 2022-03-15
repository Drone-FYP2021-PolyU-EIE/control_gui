import os

message = input('your commit comment:')
os.system('git status')
os.system('git add .')
os.system('git commit -m "{}"'.format(message))
os.system('git push')

print('finished')
