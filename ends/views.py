
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Reviews
from .models import Userr as User
from .serialisers import ProjectSerializer, ReviewSerializer, UserSerializer
from rest_framework.permissions import SAFE_METHODS, AllowAny,IsAuthenticated

# Create your views here.

class ReviewsView(APIView):
    permission_classes = (IsAuthenticated,)
   

    def get(self,request,format=None):
        reviews = Reviews.objects.all()
        serializer = ReviewSerializer(reviews,many=True)
        return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)

    
    def post(self,request,format=None):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
        else:
            return Response({"status":False,"data":serializer.errors},status.HTTP_400_BAD_REQUEST)

    


    



class GetUsersView(APIView):
        permission_classes = [IsAuthenticated]
        
        def get(self,request,format=None):
            reviews = User.objects.all()
            serializer = UserSerializer(reviews,many=True)
            return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)



       
        def post(self,request,format=None):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
            else:
                return Response({"status":False,"data":serializer.errors},status.HTTP_400_BAD_REQUEST)

        
        def delete(self, request, format=None):
            all_bloodrequest = User.objects.all().delete()
            return Response({'message': 'Donor details were deleted successfully!'},
             status=status.HTTP_204_NO_CONTENT)

    


        





class ProjectsView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self,request,userId,format=None):
        projects = Project.objects.all().filter(user=userId)
        serializer = ProjectSerializer(projects,many=True)
        return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)

    def post(self,request,format=None):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
        else:
            return Response({"status":False,"data":serializer.errors},status.HTTP_400_BAD_REQUEST)






class ProjectDescription(APIView):
      permission_classes = (IsAuthenticated,)
      def get(self,request,projectId,format=None):
        try:
            project = Project.objects.get(pk=projectId)
        except Project.DoesNotExist:
             return Response({"status":False,"data":"project not found"},status.HTTP_404_NOT_FOUND)
        else:
            serializer = ProjectSerializer(project)
            return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)

  

      def delete(self, request,projectId,format=None):
        try:
            project = Project.objects.get(pk=projectId)
        except Project.DoesNotExist:
            return Response({"status":False,"data":"project does not exist"},status.HTTP_404_NOT_FOUND)
        else:
            project.delete()
            return Response({'message': 'Project details were deleted successfully!'},status=status.HTTP_204_NO_CONTENT)

      def patch(self, request,projectId,format=None):
            try:
                project = Project.objects.get(pk=projectId)
            except Project.DoesNotExist:
                return Response({"status":False,"data":"project does not exist"},status.HTTP_404_NOT_FOUND)
            else:
                serializer = ProjectSerializer(project,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
                return Response({"status":"Ok","data":serializer.errors},status.HTTP_400_BAD_REQUEST)


class UserDescription(APIView):
    permission_classes = (IsAuthenticated,)

    # def get_user(self,userId):
    #        try:
    #            user = User.objects.get(pk=userId)
    #        except User.DoesNotExist:
    #             return Response({"status":False,"data":"user does not exist"},status.HTTP_404_NOT_FOUND)
        
    def get(self,request,userId,format=None):
            #user = self.get_user(userId)
            
           try:
               user = User.objects.get(pk=userId)
           except User.DoesNotExist:
                return Response({"status":False,"data":"user does not exist"},status.HTTP_404_NOT_FOUND)
           serializer = UserSerializer(user,many=True)
           return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
    

    def patch(self, request,userId,format=None):
            try:
                user = User.objects.get(pk=userId)
            except User.DoesNotExist:
                return Response({"status":False,"data":"user does not exist"},status.HTTP_404_NOT_FOUND)
            else:
                serializer = ProjectSerializer(user,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status":"Ok","data":serializer.data},status.HTTP_200_OK)
                return Response({"status":"Ok","data":serializer.errors},status.HTTP_400_BAD_REQUEST)
        
    




    

   










     


    



    