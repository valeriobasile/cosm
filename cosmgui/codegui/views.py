from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from codegui.models import Project

@login_required(login_url='/login/')
def dashboard(request):
    """
    This is the first view activated when users log in.
    It leads to the profile page, or 'dashboard', whose
    content depends on the type of user.
    The admin user will see an overview of all his projects, while
    the coders will see the status of the projects they are involved in.
    """

    '''
    Retrieve the username to pass it to the template.
    The login_required decorator ensures that the username is always present.
    '''
    username = request.user.username

    '''If the user is the admin, show the project management view,
       if the user is not the admin show his dashboard,
       if the user is not authenticated show the login page.
    '''

    if username == 'admin':
        return render(request,
                      'codegui/dashboard_admin.html', {})
    else:
        # regular user (coder)
        projects = Project.objects.all.filter(coders=request.user)

        return render(request,
                      'codegui/dashboard.html',
                      {'username':request.user.username})
