def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_publisher(request):
    publisher_name = request.session['publisher']
    return publisher_name


def get_publisher_id(request):
    publisher_id = request.session['publisher_id']
    return publisher_id


def get_campaign(request):
    campaign_name = request.session['campaign']
    return campaign_name


def get_campaign_id(request):
    campaign_id = request.session['campaign_id']
    return campaign_id
