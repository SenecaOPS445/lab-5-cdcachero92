#!/usr/bin/env python3
# Author ID: cdcachero


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    hello_file = open(file_name,'r')

    read_hello = hello_file.read()
    hello_file.close()
    return read_hello

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    
    hello_file = open(file_name,'r')

    list_hello = list(hello_file)
    
    clean_list = []
    for line in list_hello:
        clean_list.append(line.strip('\n'))

    hello_file.close()

    return clean_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
