"""
Misc helper functions
"""

def stdmsg(msg: str, level: str = "INFO", logfile: str = None):
    """ Print info,warning,error and other messages to standard streams
    INFO -level (default) messages print to stdout,
    other levels print to stderr
    """
    import sys
    msg = f"*** {level}: {msg}"

    if level == "INFO":
        stream = sys.stdout
    else:
        stream = sys.stderr

    print(msg, file=stream)

    if logfile:
        with open(pathcheck(logfile), 'a') as f:
            f.write(msg + "\n")


def pathcheck(target: str, maxfiles: int = 5) -> str:
    """ Test if path to file or directory exists """
    from pathlib import Path
    # TODO: is_dir() ?
    if '/' in target:
        if target.endswith('/'):
            dirpath = target
            filename = None
        else:
            foo = target.split('/')
            dirpath = '/'.join(foo[:-1]) + '/'
            filename = foo[-1]
    else:
        dirpath = "./"
        filename = target

    # test dir
    if Path(dirpath).exists():
        if filename:
            if '.' not in filename:
                filename = filename + ".txt"
                stdmsg(f"Filetype not specified, saving as txt-file")
        
            # test filename
            validpath = Path(dirpath + filename)
            bar = filename.split('.')
            i = 1
            while validpath.is_file() and i <= maxfiles:
                newname = f"({i}).".join(bar)
                validpath = Path(dirpath + newname)
                i+=1

            if i > maxfiles:
                stdmsg(f"File already exists, overwriting: {filename}", 
                level="WARNING")
        else:
            validpath = dirpath
    else:
        # TODO: avoid error?
        raise FileNotFoundError(dirpath)


    return validpath


if __name__ == "__main__":
    testpaths = ["./", "./newfile", "/newfile", "./newfile.dat", "newfile", 
        "newfile.dat"]

    for tp in testpaths:
        print(f"{tp=}")
        print(f"{pathcheck(tp)=}")
    
    print(f"\N{goat}")