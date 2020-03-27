#!/usr/bin/python
# -*- coding: utf-8 -*-
# CoronaVirusInfo
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/CoronaVirusInfo

import os, sys, time, json
import requests as r
from time import sleep

class Main:
        def __init__(self):
                self.clearsc()
                self.barlogo()
                self.barmenu()
                self.country = 'https://api.kawalcorona.com/{}'
                self.idn = 'indonesia/provinsi'
                while True:
                        self.menu()
        def restart(self):
                python = sys.executable
                os.execl(python, python, * sys.argv)
                curdir = os.getcwd()
        def loads(self):
                o = [' .   ',' ..  ',' ... ']
                for i in o:
                        print('\r\033[0m[\033[0;33m●\033[0m] Sedang mengirim'+i,end=''),;sys.stdout.flush();time.sleep(1)
        def write(self,o):
                for i in o + '\n':
                        sys.stdout.write(i)
                        sys.stdout.flush()
                        time.sleep(0.03)
        def clearsc(self):
                os.system('clear')
                os.system('reset')
                sleep(1)
        def barlogo(self):
                logo = """
            \033[0;77;1m__    __           \033[0;77;1m      ___     ____
           \033[0;77;1m|  |  |  |          \033[0;77;1m     /__ |   / __ | \033[0;91m▬▬▬▬
 \033[0;77m░░\033[0;31m█▀▀\033[0;77m░\033[0;33m█▀█\033[0;77m░░\033[0;77;1m\ \  / /\033[0;77m░░\033[0;34m▀█▀\033[0;77m░\033[0;32m█▀▄\033[0;77m░░\033[0;77;1m       | |  / /_/ / \033[0;92m▬▬▬▬▬
 \033[0;77m░░\033[0;31m█\033[0;77m░░░\033[0;33m█\033[0;77m░\033[0;33m█\033[0;77m░░░\033[0;77;1m\ \/ /\033[0;77m░░░░\033[0;34m█\033[0;77m░░\033[0;32m█\033[0;77m░\033[0;32m█\033[0;77m░░\033[0;77;1m  _   _| |_ |__  / \033[0;93m▬▬▬▬▬
 \033[0;77m░░\033[0;31m▀▀▀\033[0;77m░\033[0;33m▀▀▀\033[0;77m░░░░\033[0;77;1m\__/\033[0;77m░░░░\033[0;34m▀▀▀\033[0;77m░\033[0;32m▀▀\033[0;77m░░░\033[0;77;1m (_) |_____|  / / \033[0;94m▬▬▬▬
                                            \033[0;77;1m/_/ \033[0;95m▬▬▬ """
                print(logo)
                example = """
\033[47;90;1m[        Corona Info, My Github: @stepbystepexe          ]\033[0m"""
                print(example)
        def barmenu(self):
                menubar = """
\033[0m[\033[96;2;1m1\033[0m] \033[1;77mCorona Di Dunia
\033[0m[\033[96;2;1m2\033[0m] \033[1;77mCorona Di Indonesia
\033[0m[\033[96;2;1m3\033[0m] \033[1;77mCorona Di Provinsi

\033[0m[\033[93;1m&\033[0m] LISENSI
\033[0m[\033[94;1m#\033[0m] Informasi
\033[0m[\033[92;1m*\033[0m] Perbarui
\033[0m[\033[91;1m-\033[0m] Keluar \n"""
                print(menubar)
        def get_data(self,asw):
                data = r.get(asw).text
                return json.loads(data)
        def tampil(self,data,negara=False,Provinsi=False,world=False):
                if negara:
                        data = data[0]
                        print("\n\033[0m[\033[94;1m#\033[0m] Negara     \033[77;1m: "+data["name"])
                        print("\033[0m[\033[93;1m*\033[0m] Positif    \033[77;1m: "+data["positif"])
                        print("\033[0m[\033[92;1m+\033[0m] Sembuh     \033[77;1m: "+data["sembuh"])
                        print("\033[0m[\033[91;1mx\033[0m] Meninggal  \033[77;1m: "+data["meninggal"])
                        input('\n\033[0m[\033[42;90;1m Kembali \033[0m]')
                        self.clearsc()
                        self.barlogo()
                        self.barmenu()
                if Provinsi:
                        print("\n\033[0m[\033[94;1m#\033[0m] Provinsi   \033[77;1m: "+data["attributes"]["Provinsi"])
                        print("\033[0m[\033[93;1m*\033[0m] Positif    \033[77;1m: "+str(data["attributes"]["Kasus_Posi"]))
                        print("\033[0m[\033[92;1m+\033[0m] Sembuh     \033[77;1m: "+str(data["attributes"]["Kasus_Semb"]))
                        print("\033[0m[\033[91;1mx\033[0m] Meninggal  \033[77;1m: "+str(data["attributes"]["Kasus_Meni"]))
                        print("_"*31)
                if world:
                        print(f"\n\033[0m[\033[96;1m#\033[0m] Negara      \033[77;1m: {data['attributes']['Country_Region']}")
                        print(f"\033[0m[\033[95;1m@\033[0m] Perbarui    \033[77;1m: {data['attributes']['Last_Update']}")
                        print(f"\033[0m[\033[94;1m&\033[0m] Konfirmasi  \033[77;1m: {data['attributes']['Confirmed']}")
                        print(f"\033[0m[\033[93;1m*\033[0m] Positif     \033[77;1m: {data['attributes']['Active']}")
                        print(f"\033[0m[\033[92;1m+\033[0m] Sembuh      \033[77;1m: {data['attributes']['Recovered']}")
                        print(f"\033[0m[\033[91;1mx\033[0m] Meninggal   \033[77;1m: {data['attributes']['Deaths']}")
                        print("_"*31)
        def menu(self):
                o = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m").lower()
                if o  == "back":
                        self.clearsc()
                        self.barlogo()
                        self.barmenu()
                elif o == "2" or o == "indonesian":
                        self.write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
                        sleep(1)
                        self.clearsc()
                        self.barlogo()
                        print("\n\033[0m[\033[92;1m#\033[0m] Tool ini di buat dari API http://kawalcorona/api\033[0m\n")
                        data = self.get_data(self.country.format('indonesia'))
                        self.tampil(data,negara=True)
                elif o == "3" or o == "province":
                        self.write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
                        sleep(1)
                        self.clearsc()
                        self.barlogo()
                        self.write("\n\033[0m[ \033[32mINFO \033[0m] \033[3mYa Allah semoga kita semua di jauhkan dari wabah")
                        self.write("         Virus Corona yang konon katanya mematikan ini\n")
                        print("\n\033[0;43;90;1m[ CORONA DARI PROVINSI \033[0m]")
                        data = self.get_data(self.country.format(self.idn))
                        for x in data:
                                self.tampil(x,Provinsi=True)
                elif o == "1" or o == "world":
                        self.write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
                        sleep(1)
                        self.clearsc()
                        self.barlogo()
                        self.write("\n\033[0m[ \033[32mINFO \033[0m] \033[3mYa Allah semoga kita semua di jauhkan dari wabah")
                        self.write("         Virus Corona yang konon katanya mematikan ini.\n\n")
                        while True:
                                o = input("\033[0m[\033[41;77;1m Cari Negara \033[0m] ").title()
                                if o == "all":
                                        for x in data:
                                                self.tampil(x)
                                elif "exit" in o:
                                        while True:
                                                self.restart()
                                elif o == "back":
                                        self.clearsc()
                                        self.barlogo()
                                        self.barmenu()
                                elif o == "clear":
                                        os.system('clear')
                                elif o == "quit":
                                        print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mKeluar dari program!\033[0m\n")
                                        exit(1)
                                else:
                                        data = self.get_data("https://api.kawalcorona.com")
                                        for x in data:
                                                if o in x["attributes"]["Country_Region"]:
                                                        self.tampil(x,world=True)
                elif o == "4" or o == "&":
                        print()
                        os.system('nano LICENSE')
                        print()
                        self.restart()
                elif o == "5" or o == "#":
                        info = """
Nama        : CoronaInfo
Versi       : 1.0 (Dibuat: 27 Januari 2020, 1:00 AM)
Tanggal     : 01 Januari 2020
Author      : Nedi Senja
Tujuan      : Melihat corban yang terpapar
              COVID.19 (Corona)
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: https://tinyurl.com/wel4alo

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """
                        example = """
\033[47;90;1m[        Corona Info, My Github: @stepbystepexe          ]\033[0m"""
                        os.system('clear')
                        print(example)
                        os.system('toilet -f smslant CoVid.19')
                        print(info)
                        sleep(1)
                        input('\n[ Tekan Enter ]')
                        self.restart()
                elif o == "6" or o == "*":
                        print()
                        os.system('git pull origin master')
                        print()
                        input('\033[0m[ \033[32mTekan Enter \033[0m]')
                        self.restart()
                elif o == '0' or o == '-':
                        print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mKeluar dari program!\033[0m\n")
                        exit(1)
                else:
                        print("\n\033[0m[\033[41;77;1m Pilihan Salah \033[0m]\n")
                        sleep(1)
                        self.restart()

try:
        Main()
        self.clearsc()
except (KeyboardInterrupt,EOFError):
        print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mKeluar dari program!\033[0m\n")
        exit(1)
except r.exceptions.ConnectionError:
        print("\n\033[0m[\033[91;1m!\033[0m] \033[77;1mTidak ada koneksi\033[0m\n")
        sleep(1)
        Main()
        self.clearsc()
        self.barlogo()
        self.barmenu()
