from django.core.management.base import BaseCommand
from accounts.models import *
from ...models import *
from faker import Faker
from datetime import datetime
import random

category_item = [
    "IT",
    "Software",
    "FUN"
]

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def __init__(self, *args, **kwargs):
        super(Command,self).__init__(self,*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        
        user = User.objects.create_user(email=self.faker.email(),password='@a123456')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.faker.first_name()
        profile.last_name = self.faker.last_name()
        profile.description = self.faker.paragraph(10)
        profile.save()

        for item in category_item:
            Category.objects.get_or_create(name=item)

        for _ in range(10):
            Post.objects.create(
                author = profile,
                title = self.faker.paragraph(1),
                content = self.faker.paragraph(10),
                status = random.choice([True,False]),
                category = Category.objects.get(name=random.choice(category_item)),
                published_at = datetime.now()
            )
