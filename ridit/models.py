from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator,validate_email

class City(models.Model):
  id = models.IntegerField(primary_key=True, unique = True)
  title = models.CharField(max_length=50,unique=True)

  def __str__(self):
    return self.title

def validateEmail(value):
  try:
    validate_email(value)
  except ValidationError as e:
    print("bad email, details:", e)
  else:
    print("good email")

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  comment = models.TextField(max_length=500)
  phone = models.CharField(max_length=10)

  def __str__(self):
    return self.name


class School(models.Model):
  #uuid=models.CharField(unique=True,max_length=100)
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200,validators=[validateEmail])
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  mobile = models.CharField(max_length=10,validators=[phone_regex])
  VEHICLE = (('2w','2 wheeler'),('3w','3 wheeler'),('4w','4 wheeler'),('4cw','4 Wheeler Commercials'),('hw','Heavy Wheeler'))
  vehicle = models.CharField(max_length=20,choices=VEHICLE)
  CHOICE = (('0','Male'),('1','Female'))
  gender = models.CharField(max_length=10,choices = CHOICE)
  days=models.IntegerField(validators=[MinValueValidator(7),MaxValueValidator(30)])
  date = models.DateField()
  city = models.ForeignKey(City,on_delete=models.CASCADE)

  def __str__(self):
      return self.name


class Service(models.Model):
  id = models.IntegerField(primary_key=True, unique = True)
  title = models.CharField(max_length=50,unique=True)

  def __str__(self):
    return self.title

class Partner(models.Model):
  name = models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  service = models.ForeignKey(Service,on_delete=models.CASCADE)
  city = models.ForeignKey(City,on_delete=models.CASCADE)
  query = models.TextField(max_length=300)
  def __str__(self):
    return self.name

def validate_range(value):
     if int(value)>=1 and int(value)<=30:
        return value
     else:
        raise ValidationError("Days must be between 1-30")

class Chauffer(models.Model):
  name = models.CharField(max_length=200)
  email = models.EmailField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  address = models.CharField(max_length=400)
  date = models.DateField()
  pincode = models.CharField(max_length=6)

  days=models.IntegerField(validators=[validate_range])
  price = models.IntegerField()
  
  def __str__(self):
    return self.name
  
  @property
  def get_price(self):
    day = self.days
    return 499*day
  


  def save(self, *args, **kwargs):
    self.price = self.get_price
    super(Chauffer, self).save(*args, **kwargs)
  


class Puc(models.Model):
  name = models.CharField(max_length=200)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  TYPE = (('2w','2 wheeler'),('3w','3 wheeler'),('4w','4 wheeler'),('4cw','4 Wheeler Commercials'),('hw','Heavy Wheeler'))
  vehicle_type= models.CharField(max_length=20,choices=TYPE)
  vehicle_no = models.CharField(max_length=20)
  exp_date = models.DateField()
  city = models.ForeignKey(City,on_delete=models.CASCADE)
  price=models.IntegerField()
  def __str__(self):
      return self.name
  @property
  def get_price(self):
    vtype=self.vehicle_type
    total=0
    if vtype=='2w':
      total=50
    elif vtype=='3w':
      total=150
    elif vtype=='4w':
      total=200
    elif vtype=='4cw':
      total=250
    else:
      total=500
    return total

  def save(self, *args, **kwargs):
    self.price = self.get_price
    super(Puc, self).save(*args, **kwargs)
  