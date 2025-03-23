from rest_framework.response import Response
from rest_framework.views import APIView

from task_manager.models import Project


class FirstAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hello World"})

    def post(self, request):
        data = request.data
        print(request)
        return Response(data=data)


class ProjectAPIView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        data = []
        for i in projects:
            p = {}
            p['id'] = i.id
            p['name'] = i.name
            p['description'] = i.description
            data.append(p)

        return Response(data=data)
