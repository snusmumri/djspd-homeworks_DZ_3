from rest_framework import serializers

from main.models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    # реализуйте все поля
    # pass
    class Meta:
        model = Review
        fields = ['product', 'text', 'mark', 'created_at']

class ProductListSerializer(serializers.Serializer):
    # реализуйте поля title и price
    # pass
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

class ProductDetailsSerializer(serializers.ModelSerializer):
    # реализуйте поля title, description, price и reviews (список отзывов к товару)
    # pass

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = list(
            ReviewSerializer(rew).data for rew in Review.objects.filter(product=instance)
        )
        return representation


