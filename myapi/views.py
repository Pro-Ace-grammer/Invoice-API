from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *



@api_view(['GET','POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoice = Invoice.objects.all()
        serializers  = InvoiceSerializer(invoice, many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def edit_invoice(request,pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        invoice.delete()
        return Response('Deleted Successful', status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET','POST'])
def invoice_details_list(request):
    if request.method == 'GET':
        invoice_details = InvoiceDetails.objects.all()
        serializers  = InvoiceDetailsSerializer(invoice_details, many=True)
        return Response(serializers.data)
    if request.method == 'POST':
        serializer = InvoiceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT','DELETE'])
def edit_invoice_details(request,pk):

    try:
        invoice = InvoiceDetails.objects.get(pk=pk)
    except InvoiceDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = InvoiceDetailsSerializer(invoice)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = InvoiceDetailsSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        invoice.delete()
        return Response('Deleted Successful', status=status.HTTP_204_NO_CONTENT)