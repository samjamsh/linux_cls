from sys import stdout, argv, platform

def parameters():
    def check_os():
        os = platform
        supported = ["linux"]
        if os not in supported: exit("operational system not supported")

    check_os()

    if len(argv) == 1:
        # clean default mode
        return 0

    elif len(argv) == 2 and argv[1] == "-i": # ignore cursor default location icdl
        # cleans with option
        return 1

    elif len(argv) == 2 and argv[1] == "-h": # ignore cursor default location icdl
        help_msg = """This is help message of MCP (Multplatform Clear Program) version 1.0
usage: python3 %s {option}\n\n[option]\n       -i  ignore default cursor location: this options cleans the terminal screen but do not put cursor on the default location (left top or on the left at the top) it just cleans and ignore cursor location
\nexample: python3 %s\n""" %(argv[0], argv[0])
        exit(help_msg)

    else:
        exit("parameter error: invalid parameter")


def clean_screen(option):
    cleanscreen = "\033[2J" # ASCII characters to clean screen
    cursor_dloc = "\033[H" # cursos default location

    if option == 0: # default mode
        clear = cleanscreen + cursor_dloc # ascii characters to clean screen and put cursor on default location

    elif option == 1: # ignore cursor default location mode
        clear = cleanscreen

    else: # option must be 0 or 1
        exit("source code syntax error")

    stdout.write(clear) # cleans screen
    stdout.flush() # do it now, clean screen right now (shows or print imediately what's in buffer)

clean_screen(parameters())
