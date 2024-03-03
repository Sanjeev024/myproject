from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is homePage")
    return render(request, 'index.html')

def database(request):
    data = [
        {"name": "John", "last_name": "Doe", "age": 25, "address": "123 Main St"},
        {"name": "Jane", "last_name": "Smith", "age": 30, "address": "456 Oak St"},
        {"name": "Bob", "last_name": "Johnson", "age": 28, "address": "789 Pine St"},
        # Add more mock data as needed
    ]
    return render(request, 'database.html', {'data':data})