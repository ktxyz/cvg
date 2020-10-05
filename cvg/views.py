from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from projects.models import ProjectMeta, ProjectDetail


class CVView(TemplateView):
    template_name = 'cv.html'

    def get_context_data(self, **kwargs):
        lang = self.request.session['lang'] or 'en'
        context = super().get_context_data(**kwargs)

        projects = []
        metas = ProjectMeta.objects.all()
        for meta in metas:
            projects.append({
                'meta': meta,
                'detail': get_object_or_404(ProjectDetail, project_meta=meta, trans_lang=lang)
            })
        
        context['projects'] = projects
        return context
    