from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 

class xUserManager(BaseUserManager):
   
    def create_user(self, email,password):
        
        if not email:
            return {'error':'email invalid'}
        else:
           
            email = self.normalize_email(email)
            user = self.model(email=email)
            user.set_password(password)
            user.save(using=self._db)
            
        return user
    