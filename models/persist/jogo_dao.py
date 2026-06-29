from models.persist.operacoes_dao import OperacoesDAO
from models.persist.conexao_bd import conexao
from typing import Any
from models.jogo import Jogo

class JogoDAO(OperacoesDAO):
    def __init__(self):
        self.conexao = conexao
        self.conexao.conectar()

    def inserir(self, objeto: Any) -> bool:
        """Insere um novo registo na base de dados. Retorna True se tiver sucesso."""
        sql = """INSERT INTO jogos 
                 (status, idTimeA, idTimeB, apostadoresTimeA, apostadoresTimeB, timeVencedor, golsTimeA, golsTimeB) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (
            objeto.status, objeto.idTimeA, objeto.idTimeB, objeto.apostadoresTimeA, 
            objeto.apostadoresTimeB, objeto.timeVencedor, objeto.golsTimeA, objeto.golsTimeB
        )
        lista_valores = [valores]
        try:
            #TODO: Corrigir retorno de id
            jogoId = self.conexao.executar_comando(sql, lista_valores)
            objeto.id = jogoId
            print(f"Jogo {jogoId} inserido com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def excluir(self, id: int) -> bool:
        """Remove um registo pelo ID. Retorna True se tiver sucesso."""
        sql = "DELETE FROM jogos WHERE id=%s"
        try:
            self.conexao.executar_comando(sql, id)
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def editar(self, id: int, objeto: Any) -> bool:
        """Edita os dados de um registo existente. Retorna True se tiver sucesso."""
        sql = """UPDATE jogos SET 
                 status = %s, idTimeA = %s, idTimeB = %s, apostadoresTimeA = %s, 
                 apostadoresTimeB = %s, timeVencedor = %s, golsTimeA = %s, golsTimeB = %s 
                 WHERE id = %s"""
        valores = (
            objeto.status, objeto.idTimeA, objeto.idTimeB, objeto.apostadoresTimeA, 
            objeto.apostadoresTimeB, objeto.timeVencedor, objeto.golsTimeA, objeto.golsTimeB, objeto.id
        )
        lista_valores = [valores]
        try:
            self.conexao.executar_comando(sql, lista_valores)
            print(f"Jogo {objeto.id} atualizado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def pesquisar(self, id: int) -> Any:
        """Procura um registo pelo ID. Retorna o objeto se encontrar, ou None."""
        sql = "SELECT * FROM jogos WHERE id=%s"
        try:
            resultado = self.conexao.executar_consulta(sql, ([id]))[0]
            
            status = resultado.get("status")
            idTimeA = resultado.get("idTimeA")
            idTimeB = resultado.get("idTimeB")
            apostadoresTimeA = resultado.get("apostadoresTimeA")
            apostadoresTimeB = resultado.get("apostadoresTimeB")
            timeVencedor = resultado.get("timeVencedor")
            golsTimeA = resultado.get("golsTimeA")
            golsTimeB = resultado.get("golsTimeB")
            id_res = resultado.get("id")
            
            jogo = Jogo(
                status=status, idTimeA=idTimeA, idTimeB=idTimeB, apostadoresTimeA=apostadoresTimeA,
                apostadoresTimeB=apostadoresTimeB, timeVencedor=timeVencedor, golsTimeA=golsTimeA, 
                golsTimeB=golsTimeB, id=id_res
            )
            return jogo
        except Exception as e:
            print(f"Erro ao pesquisar: {e}")
            return None