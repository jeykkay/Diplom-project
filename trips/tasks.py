from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Booking
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status


@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, **kwargs):
    subject = 'Машина успешно забронирована'
    message = f'Уважаемый {instance.passenger.first_name}, вы успешно забронировали машину {instance.car.brand}-{instance.car.num_car} на дату {instance.date} и время {instance.time}'
    try:
        send_mail(subject, message, 'from@example.com', [instance.passenger.email])
    except ObjectDoesNotExist:
        return Response({'error': 'Пользователя не существует'}, status=status.HTTP_400_BAD_REQUEST)
