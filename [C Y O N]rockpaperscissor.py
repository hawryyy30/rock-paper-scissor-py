import random
import getpass
import os

def vsuser():
    skorPlayerOne=0
    skorPlayerTwo=0
    playerOne=input("Nama pemain-1 :")
    playerTwo=input("Nama pemain-2 :")
    os.system('clear')
    print("=============================\n\n")
    print(
        '''
    Tips : input akan disembunyikan untuk menjaga kerahasiaan
    Masukkan G untuk GUNTING, K untuk KERTAS dan B untuk BATU
    
    '''
    )
    while skorPlayerOne<skor:
        print(playerOne+" : ",skorPlayerOne)
        print(playerTwo+" : ",skorPlayerTwo)
        if skorPlayerTwo==skor:
            break
        tanganPlayerOne=getpass.getpass(playerOne+" Giliranmu :")
        tanganPlayerTwo=getpass.getpass(playerTwo+" Giliranmu :")
        tanganPlayerOne=tanganPlayerOne.upper()
        tanganPlayerTwo=tanganPlayerTwo.upper()
        if tanganPlayerOne==tanganPlayerTwo:
            print("Seri")
        elif tanganPlayerOne=="B":
            if tanganPlayerTwo=="G":
                print(tanganPlayerOne+" vs "+tanganPlayerTwo +":" +playerOne+" Menang")
                skorPlayerOne+=1
            else:
                print(tanganPlayerTwo+" vs "+tanganPlayerOne +":" +playerTwo+" Menang")
                skorPlayerTwo+=1
                
        elif tanganPlayerOne=="G":
            if tanganPlayerTwo=="K":
                print(tanganPlayerOne+" vs "+tanganPlayerTwo +":" +playerOne+" Menang")
                skorPlayerOne+=1
            else:
                print(tanganPlayerTwo+" vs "+tanganPlayerOne +":" +playerTwo+" Menang")
                skorPlayerTwo+=1
                
        elif tanganPlayerOne=="K":
            if tanganPlayerTwo=="B":
                print(tanganPlayerOne+" vs "+tanganPlayerTwo +":" +playerOne+" Menang")
                skorPlayerOne+=1
            else:
                print(tanganPlayerTwo+" vs "+tanganPlayerOne +":" +playerTwo+" Menang")
                skorPlayerTwo+=1
    os.system('cls')
    print("======================")
    print("Permainan Selesai")
    print("======================")
    print(playerOne,skorPlayerOne)
    print(playerTwo,skorPlayerTwo)
    if skorPlayerOne>skorPlayerTwo:
        print("==="+playerOne+" Menang === ")
    else:
        print("=== "+playerTwo+" Menang === ")
                
def botuser():
    user=0
    bot=0
    while user<skor:
        print("==================")
        print("skor user : ",user)
        print("skor bot : ",bot)
        print("==================")
        if bot==skor:
            break
        randomize=random.randrange(0,3)
        botPilih=gbk[randomize]
        userPilih=input("Pilih apa hayo : ")
        userPilih=userPilih.upper()
        if userPilih==gbk[randomize] :
            print(userPilih + " vs "+ botPilih +" = seri")
        
        elif userPilih==gbk[2]:
            if botPilih==gbk[1]:
                print(userPilih +" vs " + botPilih + "= Anda menang" )
                user+=1
            else:
                print(botPilih +" vs "+ userPilih +"= Bot menang" )
                bot+=1
        
        elif userPilih==gbk[0]:
            if botPilih==gbk[2]:
                print(userPilih +" vs "+ botPilih +"= Anda menang" )
                user+=1
            else:
                print(botPilih +" vs "+ userPilih +"= Bot menang" )
                bot+=1
                
        elif userPilih==gbk[1]:
            if botPilih==gbk[0]:
                print(userPilih +" vs "+ botPilih + "= Anda menang" )
                user+=1
            else:
                print(botPilih +" vs "+ userPilih +"= Bot menang" )
                bot+=1
    os.system('cls')
    print("=================")
    print("Permainan Selesai")
    print("Bot : ",bot)
    print("User : ",user)
    if user>bot:
        print("Anda menang")
    else:
        print("Bot Menang. Goodluck next time")
        
#main_program
gbk = ["GUNTING","BATU","KERTAS"]
print("Suit : Batu, Gunting Kertas")
print("___________________________\n")
print("1. User vs User")
print("2. User Vs Bot")
print("3. Keluar")
pilihan=int(input("Pilih mode yang anda inginkan : "))
if pilihan==3:
    print("Terima kasih telah bermain")
    exit();
skor=int(input("Skor yang ingin diraih : "))
if pilihan==1:
    vsuser()
elif pilihan==2:
    botuser()
else:
    print("Input salah")
    exit()



