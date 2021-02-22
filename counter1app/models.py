from __future__ import print_function

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import json
import requests


class Talking(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    api_key = models.CharField(max_length=201, blank=True, null=True)
    recipients = models.TextField(max_length=1000, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)
    sender_id = models.CharField(max_length=200, blank=True, null=True)
    
    
    def _str_(self):
        return self.username

    
    def save(self, *args, **kwargs):     

        url = 'https://api.sandbox.africastalking.com/version1/messaging'  
        
        headers = {
            'ApiKey': self.api_key, 
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        
        data = {
            'username': self.username,
            'from': self.sender_id,
            'message': self.message,
            'to': self.recipients,
        }
        
        def make_post_request():  
            response = requests.post(url=url, headers=headers, data=data )
            return response
        
        print( make_post_request().json() )

        return super(Talking, self).save(*args, **kwargs)