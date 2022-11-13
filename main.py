import os, time

dicKey = {
'Home' : 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
'Home N' : '3KHY7-WNT83-DGQKR-F7HPR-844BM',
'Home Single Language' : '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
'Home Country Specific' : 'PVMJN-6DFY6–9CCP6–7BKTT-D3WVR',
'Professional' : 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
'Professional N' : 'MH37W-N47XK-V7XM9-C7227-GCQG9',
'Education' : 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
'Education N' : '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
'Enterprise' : 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
'Enterprise N' : 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4'
}

def fnConsole(strComando:str)->None:
    os.system(strComando)
    time.sleep(1)
def fnMenu():
    intIndex = 0
    listKey = []
    print('Eliga una licencia')
    for key,value in dicKey.items():
        print(f'{intIndex}  <- {key}')
        intIndex +=1
        listKey.append(value)
    print('99 <- Exit')
    strOpt = int(input('-> '))

    if strOpt == 99:
        exit()

    fnAutoKey(listKey[int(strOpt)])

def fnAutoKey(strKey:str):
    fnConsole(f'slmgr /ipk {strKey}')
    fnConsole(f'slmgr /skms kms8.msguides.com')
    fnConsole(f'slmgr /ato')
    print('[+] Clave de windows activada')

fnMenu()