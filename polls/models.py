from django.db import models


class donor_Registration(models.Model):

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    father_name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(
        max_length=6,
        blank=True,
        null=True,
        choices=gender_choices,
    )

    email = models.EmailField(
        max_length=50,
        blank=True,
        null=True
    )

    phone_number = models.IntegerField(
        blank=True,
        null=True,
    )

    state = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    occupation = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )

    blood_group_choices = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b', 'B'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ]

    blood_group = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=blood_group_choices,
    )

    home_address = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    last_donate_date = models.DateField(
        blank=True,
        null=True,
    )

    any_diseases_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    any_disease = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=any_diseases_choices,
    )

    allergies_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    allergies = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=allergies_choices,
    )

    cardiac_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    cardiac = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=cardiac_choices,
    )

    bleeding_disorder_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    bleeding_disorder = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=bleeding_disorder_choices,
    )

    hbsAg_hcv_hIV_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    hbsAg_hcv_hIV = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=hbsAg_hcv_hIV_choices,
    )

    def __str__(self):
        return self.name


class sea_rch(models.Model):

    blood_group_choices = [
        ('a+', 'A+'),
        ('a-', 'A-'),
        ('b+', 'B+'),
        ('b', 'B'),
        ('b-', 'B-'),
        ('o+', 'O+'),
        ('ab+', 'AB+'),
        ('ab-', 'AB-'),
    ]

    blood_group = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        choices=blood_group_choices,
    )

    state = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )


class con_tact(models.Model):

    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    phone_number = models.IntegerField(
        blank=True,
        null=True,
    )

    email = models.EmailField(
        max_length=50,
        blank=True,
        null=True
    )

    subject = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
