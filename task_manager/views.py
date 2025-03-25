from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.models import Project
from task_manager.serializers import ProjectSerializers, ProjectDetailModelSerializer, ProjectCreateAndUpdateSerializers


class FirstAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello World"})

    def post(self, request):
        data = request.data
        print(request)
        return Response(data=data)


class ProjectAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            p = get_object_or_404(Project, id=pk)
            serializer = ProjectDetailModelSerializer(p)
            return Response(serializer.data)
        else:
            projects = Project.objects.all()
            # data = []
            # for i in projects:
            #     p = {}
            #     p['id'] = i.id
            #     p['name'] = i.name
            #     p['description'] = i.description
            #     data.append(p)
            serializers = ProjectDetailModelSerializer(projects, many=True)
            return Response(serializers.data)

    def post(self, request):
        serializers = ProjectCreateAndUpdateSerializers(data=request.data)
        # 1
        # if serializers.is_valid():
        #     serializers.save()
        #     return Response(data=serializers.data)
        # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        # 2
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(data=serializers.data)
        # 3
        # serializers.is_valid(raise_exception=True)
        # data = serializers.validated_data
        # p = Project.objects.create(
        #     name=data.get('name'),
        #     description=data.get('description')
        # )
        # serializers = ProjectSerializers(p)
        # return Response(data=serializers.data)

    def put(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        serializer = ProjectCreateAndUpdateSerializers(data=request.data, instance=project)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        project = get_object_or_404(Project, id=pk)
        project.delete()
        return Response(data={"message": "deleted success"})
