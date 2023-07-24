from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    """
    Cette classe représente une tâche (un mémo) à réaliser

    Attributes:
    -----------
    todo_title : CharField
        Représente le nom de la tâche à effectuer
    todo_text : TextField
        Représente le texte descriptif de la tâche à effectuer
    todo_created : DateField
        Date de la création de la tâche
    todo_level : IntegerField
        Niveau d'importance de la tâche
    """
    class TodoLevel(models.IntegerChoices):
        """
        Cette classe décrit les niveaux d'importance d'une tâche

        Attributes:
        -----------
        LOW : int
            Tâche de niveau d'importance faible
        MEDIUM : int
            Tâche de niveau d'importance intermédiaire
        URGENT : int
            Tâche de niveau urgent
        NOW : int
            Tâche à réaliser dans l'immédiat
        """
        NOT_PROVIDED = 0
        LOW = 1
        MEDIUM = 2
        URGENT = 3
        NOW = 4

    todo_title = models.CharField(max_length=200)
    todo_text = models.TextField(null=True, blank=True)
    todo_created = models.DateField(auto_now_add=True)
    todo_level = models.IntegerField(choices=TodoLevel.choices, default=0)

