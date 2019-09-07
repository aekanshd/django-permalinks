from permalinks.models import Permalinks
from django.http import JsonResponse
import random
from django.views import View


def getRandomWord(length=5):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


class get_random_string(View):

    def get(self, request, *args, **kwargs):
        response = dict()
        response['status'] = 'success'
        response['result'] = None

        randomWord = None
        all_old_urls = set(Permalinks.objects.values_list('old_url', flat=True))

        while True:
            randomWord = getRandomWord(7)
            full_url = str(request.scheme) + "://" + str(request.get_host()) + "/" + str(randomWord)
            if full_url not in all_old_urls:
                break

        response['result'] = randomWord

        return JsonResponse(response, status=200)
