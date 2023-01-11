import sys
sys.path.append(r'C:/Users/alexsandro.ignacio/OneDrive - WCA Soluções de Inteligência Comercial/Documentos/Docs/Git/python_alura/Python parte 10 TDD')

# https://docs.pytest.org/en/7.1.x/how-to/mark.html

from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    # toda função deve ter test_ + nome do teste e 
    # Deve ser verboso.
    # Give-When-Then | Dado(contexto)-Quando(ação)-Então(desfecho)
    def test_quando_idade_recebe_13_03_2020_deve_retornar_22(self):
        entrada = '13/03/2020' # Given-Contexto
        esperado = 3 

        funcionario_teste = Funcionario('Teste', entrada, 1111) 
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado # Then-Desfecho

    def test_quando_idade_recebe_13_03_2020_deve_retornar_23(self):
        entrada = '13/03/2000' # Given-Contexto
        esperado = 23 

        funcionario_teste = Funcionario('Teste', entrada, 1111) 
        resultado = funcionario_teste.idade() # When-Ação

        assert resultado == esperado # Then-Desfecho
    
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):

        entrada = ' Lucas Carvalho ' # Given
        esperado ='Carvalho' 

        funcionario_teste = Funcionario(entrada, '11/11/2000', 1111)
        resultado = funcionario_teste.sobrenome() # When-Ação

        assert resultado == esperado # Then-Desfecho

    # @mark.skip(reason="não quero executar isso agora")
    # @pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
    # @pytest.mark.xfail
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):

        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario() # When-Ação
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then-Desfecho

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):

        entrada_salario = 1000 # Given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus() # When-Ação

        assert resultado == esperado # Then-Desfecho

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):

        with pytest.raises(Exception):

            entrada_salario = 1000000 # Given

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus() # When-Ação

            assert resultado # Then-Desfecho

    # def test_retorno_str(self):      
    #     nome, data_nascimento, salario = 'Teste', '12/03/2020', 1000 #given
    #     esperado = 'Funcionario(Teste, 12/03/2020, 1000)' 

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() #When 

    #     assert resultado == esperado # then



    

