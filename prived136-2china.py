##############################################################################################

##############################################################################################

from privedEngmod import *

###############################################################################
#Input data

tvx=20.5
Pvx=0.7149

#Start data
N_prived=[]
Gt_prived=[]
Pk_prived=[]
ngg_prived=[]           ####Dont rewrite!!!!!!!
tct_prived=[]
Gt_fizik=[]
tct_fizik=[]
Nct_fizik=[]

#Fizik parametrs

N_fiz=[]
Gt_fiz=[]
Pk_fiz=[]
ngg_fiz=[]
tct_fiz=[]

#Priveden parametrs

Gt_priveden=[]
tct_priveden=[]
Nct_priveden=[10500,10500,12400,12500]

################################################################################
#end data

for i in N_fiz:
    N_prived.append(int((Nctpr(i,tvx,Pvx))))
print "N_prived=",N_prived

for i in Nct_priveden:
    Nct_fizik.append(int(Nctf(i,tvx,Pvx)))
print "Nct_fizik=",Nct_fizik

for i in Gt_fiz:
    Gt_prived.append(Gtpr(i,tvx,Pvx))
print "Gt_prived=",Gt_prived

for i in Gt_priveden:
    Gt_fizik.append(int(Gtf(i,tvx,Pvx)))
print "Gt_fizik=",Gt_fizik

for i in Pk_fiz:
    Pk_prived.append(Ppr(i,Pvx))
print "Pk_prived=",Pk_prived

for i in ngg_fiz:
    ngg_prived.append(npr(i,tvx))
print "ngg_prived=",ngg_prived

for i in tct_fiz:
    tct_prived.append(Tpr((i+273.15),tvx)-273.15)
print "tct_prived=",tct_prived

for i in tct_priveden:
    tct_fizik.append(Tf((i+273.15),tvx)-273.15)
print "tct_fizik=",tct_fizik
