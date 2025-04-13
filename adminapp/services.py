from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))



def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_faculty""")
        faculties = dictfetchall(cursor)
        return faculties


def get_kafedras():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_subject""")
        subject = dictfetchall(cursor)
        return subject


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_teacher""")
        teacher = dictfetchall(cursor)
        return teacher


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_student""")
        student = dictfetchall(cursor)
        return student


def get_groups():
    with closing(connection.cursor()) as cursor:
        # cursor.execute("""SELECT * FROM adminapp_group""")
        cursor.execute("""SELECT g.id, g.name, COALESCE(t.first_name || ' ' || t.last_name, 'Unknown person') AS full_name
                                FROM adminapp_group g LEFT JOIN adminapp_teacher t ON g.teacher_id = t.id;""")
        group = dictfetchall(cursor)
        return group
