import sys

class AFD:
    def __init__(self):
        self.estados = set()
        self.estado_inicial = None
        self.estados_finais = set()
        self.simbolos = set()
        self.transicoes = {}

    def adicionar_estado(self, estado):
        self.estados.add(estado)

    def definir_estado_inicial(self, estado):
        self.estado_inicial = estado

    def adicionar_estado_final(self, estado):
        self.estados_finais.add(estado)

    def adicionar_simbolo(self, simbolo):
        self.simbolos.add(simbolo)

    def adicionar_transicao(self, estado_atual, simbolo, estado_destino):
        if estado_atual not in self.transicoes:
            self.transicoes[estado_atual] = {}
        self.transicoes[estado_atual][simbolo] = estado_destino

    def aceita_cadeia(self, cadeia):
        estado_atual = self.estado_inicial
        for simbolo in cadeia:
            if estado_atual in self.transicoes and simbolo in self.transicoes[estado_atual]:
                estado_atual = self.transicoes[estado_atual][simbolo]
            else:
                return False
        return estado_atual in self.estados_finais


def criar_automato():
    afd = AFD()

    num_estados = int(input("Número de estados do autômato: "))
    estado_inicial = input("Estado inicial: ")
    num_estados_finais = int(input("Número de estados finais: "))
    estados_finais = list(input("Estados finais (separados por espaço): ").split())
    num_simbolos = int(input("Número de símbolos do alfabeto: "))
    simbolos = input("Símbolos do alfabeto (separados por espaço): ").split()
    num_transicoes = int(input("Número de transições: "))

    for _ in range(num_estados):
        afd.adicionar_estado(str(_ + 1))

    afd.definir_estado_inicial(estado_inicial)

    for estado_final in estados_finais:
        afd.adicionar_estado_final(estado_final)

    for simbolo in simbolos:
        afd.adicionar_simbolo(simbolo)

    for _ in range(num_transicoes):
        estado_atual, simbolo, estado_destino = input("Transição (estado_atual símbolo estado_destino): ").split()
        afd.adicionar_transicao(estado_atual, simbolo, estado_destino)

    cadeia = input("Cadeia de entrada: ")

    return afd, cadeia


def main():
    afd, cadeia = criar_automato()
    if afd.aceita_cadeia(cadeia):
        print("A cadeia foi aceita pelo AFD.")
    else:
        print("A cadeia foi rejeitada pelo AFD.")


if __name__ == '__main__':
    main()
