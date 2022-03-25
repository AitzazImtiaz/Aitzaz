from colorama import Fore
def main():
    infinity=1
    while infinity==1:
        print(Fore.GREEN+"~ $ I am Aitzaz Imtiaz")
    try:
        main()
    except KeyboardInterrupt:
        print('~ $ I am Aitzaz Imtiaz')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
