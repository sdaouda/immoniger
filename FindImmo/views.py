from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from .models import Category, Product, Vendor
from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import auth
from FindImmo.forms import ProductForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Vendor
from django.db.models import Q
import operator
from django.utils.six.moves import reduce
from .filters import UserFilter, VendorFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    Lproducts = Product.objects.filter(available=True,action_type='LOCATION')
    Vproducts = Product.objects.filter(available=True,action_type='VENTE')
    top10=Product.objects.all().order_by('price')[:5]
    #Nvilla = Product.objects.filter(category__name='Beatles Blog')
    queryset = Product.objects.filter(details__slug='aucun',)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        #category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
        Lproducts = Product.objects.filter(available=True,action_type='LOCATION',category=category)
        Vproducts = Product.objects.filter(available=True,action_type='VENTE',category=category)
    if category_slug:
        return render(request, 'shop/product/listPerCategory.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'Lproducts':Lproducts,'Vproducts':Vproducts,})
    else:
        return render(request, 'shop/product/mainpage.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'top10':top10,'Lproducts':Lproducts,
                                                      'Vproducts':Vproducts,'queryset':queryset,})

    

def list_vide(request, action=None, Cat_slug=None, comm=None):
    prod= None
    prod1= None
    prod2= None
    if Cat_slug != 'all':
        categories = Category.objects.all()
        prod = Product.objects.filter(action_type=action, available=True)
        prod1 = prod.filter(category__slug = Cat_slug)
        prod2 = prod1.filter(commdt=comm)
        return render(request, 'shop/product/list1.html', {'prod1': prod1, 'prod2': prod2, 'categories':categories})
    else:
        categories = Category.objects.all()
        prod = Product.objects.filter(action_type=action, available=True)
        return render(request, 'shop/product/list1.html', {'prod': prod, 'categories':categories})

def product_detail(request, pid, slug):
    product = get_object_or_404(Product, id=pid, slug=slug, available=True)
    JoinProddetails = product.details.all()
    categories = Category.objects.all()
    queryset_list = Product.objects.all()
    like_queryset_list = queryset_list.filter(Q(description__icontains=product.description))
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,'categories': categories,'like_queryset_list':like_queryset_list,
                  'JoinProddetails':JoinProddetails,})

def qsearch(*argv):
    return len(argv[0])

def SearchList(request):
    lqueryset_list = ""
    vqueryset_list = ""
    commTab = []
    filters = []
    filtre = Q()
    queryset_list = Product.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    Lproducts = Product.objects.filter(available=True,action_type='LOCATION')
    Vproducts = Product.objects.filter(available=True,action_type='VENTE')
    act = request.GET.get('actId')
    vquery = request.GET.get('v_KeyWords')
    lquery = request.GET.get('l_KeyWords')
    l_localite = request.GET.get('l_local')
    l_typeBien = request.GET.get('l_type')
    l_toilette = request.GET.get('l_douche')
    l_Nchambre = request.GET.get('l_chambre')
    l_prixmin = request.GET.get('l_pmin')
    l_prixmax = request.GET.get('l_pmax')
    v_localite = request.GET.get('v_local')
    v_typeBien = request.GET.get('v_type')
    v_toilette = request.GET.get('v_douche')
    v_Nchambre = request.GET.get('v_chambre')
    v_prixmin = request.GET.get('v_pmin')
    v_prixmax = request.GET.get('v_pmax')

    # douche_ext = request.GET.get('douext')
    # aucun = request.GET.get('aucun')
    # depen_ext = request.GET.get('depext')
    # clim = request.GET.get('clim')
    # chauff_eau = request.GET.get('chauffo')
    # gason_jardin = request.GET.get('gazonjar')

    # if douche_ext != None:
    #     commTab.append(douche_ext)
    #     filters.append(Q(details__slug=douche_ext,))
    #     filtre &= Q(details__slug=douche_ext,)
    # if aucun != None:
    #     commTab.append(aucun)
    #     filters.append(Q(details__slug=aucun,))
    #     filtre &= Q(details__slug=aucun,)
    # if depen_ext != None:
    #     commTab.append(depen_ext)
    #     filters.append(Q(details__slug=depen_ext,))
    #     filtre &= Q(details__slug=depen_ext,)
    # if clim != None:
    #     commTab.append(clim)
    #     filters.append(Q(details__slug=clim,))
    #     filtre &= Q(details__slug=clim,)
    # if chauff_eau != None:
    #     commTab.append(chauff_eau)
    #     filters.append(Q(details__slug=chauff_eau,))
    #     filtre &= Q(details__slug=chauff_eau,)
    # if gason_jardin != None:
    #     commTab.append(gason_jardin)
    #     filters.append(Q(details__slug=gason_jardin,))
    #     filtre &= Q(details__slug=gason_jardin,)

    #queryset = queryset_list.filter(filtre)
    #queryset = queryset_list.filter(Q(details__slug__icontains=clim))    
    
    #for arg in commTab:
       # filtre &= Q(details__slug__icontains=arg)
    
    #queryset = Product.objects.filter(reduce(operator.iand, filters))
    #lglobquery = Q(localite__localite__icontains=l_localite) | Q(category__name__icontains=l_typeBien)|Q(nbDouche__exact=l_toilette) | Q(nbChambre__exact=l_Nchambre) | (Q(price__gte=l_prixmin) & Q(price__lte=l_prixmax)) | Q(localite__localite__icontains=lquery)
    if act == "louer":
        if (lquery=="" and l_localite=="" and l_typeBien=="" and l_toilette=="" and l_Nchambre=="" and l_prixmin=="" and l_prixmax==""):
            return render(request,'shop/product/searchlist.html',{'act':act,'categories':categories,'Lproducts':Lproducts,})
        else:
            lqueryset_list = queryset_list.filter(Q(localite__localite__icontains=l_localite),Q(category__name__icontains=l_typeBien),
                                                  Q(description__icontains=lquery),action_type__iexact='LOCATION')
            #lqueryset_list = queryset_list.filter(Q(details__slug__icontains='climatisation'),action_type__iexact='LOCATION')
            
            return render(request,'shop/product/searchlist.html',{'categories':categories,'lqueryset_list':lqueryset_list,})  
    if act == "vendre":
        if not (vquery and v_localite and v_typeBien and v_toilette and v_Nchambre and v_prixmin and v_prixmax):
            return render(request,'shop/product/searchlist.html',{'act':act,'categories':categories,'Vproducts':Vproducts,})
        else:
            vqueryset_list = queryset_list.filter(Q(localite__localite__icontains=v_localite),Q(category__name__icontains=v_typeBien),
                                                  Q(description__icontains=vquery),action_type__startswith='VENTE')
            return render(request,'shop/product/searchlist.html',{'categories':categories,'vqueryset_list':vqueryset_list,})
def AdvSearchList(request):
    prodform = ProductForm()
    categories = Category.objects.all()
    return render(request,'shop/product/advancedSearch.html',{'categories':categories,'prodform':prodform,})
    #return render(request,'shop/product/advancedSearch.html',{'categories':categories,'prodform':prodform,'douche_ext':douche_ext,
       # 'depen_ext':depen_ext,'clim':clim,'chauff_eau':chauff_eau,'gason_jardin':gason_jardin,'aucun':aucun,})

def vendreUnBien(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/vendre1.html', {'products': products,'categories':categories})

def nosprestation(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/prestation.html', {'products': products,'categories':categories})

def contacteznous(request):
    contact = Vendor.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/product/contact.html', {'contact': contact,'categories':categories,})

def search(request):
    product_list1 = Product.objects.all()
    categories = Category.objects.all()
    product_filter = UserFilter(request.GET, queryset=product_list1)
    return render(request, 'shop/product/user_list.html', {'filter': product_filter,'categories':categories})

def vendorform(request):
    vendorInfo = Vendor.objects.all()
    categories = Category.objects.all()
    vendor_filter = VendorFilter(request.GET, queryset=vendorInfo)
    return render(request, 'shop/product/vendor_list.html', {'filter': vendor_filter,'categories':categories})

class VendorDetailView(generic.DetailView):
    model = Vendor
    template_name = 'shop/product/vendor_detail.html'

class VendorCreate(CreateView):
    model = Vendor
    fields = '__all__'
    template_name = 'shop/product/vendor_form.html'
    #initial = {'date_of_death': '05/01/2000'}