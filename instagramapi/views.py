from .serializers import StorySerializers, UserSerializers
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Response
from rest_framework import status
from .models import Story, User
import threading # potoklarni ishlatish uchun
from datetime import datetime

class StoryAPIView(APIView):
    def __init__(self):
        timer_thread = threading.Thread(target=self.func) # func funksiya chaqirilgan holda potok yaratish
        timer_thread.start() # potokni ishga tushirish

    def func(self):
        storySet = Story.objects.all().values()
        need_time = datetime(1,1,1, 7, 0, 0) # story uchirish vaqti (soati kerak holos)
        while True: # tugamas sikl
            for story in storySet: # storySet'dan yuradigan sikl
                # hozirgi vaqt uchirilish vaqtiga tengligini tekshirish
                if datetime.now().strftime("%H:%M:%S") == need_time.strftime("%H:%M:%S"): 
                    Story.objects.all().delete() # hamma storyni uchirish

    def get(self, request): #get so'rovini yurish xolati 
        try:        #agar bizga kerakli userga tegishli storylarni olish uchun {"user": 1}
            user = request.data["user"] #
            storySet = Story.objects.filter(author=user).values()
        except KeyError: #barcha storylarni ko'rish uchun
            storySet = Story.objects.all().values()  
            return Response({"data": storySet}, status=status.HTTP_200_OK)

        return Response({"data": storySet}, status=status.HTTP_200_OK)

class UserAPIView(APIView):
    def get(self, request):
        userSet = User.objects.all().values("id", "username")
        return Response({"data": userSet}, status=status.HTTP_200_OK)
