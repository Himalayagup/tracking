import uuid

from analytics.models import UniqueID


def get_uni_id():
    global uni_id
    uni_id = uuid.uuid4()
    is_not_unique = UniqueID.objects.filter(uniqueid=uni_id)
    if is_not_unique:
        get_uni_id()
    else:
        UniqueID.objects.create(uniqueid=uni_id)
        uni_id = str(uni_id)
    return uni_id
