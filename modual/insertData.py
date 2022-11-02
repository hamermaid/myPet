import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myPet.settings")

import django

django.setup()

from reviews.models import Clinic

# 진료항목 코드 입력
name = ['진료효과', '의사의 친절', '직원의 친절', '청결함']
for i in range(0, len(name)):
    cli_id = str(i + 1) + "4"
    # 코드 4자리 채우기
    id = cli_id.zfill(4)
    cli = Clinic(clinic_id=id, name=name[i])
    cli.save()