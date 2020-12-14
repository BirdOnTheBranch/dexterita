import json

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Questions


class QuestionsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_questions = Questions.object.create(
            {
                "text": "",
                "fecha": {
                    "mes": "Juny",
                    "year": "2020",
                    "modelo": "1"
                },
                "responses": [
                    {"text": "answer one"},
                    {"text": "answer two"},
                    {"text": "answer three", "correct": "true"}
                ]
            }
        )

    def test_create_questions(self):
        """test status and method post"""

        response = self.client.post(
            '/data-center/api/v1.0/data-center/',
            self.test_question,
            format='json'
        )

        result = json.loads(response.content)
        self.assertIn('code', result)
        self.assertIn('adress', result)
        self.assertEqual(result, self.test_questions)

    def test_update_questions(self):
        """test status and method put"""

        question = self.test_questions

        test_update = {
            "text": "",
            "fecha": {
                "mes": "January",
                "year": "3021",
                "modelo": "3"
            },
            "responses": [
                {"text": "tomatoes"},
                {"text": "carrots"},
                {"text": "lemon", "correct": "true"}
            ]
        }

        response = self.client.put(
            f'/data-center/api/v1.0/data-center/{question.id}/',
            test_update,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, test_update)

    def test_delete_questions(self):
        """test no content and method delete"""

        question = self.test_questions

        response = self.client.delete(
            f'/data-center/api/v1.0/data-center/{question.pk}/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        questions_exists = Questions.objects.filter(pk=question.pk)
        self.assertFalse(questions_exists)

    def test_get_questions(self):
        """test status and method get in api"""

        Questions.object.create(
            {
                "text": "",
                "fecha": {
                    "mes": "Juny",
                    "year": "2020",
                    "modelo": "1"
                },
                "responses": [
                    {"text": "answer one"},
                    {"text": "answer two"},
                    {"text": "answer three", "correct": "true"}
                ]
            }
        )

        Questions.object.create(
            {
                "text": "",
                "fecha": {
                    "mes": "Juny",
                    "year": "2020",
                    "modelo": "2"
                },
                "responses": [
                    {"text": "answer four"},
                    {"text": "answer five"},
                    {"text": "answer six", "correct": "true"}
                ]
            }
        )

        response = self.client.get('/data-center/api/v1.0/data-center/')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        questions = Questions.objects.all()
        self.assertEqual(2, len(questions))

        for center in result:
            self.assertIn('id', center)
            self.assertIn('code', center)
            self.assertIn('adress', center)
            break
