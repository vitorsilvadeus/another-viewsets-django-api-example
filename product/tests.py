from django.test import TestCase
from product.models import Product, Kit
from django.urls import reverse


class TestProductViewSet(TestCase):

    fixtures = ['test']

    def test_get(self):
        url = reverse('products-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_delete(self):
        url = reverse('products-detail',args=[Product.objects.all().first().id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        url = reverse('products-list')

        data = {
            "name": "Bola",
            "sku": "AB002213",
            "price": "50.000",
            "cost": "23.000",
            "stock": 10
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_patch(self):
        product_id = Product.objects.all().first().id
        url = reverse('products-detail', args=[product_id])

        data = {
            "id": product_id,
            "name": "Produto teste",
        }

        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name',None), "Produto teste")


class TestKitRetrieveViewSet(TestCase):

    fixtures = ['test']

    def test_get(self):
        url = reverse('retrievekits-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data)

    def test_delete(self):
        url = reverse('retrievekits-detail',args=[Kit.objects.all().first().id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


class TestKitPostViewSet(TestCase):

    fixtures = ['test']

    def test_post(self):
        url = reverse('postkits-list')

        data = {
            "name": "Tenis + meias + jacketa",
            "sku": "XXZZ2298",
            "products": [
                {
                    "sku": "Ac002248",
                    "amount": 3,
                    "discount": 0.3
                },
                {
                    "sku": "MMOA0023",
                    "amount": 4,
                    "discount": 0.5
                },
                {
                    "sku": "BNKW0012",
                    "amount": 2,
                    "discount": 0.1
                }
            ]
        }

        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def test_patch(self):
        kit_id = Kit.objects.all().first().id
        url = reverse('postkits-detail', args=[kit_id])

        data = {
            "kit_id": 1,
            "name": "Produto teste",
        }

        response = self.client.patch(url,data, content_type='application/json' )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('name', None), "Produto teste")