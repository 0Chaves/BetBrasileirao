from abc import ABC, abstractmethod
from typing import Any

class OperacoesDAO(ABC):

    """
    Classe abstrata que define o contrato obrigatório para todos os DAOs do sistema.
    Assegura que qualquer classe que herde dela implemente as operações CRUD básicas.
    """

    @abstractmethod
    def inserir(self, objeto: Any) -> bool:
        """Insere um novo registo na base de dados. Retorna True se tiver sucesso."""
        pass

    @abstractmethod
    def excluir(self, id: int) -> bool:
        """Remove um registo pelo ID. Retorna True se tiver sucesso."""
        pass

    @abstractmethod
    def editar(self, id: int, objeto: Any) -> bool:
        """Edita os dados de um registo existente. Retorna True se tiver sucesso."""
        pass

    @abstractmethod
    def pesquisar(self, id: int) -> Any:
        """Procura um registo pelo ID. Retorna o objeto se encontrar, ou None."""
        pass