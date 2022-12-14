from rest_framework import serializers
from APP.models import WatchList,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        #fields = "__all__"
    

class WatchListSerializer(serializers.ModelSerializer):

    Reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    WatchList = WatchListSerializer(many=True, read_only=True)
    #WatchList= serializers.HyperlinkedRelatedField(many=True, read_only=True,view_name='movies_detail')

    class Meta:
        model = StreamPlatform
        fields = "__all__"


        
        #fields = ['id', 'name', 'description']
        #exculde = ['active']
        
    # def get_len_name(self, object):
    #     return len(object.name)

    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value
        
    # def validate(self, data):
    #     if data['name']== data['description']:
    #         raise serializers.ValidationError("Name and description are not the same")
    #     return data
    
    

    
    
    
    
    