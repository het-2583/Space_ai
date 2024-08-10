from django.shortcuts import render
from .services.ai_service import ask_space_question

def space_ai_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = ask_space_question(question)
        return render(request, 'space_ai.html', {'question': question, 'answer': answer})
    return render(request, 'space_ai.html')
