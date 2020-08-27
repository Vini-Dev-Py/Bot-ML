def escreve(Bot, Lista, date, Salvar):
    bot = Bot(Lista)

    lista_certa = bot.conferirLista(Lista)

    print(lista_certa)

    File = open(f'C:\programas\Programaçâo\GitHub\{date} QR-BarCode-Unity.txt', 'w+')

    abrir_arquivo = Salvar(File, date, Lista)

    escrevendo = abrir_arquivo.SalvarTxT(File, Lista, date)