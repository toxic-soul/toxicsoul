import os

os.system("python logo.py")
print ("""\t\033[31m[\033[37m1\033[31m] \033[37mBASIC PACKAGE INSTALL
\t\033[31m[\033[37m2\033[31m] \033[37mSMS BOMBER
\t\033[31m[\033[37m3\033[31m] \033[37mEMAIL BOMBER (LOGIN)
\t\033[31m[\033[37m4\033[31m] \033[37mURL SHORTNER
\t\033[31m[\033[37m5\033[31m] \033[37mKALI LINUX INSTALL (bdhackers009)
\t\033[31m[\033[37m6\033[31m] \033[37mTERMUX EKTRA KEY
\t\033[31m[\033[37m7\033[31m] \033[37mNGROK INSTALL (MAO2116)
\t\033[31m[\033[37m8\033[31m] \033[37mFACEBOOK CLONE
\t\033[31m[\033[37m9\033[31m] \033[37mVISIT GITHUB
\t\033[31m[\033[37m10\033[31m] \033[37mCONTACT WITH DEVOLOPER
\t\033[31m[\033[37m11\033[31m] \033[37mJOIN TELEGRAM
\t\033[31m[\033[37m12\033[31m] \033[37mJOIN GROUP
\t\033[31m[\033[37m13\033[31m] \033[37mEXIT\n""")

inp = str(input("\033[31m[\033[37m?\033[31m] \033[32mSELECT YOUR OPTION : \033[37m"))

if inp == "1":
  os.system("python basic.py")
elif inp == "2":
  os.system ("python sms.py")
elif inp == "3":
  os.system ("python email.py")
elif inp == "4":
  os.system ("python url.py")
elif inp == "5":
  os.system ("curl -L https://git.io/JiZwx | bash")
  print("\033[31m[\033[32mOK\033[31m]\033[32m INSTALL SUCCESS....!! ")
elif inp == "6":
  os.system ("python tkey.py")
elif inp == "7":
  os.system ("python ngrok.py")
elif inp == "8":
  os.system ("python2 clone.py")
elif inp == "9":
  os.system ("xdg-open https://www.github.com/TOXIC-SOUL")
  os.system ("python toxicsoul.py")
elif inp == "10":
  os.system ("xdg-open https://www.facebook.com/toxicsoulx")
  os.system ("python toxicsoul.py")
elif inp == "11":
  os.system ("xdg-open https://t.me/tx_soul")
  os.system ("python toxicsoul.py")
elif inp == "12":
  os.system ("xdg-open https://www.facebook.com/groups/1974132379435594/?ref=share")
  os.system ("python toxicsoul.py")
elif inp == "13":
  os.system("sys.exit()")
else:
  os.system ("python toxicsoul.py")
