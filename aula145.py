# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod
from os import system
system('cls')

# Classe abstrata notificação
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


# Classes que herdam da >>Classe Abstrata<< Notificação
class NotificacaoEmail(Notificacao):
    tipo = "E-Mail"
    def enviar(self) -> bool:
        print(f'Enviando E-Mail: "{self.mensagem}"')
        return True


class NotificacaoSMS(Notificacao):
    tipo = "SMS"
    def enviar(self) -> bool:
        print(f'Enviando SMS: "{self.mensagem}"')
        return True


# Função notificar que utiliza das classes de notificação (magia negra)
def notificar(notificacao: Notificacao):
    notificaco_enviada = notificacao.enviar()

    if notificaco_enviada:
        print(f"Notificação via {notificacao.tipo} enviada com sucsso!\n")
    else:
        print(f"Algo deu errado. Notificação via {notificacao.tipo} NÃO enviada!\n")


# Notificação de E-Mail
notificar(NotificacaoEmail("Lorem Ipsum Dolor Sit Amet."))

# Notificação de SMS
notificacao_sms = NotificacaoSMS("Lorem Ipsum Dolor Sit Amet.")
notificar(notificacao_sms)
