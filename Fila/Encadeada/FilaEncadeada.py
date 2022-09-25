class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class NoCabeca:
    def __init__(self):
        self.inicio = None
        self.final  = None
        self.tamanho = 0

class No:
    def __init__(self, carga):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'

class Fila:
    def __init__(self):
        self.__head = NoCabeca()

    def estaVazia(self)->bool:
        return self.__head.tamanho == 0

    def tamanho(self)->int:
        return self.__head.tamanho

    def __len__(self)->int:
        return self.__head.tamanho

    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__head.tamanho

            cursor = self.__head.inicio
            count = 1
            while(count < posicao):
                cursor = cursor.prox
                count += 1
            return cursor.carga
        except AssertionError:
            raise FilaException(f'Posicao inválida para a fila atual com {self.__head.tamanho} elementos')

    def busca(self, conteudo:any)->int:
        cont = 0
        cursor = self.head.incio

        while (cursor != None):
            if cursor.carga == conteudo:
                return cont + 1
            cursor = cursor.prox
            cont += 1
        
        raise FilaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo:any):
        pass

    def enfileira(self, conteudo:any):
        novo = No(conteudo)
        if self.estaVazia():
            self.__head.inicio = novo
            self.__head.fim = novo
        else:
            self.__head.final.prox = novo
            self.__head.final = novo

        self.__head.tamanho += 1

    def desenfileira(self)->any:
        #try:
        #    assert not self.estaVazia():
        #    inicial = self.__head.inicio
        #    self.__head.inicio = inicial.prox
        #    self.__head.tamanho -= 1
        #    return inicial.carga
#
        #except AssertionError:
        #    raise FilaException(f'A pilha está Vazia, impossível desempilhar')

        saiu = self.__head.inicio
        novo_inicio = self.__head.inicio.prox
        self.__head.inicio = novo_inicio
        self.__head.tamanho -= 1
        if self.__head.inicio.prox == None:
            self.__head.final = None
        return saiu



















    def busca(self, chave:any)->int:
        inicio = self.__frente
        count = 0
        for i in range(self.__ocupados):
            count += 1
            if self.__dados[inicio] == chave:
                return count

            inicio = (inicio + 1) % self.__tamanho

        raise FilaException(f'A chave {chave} não está na Fila.')


    def __str__(self):
        s = '[ '

        inicio = self.__frente
        for i in range(self.__ocupados):
            s += f'{self.__dados[inicio]} '
            inicio = (inicio + 1) % self.__ocupados

        s += ']'
        return s


    def esvazia(self):
        self.__ocupados = 0
        self.__frente = 0
        self.__final = -1
        '''
        while(not self.estaVazia()):
            self.desenfileira()
        '''