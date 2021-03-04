from django.shortcuts import render,redirect
from user.models import UserRecord, ContactUs, userProfile
from management.models import employee,crop,seedsModel,pesticidesModel
from django.contrib import messages
from management.forms import EmployeeForm,CropForm,SeedsForm,PesticidesFrom

# Create your views here.
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def home(request):
    return render(request, 'management/base.html')

def manage(request):
    if request.POST.get("Approve"):
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Approve"))
        ToHandle.update(status="approved")
        

    elif request.POST.get("Reject"):  
        ToHandle=UserRecord.objects.filter(recordId=request.POST.get("Reject"))
        ToHandle.update(status="rejected")
     
    
    
    
    recordsPending = UserRecord.objects.filter(status="pending")
    recordsRejected = UserRecord.objects.filter(status="rejected")
    recordsApproved = UserRecord.objects.filter(status="approved")
    Allrecords = {'recordsPending': recordsPending,'recordsRejected':recordsRejected,'recordsApproved':recordsApproved}
    return render(request, 'management/manage.html',Allrecords)

def cropRecord(request):
    cropRecord = crop.objects.all()

    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/crop/')
    else:
        form = CropForm()
    dict = {'form': form,'cropRecord':cropRecord}
    return render(request, 'management/crop.html', dict)

def seeds(request):
    return render(request, 'management/base.html')

def finance(request):
    return render(request, 'management/base.html')

def employeeRecords(request):
    employeeRecord = employee.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/employee/')
    else:
        form = EmployeeForm()
    dict = {'form': form, 'employeeRecord': employeeRecord}
    return render(request, 'management/employee.html', dict)

def employeeProfile(request,id):
    employeeId = employee.objects.filter(employee_id=id)
    return render(request,'management/employeeProfile.html',{'emid':employeeId[0]})


def cropAllDetails(request,id):
    crop_id = crop.objects.filter(crop_id=id)
    seedsRecord = seedsModel.objects.filter(crop_name=crop_id[0].cropName)
    pesticidesRecord = pesticidesModel.objects.filter(crop_name=crop_id[0].cropName)

    if request.method == 'POST':
        form = SeedsForm(request.POST, request.FILES)
        if form.is_valid():
            seedsCrop = form.save(commit=False)
            seedsCrop.crop_name = crop_id[0].cropName
            form.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/crop/'+str(id))
    else:
        form = SeedsForm()

    if request.method == 'POST':
        form1 = PesticidesFrom(request.POST, request.FILES)
        if form1.is_valid():
            seedsCrop = form1.save(commit=False)
            seedsCrop.crop_name = crop_id[0].cropName
            form1.save()
            messages.info(request, 'You have added new record successfully.')
            return redirect('/management/crop/' + str(id))
    else:
        form1 = PesticidesFrom()

        dict = {'form1':form1,'form':form,'cropId':crop_id[0],'seedsRecord':seedsRecord,'pesticidesRecord':pesticidesRecord}
    return render(request,'management/cropAllDetails.html',dict)
