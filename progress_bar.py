import colorama
# https://stackoverflow.com/questions/6840420/rewrite-multiple-lines-in-the-console
colorama.init()     # this enables \033[A characters


# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\033[K{prefix}')    # \033[K to clear line
    print(f'|{bar}| {percent}% {suffix}', end='\r\033[A')   # \033[A to move up one line
    # Print New Line on Complete
    if iteration == total:
        print('\033[KComplete!')
        print('\033[K', end='\r')

# old version
# print(f'\r{prefix}\n |{bar}| {percent}% {suffix}', end=print_end)
#     # Print New Line on Complete
#     if iteration == total:
#         print()
