#!/usr/local/bin/python3

import os
import sys
import json
import base64
from time import sleep
from shutil import copy
from pprint import pprint

default = ("server", "server_port", "protocol", "method", "obfs", "password")


def change():
    ssr = input('[*] SSR:\n')
    if not ssr.startswith('ssr://'):
        print('[-] SSR Code Not Correct!\n')
        return
    ssr = ssr.replace('ssr://', '')
    if len(ssr) % 4:
        ssr += '=' * (4 - len(ssr) % 4)
    bdecode = base64.b64decode if not (
        '_' in ssr or '-' in ssr) else base64.urlsafe_b64decode

    try:
        bd = bdecode(ssr).decode('utf-8').split(':')
    except Exception as e:
        print("[-] An Error Came Out:\n" + str(e) + '\n')
        return
    pwd, _ = bd[-1].split('/?')
    if len(pwd) % 4:
        pwd += '=' * (4 - len(pwd) % 4)
    pwd = base64.b64decode(pwd).decode('utf-8')
    bd[-1] = pwd

    json_dict = dict(zip(default, bd))
    print('[+] JSON:\n' + '-' * 50)
    pprint(json_dict)
    print('-' * 50)

    if input('[*] Do you want to write it to shadowsocks.json ?(Y/n):') in (
            'yes', 'Y', 'y', 'Yes'):
        with open('./shadowsocks.json', 'w') as fp:
            json.dump(json_dict, fp, indent=4)
        print('[+] shadowsocks.json writed.\n')


def switch():
    try:
        choice = int(input("\n[*] What would you like to choice?\n[1] Start Proxy\n[2] Stop Proxy\n[*]:")) - 1
        cmd = ("restart", "stop")[choice]
    except:
        print("[-] Wrong Input!\n")
        return
    print("[+] Let's Fly!")
    sleep(0.5)
    os.system("./shadowsocksr/shadowsocks/local.py -c ./shadowsocks.json -d " + cmd)
    print()


def backup():
    while True:
        options = input('\n[1] Use "shadowsocks.json.bak" To Replace(Produce) "shadowsocks.json"\n[2] Use "shadowsocks.json" To Replace(Produce) "shadowsocks.json.bak"\n[3] Quit\n[*]:')
        if options in ('1', '2'):
            if options == '1':
                copy("./shadowsocks.json.bak", "./shadowsocks.json")
            if options == '2':
                copy("./shadowsocks.json", "./shadowsocks.json.bak")
            print("[+] Done!")
            break
        if options=='3':
            break
    print()


def main():
    os.chdir(sys.path[0])
    print('Welcome !')
    while True:
        s = input(
            '[1] Translate SSR Code to JSON\n[2] Proxy Server Options\n[3] Backup Options\n[4] Quit\n[*]:'
        )
        change() if s == '1' else switch() if s == '2' else backup(
        ) if s == '3' else exit(0) if s in ('4', 'q', 'quit',
                                            'exit') else print()


if __name__ == '__main__':
    main()
