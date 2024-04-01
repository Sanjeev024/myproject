from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Protein

from .models import CustomUser

def home(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        user = authenticate(request, access_code=access_code)
        if user is not None:
            login(request, user)
            masked_access_code = ' '.join(list('⬤' * (len(access_code) - 2) + access_code[-2:]))
            request.session['access_code'] = masked_access_code  # Store access code in session
            return redirect('database')
        else:
            messages.error(request, "Wrong Credentials")
    return redirect('home')

# def database(request):
#     access_code = None

#     if not request.user.is_authenticated:
#         messages.error(request, "You are not logged in.")
#         # return redirect('home')

#     if request.method == "POST":
#         access_code = request.POST.get("access_code")

#     user = authenticate(request, access_code=access_code)

#     if user is not None:
#         login(request, user)
#         masked_access_code =' '.join(list('⬤' * (len(access_code) - 2) + access_code[-2:]))

#         # Fetch data from the Protein table
#         protein_data = Protein.objects.all()

#         # Pagination
#         paginator = Paginator(protein_data, 10)  # Show 10 records per page
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)

#         return render(request, 'database.html', {'access_code': masked_access_code, 'page_obj': page_obj})
#     else:
#         messages.error(request, "Wrong Credentials")
#         return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def database(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in.")
        return redirect('home')

    # Retrieve access code from session
    masked_access_code = request.session.get('access_code', '')

    # Fetch data from the Protein table
    protein_data = Protein.objects.all()

    # Pagination
    paginator = Paginator(protein_data, 10)  # Show 10 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

     # Add start and end values for all records
    for protein in page_obj:
        domain_parts = protein.domain.split('(')[1].split(')')[0].split('-')
        start = int(domain_parts[0])
        end = int(domain_parts[1])
        protein.start = start
        protein.end = end
        protein.dispStart = int(start) - 20
        protein.dispEnd = int(end) + 30

    for protein in page_obj:
        print(protein.dispStart)
        print(protein.dispEnd)

    # Retrieve unique organism names from the Protein model
    organism_names = Protein.objects.values_list('organism', flat=True).distinct()

     # Retrieve unique domains names from the Protein model
    domains_names = Protein.objects.values_list('domain', flat=True).distinct()

    context = {
        'organism_names': organism_names
    }

    return render(request, 'database.html', {'access_code': masked_access_code, 'page_obj': page_obj,  'organism_names': organism_names, 'domains_names': domains_names})
