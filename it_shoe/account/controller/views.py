from rest_framework import viewsets

class AccountView(viewsets.ViewSet):

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")