from .signals import object_viewed_signal, object_lead_signal
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class ObjectViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except DoesNotExist:
            instance = None
        if instance is not None:
            object_viewed_signal.send(
                instance.__class__, instance=instance, request=request)
        return super(ObjectViewMixin, self).dispatch(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class ObjectLeadMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            instance = request.COOKIES
        except DoesNotExist:
            instance = None
        if instance is not None:
            object_lead_signal.send(
                instance.__class__, instance=instance, request=request)
        return super(ObjectLeadMixin, self).dispatch(request, *args, **kwargs)
