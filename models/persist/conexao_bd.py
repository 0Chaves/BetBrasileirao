import psycopg2
from typing import Any, Tuple, List, Dict

class ConexaoBD:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.cursor = None
    
    def conectar(self):
        try:
            # # TODO: Criar docker compose
            # try:
            #     #Cria novo container com postgres
                # !docker run --name db_apostas -e POSTGRES_PASSWORD=self.password -e POSTGRES_DB=self.database -p 5433:5432 -d postgres
            # finally:
            #     !docker start db_apostas
            
            # Conectando agora na porta 5433
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port, # <--- Mudança crucial aqui
                database=self.database
            )

            self.cursor = self.connection.cursor()

            # Verificando a versao do db
            self.cursor.execute("SELECT version();")
            db_version = self.cursor.fetchone()
            print("Conectado com sucesso!")
            print(f"Versão: {db_version}")
        except Exception as e:
             print(e)
    
    def excluir_banco(self):
        try:
            self.cursor.execute("""
            DROP TABLE apostas;
            DROP TABLE usuarios;
            DROP TABLE jogos;
            DROP TABLE times;
            """)
        except Exception as e:
            print(e)

    def criar_banco(self):
        # Criando a tabela
        self.cursor.execute("""
            CREATE TABLE times (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                vitorias INTEGER NOT NULL,
                derrotas INTEGER NOT NULL,
                empates INTEGER NOT NULL
            );
            CREATE TABLE usuarios (
                id SERIAL PRIMARY KEY,
                isAdmin BOOLEAN NOT NULL,
                statusAtivo BOOLEAN NOT NULL,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                cpf VARCHAR(14) UNIQUE NOT NULL,
                dataNascimento DATE NOT NULL,
                login VARCHAR(100) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL,
                pontos DOUBLE PRECISION NOT NULL,
                pontos_maximo DOUBLE PRECISION NOT NULL,
                totalAcertos INTEGER NOT NULL
            );
            CREATE TABLE jogos (
                id SERIAL PRIMARY KEY,
                status VARCHAR(100) NOT NULL,
                idTimeA INTEGER NOT NULL,
                idTimeB INTEGER NOT NULL,
                apostadoresTimeA INTEGER NOT NULL,
                apostadoresTimeB INTEGER NOT NULL,
                timeVencedor INTEGER,
                golsTimeA INTEGER NOT NULL,
                golsTimeB INTEGER NOT NULL,
                CONSTRAINT fk_time_a FOREIGN KEY (idTimeA) REFERENCES times (id),
                CONSTRAINT fk_time_b FOREIGN KEY (idTimeB) REFERENCES times (id),
                CONSTRAINT fk_time_vencedor FOREIGN KEY (timeVencedor) REFERENCES times (id)
            );
            CREATE TABLE apostas (
                id SERIAL PRIMARY KEY,
                pontos DOUBLE PRECISION NOT NULL,
                palpite VARCHAR(255) NOT NULL,
                status VARCHAR(100) NOT NULL,
                multiplicador DOUBLE PRECISION NOT NULL,
                idUsuario INTEGER NOT NULL,
                idJogo INTEGER NOT NULL,
                CONSTRAINT fk_aposta_usuario FOREIGN KEY (idUsuario) REFERENCES usuarios (id),
                CONSTRAINT fk_aposta_jogo FOREIGN KEY (idJogo) REFERENCES jogos (id)
            );
        """)
        
        self.connection.commit()

    def executar_comando(self, sql: str, valores: List[(Any)]) -> int:
        """
        Executa comandos SQL que alteram dados (INSERT, UPDATE, DELETE).
        Utiliza transação e garante que o Commit (gravação) seja feito.
        
        :param sql: Instrução SQL estruturada.
        :param valores: lista com valores a serem inseridos.
        :return: O número de linhas que foram afetadas pela operação.
        """
        linhas_afetadas = 0

        try:
            self.cursor.executemany(sql, valores)
            # Operações de escrita PRECISAM de commit para persistir na unidade de armazenamento
            self.connection.commit()
            linhas_afetadas = self.cursor.rowcount
            return linhas_afetadas

            #self.cursor.close()
        except Exception as erro:
            # Em caso de erro de banco de dados, fazemos rollback para proteger o estado
            self.connection.rollback()
            print(f"❌ [DB Erro] Falha ao executar comando de escrita: {erro}")
            raise erro
            
        # finally:
        #     # Fechamos recursos em bloco finally para evitar conexões "vazando" ou presas
        #     self.cursor.close()
        #     self.conexao.close()

    def executar_consulta(self, sql: str, parametros: Tuple[Any, ...] = ()) -> List[Dict[str, Any]]:
    #def executar_consulta(self, sql: str, valores: List[(Any)]) -> List[Dict[str, Any]]: 
        """
        Executa instruções SQL de leitura (SELECT).
        Não altera o estado do banco, logo não precisa de commit.
        
        :param sql: Instrução SELECT estruturada.
        :param parametros: Tupla com argumentos seguros.
        :return: Uma lista de dicionários onde as chaves são os nomes das colunas.
        """

        resultados = []

        try:
            if parametros:
                #TODO: VErificar se o cursor está conectado e aberto antes de executar a consulta
                self.cursor.execute(sql, parametros)
            # else:
            #     self.cursor.execute(sql)
                # Convertemos o resultado especial sqlite3.Row em dicionários comuns
            resultados = self.cursor.fetchall()
            print("quantidade de registros encontrados:", len(resultados))
            
        except Exception as erro:
            print(f"❌ [DB Erro] Falha ao executar consulta de leitura: {erro}")
            raise erro
            
        # finally:
        #     self.cursor.close()
        #     self.conexao.close()

        return resultados

conexao = ConexaoBD(user='postgres', password='senha123', host='127.0.0.1', port='5433', database='db_apostas')