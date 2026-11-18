from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Atendimento(models.Model):
    STATUS = [
        ("pendente", "Pendente"),
        ("andamento", "Em andamento"),
        ("concluido", "Concluído"),
    ]

    tecnico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    cliente = models.CharField(max_length=150)
    data = models.DateField()
    descricao = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="pendente"
    )

    def __str__(self):
        return f"{self.cliente} - {self.get_status_display()}"


class MaterialUtilizado(models.Model):
    atendimento = models.ForeignKey(
        Atendimento,
        on_delete=models.CASCADE,
        related_name="materiais"
    )
    nome_material = models.CharField(max_length=150)
    quantidade_utilizada = models.PositiveIntegerField()
    quantidade_danificada = models.PositiveIntegerField(default=0)
    motivo_dano = models.TextField(blank=True)

    def clean(self):
        if self.quantidade_danificada > self.quantidade_utilizada:
            raise ValidationError(
                "A quantidade danificada não pode superar a utilizada."
            )
        if self.quantidade_danificada > 0 and not self.motivo_dano.strip():
            raise ValidationError(
                "Informe o motivo do dano."
            )

    def __str__(self):
        return self.nome_material