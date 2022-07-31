from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from .serializer import UserFinancialdataSerializer
from .models import UserFinancialdata
from agl_financial_backend.renderers import UserRenderer

# Create your views here.



class User_Financial_data(generics.ListCreateAPIView):
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    # queryset = UserFinancialdata.objects.filter(user_id=False)
    serializer_class = UserFinancialdataSerializer
    renderer_classes = [UserRenderer]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        errorcontext = {
            "clerk_file": serializer.errors["clerk_file"][
                0
            ]
        }
        return Response(errorcontext, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user_id = request.data['user_id']
        if queryset := UserFinancialdata.objects.filter(user_id=user_id):
            # print("::::::::::::::",queryset)
            serializer = self.serializer_class(queryset, many=True)
            context = {"data": serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        else:
            not_found = {"message": "success",
                        "data": [
        {
            "user_id": None,
            "clerk_file": {
                "planId": None,
                "endDate": None,
                "planName": None,
                "startDate": None
            }
        }]
        }
            
            return Response(not_found, status=status.HTTP_200_OK)
            




