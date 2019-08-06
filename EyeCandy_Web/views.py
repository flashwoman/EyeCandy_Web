from django.shortcuts import render,redirect, get_object_or_404
from .models import Image
from django.conf import settings
import os
import io

def index(request):
    return render(request, 'EyeCandy_Web/index.html')

def analyse(request):
    rows = request.POST.get('how-many') # 책장 row 수
    origin = request.FILES.get('file')
    name = origin.name
    # print(origin.name)

    # 1.input 이미지 저장
    image = Image(name=name, origin=origin)
    image.save() #print(image.origin.name)

    # openCV
    param = f'{rows}+{name}+{image.pk}'  # 4 + test1.jpg + 5
    return redirect('CandyMaker:startmaker', param)


def result(request, image_pk):
    from .models import Image
    # 저장된 결과 이미지 가져오기
    image = Image.objects.get(pk=image_pk)

    output_path =f'/media/output/output_{image.name}'
    print(output_path)
    # 저장된 결과 이미지 result 컬럼에 저장
    image.result = output_path
    image.save()
    from .models import Image
    # 재확인 후 context 저장
    image = get_object_or_404(Image, pk=image_pk)
    context = {'image': image}
    return render(request, 'EyeCandy_Web/result.html', context)

def savetogallery(request, image_pk):
    image = Image.objects.get(pk=image_pk)
    image.to_gallery = True
    image.save()
    return render(request, 'EyeCandy_Web/gallery.html')

def gallery(request):
    # 갤러리로 보여줄 것들만 가져온다.
    images = Image.objects.filter(to_gallery = True)
    last = Image.objects.last()

    context= {'images':images, 'last':last }
    return render(request, 'EyeCandy_Web/gallery.html', context)



