from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Course
from .forms import CourseModelForm
# BASE VIEW class => View

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    
    def get(self, request, *args, **kwargs):
        # initialise empty form
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

class CourseView(View):
    template_name = 'courses/course_detail.html'

    # method names relate to HTTP verbs
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)
