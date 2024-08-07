import contas
import pessoas

class banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas   = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.agencias:
            return True
        return False
    
    def _checa_conta(self, conta):
        if conta in self.agencias:
            return True
        return False
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
