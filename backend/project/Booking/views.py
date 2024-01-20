from django.shortcuts import render
import razorpay
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import HotelBooking
from django.db import transaction
from.serializers import HotelBookingSerializer
from hotels.models import Hotel
from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def hotel_booking(request):
    print(request.method)  

    if request.method == 'POST':
        print("hii")
        try:
            data = json.loads(request.body.decode('utf-8'))
            total_price = data.get('totalPrice')
            room_type = data.get('roomType')  # Include roomType in the request
            hotelId = data.get('hotelId')  # Include roomType in the request

            print(room_type,"roomtype")
            print(hotelId,"hotelid")

            print(total_price, "totalprice")

            razorpay_key = "rzp_test_4o90y50Nv7s1jR"
            razorpay_secret = "nlmYaIYmAyx29rc3BUZSmDRu"
            
            client = razorpay.Client(auth=(razorpay_key, razorpay_secret))

            order_amount = int(float(total_price) * 100)
            order_currency = "INR"
            order_receipt = "order_rcptid_11" 

            response = client.order.create(
                data={
                    'amount': order_amount,
                    'currency': order_currency,
                    'receipt': order_receipt,
                }
            )

            # Pass the order details to the frontend
            context = {
                "order_id": response["id"],
                "order_amount": order_amount,
                "order_currency": order_currency,
                "order_receipt": order_receipt,
                "razorpay_key": razorpay_key,  
            }
            return JsonResponse(context)
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({'status': 'failure', 'reason': str(e)})
    else:
        return JsonResponse({'status': 'failure', 'reason': 'Invalid request method'})

@csrf_exempt
def confirm_booking(request):
    print("entered")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data, 'data')
        razorpay_signature = data.get('razorpaySignature')
        print(razorpay_signature, 'signature')
        razorpay_payment_id = data.get('razorpayPaymentId')
        print(razorpay_payment_id, 'payment_id')    
        user_name = data.get('user', '')
        try:
            user = User.objects.get(email=user_name)
            print(user,'userrrrr')
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'failure', 'reason': 'User not found'})
        hotel_id = data.get('hotel', '')
        try:
            hotel = Hotel.objects.get(id=hotel_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'failure', 'reason': 'Hotel not found'})
        room_type=data.get('roomType', '')
        print(room_type,'roomtype')
        total_price=data.get('totalPrice', '')
        print(total_price,'totalprice')
        check_in_date=data.get('checkInDate', '')
        print(check_in_date,'checkint')
        check_out_date=data.get('checkOutDate', '')
        print(check_out_date,'checkout')
        is_main_guest=data.get('isMainGuest', False)
        print(is_main_guest,'gurst')
        guest_first_name=data.get('firstName', '')
        print(guest_first_name,'firstname')
        guest_last_name=data.get('lastName', '')
        print(guest_last_name)
        guest_email=data.get('email', ''),
        guest_phone=data.get('phone', ''),
        razorpay_order_id=data.get('razorpay_order_id', ''),
        razorpay_signature=razorpay_signature,
        razorpay_payment_id=razorpay_payment_id,

        try:
            razorpay_key = "rzp_test_4o90y50Nv7s1jR"
            razorpay_secret = "nlmYaIYmAyx29rc3BUZSmDRu"
            # Verify Razorpay signature
            client = razorpay.Client(api_key=razorpay_key, api_secret=razorpay_secret)
            params_dict = {
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            }
            print(params_dict,'dict')

            # client.utility.verify_payment_signature(params_dict)

            # Payment verification successful, create a booking entry
            # with transaction.atomic():
            booking =HotelBooking.objects.create(
                    user=user,
                    hotel=hotel,
                    room_type=data.get('roomType', ''),
                    total_price=data.get('totalPrice', ''),
                    check_in_date=data.get('checkInDate', ''),
                    check_out_date=data.get('checkOutDate', ''),
                    is_main_guest=data.get('isMainGuest', False),
                    guest_first_name=data.get('firstName', ''),
                    guest_last_name=data.get('lastName', ''),
                    guest_email=data.get('email', ''),
                    guest_phone=data.get('phone', ''),
                    razorpay_order_id=razorpay_payment_id,
                    
                )
            serializer=HotelBookingSerializer(data=booking)
            if serializer.is_valid():
                booking=serializer.save()

            return JsonResponse({'status': 'success', 'message': 'Booking confirmed successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'reason': str(e)})
    return JsonResponse({'status': 'failure', 'reason': 'Invalid request method'})


def cancel_booking(request, booking_id):
    print('enteredt to funct')
    try:
        booking = HotelBooking.objects.get(id=booking_id)
        booking.is_cancelled = True
        booking.save()
        return JsonResponse({'message': 'Booking cancelled successfully'}, status=200)
    except HotelBooking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)