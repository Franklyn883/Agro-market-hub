from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    stock = serializers.IntegerField(source='inventory')
    
    def validate_price(self, value):
            if(value < 0):
                raise serializers.ValidationError('price should be more than zero')
            
    def validate_stock(self,value):
            if(value < 0):
                raise serializers.ValidationError('Stock cannot be Negative')
            
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'category', 'stock', 'category_id']
        
        
            