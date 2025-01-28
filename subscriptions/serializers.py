from rest_framework import serializers
from .models import Package, Subscription

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Package
        fields=('id','title','sku','description','avatar','is_enable','price','duration','created_time','updated_time')



class SubscriptionSerializer(serializers.ModelSerializer):
    package=PackageSerializer()
    class Meta:
        model=Subscription
        fields = ('id','user','package','created_time','expire_time')