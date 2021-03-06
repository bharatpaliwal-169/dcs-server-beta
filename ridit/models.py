from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator,validate_email
import uuid

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
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=100)
  email = models.EmailField()
  comment = models.TextField(max_length=500)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  phone = models.CharField(max_length=10,validators=[phone_regex])

  def __str__(self):
    return self.name

class School(models.Model):
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
  email = models.EmailField(max_length=200,validators=[validateEmail])
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  mobile = models.CharField(max_length=10,validators=[phone_regex])
  VEHICLE = (('2w','2 wheeler'),('3w','3 wheeler'),('4w','4 wheeler'),('hw','Heavy Wheeler'))
  vehicle = models.CharField(max_length=20,choices=VEHICLE)
  CHOICE = (('0','Male'),('1','Female'))
  gender = models.CharField(max_length=10,choices = CHOICE)
  DAY=(('0','7 days'),('1','15 days'))
  #days=models.IntegerField(validators=[MinValueValidator(7),MaxValueValidator(30)])
  days=models.CharField(max_length=10,choices=DAY)
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
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
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
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
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
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  TYPE = (('2w','2 wheeler'),('3w','3 wheeler'),('4w','4 wheeler'),('4cw','4 Wheeler Commercials'),('hw','Heavy Wheeler'))
  vehicle_type= models.CharField(max_length=20,choices=TYPE)
  vehicle_no = models.CharField(max_length=10)
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
  

class Insurance(models.Model):
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  city = models.ForeignKey(City,on_delete=models.CASCADE)
  exp_date = models.DateField()
  TYPE=(('li','Life Insurance'),('mi','Motor Insurance'),('hi','Health Insurance'),('ti','Travel Insurance'),('pi','Property Insurance'),('mo','Mobile Insurance'),('ci','Cycle Insurance'),('bi','Bite-size Insurance'))
  ins_type = models.CharField(max_length=30,choices=TYPE)
  def __str__(self):
      return self.name

class Rto(models.Model):
  eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name_regex = RegexValidator(regex=r'^[A-Za-z\s]*$',message="Only Alphabets and spaces are allowed")
  name = models.CharField(max_length=200,validators=[name_regex])
  phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be of 10 digits")
  contact = models.CharField(max_length=10,validators=[phone_regex])
  city = models.ForeignKey(City,on_delete=models.CASCADE)
  SERVICE=(('0','Transfer'),('1','Fitness'),('2','DL'),('3','NOC'),('4','RC Removal'),('5','Others'))
  serv = models.CharField(max_length=60,choices=SERVICE)
  others = models.TextField(max_length=300)
  def __str__(self):
    return self.name