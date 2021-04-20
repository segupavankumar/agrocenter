from django.shortcuts import render,redirect
from login.models import mailinglist
from farmer.models import fruits
def home(request):
    '''
    **Functionality**

    *if the request method is get :-*


    displays home page to the users

    *if the request method  is post :-*

    it takes the entered email id and stores it in a model :model:`login.mailinglist`.
    

    **Template:**

    :template:`home.html`



    '''
    if request.method == "POST":
        email = request.POST['email']
        a = mailinglist(email = email)
        a.save()
        print(email)

        return redirect('/')
    return render(request,'home.html')

def about(request):

    '''
    **Functionality**

    
    Displays about page to the user 
    
    '''
    return render(request,'about.html')