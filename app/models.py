# django_project/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Utilisateur(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    pass
    # Ajout de related_name pour éviter le conflit
    groups = models.ManyToManyField(
        Group,
        related_name='utilisateur_set',  # Nouveau nom pour l'accès inverse
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='utilisateur',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='utilisateur_set',  # Nouveau nom pour l'accès inverse
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='utilisateur',
    )

    class Meta:
        app_label = 'app'  # Assurez-vous que cela est défini
    # Modèle Document
class Document(models.Model):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    contenu = models.TextField()
    date_upload = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
