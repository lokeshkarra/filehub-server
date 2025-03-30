# from rest_framework import serializers
# from .models import File

# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = [
#             'id', 
#             'filename', 
#             'size', 
#             'uploaded_at', 
#             'file_type'
#         ]
#         read_only_fields = ['id', 'uploaded_at']

#     def create(self, validated_data):
#         file = self.context['request'].FILES.get('file')
#         validated_data['file'] = file
#         validated_data['owner'] = self.context['request'].user
#         validated_data['size'] = file.size
#         validated_data['filename'] = file.name
#         return super().create(validated_data)




#files/serializers.py
from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    file_name = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at', 'file_name']  # Make sure all fields are included.
        read_only_fields = ['id', 'uploaded_at', 'file_name']

    def get_file_name(self, obj):
        return obj.file.name  # Access filename from the FileField
    

class FileDashboardSerializer(serializers.Serializer):
    total_files = serializers.IntegerField()
    total_storage_used = serializers.IntegerField()
    recent_uploads = FileSerializer(many=True)
    file_type_distribution = serializers.DictField(
        child=serializers.IntegerField()
    )