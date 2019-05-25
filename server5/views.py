from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pika
import datetime
import time

@csrf_exempt
def sendTime(request):
	credentials = pika.PlainCredentials('1506725003', '697670')
	connection = pika.BlockingConnection(pika.ConnectionParameters('152.118.148.103',5672,'1506725003', credentials))
	channel = connection.channel()
	exchange = '1506725003_fanout'
	channel.exchange_declare(exchange=exchange, exchange_type='fanout', passive=False, durable=False, auto_delete=False)

	while(True) :
		ts = datetime.datetime.today().strftime('%A, %d %B %Y, %H:%M:%S')
		print("Jam : " + ts)
		channel.basic_publish(exchange=exchange,
							  routing_key='waktuServer',
							  body="Jam : " + ts)
		time.sleep(1)
	connection.close()
	return JsonResponse({"status": "ok"})