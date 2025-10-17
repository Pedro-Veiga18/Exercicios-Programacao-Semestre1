resposta = int(input("Qual sistema operacional, de 1 a 6, é o melhor?: "))

windows = 0
unix = 0
linux = 0
netware = 0
macos = 0
outro = 0

maior = 0


while resposta != 0 and resposta >=1 and resposta <= 6:
    
    match resposta:
        case 1:
            windows += 1
        case 2: 
            unix += 1
        case 3:
            linux += 1
        case 4: 
            netware += 1
        case 5:
            macos += 1
        case 6:
            outro += 1
            


    resposta = int(input("Qual sistema operacional, de 1 a 6, é o melhor?: "))
    
total = windows + unix + linux + netware + macos + outro

windows_porc = (windows / total) * 100
unix_porc = (unix / total) * 100
linux_porc = (linux / total) * 100
netware_porc = (netware / total) * 100
macos_porc = (macos / total) * 100
outro_porc = (outro / total) * 100

print(f"Windows: {windows_porc: .2f}%")
print(f"Unix: {unix_porc: .2f}%")
print(f"Linux: {linux_porc: .2f}%")
print(f"Netware: {netware_porc: .2f}%")
print(f"MacOS: {macos_porc: .2f}%")
print(f"Outro: {outro_porc: .2f}%")

if windows_porc > unix_porc and linux_porc and netware_porc and macos_porc and outro_porc:
    maior = windows_porc
    print(f"O Sistema Operacional mais votado foi o Windows com {maior}% dos votos.")
elif unix_porc > windows_porc and linux_porc and netware_porc and macos_porc and outro_porc:
    maior = unix_porc
    print(f"O Sistema Operacional mais votado foi o Unix com {maior}% dos votos.")
elif linux_porc > windows_porc and unix_porc and netware_porc and macos_porc and outro_porc:
    maior = linux_porc
    print(f"O Sistema Operacional mais votado foi o Linux com {maior}% dos votos.")
elif netware_porc > windows_porc and linux_porc and unix_porc and macos_porc and outro_porc:
    maior = netware_porc
    print(f"O Sistema Operacional mais votado foi o Netware com {maior}% dos votos.")
elif macos_porc > windows_porc and linux_porc and netware_porc and unix_porc and outro_porc:
    maior = macos_porc
    print(f"O Sistema Operacional mais votado foi o MacOS com {maior}% dos votos.")
elif outro_porc > windows_porc and linux_porc and netware_porc and macos_porc and unix_porc:
    maior = outro_porc
    print(f"O Sistema Operacional mais votado foi Outros com {maior}% dos votos.")
    





    
            
        