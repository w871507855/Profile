import os

from django.test import TestCase
from django.conf import settings
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import BookList
from .forms import BookListForm


class Views_Testing(TestCase):

    def __init__(self, *args, **kwargs):
        super(Views_Testing, self).__init__(*args, **kwargs)
        self.file_path1 = os.path.join(settings.BASE_DIR, 'testing_files', '1.jpeg')
        self.file_path2 = os.path.join(settings.BASE_DIR, 'testing_files', '2.jpeg')

    def setUp(self):
        data = {
            'title'      :  'python for you',
            'author'     :  'Michael Jackson',
            'publisher'  :  'Apress',
            'review'     :  'You will like it, Everyone will enjoy it.',        
        }
        with open(self.file_path1, 'rb') as f:
            files = {'cover': SimpleUploadedFile('cover', f.read(), content_type='image/jpeg')}
        form = BookListForm(data=data, files=files)
        # self.asserttrue(form.is_valid()) testing is valid
        # form.save() -- create a book instance
        if form.is_valid():
            form.save()

    def test_model_booklist(self):
        book = BookList.objects.get(id=1)
        now = timezone.now()
        self.assertEqual(book.title, 'python for you')
        self.assertEqual(book.author, 'Michael Jackson')
        self.assertEqual(book.publisher, 'Apress')
        self.assertEqual(book.review, 'You will like it, Everyone will enjoy it.')
        self.assertIn("/media/cover/" + now.strftime('%Y/%m/%d'), book.cover.url)

    def test_view_add_book(self):
        response = self.client.get(reverse('books:add_book'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/add_book.html')

        # method post with empty data
        response = self.client.post(reverse('books:add_book'))
        self.assertContains(response, 'This field is required.', count=5)

        # method post with data
        with open(self.file_path1, 'rb') as f:
            response = self.client.post(reverse('books:add_book'),
                    {
                        'title'      :  'tttttttt',
                        'author'     :  'aaaaaaaa',
                        'publisher'  :  'pppppppp',
                        'review'     :  'rrrrrrrr',
                        'cover'      :  f,
                    },
                    follow=True,
                )
            # I have create a book model in setUp, so this book id is 2
            self.assertRedirects(response, reverse('books:detail_book', kwargs={'id': 2}))
            self.assertEqual(BookList.objects.count(), 2)
            self.assertContains(response, 'tttttttt')
            self.assertContains(response, 'aaaaaaaa')
            self.assertContains(response, 'pppppppp')
            self.assertContains(response, 'rrrrrrrr')


    def test_view_detail_book(self):
        response = self.client.get(reverse('books:detail_book', kwargs={'id': 1}))
        self.assertContains(response, 'python for you')
        self.assertContains(response, 'Michael Jackson')
        self.assertContains(response, 'Apress')
        self.assertContains(response, 'You will like it, Everyone will enjoy it.')


    def test_view_change_book(self):
        response = self.client.get(reverse('books:change_book', kwargs={'id': 1}))
        self.assertContains(response, 'python for you')
        self.assertContains(response, 'Michael Jackson')
        self.assertContains(response, 'Apress')
        self.assertContains(response, 'You will like it, Everyone will enjoy it.')

        # change data
        book = BookList.objects.get(id=1)
        now = timezone.now()
        with open(self.file_path2, 'rb') as f:
            files = {'cover': SimpleUploadedFile('cover', f.read(), content_type='image/jpeg')}
            response = self.client.post(
                reverse('books:change_book', kwargs={'id': 1}),
                {
                    'title'      :  't-i-t-l-e',
                    'author'     :  'a-u-t-h-o-r',
                    'publisher'  :  'p-u-b-l-i-s-h-e-r',
                    'review'     :  'r-e-v-i-e-w',
                    'cover'      :  files
                },
                follow=True,
                )
            self.assertRedirects(response, reverse('books:detail_book', kwargs={'id': 1}))
            self.assertContains(response, 'Congratulation! Book have been updated.')
            self.assertContains(response, 't-i-t-l-e')
            self.assertContains(response, 'a-u-t-h-o-r')
            self.assertContains(response, 'p-u-b-l-i-s-h-e-r',)
            self.assertContains(response, 'r-e-v-i-e-w')
            self.assertIn("/media/cover/" + now.strftime('%Y/%m/%d'), book.cover.url)


    def test_view_delete_book(self):
        book = BookList.objects.get(id=1)
        img = book.cover.path
        title = book.title.upper()
        response = self.client.get(reverse('books:delete_book', kwargs={'id': 1}), follow=True)
        self.assertRedirects(response, reverse('books:books'))
        self.assertContains(response, 'The book %s is deleted.' % title)
        # if model instance is delete, cover image is delete either.
        self.assertFalse(os.path.isfile(img))


    def tearDown(self):
        # delect all generated pictures
        for file in BookList.objects.all():
            os.remove(file.cover.path)
