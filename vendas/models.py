from django.db import models
from clientes.models import Cliente
from produtos.models import Produto
from django.utils import timezone

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateTimeField(default=timezone.now)

    def valor_total(self):
        return self.produto.preco * self.quantidade

    def __str__(self):
        return f'{self.cliente.nome} - {self.produto.nome} ({self.quantidade})'
