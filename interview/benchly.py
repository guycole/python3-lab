#
# Title:benchly.py
# Description: benchly interview, html formatter
# Development Environment:Ubuntu 18.04.3 LTS (Bionic Beaver)/Python 3.6.8
# Legalise:Copyright (C) 2019 Miserable Bastards, INC.
# Author:G.S. Cole (guycole at gmail dot com)
#

def formatter(raw_string:str, format_commands:dict) -> str:
    raw_buffer = list(raw_string)
    result_buffer = []
    for ndx0, item in enumerate(raw_buffer):
        for ndx1 in format_commands:
            command_tuple = format_commands[ndx1]
            if command_tuple[0] == ndx0:
                result_buffer.append('<')
                result_buffer.append(ndx1)
                result_buffer.append('>')
            elif command_tuple[1] == ndx0:
                result_buffer.extend('</')
                result_buffer.append(ndx1)
                result_buffer.append('>')

        result_buffer.append(raw_buffer[ndx0])

    return ''.join(result_buffer)

if __name__ == '__main__':
    print(formatter("ABCDE", {'b': (0, 3), 'i': (1, 4)}))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
