from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=111, null=True, blank=True)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=111, null=True, blank=True)


    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=66)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField(null=False, blank=False)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    faculty_teacher = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    kafedra_teacher = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Group(models.Model):
    name = models.CharField(max_length=55)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=55, null=False, blank=False)
    last_name = models.CharField(max_length=55, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    class_leader = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='stud')
    image = models.ImageField(upload_to='images', null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
