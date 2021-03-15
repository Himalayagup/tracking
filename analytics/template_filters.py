for click_i in data_ne:
    var_filter3 = Q(
        try_new__user=click_i.pk)
    click_data = ObjectViewed.objects.all().filter(
        val_filter1).filter(var_filter3).count()
    context['click_data'] = (dict_click.items())
