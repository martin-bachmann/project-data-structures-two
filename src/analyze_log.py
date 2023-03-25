import csv


def contador_mais_pedido(data):
    mais_pedido = ""
    mais_pedido_contador = 0

    for pedido in data.items():
        if pedido[1] > mais_pedido_contador:
            mais_pedido = pedido[0]
            mais_pedido_contador = pedido[1]

    return mais_pedido


def verificar_mais_pedido(data, cliente):
    pedidos = {}
    for item in data:
        if item["cliente"] == cliente:
            if item["pedido"] not in pedidos:
                pedidos[item["pedido"]] = 1
            else:
                pedidos[item["pedido"]] += 1

    return contador_mais_pedido(pedidos)


def contador_de_pedidos_por_cliente(data, pedido, cliente):
    contador = 0
    for item in data:
        if item["cliente"] == cliente and item["pedido"] == pedido:
            contador += 1

    return contador


def contador_nao_pedidos(data):
    nao_pedidos = set()

    for pedido in data.items():
        if pedido[1] == 0:
            nao_pedidos.add(pedido[0])

    return nao_pedidos


def verificar_pratos_nao_pedidos(data, cliente):
    pedidos = {}
    for item in data:
        if item["pedido"] not in pedidos:
            pedidos[item["pedido"]] = 0
        if item["cliente"] == cliente:
            pedidos[item["pedido"]] += 1

    return contador_nao_pedidos(pedidos)


def verificar_dias_nao_pedidos(data, cliente):
    pedidos = {}
    for item in data:
        if item["dia"] not in pedidos:
            pedidos[item["dia"]] = 0
        if item["cliente"] == cliente:
            pedidos[item["dia"]] += 1

    return contador_nao_pedidos(pedidos)


def analyze_log(path_to_file):
    if not path_to_file:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    conteudo = []

    try:
        with open(path_to_file, mode="r") as file:
            campos = ["cliente", "pedido", "dia"]
            conteudo = [
                item for item in csv.DictReader(file, fieldnames=campos)
            ]
    except Exception:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    mais_pedido_maria = verificar_mais_pedido(conteudo, "maria")
    pedidos_hamburguer_arnaldo = contador_de_pedidos_por_cliente(
        conteudo, "hamburguer", "arnaldo"
    )
    nao_pedidos_joao = verificar_pratos_nao_pedidos(conteudo, "joao")
    dias_nao_pedidos_joao = verificar_dias_nao_pedidos(conteudo, "joao")

    with open("data/mkt_campaign.txt", mode="w") as file:
        new_file = "\n".join(
            [
                mais_pedido_maria,
                str(pedidos_hamburguer_arnaldo),
                str(nao_pedidos_joao),
                str(dias_nao_pedidos_joao),
            ]
        )
        file.write(new_file)
