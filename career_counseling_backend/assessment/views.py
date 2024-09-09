from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, UserProfile
from .serializers import QuestionSerializer, UserProfileSerializer
from django.contrib.auth.models import User
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class GenerateTest(APIView):
    def get(self, request, test_type):
        subcategories = {
            'psychometric': ['o_score', 'c_score', 'e_score', 'a_score', 'n_score'],
            'aptitude': ['numerical'],
            'reasoning': ['verbal', 'logical']
        }
        if test_type not in subcategories:
            return Response({'error': 'Invalid test type'}, status=400)
        
        questions = {}
        for subcategory in subcategories[test_type]:
            questions[subcategory] = list(Question.objects.filter(category=test_type, subcategory=subcategory)[:5].values())

        return Response({'questions': questions})
    

class SubmitTest(APIView):
    def post(self, request):
        user = request.user
        responses = request.data.get('responses', {})
        user_profile = UserProfile.objects.get(user=user)
        
        # Calculate scores for each subcategory
        subcategory_scores = {}
        
        for subcategory, answers in responses.items():
            total_score = 0
            question_count = 0
            for question_id, selected_option in answers.items():
                question = Question.objects.get(question_id=question_id)
                if selected_option == question.correct_option:
                    # Assuming each correct option is worth 5 points
                    total_score += 5
                else:
                    # Option scoring could be implemented here
                    pass
                question_count += 1
            
            # Calculate average score
            if question_count > 0:
                average_score = total_score / question_count
                subcategory_scores[subcategory] = average_score
                setattr(user_profile, subcategory, average_score)
        
        # Save the updated profile
        user_profile.save()
        
        # You can trigger the ML model prediction here
        # For example: predict_career(user_profile)
        
        return Response({'message': 'Test submitted successfully', 'scores': subcategory_scores})

# Note: Implement the predict_career function as per your ML model
def predict_career(user_profile):
    features = [
        user_profile.o_score,
        user_profile.c_score,
        user_profile.e_score,
        user_profile.a_score,
        user_profile.n_score,
        user_profile.numerical_ability,
        user_profile.verbal_reasoning,
        user_profile.logical_reasoning
    ]
    # Call your ML model to predict career
    # Example:
    # return ml_model.predict(features)
    pass



