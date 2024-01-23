from django.db import models

'''
файл models.py -> используется для определения моделей
Модель -> класс, характеризующий структуру таблицы в бд, где атрибуты класса - колонки в таблице. Модели всегда наследуются от django.db.models.Model
'''

# auto_now_add -> автоматически фиксирует время, только один раз, при создании объекта
# auto_now -> автоматически фиксирует время, каждый раз, при изменении объекта
        
# 1. pyton3 manage.py makemigration -> создает файл миграций
# 2. python3 manage.py migrate -> применяет файл миграций к бд

class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    deadline = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tasks_img/')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'task'

    
 

class Comments(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    
'''
ключевые параметры

null -> True, будет ставить в бд null, если данные не переданы

blank -> True, будет записываться пустая строка, если данные не переданы. Поле необязательное для заполнения

choices -> позволяет ограничить возможные варианты для записи в это поле

default -> значение по умолчанию

editable -> False, то запись нельзя будет изменить

primary_key -> если True, то поле будет идентификатором (первичный ключ)

unique -> True, будет ошибка, если передать данные, которые уже есть в таблице (в этой колонке) (для уникальных значений)

validators ->  список для проверки поля
'''


'''
on_delete = ...
'''


