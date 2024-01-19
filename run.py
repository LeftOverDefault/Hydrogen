from src.utils.imports import *

from src.main import Main
from src.shell import Shell


if __name__ == "__main__":
    exec_time = time.time()
    os.system(command="cls")
    main = Main()
    shell = Shell()
    print("- Enter Mode -")
    print(" 1) Debug")
    print(" 2) Shell")
    mode = str(input(">>> "))
    if mode == "1" or mode.lower() == "debug":
        main.run()
    elif mode == "2" or mode.lower() == "shell":
        shell.run()

    print("Estimated Execution Time:", str(round(time.time() - exec_time, 5)) + "s")
