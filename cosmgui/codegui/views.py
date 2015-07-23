from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def dashboard(request):

    '''If the user is the admin, show the project management view,
       if the user is not the admin show his dashboard,
       if the user is not authenticated show the login page.
    '''

    if username == 'admin':
        return render(request, 'codegui/dashboard_admin.html', {})
    else:
        #if username != None:
        return render(request, 'codegui/dashboard.html', {})
