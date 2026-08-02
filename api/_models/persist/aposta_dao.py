from models.persist.operacoes_dao import OperacoesDAO
from models.persist.conexao_bd import conexao
from typing import Any
from models.aposta import Aposta

class ApostaDAO(OperacoesDAO):
    def __init__(self):
        self.conexao = conexao
        self.conexao.conectar()

    def inserir(self, objeto: Any) -> bool:
        """Insere um novo registo na base de dados. Retorna True se tiver sucesso."""
        sql = """INSERT INTO apostas 
                 (pontos, palpite, status, multiplicador, idUsuario, idJogo) 
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (
            objeto.pontos, objeto.palpite, objeto.status, 
            objeto.multiplicador, objeto.idUsuario, objeto.idJogo
        )
        lista_valores = [valores]
        try:
            #TODO: Corrigir retorno de id
            apostaId = self.conexao.executar_comando(sql, lista_valores)
            objeto.id = apostaId
            print(f"Aposta {apostaId} inserida com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def excluir(self, id: int) -> bool:
        """Remove um registo pelo ID. Retorna True se tiver sucesso."""
        sql = "DELETE FROM apostas WHERE id=%s"
        try:
            self.conexao.executar_comando(sql, id)
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def editar(self, id: int, objeto: Any) -> bool:
        """Edita os dados de um registo existente. Retorna True se tiver sucesso."""
        sql = """UPDATE apostas SET 
                 pontos = %s, palpite = %s, status = %s, multiplicador = %s, idUsuario = %s, idJogo = %s 
                 WHERE id = %s"""
        valores = (
            objeto.pontos, objeto.palpite, objeto.status, objeto.multiplicador, 
            objeto.idUsuario, objeto.idJogo, objeto.id
        )
        lista_valores = [valores]
        try:
            self.conexao.executar_comando(sql, lista_valores)
            print(f"Aposta {objeto.id} atualizada com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def pesquisar(self, id: int) -> Any:
        """Procura um registo pelo ID. Retorna o objeto se encontrar, ou None."""
        sql = "SELECT * FROM apostas WHERE id=%s"
        try:
            resultado = self.conexao.executar_consulta(sql, ([id]))[0]
            
            pontos = resultado.get("pontos")
            palpite = resultado.get("palpite")
            status = resultado.get("status")
            multiplicador = resultado.get("multiplicador")
            idUsuario = resultado.get("idUsuario")
            idJogo = resultado.get("idJogo")
            id_res = resultado.get("id")
            
            aposta = Aposta(
                pontos=pontos, palpite=palpite, status=status, multiplicador=multiplicador, 
                idUsuario=idUsuario, idJogo=idJogo, id=id_res
            )
            return aposta
        except Exception as e:
            print(f"Erro ao pesquisar: {e}")
            return None