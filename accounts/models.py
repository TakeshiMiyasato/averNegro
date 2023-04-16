from django.contrib.auth.hashers import check_password
from django.db import models
from django.utils.crypto import get_random_string


class SEGUsuario(models.Model):
    US_UsuarioId = models.IntegerField(db_column='US_UsuarioId', primary_key=True)
    US_Login = models.CharField(max_length=100, db_column='US_Login')
    US_Password = models.CharField(max_length=100, db_column='US_Password')
    remember_token = models.CharField(max_length=100, db_column='remember_token')

    class Meta:
        managed = False
        db_table = 'SEGUsuario'

    def check_password(self, username, raw_password):
        return True

    def generate_auth_token(self):
        self.remember_token = get_random_string(length=40)
        self.save()
