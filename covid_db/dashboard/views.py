from django.shortcuts import render
from .models import Record

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import RecordSerializer


def index(request):
    records = Record.objects.all()
    return render(request, 'dashboard/index.html', context={'records': records})


@csrf_exempt
def record_list(request):
    """
    List all records.
    """
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def record_detail(request, pk):
    """
    Retrieve a record.
    """
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return JsonResponse(serializer.data)
