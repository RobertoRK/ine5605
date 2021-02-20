"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        self._array_para_ordenar = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        menor = self._array_para_ordenar[0]
        array_ordenado = []
        posimenor = 0
        while len(self._array_para_ordenar) > 0:
            for i in range (len(self._array_para_ordenar)):
                if self._array_para_ordenar[i] < menor:
                    menor = self._array_para_ordenar[i]
                    posimenor = i
            array_ordenado.append(menor)
            self._array_para_ordenar.pop(posimenor)
            posimenor = 0
            if len(self._array_para_ordenar) > 0:
                menor = self._array_para_ordenar[0]
        self._array_para_ordenar = array_ordenado
        
        return self._array_para_ordenar

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        
        return ",".join([str(num) for num in self._array_para_ordenar])