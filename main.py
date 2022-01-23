'''
>>> import csv
>>> with open('eggs.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
'''

# %%
import os
import csv
from datetime import datetime


def load_file(path: str):
    '''Simply load a CSV file and return it'''
    output = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            output.append(row)

    return output


def save_file(path: str, data):
    '''Simply save a CSV file'''
    with open(path, 'wt', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)


def fix_format(data):
    '''Add a column on the left and transform the date to something Notion will read'''

    header = True
    row: list
    for row in data:
        # Convert the date on non-header rows
        if not header:
            row[0] = convert_date(row[0])

        # Add a rows to the left
        if header:
            row.insert(0, 'Game')
        else:
            row.insert(0, '')

        if header:
            header = False


def convert_date(text):
    '''Convert a date in the form "Mon Feb 24 2020" into the form "September 10, 2021"'''

    twitch_date = datetime.strptime(text, '%a %b %d %Y')
    notion_text = twitch_date.strftime('%Y-%m-%d')
    return notion_text


def do_file(path, in_dir, out_dir):
    data = load_file(f'{in_dir}/{path}')
    fix_format(data)
    save_file(f'{out_dir}/{path}', data)


def do_whole_dir(in_dir, out_dir):
    files = os.listdir(in_dir)
    for file in files:
        print(f'Doing {file}...')
        do_file(file, in_dir, out_dir)


# %%
# set these to you intake folder and output folder
in_dir = 'data_raw'
out_dir = 'data_notion'


print('Mentally preparing to do the thing!')
# do_file(path, in_dir, out_dir)
do_whole_dir(in_dir, out_dir)
print('Did the thing!')

# %%
