from django.shortcuts import render
import math

def index(request):
    return render(request, 'calculator/index.html')

def result(request):
    yes = int(request.POST['yes'])
    no = int(request.POST['no'])
    total = yes + no

    p_yes = yes / total
    p_no = no / total

    # Correct Gini Formula
    gini = 1 - (p_yes**2 + p_no**2)

    # Entropy Formula
    entropy = -(p_yes * math.log2(p_yes) + p_no * math.log2(p_no))

    context = {
        'gini': round(gini, 4),
        'entropy': round(entropy, 4)
    }
    return render(request, 'calculator/result.html', context)
