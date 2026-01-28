import os
import django
from dotenv import load_dotenv
from datacenter.models import Passcard
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


if __name__ == '__main__':
    active_passcard = Passcard.objects.filter(is_active=True)
    print('Количество пропусков:', Passcard.objects.count())
    print("Активных пропусков:", len(active_passcard))
