from .signals import object_viewed_signal, object_lead_signal


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


class ObjectLeadMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            instance = request.session
        except DoesNotExist:
            instance = None
        if instance is not None:
            object_lead_signal.send(
                instance.__class__, instance=instance, request=request)
        return super(ObjectLeadMixin, self).dispatch(request, *args, **kwargs)
