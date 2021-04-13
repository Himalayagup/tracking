from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView)
from accounts.models import Publisher
from campaign.models import CampaignToPublisher, Campaign
from analytics.models import ObjectLead, ObjectViewed
from .forms import CampaignToPublisherForm, ApplyCampaignFormCreate, CampaignToPublisherCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import owner_required, publisher_required, manager_or_owner_required
from analytics.mixins import ObjectLeadMixin
from .filters import CampaignStatuFilter
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from analytics.utils import get_client_ip
# Create your views here.


class HomePage(TemplateView):
    template_name = 'publisher/index.html'


# For setting up cookies

# class CampaignToPublisherDetail(ObjectViewMixin, DetailView):
#     model = CampaignToPublisher
#
    # def render_to_response(self, context, **response_kwargs):
    #     response = super(CampaignToPublisherDetail, self).render_to_response(
    #         context, **response_kwargs)
    #     publisher = self.object.user
    #     campaign = self.object.campaign
    #
    #     response.set_cookie("publisher", publisher)
    #     response.set_cookie("campaign", campaign)
    #     return response

# For setting up sessions

# class CampaignToPublisherDetail(ObjectViewMixin, DetailView):
#     model = CampaignToPublisher
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(CampaignToPublisherDetail,
#                         self).get_context_data(*args, **kwargs)
#         self.request.session['publisher'] = self.object.user.company_name
#         self.request.session['campaign'] = self.object.campaign.campaign_name
#         return context

# For setting up cookies and sessions both


# Publisher applying for campaigns
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(xframe_options_exempt, name='dispatch')
class ReadingSession(ObjectLeadMixin, TemplateView):
    template_name = 'session.html'

    def get(self, request, *args, **kwargs):
        print("YAYAYAY")
        try:
            ip_address = get_client_ip(request)
        except:
            pass
        new_lead_instance = ObjectLead.objects.create(
            campaign=self.request.COOKIES['campaign1'],
            campaign_id=self.request.COOKIES['campaign_id1'],
            publisher=self.request.COOKIES['publisher1'],
            publisher_id=self.request.COOKIES['publisher_id1'],
            ip_address=ip_address,
        )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.keys():
            context['publisher'] = self.request.session['publisher']
            context['publisher_id'] = self.request.session['publisher_id']
            context['campaign'] = self.request.session['campaign']
            context['campaign_id'] = self.request.session['campaign_id']

        if 'publisher1' in self.request.COOKIES and 'publisher_id1' in self.request.COOKIES and 'campaign1' in self.request.COOKIES and 'campaign_id1' in self.request.COOKIES:
            context['publisher1'] = self.request.COOKIES['publisher1']
            context['publisher_id1'] = self.request.COOKIES['publisher_id1']
            context['campaign1'] = self.request.COOKIES['campaign1']
            context['campaign_id1'] = self.request.COOKIES['campaign_id1']
        # print(context)
        return context


@ login_required
@ publisher_required(login_url='../../accounts/not_allowed')
def publisher_register(request):
    user = request.user

    if user.is_authenticated:
        if request.method == 'POST':
            publisher_form = CampaignToPublisherForm(data=request.POST)

            if publisher_form.is_valid():
                # this is the trick.
                instance = publisher_form.save(commit=False)
                instance.user = request.user.Publisher_User
                instance.save()  # to commit the new info
                return HttpResponseRedirect('/')
            else:
                print(publisher_form.errors)
    else:
        return HttpResponseRedirect('/publisher')
    form = CampaignToPublisherForm()
    context = {'form': form}
    return render(request, 'publisher/campaigntopublisher_form.html', context)


# To apply campaign by using url and passing parameters to it
@ method_decorator([login_required, publisher_required(login_url='../../accounts/not_allowed')], name='dispatch')
class ApplyForCampaign(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("campaignlist")

    def get(self, request, *args, **kwargs):
        campaign = get_object_or_404(
            Campaign, campaign_key=self.kwargs.get("campaign_key"))

        try:
            CampaignToPublisher.objects.create(
                user=self.request.user.Publisher_User, campaign=campaign)

        except IntegrityError:
            messages.warning(
                self.request, ("Warning, already a applied of {}".format(campaign.campaign_name)))

        else:
            messages.success(self.request, "You have applied for the campaign.".format(
                campaign.campaign_name))

        return super().get(request, *args, **kwargs)


@ method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherList(ListView):
    # specify the model for list view
    template_name = 'publisher/campaigntopublisher_list.html'
    model = CampaignToPublisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CampaignStatuFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


# to only show campaigns running by individual publishers
@ method_decorator([login_required, publisher_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherIndividaulList(ListView):
    # specify the model for list view
    model = CampaignToPublisher
    template_name = 'publisher/campaigntopublisher_list1.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user.Publisher_User)

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CampaignToPublisherIndividaulList,
    #                     self).get_context_data(*args, **kwargs)
    #
    #     context['publisher'] = CampaignToPublisher.objects.filter(
    #         user=self.request.user.Publisher_User)
    #
    #     return context


@ method_decorator([login_required], name='dispatch')
class CampaignDataDetail(DetailView):
    model = Campaign
    template_name = 'publisher/publisher_campaign_detail.html'

    def get_context_data(self, *args, **kwargs):
        val_filter1 = Q(
            try_new__campaign=self.get_object().campaign_key)
        val_filter2 = Q(
            try_new__user=self.request.user.Publisher_User
        )
        self.object = self.get_object()
        context = super(CampaignDataDetail,
                        self).get_context_data(*args, **kwargs)
        context['lead'] = ObjectLead.objects.filter(
            campaign=self.get_object().campaign_name, publisher=self.request.user.Publisher_User.company_name)
        context['click'] = ObjectViewed.objects.filter(
            val_filter1).filter(val_filter2)
        return context


@ method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = CampaignToPublisher
    template_name = 'publisher/campaigntopublisher_update_form.html'

    # specify the fields
    fields = [
        "status_cam",
        "pixel"
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/publisher/runningcamp"


@ method_decorator([login_required, publisher_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherPixelAddView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = CampaignToPublisher
    template_name = 'publisher/campaigntopublisher_add_pixel_form.html'

    # specify the fields
    fields = [
        "pixel"
    ]

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = "/publisher/individual"


@ method_decorator([login_required, owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherDeleteView(DeleteView):
    # specify the model you want to use
    template_name = "publisher/campaigntopublisher_confirm_delete.html"
    model = CampaignToPublisher

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/publisher/runningcamp"


class PublisherList(ListView):
    template_name = "publisher/publisher_list.html"
    model = Publisher

# ////////////////////////////////////////


@ method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class PublisherDetail(DetailView):
    model = Publisher
    template_name = "publisher/publisher_detail.html"

    def get_context_data(self, *args, **kwargs):
        self.object = self.get_object()
        context = super(PublisherDetail,
                        self).get_context_data(**kwargs)
        context['campaigns'] = CampaignToPublisher.objects.filter(
            user=self.get_object().user_name.Publisher_User)
        return context

# ////////////////////////////////////////


@ method_decorator([login_required, manager_or_owner_required(login_url='../../accounts/not_allowed')], name='dispatch')
class CampaignToPublisherCreate(CreateView):
    model = CampaignToPublisher
    template_name = "publisher/campaigntopublishermanual_form.html"
    fields = ["user",
              "campaign",
              ]

    success_url = "/publisher/runningcamp"
