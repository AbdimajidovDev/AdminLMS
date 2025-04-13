from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.views.generic import TemplateView

from .models import *
from .forms import *
from . import services



def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    kafedras = services.get_kafedras()
    subjects = services.get_subjects()
    teachers = services.get_teachers()
    groups = services.get_groups()
    students = services.get_students()
    ctx = {
        'counts': {
            'faculties' : len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(request, 'index.html', ctx)



# ---  FACULTY Views  ---

@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions

        faculty_count = request.session.get('faculty_count', 0)
        faculty_count += 1
        request.session['faculty_count'] = faculty_count
        return redirect('faculty_list')
    ctx = {
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('faculty_list')
    ctx = {
        'form': form,
        'model': model
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    actions = request.session.get('actions', [])
    actions += [f"You deleted faculty: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    ctx = {
        'faculties': faculties
    }
    return render(request, 'faculty/list.html', ctx)



#   ---  KAFEDRA Views ---

@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions

        kafedra_count = request.session.get('kafedra_count', 0)
        kafedra_count += 1
        request.session['kafedra_count'] = kafedra_count

        return redirect('kafedra_list')
    ctx = {
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(id=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('kafedra_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(id=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted kafedra: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedras()
    ctx = {
        'kafedras': kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


# ---  SUBJECT Views  ---

@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created subject: {request.POST.get('name')}"]
        request.session['actions'] = actions

        subject_count = request.session.get('subject_count', 0)
        subject_count += 1
        request.session['subject_count'] = subject_count
        return redirect('subject_list')
    ctx = {
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(id=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited subject: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('subject_list')
    ctx = {
        'model': model,
        'form': form
    }
    return redirect(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(id=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted subject: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = Subject.objects.all()
    # model = services.get_subjects()
    ctx = {
        'subjects': subjects
    }
    return render(request, 'subject/list.html', ctx)


# ---  TEACHER Views  ---

@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created teacher: {request.POST.get('name')}"]
        request.session['actions'] = actions

        teacher_count = request.session.get('teacher_count', 0)
        teacher_count += 1
        request.session['teacher_count'] = teacher_count
        return redirect('teacher_list')
    ctx = {
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(id=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited teacher: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('teacher_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    actions = request.session.get('actions', [])
    actions += [f"You deleted teacher: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('teacher_list')


@login_required_decorator
def teacher_list(request):
    # teachers = services.get_teachers()
    teachers = Teacher.objects.all()
    ctx = {
        'teachers': teachers
    }
    return render(request, 'teacher/list.html', ctx)


# ---  STUDENT Views  ---

@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created student: {request.POST.get('name')}"]
        request.session['actions'] = actions

        student_count = request.session.get('student_count', 0)
        student_count += 1
        request.session['student_count'] = student_count
        return redirect('student_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited student: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('student_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted student: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    # students = services.get_students()
    students = Student.objects.all()
    ctx = {
        'students': students
    }
    return render(request, 'student/list.html', ctx)


# ---  GROUP Views  ---

@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created group: {request.POST.get('name')}"]
        request.session['actions'] = actions

        group_count = request.session.get('group_count', 0)
        group_count += 1
        request.session['group_count'] = group_count
        return redirect('group_list')
    ctx = {
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(id=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited group: {request.POST.get('name')}"]
        request.session['actions'] = actions
        return redirect('group_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    actions = request.session.get('actions', [])
    actions += [f"You deleted group: {request.POST.get('name')}"]
    request.session['actions'] = actions
    return redirect('group_list')


@login_required_decorator
def group_list(request):
    groups = services.get_groups()
    # groups = Group.objects.all()
    ctx = {
        'groups': groups
    }
    return render(request, 'group/list.html', ctx)


@login_required_decorator
def  profile(request):
    return render(request, 'profile.html')


@login_required_decorator
def history(request):
    return render(request, 'history.html')