from .models import Student
from faker import Faker
import random
from subjects.models import Subject


fake = Faker()


def custom_random_int(from_id, to_id, exclude_id):
    '''
    custom random int generator to exclude the provided integers from generating
    '''
    random_int = random.randint(from_id, to_id)
    if random_int not in exclude_id:
        return random_int
    else:
        return custom_random_int(from_id, to_id, exclude_id)


class SeedStudentData(object):
    StudentSubjectRelation = Student.subjects.through

    def create_students(self, number_of_students=50):
        Student.objects.all().delete()
        persons = []
        rank = 1
        for i in range(number_of_students):
            name = fake.first_name()
            date = fake.date_between(start_date='-30y', end_date='today')
            standard = random.randint(10, 13)
            ranking = rank
            persons.append(Student(name=name, doj=date, standard=standard, ranking=ranking))
        Student.objects.bulk_create(persons)
        persons = []

    def create_relation_table_subj_stud(self):
        relation_table = []
        subjects = list(Subject.objects.all().only('id'))
        subject_ids = [subject.id for subject in subjects]
        last_created_student_id = Student.objects.all().last().id
        for student_id in range(last_created_student_id-50+1, last_created_student_id):
            student_subjects_id = []
            for _ in range(3):
                subject_id = custom_random_int(0, len(subject_ids)-1, student_subjects_id)
                student_subjects_id.append(subject_id)
                relation_table.append(self.StudentSubjectRelation(student_id=student_id, subject_id=subject_ids[subject_id]))
            student_subjects_id = []
        self.StudentSubjectRelation.objects.bulk_create(relation_table)
