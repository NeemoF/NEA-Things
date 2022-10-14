import os

mainDirectory = os.getcwd()

while True:
    dirlist = os.listdir()
    removedFiles = [".git", ".upm", "poetry.lock",
                    "pyproject.toml", "README.md", ".config", "replit.nix", "venv", ".replit", 				 
                  	"__pycache__", ".cache"]
    for a in removedFiles:
        try:
            dirlist.remove(a)
        except:
            pass

    for i in range(len(dirlist)):
        print("%s: %s" % (i+1, dirlist[i]))
    print("-1: Back to start")

    userInput = int(input("Selection: "))
    if userInput == -1:
        os.chdir(mainDirectory)
    elif dirlist[userInput-1].endswith(".py"):
        os.system('python "%s"' % dirlist[userInput-1])
        print("="*50)
        print()
    else:
        os.chdir(dirlist[userInput-1])
    print()