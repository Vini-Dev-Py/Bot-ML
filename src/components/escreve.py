def escreve(Bot, Lista, date, Salvar):
    bot = Bot(Lista)

    lista_certa = bot.conferirLista(Lista)

    print(lista_certa)

    File = open(f'C:\programas\Programaçâo\GitHub\Bot-ML\Bot-ML\Container\mail\{date} QR-BarCode-Unity.txt', 'w+')

    abrir_arquivo = Salvar(File, date, lista_certa)

    escrevendo = abrir_arquivo.SalvarTxT(File, lista_certa, date)