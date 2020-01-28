from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'homepage.html'
    school_name = 'Sahayamatha School'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school_name'] = self.school_name
        return context
