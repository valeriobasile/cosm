from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from codegui.models import Project, Message, Code, Category, Progress
from django.shortcuts import redirect
from codegui.forms import ProjectForm
from django.db.models import Q

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

    '''
    Show the project the user is involved in, and the project owned, separately.
    If the user is not authenticated show the login page.
    '''

    # weird syntax to put OR in a query
    projects = Project.objects.all().filter(Q(coders=request.user) | Q(owner=request.user)).distinct()
    #projects = Project.objects.all().filter(coders=request.user)
    #owned = Project.objects.all().filter(owner=request.user)

    return render(request,
                  'codegui/dashboard.html',
                  {'username':username,
                   'projects':projects})

@login_required(login_url='/login/')
def project(request, project_id):
    project = Project.objects.get(pk=project_id)
    coders = project.coders.all()

    # only users assigned to the project can see the project page
    if (not request.user in coders.all()) and (not request.user.is_superuser) :
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

@login_required(login_url='/login/')
def coding(request, project_id):
    project = Project.objects.get(pk=project_id)
    coders = project.coders.all()

    # only users assigned to the project can see the project page
    # TODO this is replicated, find a better way, e.g. a decorator
    if not request.user in coders.all():
        return render(request,
                      'codegui/unauthorized.html',
                      {'username':request.user.username,
                       'project':project})

    # get the next message to code
    try:
        last_index = Progress.objects.get(project=project,
                                          coder=request.user).index
    except (ValueError, Progress.DoesNotExist):
        '''if there is no Progress it means that it is the first time this user
           is coding, therefore a Progress object is created
        '''
        progress = Progress(project=project,
                            coder=request.user,
                            index=0)
        progress.save()

        last_index = 0
    message = project.message_set.get(index=last_index+1)
    variables = project.variable_set.all()
    return render(request,
                  'codegui/coding.html', {'project':project,
                                          'message':message,
                                          'variables':variables})

@login_required(login_url='/login/')
def save(request):
    message = Message.objects.get(id=request.POST["message"])
    project = message.project
    for key, value in request.POST.iteritems():
        if key.startswith("variable_"):
            # create a new code
            code = Code(coder=request.user,
                        message=message,
                        code=Category.objects.get(value=value))
            code.save()

    # update the progress (increase by one)
    progress = Progress.objects.get(project=project,
                                    coder=request.user)
    progress.index = progress.index + 1
    progress.save()

    return redirect("coding", project_id=project.id)


@user_passes_test(lambda u: u.is_superuser)
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print form.errors
            #return redirect('dashboard')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()
        return render(request,
                      'codegui/new_project.html',
                      {'form':form})
