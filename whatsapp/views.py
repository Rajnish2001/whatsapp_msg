from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json


class Index(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"msg":"hello worls"})
    

class WhatsAppAPI(APIView):
    def get(self, request):
        token = "02883edc-acc5-460e-bf51-95b5980e81e8"
        mode = request.data["hub.mode"]
        challenge=request.data["hub.challenge"]
        verify_token = request.data["hub.verify_token"]
        if mode=="subscribe" and token==verify_token:
            return Response(status = status.HTTP_200_OK)
        else:
            return Response(challenge,status=status.HTTP_400_BAD_REQUEST)
        # data = [mode, verify_token]
        # data = json.dumps(request.data)

        # return Response(1253475434)
    
    def post(self, request):
        # data = json.loads(request.body)
        # print('data: ', data)
        return Response(request.data)