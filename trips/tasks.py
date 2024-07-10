from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Booking


@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, **kwargs):
    subject = 'Машина успешно забронирована'
    message = 'Уважаемый {}, вы успешно забронировали машину {}-{} на дату {} и время {}'.format(
        instance.passenger.first_name, instance.car.brand,
        instance.car.num_car, instance.date, instance.time)
    send_mail(subject, message, 'from@example.com', [instance.passenger.email])
