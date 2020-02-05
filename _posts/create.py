# Script for creating a new blog post
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='create new blog post')
parser.add_argument('post_name', type=str, help='name of post')
args = parser.parse_args()
now = datetime.now()

if len(str(now.month)) == 1:
    month = '0' + str(now.month)
else:
    month = str(now.month)

if len(str(now.day)) == 1:
    day = '0' + str(now.day)
else:
    day = str(now.day)

file_name = str(now.year) + '-' + month + '-' + day + '-' + args.post_name + '.md'
file_name = file_name.replace(' ', '-')

file = open(file_name, 'w')

file.write('---\n')
file.write('layout: post\n')
file.write('title: "' + args.post_name + '"\n')
file.write('---\n')
file.write ('\n\n')
file.write('# ' + args.post_name)
file.write('\n\n\n')
