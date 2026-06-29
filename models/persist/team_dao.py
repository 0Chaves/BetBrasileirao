from models.persist.operacoes_dao import OperacoesDAO
from models.persist.conexao_bd import conexao
from typing import Any
from models.team import Team

class TeamDAO(OperacoesDAO):
    def __init__(self):
        self.conexao = conexao
        self.conexao.conectar()


    def inserir(self, objeto: Any) -> bool:
        """Insere um novo registo na base de dados. Retorna True se tiver sucesso."""
        sql = "INSERT INTO times (nome, vitorias, derrotas, empates) VALUES (%s, %s, %s, %s)"
        valores = (objeto.nome, objeto.vitorias, objeto.derrotas, objeto.empates)
        lista_valores = [valores]
        try:
            #TODO: Corrigir retorno de id
            teamId = self.conexao.executar_comando(sql, lista_valores)
            objeto.id = teamId
            print(f"Time {teamId} inserido com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False


    def excluir(self, id: int) -> bool:
        """Remove um registo pelo ID. Retorna True se tiver sucesso."""
        sql = "DELETE FROM times WHERE id=%s"
        try:
            self.conexao.executar_comando(sql, id)
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def editar(self, id: int, objeto: Any) -> bool:
        """Edita os dados de um registo existente. Retorna True se tiver sucesso."""
        sql = "UPDATE times SET nome = %s, vitorias = %s, derrotas = %s, empates = %s WHERE id = %s"
        valores = (objeto.nome, objeto.vitorias, objeto.derrotas, objeto.empates, objeto.id)
        lista_valores = [valores]
        try:
            self.conexao.executar_comando(sql, lista_valores)
            print(f"Time {objeto.id} atualizado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False


    def pesquisar(self, id: int) -> Any:
        """Procura um registo pelo ID. Retorna o objeto se encontrar, ou None."""
        sql = "SELECT * FROM times WHERE id=%s"
        try:
            resultado = self.conexao.executar_consulta(sql, ([id]))[0]
            nome = resultado.get("nome")
            vitorias = resultado.get("vitorias")
            derrotas = resultado.get("derrotas")
            empates = resultado.get("empates")
            id = resultado.get("id")
            team = Team(nome=nome, vitorias=vitorias, derrotas=derrotas,empates=empates, id=id)
            return team
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return None