from models.persist.operacoes_dao import OperacoesDAO
from models.persist.conexao_bd import conexao
from typing import Any
from models.usuario import Usuario

class UsuarioDAO(OperacoesDAO):
    def __init__(self):
        self.conexao = conexao
        self.conexao.conectar()

    def inserir(self, objeto: Any) -> bool:
        """Insere um novo registo na base de dados. Retorna True se tiver sucesso."""
        sql = """INSERT INTO usuarios 
                 (isAdmin, statusAtivo, nome, email, cpf, dataNascimento, login, senha, pontos, pontos_maximo, totalAcertos) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (
            objeto.isAdmin, objeto.statusAtivo, objeto.nome, objeto.email, 
            objeto.cpf, objeto.dataNascimento, objeto.login, objeto.senha, 
            objeto.pontos, objeto.pontos_maximo, objeto.totalAcertos
        )
        lista_valores = [valores]
        try:
            #TODO: Corrigir retorno de id
            userId = self.conexao.executar_comando(sql, lista_valores)
            objeto.id = userId
            print(f"Usuário {userId} inserido com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def excluir(self, id: int) -> bool:
        """Remove um registo pelo ID. Retorna True se tiver sucesso."""
        sql = "DELETE FROM usuarios WHERE id=%s"
        try:
            self.conexao.executar_comando(sql, id)
            return True
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            return False

    def editar(self, id: int, objeto: Any) -> bool:
        """Edita os dados de um registo existente. Retorna True se tiver sucesso."""
        sql = """UPDATE usuarios SET 
                 isAdmin = %s, statusAtivo = %s, nome = %s, email = %s, cpf = %s, 
                 dataNascimento = %s, login = %s, senha = %s, pontos = %s, 
                 pontos_maximo = %s, totalAcertos = %s 
                 WHERE id = %s"""
        valores = (
            objeto.isAdmin, objeto.statusAtivo, objeto.nome, objeto.email, objeto.cpf, 
            objeto.dataNascimento, objeto.login, objeto.senha, objeto.pontos, 
            objeto.pontos_maximo, objeto.totalAcertos, objeto.id
        )
        lista_valores = [valores]
        try:
            self.conexao.executar_comando(sql, lista_valores)
            print(f"Usuário {objeto.id} atualizado com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False

    def pesquisar(self, id: int) -> Any:
        """Procura um registo pelo ID. Retorna o objeto se encontrar, ou None."""
        sql = "SELECT * FROM usuarios WHERE id=%s"
        try:
            resultado = self.conexao.executar_consulta(sql, ([id]))[0]
            
            isAdmin = resultado.get("isAdmin")
            statusAtivo = resultado.get("statusAtivo")
            nome = resultado.get("nome")
            email = resultado.get("email")
            cpf = resultado.get("cpf")
            dataNascimento = resultado.get("dataNascimento")
            login = resultado.get("login")
            senha = resultado.get("senha")
            pontos = resultado.get("pontos")
            pontos_maximo = resultado.get("pontos_maximo")
            totalAcertos = resultado.get("totalAcertos")
            id_res = resultado.get("id")
            
            usuario = Usuario(
                isAdmin=isAdmin, statusAtivo=statusAtivo, nome=nome, email=email, 
                cpf=cpf, dataNascimento=dataNascimento, login=login, senha=senha, 
                pontos=pontos, pontos_maximo=pontos_maximo, totalAcertos=totalAcertos, id=id_res
            )
            return usuario
        except Exception as e:
            print(f"Erro ao pesquisar: {e}")
            return None