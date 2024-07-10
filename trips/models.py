from django.db import models
from users.models import CustomUser, Driver


class Car(models.Model):
    CAR_STATUS = (
        ('Available', 'Available'),
        ('Not available', 'Not available'),

    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель')
    brand = models.CharField(max_length=255, verbose_name='Марка автомобиля')
    model = models.CharField(max_length=255, verbose_name='Модель автомобиля')
    year = models.PositiveIntegerField(verbose_name='Год')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    num_car = models.CharField(unique=True, verbose_name='Гос номер автомобиля')
    car_status = models.CharField(choices=CAR_STATUS, default='Available', max_length=100, verbose_name='Статус')

    def __str__(self):
        return f"{self.brand} {self.model}: {self.num_car}"

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Trip(models.Model):
    TRIP_STATUS = (
        ('Awaiting order', 'Awaiting order'),
        ('Started', 'Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),

    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="trip_as_driver")
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="trip_as_passenger")
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата поездки')
    start_time = models.TimeField(verbose_name='Время начала поездки')
    end_time = models.TimeField(verbose_name='Время окончания поездки')
    destination = models.CharField(max_length=255, verbose_name='Место назначения')
    price = models.FloatField(blank=False, null=False, verbose_name='Цена')
    driver_status = models.CharField(choices=TRIP_STATUS, default='Awaiting order', max_length=100, verbose_name='Статус')

    def __str__(self):
        return f"{self.driver.first_name}-{self.car};\nPrice: {self.price}"

    class Meta:
        verbose_name = "Поездка"
        verbose_name_plural = "Поездки"


class Booking(models.Model):
    BOOKING_STATUS = (
        ('Not booked', 'Not booked'),
        ('Booked', 'Booked'),

    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="booking_as_car")
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="booking_as_driver")
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="booking_as_passenger")
    date = models.DateField(blank=False, null=False, verbose_name='Дата брони')
    time = models.TimeField(blank=False, null=False, verbose_name='Время брони')
    booking_status = models.CharField(choices=BOOKING_STATUS, default='Not booked', max_length=100, verbose_name='Статус')

    def __str__(self):
        return f"The car {self.car} is reserved {self.date} at {self.time}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"


class Rating(models.Model):
    driver = models.ForeignKey(Driver, related_name='rating_received', on_delete=models.CASCADE)
    passenger = models.ForeignKey(CustomUser, related_name='rating_left', on_delete=models.CASCADE)
    rating = models.DecimalField(verbose_name='Рейтинг', max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.driver.first_name} rating is {self.rating} from {self.passenger.first_name}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Comment(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='comments')
    passenger = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.passenger.first_name} commented on {self.trip} at {self.created_at}\n{self.text}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
