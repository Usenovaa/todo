from django.db import models

'''
файл models.py -> используется для определения моделей
Модель -> класс, характеризующий структуру таблицы в бд, где атрибуты класса - колонки в таблице. Модели всегда наследуются от django.db.models.Model
'''

# auto_now_add -> автоматически фиксирует время, только один раз, при создании объекта
# auto_now -> автоматически фиксирует время, каждый раз, при изменении объекта
        
# 1. pyton3 manage.py makemigration -> создает файл миграций
# 2. python3 manage.py migrate -> применяет файл миграций к бд

class Tag(models.Model):
    title = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    deadline = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='tasks_img/')
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'task'


class Comments(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')



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
on_delete -> поведение связанных объектов при удалении

models.CASCADE # каскадное удаление (при удалении главного объекта, удаляются все зависящие) (удалет пост -> удаляются коменты к посту)

models.PROTECT -> защищает объект от удаления (при попыке удалить - ошибка)

models.RESTRICT -> примерно как PROTECT, но разрещает удаление, если главный объект в другой связи удаляется через CASCADE

models.SET_NULL -> при удалении главного объекта, зависящие не удаляются (в колонке задается значение null)
models.SET_DEFAULT при удалении главного объекта, зависящие не удаляются (в колонке задается значение по умолчанию)
'''


'''

1. создание объекта и сохранение в бд 

    .save()
    .objects.create(**kwargs)

obj = Model(**kwargs)
obj.save() # обращаемся к конкретному объекту

self.model.objects.create(**kwargs)
мэнеджер objects доступен только через модель

INSERT INTO model VALUES (**kwargs);


2. Получение одно объекта из бд

self.model.objects.get(условие/id=1)

SELECT * FROM model WHERE id=1;

3. all() -> QuerySet (набор данных (все объекты))

4. filter(**kwargs) -> QuerySet, содержит объекты, которые соответствуют заданным параметрам
Task.objects.filter(created_at__year=2023)
Task.objects.all().filter(created_at__year=2023)

5.exclude(**kwargs) -> QuerySet, содержит объекты, которые не соответствуют заданным параметрам

6. order_by(field) -> order by
'''

# QuerySet -> набор запросов в бд, для получения определенного набора объектов

'''
related_name -> позволяет обращаться из связанных объектов к тем, от которых связь была создана (для обратной связи, для получения связанных объектов)
obj = Task.objects.get(id=1)
 .comments.all() -> получили все объекты комментариев, которые связаны с указанным таском


related_query_name -> используется в запросах, как условие фильстации
Task.objects.filter(related_query_name=...)
'''
