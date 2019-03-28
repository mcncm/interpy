#! /bin/python

import io
import re
import sys
import importlib
import argparse
import os
import os.path as path
import tokenize

interpy_dir = path.dirname(path.abspath(__file__))
lang_dir = path.join(interpy_dir, 'bindings')


def supported_langs():
    # Get the list of language bindings in the language directory.
    # This implementation is a little fragile, but it should work for now.
    excluded_items = set({'__init__.py', '__pycache__', 'template.py'})
    return [ l[:-3] for l in set(os.listdir(lang_dir)) - excluded_items]

def lang_from_args():
    # Parse the command-line arguments to check for language.
    ap = argparse.ArgumentParser()
    ap.add_argument("-l", "--lang", required=False,
                    help="language: " + ", ".join(supported_langs()))
    ap.add_argument('filename', nargs='+', action='store')
    args = vars(ap.parse_args()) 
    try:
        lang = args["lang"]
        if lang not in supported_langs():
            return None
    except:
        lang = None
    return lang


def lang_from_annotation(script_file):
    # Search the input file for a language hint of the form `# lang=xx`
    regex = "^\s*\#\s*lang=.*$"
    # Search so many of the first lines. This is an ugly magic constant that
    # you should get rid of whne it makes sense to do so.
    num_lines = 10
    with open(script_file, 'r') as f:
        for _ in range(num_lines):
            line = f.readline()
            match = re.match(regex, line)
            if match:
                lang = line.rstrip().split("=")[-1] 
                if lang in supported_langs():
                    return lang
    return None


def lang_from_wc(script_file):
    # Check script file for clues about the language from naive word frequency
    # analysis.
    return None


def script_arg_passed():
    # Checks whether the last argument is a python script
    # (In current implementation, only makes sure that it's a file.)
    last_arg = sys.argv[-1]
    return path.isfile(path.abspath(last_arg))


def get_mode():
    # First try to get the language from command-line arguments and enter an
    # repl if no script is supplied.
    mode_func = None    
    lang_name = lang_from_args()
    if not script_arg_passed():
        if lang_name:
            set_lang(lang_name)
            return repl_mode
        # Otherwise, check if there's an '-o' option. If so, compile it. Otherwise,
        # execute the script.
        # For now, we'll just execute the script unconditionally.
    else:
        if lang_name:
            set_lang(lang_name)
            return exec_mode
        else:
            lang_name = lang_from_annotation(sys.argv[-1])
            set_lang(lang_name)
            return exec_mode

    return mode_func


def identify_lang():
    # Either accept a language option or infer language from script annotation
    if len(sys.argv) > 2:
        if sys.argv[1][0:2] == '--' and sys.argv[1][2:] in supported_langs():
            lang_name = sys.argv[1][2:]
        script_file = sys.argv[2]
    else:
        # Look for an annotation for hints
        script_file = sys.argv[1]
        with open(script_file, 'r') as f:
            line = f.readline()
            while line:
                pass
    
    # Do something if you encounter an unsupported language
    if lang_name not in supported_langs():
        raise Error()

    return lang_name, script_file


def set_lang(lang_name):
    # Reads the file of special identifiers for the desired language and returns
    # the resulting dictionary.
    try:
        # Note that this genuinely breaks abstraction barriers. Must not be
        # lazy about namespaces like this.
        global lang
        lang = importlib.import_module("bindings." + lang_name)
    except:
        print("No such language file was found!")
    
    return


def transcribe_line(line):
    # Transcripe a single line of text and return the normal-python result.

    line = bytes(line.encode())
    line = io.BytesIO(line)
    line = list(tokenize.tokenize(line.readline))
    # `offset` tracks the difference in character number between the
    # original and modified scripts.
    offset = 0
    for i in range(len(line)):
        token = line[i]
        new_start = (token.start[0], token.start[1] + offset)
        new_string = token.string
        if new_string in lang.tokens.keys():
            offset += len(lang.tokens[token.string]) - len(token.string) 
            new_string = lang.tokens[token.string]
        new_end = (token.end[0], token.end[1] + offset)
        line[i] = tokenize.TokenInfo(type=token.type, string=new_string,
            start=new_start, end=new_end, line=token.line)
    line = tokenize.untokenize(line).decode('utf8')
    return line


def read_input(script_file):
    # Read in and tokenize the script, translating each identifier.
    # Return the translated script.
    with open(script_file, 'r') as f:
        script = f.readlines()
    out_script = ''
    for line in script:
        out_script += transcribe_line(line)
    return out_script


### MODE FUNCTIONS

def repl_mode():
    pass

def compiler_mode():
    pass

def exec_mode():
    script = read_input(path.abspath(sys.argv[-1]))
    exec(script)

### END MODE FUNCTIONS

if __name__ == '__main__':
    # Determine what to do with the code
    mode_func = get_mode()
    # Do it!
    mode_func()
