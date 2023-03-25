from django.views import generic


class IndexView(generic.TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Empty Blog'
        return context


class AboutView(generic.TemplateView):

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context


class ContactsView(generic.TemplateView):

    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contacts'
        return context
