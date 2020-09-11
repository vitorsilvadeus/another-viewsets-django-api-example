from rest_framework.serializers import ManyRelatedField, ModelSerializer, Serializer, CharField, SerializerMethodField, IntegerField, DecimalField, ValidationError
from product.models import Product, Kit, KitRelation


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'price', 'cost', 'stock')

class KitRetrieveSerializer(Serializer):

    name = CharField(max_length=100)
    sku = CharField(max_length=8)
    products = SerializerMethodField()

    def get_products(self, instance):
        return KitRelation.objects.filter(kit_id=instance.id).values('product__sku', 'amount', 'discount')


class KitProductsSerializer(Serializer):
    sku = CharField(max_length=200)
    amount = IntegerField()
    discount = DecimalField(max_digits=6, decimal_places=3)

    def validate_discount(self, value):
        if not 0.0 <= value <= 1.0:
            raise ValidationError("The discount must be a percentage between 0 and 1.")
        return value


class KitPostSerializer(Serializer):

    name = CharField(max_length=100)
    sku = CharField(max_length=8)
    products = KitProductsSerializer(many=True,write_only=True)

    def create(self, validated_data):
        products = validated_data.pop('products')
        kit = Kit.objects.create(**validated_data)
        for item in products:
            KitRelation.objects.create(
                product=Product.objects.get(sku=item.get('sku')),
                kit=kit,
                amount=item.get('amount'),
                discount=item.get('discount'),
            )

        return kit

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sku = validated_data.get('sku', instance.sku)

        try:
            products = validated_data.pop('products')
        except KeyError:
            pass
        else:
            instance.products.clear()
            for item in products:
                KitRelation.objects.create(
                    product=Product.objects.get(sku=item.get('sku')),
                    kit=instance,
                    amount=item.get('amount'),
                    discount=item.get('discount'),
                )

        instance.save()
        return instance





