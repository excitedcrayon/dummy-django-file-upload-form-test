from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        print("What is the filename by Shylet?: ", request.POST['filename'])
        print("What is the name of the document file?: ", request.FILES)
        # http://localhost:8000 | http://localhost
        # directory is /media/
        # file from request.FILES is CV-Template.jpeg

        # create a link to save in MySQL DB Table 
        # such as http://localhost/media/filename
    return render(request, 'upload.html')