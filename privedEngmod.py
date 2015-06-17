##############################################################################################
#                               Novi modul privedeniya i rasprivedeniya parametrov           #
#          n-parametr dvigatelya; t-temperatura okrygauwei sredi; B-barometricheskoe davleni #
#           okrygauwei sredi                                                                 #
#                                                                                            #
##############################################################################################

from math import sqrt as sq								#Importirovanie fynkcii sqrt iz modulya math
B0=1.0332


def Npr(n,t):											#Privedenie mownosti dvigatelya
	return n*sq(288.15/(t+273.15))
def Gtpr(n,t,B):										#Privedenie rasxoda topliva dvigatelya
	return n*(B0/B)*sq(288.15/(t+273.15))
def Gvpr(n,t,B):										#Privedenie rasxoda  vozdyxa dvigatelya
	return n*(B0/B)*sq((t+273.15)/288.15)
def npr(n,t):											#Privedenie chastoti vraweniya dvigatelya
	return n*sq(288.15/(t+273.15))
def Ppr(n,B):											#Privedenie davleniya dvigatelya
	return n*(B0/B)
def Tpr(n,t):											#Privedenie temperatyri dvigatelya
	return n*(288.15/(t+273.15))
def Nctpr(n,t,B):										#Privedenie mownosti silovoi tyrbini dvigatelya
	return n*sq(288.15/(t+273.15))*(B0/B)
def cepr(n,t):											#Privedenie ydelnogo rasxoda topliva dvigatelya
	return n*sq(288.15/(t+273.15))
def Nf(n,t):											#Rasprivedenie mownosti dvigatelya
	return n*sq((t+273.15)/288.15)
def Gtf(n,t,B):											#Rasprivedenie rasxoda topliva dvigatelya
	return n*(B/B0)*sq((t+273.15)/288.15)
def Gvf(n,t,B):											#Rasprivedenie rasxoda  vozdyxa dvigatelya
	return n*(B/B0)*sq(288.15/(t+273.15))
def nf(n,t):											#Rasprivedenie chastoti vraweniya dvigatelya
	return n*sq((t+273.15)/288.15)
def Pf(n,B):											#Rasprivedenie davleniya dvigatelya
	return n*(B/B0)
def Tf(n,t):											#Rasprivedenie temperatyri dvigatelya
	return n*((t+273.15)/288.15)
def Nctf(n,t,B):										#Rasprivedenie mownosti silovoi tyrbini dvigatelya
	return n*sq((t+273.15)/288.15)*(B/B0)
def cef(n,t):											#Rasprivedenie ydelnogo rasxoda topliva dvigatelya
	return n*sq((t+273.15)/288.15)

