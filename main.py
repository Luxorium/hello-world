from time import sleep
from datetime import date
from os import system

def main():
    system('clear')
    print('Hello world! My name is Caleb.')
    print('Today\'s date is ' + date.today().strftime('%B %d, %Y') + '.')
    print('My favorite food is pizza.')

    x = 5
    x = x + 10
    print(x)

    x = 10
    x = x + 10
    print(x)

    sleep(10)

if __name__ == '__main__':
    main()