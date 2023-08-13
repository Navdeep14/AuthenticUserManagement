from .models import CustomUser
from django.http import HttpResponse

class CustomUserService:
    @classmethod
    def create_object(cls, name, content):
        return CustomUser.objects.create(name=name, content=content)

    @classmethod
    def get_all_objects(cls):
        return CustomUser.objects.all()

    @classmethod
    def get_object(cls, object_id):
        return CustomUser.objects.get(pk=object_id)

    @classmethod
    def delete_object(cls, object_id):
        print(object_id)
        object = CustomUser.objects.get(pk=object_id)
        object.delete()
        

