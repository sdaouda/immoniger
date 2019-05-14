from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Zone(models.Model):
    zone = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.zone
    
class Localite(models.Model):
    zone = models.ForeignKey(Zone ,on_delete=models.SET_NULL,blank=True,null=True)
    localite =models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return "%s-%s" % (self.zone,self.localite)



class TypeService(models.Model):
    typeserv = models.CharField(max_length=80, db_index=True)
    
    def __str__(self):
        return self.typeserv
    
class TypeProject(models.Model):
    typeproj = models.CharField(max_length=80, db_index=True)
    
    def __str__(self):
        return self.typeproj

class Commodite(models.Model):
    name = models.CharField(max_length=200, help_text="Precisez un detail")
    slug = models.SlugField(max_length=200, db_index=True, unique=True,null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    reference = models.CharField(max_length=50, blank=True,db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    dimmension = models.CharField(max_length=20, blank=True,null=True)
    localite = models.ForeignKey(Localite ,on_delete=models.SET_NULL ,blank=True,null=True,verbose_name='localité')
    numeroParcelle = models.CharField(max_length=15, default="n/a",blank=True,null=True)
    lotissement = models.CharField(max_length=200, default="n/a",blank=True,null=True)
    actsession = models.CharField(max_length=200, blank=True,null=True)
    image = models.ImageField(upload_to='products/imgs/', blank=True)
    image1 = models.ImageField(upload_to='products/imgs/', blank=True,null=True)
    image2 = models.ImageField(upload_to='products/imgs/', blank=True,null=True)
    image3 = models.ImageField(upload_to='products/imgs/', blank=True,null=True)
    image4 = models.ImageField(upload_to='products/imgs/', blank=True,null=True)
    image5 = models.ImageField(upload_to='products/imgs/', blank=True,null=True)
    description = models.TextField(blank=True,verbose_name='Decrire votre rechecher svp')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='Prix à partir de')
    available = models.BooleanField(default=True)
    nbChambre = models.PositiveIntegerField(verbose_name='Nombre Chambre(s)')
    nbDouche = models.PositiveIntegerField(verbose_name='Nombre Douches(s)')
    ACT_TYPE = (
        ('LOCATION','LOCATION'),
        ('VENTE', 'VENTE'),
    )
    commd = (
        ('VIDE','VIDE'),
        ('MEUBLE', 'MEUBLE'),
    )
    action_type = models.CharField(max_length=10, choices=ACT_TYPE, blank=True, 
                    default='LOCATION', help_text='Vente/Location',verbose_name='action')
    commdt = models.CharField(max_length=10, choices=commd, blank=True, default='VIDE', help_text='Vide/meuble',verbose_name='Intérieur')
    details = models.ManyToManyField(Commodite, help_text='Select a genre for this book',related_name='commodite')
    created = models.DateTimeField(auto_now_add=True)
    vendeur = models.ForeignKey("Vendor" ,blank=True,null=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_details', args=[self.id, self.slug])
    
    
class Service(models.Model):
    reference = models.CharField(max_length=50, blank=True,db_index=True)
    typeservice = models.ForeignKey(TypeService, related_name='tservice')
    image = models.ImageField(upload_to='service/imgs/', blank=True)
    description = models.TextField(blank=True,verbose_name='Description du service')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("Vendor" ,blank=True,null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.reference
    
class Project(models.Model):
    name = models.CharField(max_length=80, db_index=True)
    reference = models.CharField(max_length=50, blank=True,db_index=True)
    typeproject = models.ForeignKey(TypeProject, related_name='tproject')
    image = models.ImageField(upload_to='project/imgs/', blank=True)
    description = models.TextField(blank=True,verbose_name='Description du project')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("Vendor" ,blank=True,null=True)
 
    class Meta:
        ordering = ('-created',)
 
    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20,blank=True,null=True)
    phone3 = models.CharField(max_length=20,blank=True,null=True)
    address = models.CharField(max_length=200,blank=True,null=True)
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50,blank=True,null=True)
    localization = models.TextField()

    def __str__(self):
        return self.name + "-" + self.phone1

    def get_absolute_url(self):
        return reverse('shop:vendor-detail', args=[self.id])
