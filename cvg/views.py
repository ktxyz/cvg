from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from projects.models import ProjectMeta, ProjectDetail
from informations.models import InformationMeta, InformationDetail
from jobs.models import JobMeta, JobDetail

class CVView(TemplateView):
    template_name = 'cv.html'

    def get_context_data(self, **kwargs):
        try:
            lang = self.request.session['lang']
        except:
            self.request.session['lang'] = 'en'
            lang = 'en'
        
        from django.utils import translation
        translation.activate(lang)
        
        context = super().get_context_data(**kwargs)

        info_meta = InformationMeta.objects.all().last()
        info = {
            'meta': info_meta,
            'detail': get_object_or_404(InformationDetail, meta=info_meta, trans_lang=lang)
        }
        context['info'] = info

        jobs = []
        metas = JobMeta.objects.all()
        for job in metas:
            jobs.append({
                'meta': job,
                'detail': get_object_or_404(JobDetail, job=job, trans_lang=lang)
            })
        context['jobs'] = jobs

        projects = []
        metas = ProjectMeta.objects.all()
        for meta in metas:
            projects.append({
                'meta': meta,
                'detail': get_object_or_404(ProjectDetail, project_meta=meta, trans_lang=lang)
            })
        
        context['projects'] = projects
        return context
    