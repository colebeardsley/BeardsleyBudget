#import numpy as np
import os
#import matplotlib as plt

run = 1

options = ['load', 'report', 'modify', 'exit']

master_file = 'Master.csv'

class Master:
    def __init__(self, filename):
        self.filename = filename

    def create_master(self):

        return 0

    def load_master(self):

        return 0

def Load():
    files = os.listdir()
    newfiles = []
    master_exists = 0

    for f in files:
        if f[-3:] == 'CSV':
            if f is not master_file:
                newfiles.append(f)
            else:
                master_exists = 1

    print('I found ' + str(len(newfiles)) + " csv files to use...")

    if master_exists == 1:
        print('Found the Master file...')
    else:
        create_master_option = input("I didn't find the Master file, do you want to create a new one? (yes or no): ")

        if create_master_option == "yes":
            create_master()
            master_exists = 1
        else:
            print('returning to menu...')


    return 0




while run == 1:

    do = input('What do you want to do? ("o" to see options): ')

    if do == 'o':
        for o in options:
            print(o)

    if do == 'load':
        Load()

    if do == 'report':
        print('Report is not yet implemented')

    if do == 'modify':
        print('Modify is not yet implemented')

    if do == 'exit':
        print('Goodbye!')
        run = 0




