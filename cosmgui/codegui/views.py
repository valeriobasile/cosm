from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from codegui.models import Project, Message, Code

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
        # if admin, show the admin page with all the projects
        projects = Project.objects.all()

        return render(request,
                      'codegui/dashboard_admin.html',
                      {'projects':projects})
    else:
        # regular user (coder)
        projects = Project.objects.all().filter(coders=request.user)

        return render(request,
                      'codegui/dashboard.html',
                      {'username':username,
                       'projects':projects})

@login_required(login_url='/login/')
def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    coders = project.coders.all()

    # only users assigned to the project can see the project page
    if not request.user in coders.all():
        return render(request,
                      'codegui/unauthorized.html',
                      {'username':request.user.username,
                       'project':project})

    # get all the messages of the project
    messages = project.message_set.all()
    # count the messages of the project
    n_messages = project.message_set.count()
    # for each message, count 1 if there is at least one code
    # (not sure how efficient/scalable this is)
    n_codes = sum(map(lambda x: int(x.code_set.all().count()>0), messages))

    return render(request,
                  'codegui/project.html', {'project':project,
                                           'coders':coders,
                                           'n_messages':n_messages,
                                           'n_codes':n_codes})
