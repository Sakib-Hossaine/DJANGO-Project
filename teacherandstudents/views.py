from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student, ExamResult

@login_required
def profile(request):
    if request.user.is_teacher:
        try:
            teacher = Teacher.objects.get(user=request.user)
            return render(request, 'teacher.html', {'teacher': teacher})
        except Teacher.DoesNotExist:
            return redirect('login')
    elif request.user.is_student:
        try:
            student = Student.objects.get(user=request.user)
            return render(request, 'student.html', {'student': student})
        except Student.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

@login_required
def student_marks(request):
    if not request.user.is_student:
        return redirect('profile')
    
    student = Student.objects.get(user=request.user)
    exam_results = ExamResult.objects.filter(student=student).order_by('-date_taken')
    return render(request, 'student_marks.html', {'student': student, 'exam_results': exam_results})