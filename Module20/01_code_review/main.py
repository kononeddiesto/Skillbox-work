students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function_stud(student_dict):
    stud_interests = []
    string = ''
    for _, i_name in student_dict.items():
        stud_interests.extend(i_name['interests'])
        string += i_name['surname']
    return stud_interests, len(string)


pairs = {
    i_id: i_student['age']
    for i_id, i_student in students.items()
}
print('Ключ и возраст студента: {0}'.format(pairs))

lst_interests, length = function_stud(students)
print('Интересы студентов: {0}\nДлина фамилий студентов: {1}'.format(lst_interests, length))
