import datetime
import sys

#S5  EP 1 980216073932.28       123.5 S 3
#0123456789012345678901234567890123456789
f = open('dados_mestrado.txt','r')
s = open('hypocenter', 'w')
lines  = f.readlines()
for line in lines:
	estacao = line[0:4] 
	t0 = line[15:24]
	h = line[15:17]
	minuto = line[17:19]
	segs = line[19:24]
	seg = line[19:21]
	ms = line [22:24]
	pick_P = line[4:6]
	pick_S = line[4:5]
	peso_P = line[7:8]
	tempo_s = line[31:34]
	peso_S = line[39:40]
	mili_da_s = line[35:36]
	tempo_s_minuto = int(tempo_s) / 60 
	resto_tempo_s = int(tempo_s) % 60
	# Calcular o tempo da S 
	timeList = ['%2s:%2s:%2s:%s0' %(h,minuto,seg,ms) ,'0:%01s:%01s:%s00' %(tempo_s_minuto, resto_tempo_s, mili_da_s)] 
	sum = datetime.timedelta()
	for i in timeList:
		(h, m, s, ms) = i.split(':')
		d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s), milliseconds=int(ms))
		sum += d
		#print('' + str(sum))
	h_cal, minuto_cal, segmili = str(sum).split(':')
	h_cal = h_cal.zfill(2)
	minuto_cal = minuto_cal.zfill(2)
	segundo_cal, mili_cal = segmili.split('.') 
	segundo_cal = segundo_cal.zfill(2)
	mili_cal = mili_cal[0:3]
	hora = ('%s%s%s.%s'%(h_cal, minuto_cal, segundo_cal, mili_cal))
	#print(hora)
	print(' %4s SZ %2s   %s C %s0\n %s SZ %sS   %s C %s\n' %(estacao,pick_P, peso_P, t0, estacao, pick_S, peso_S, hora)) 
	

# Abra o arquivo (leitura)
	arquivo = open('hypocenter', 'r')
	conteudo = arquivo.readlines()

# insira seu conteudo
# obs: o metodo append() e proveniente de uma lista
	conteudo.append(' %s SZ %s   %s C %s0\n %s SZ %sS   %s C %s\n' 
	%(estacao,pick_P, peso_P, t0, estacao, pick_S, peso_S, hora)) 

# Abre novamente o arquivo (escrita)
# e escreva o conteudo criado anteriormente nele.
	arquivo = open('hypocenter', 'w')
	arquivo.writelines(conteudo)
	arquivo.close()
