from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import *
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [AllowAny]


    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            # print(user)
            # user = User.objects.get(id=1) #static
            # print('movie title', movie.title)
            # print('user', user.username)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many =False)
                response = {'message': 'Rating Update', 'result': serializer.data}
                return Response(response, status=HTTP_200_OK)

            except:
                rating = Rating.objects.create(user=user, movie=movie, stars = stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=HTTP_200_OK)

        else:
            response = {'message': 'you need to provide stars'}
            return Response (response, status=HTTP_400_BAD_REQUEST)





class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like this'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like this'}
        return Response(response, status = status.HTTP_400_BAD_REQUEST)


