from django.core.management.base import BaseCommand
from faker import Faker
from posts.models import Post

class Command(BaseCommand):
    help = "Create Dummy Posts"
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            title = fake.sentence(nb_words = 6)
            body = fake.text(max_nb_chars = 200)
            slug = fake.slug()
            post = Post(title=title, body=body, slug=slug)
            post.save()
            self.stdout.write(self.style.SUCCESS('Successfully created dummy posts!'))
