# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from django.db.models import Sum, Count

# from .models import File
# from .serializers import FileSerializer, FileDashboardSerializer

# class FileViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = FileSerializer

#     def get_queryset(self):
#         return File.objects.filter(owner=self.request.user)

#     @action(detail=False, methods=['GET'])
#     def dashboard(self, request):
#         files = self.get_queryset()
        
#         # Total files and storage
#         total_files = files.count()
#         total_storage = files.aggregate(total_size=Sum('size'))['total_size'] or 0

#         # Recent uploads (last 5)
#         recent_uploads = files.order_by('-uploaded_at')[:5]

#         # File type distribution
#         file_type_distribution = files.values('file_type').annotate(count=Count('id'))
#         distribution_dict = {
#             item['file_type']: item['count'] 
#             for item in file_type_distribution
#         }

#         data = {
#             'total_files': total_files,
#             'total_storage_used': total_storage,
#             'recent_uploads': recent_uploads,
#             'file_type_distribution': distribution_dict
#         }
        
#         serializer = FileDashboardSerializer(data)
#         return Response(serializer.data)


#files/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from .models import File
from .serializers import FileSerializer, FileDashboardSerializer

class FileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    @action(detail=False, methods=['GET'])
    def dashboard(self, request):
        files = self.get_queryset()
        # Total files and storage
        total_files = files.count()
        total_storage = files.aggregate(total_size=Sum('size'))['total_size'] or 0
        # Recent uploads (last 5)
        recent_uploads = files.order_by('-uploaded_at')[:5]
        # File type distribution
        file_type_distribution = files.values('file_type').annotate(count=Count('id'))
        distribution_dict = {
            item['file_type']: item['count']
            for item in file_type_distribution
        }
        data = {
            'total_files': total_files,
            'total_storage_used': total_storage,
            'recent_uploads': recent_uploads,
            'file_type_distribution': distribution_dict
        }
        serializer = FileDashboardSerializer(data)
        return Response(serializer.data)