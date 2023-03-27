from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    data = {'hello': 'Hello'}
    return Response(data)


@api_view(['GET'])
def imperial(request, lbs, inch):
    bmi = 703 * float(lbs) / (float(inch)**2)
    return Response({'bmi': bmi})


@api_view(['GET'])
def metric(request, kg, meters):
    bmi = float(kg)/(float(meters)**2)
    return Response({'bmi': bmi})


@api_view(['GET'])
def metric_all(request, metric_system, weight, hight):
    if metric_system == 'metric':
        bmi = weight/hight**2
    elif metric_system == 'imperial':
        bmi = 703*weight/hight**2
    else:
        data = {'error': f'{metric_system}: no such metric system'}
        return Response(data, status.HTTP_400_BAD_REQUEST)

    data = {'bmi': bmi}
    return Response(data)
