import os.path
import uuid

from django.core.files.storage import default_storage


from second.models import User


def get_profile_img_src(user, img_file):
    file_name, extension = os.path.split(img_file.name)
    newfilename= str(uuid.uuid4()) + extension #str(uuid.uuid4()) : uuid는 길이가 32byte인 하나의 uuid 객체이기 때문에 이를 파일 이름으로 사용하려면문자열로 변환해야 한다.
    filepath = os.path.join('img',user.username, newfilename)
    default_storage.save(filepath, img_file)
    profile_img_url = default_storage.url(filepath)
    return profile_img_url


def profile_update(user, img_file):
    edit_user = User.objects.get(username=user.username)
    edit_user.profile_img = img_file
    edit_user.save()
    return edit_user
