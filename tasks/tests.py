from rest_framework.test import APITestCase


class TaskAPITests(APITestCase):
    def test_crud_flow(self):
        r = self.client.post('/api/tasks/', {'title': 'Write report', 'priority': 'high'}, format='json')
        self.assertEqual(r.status_code, 201)
        pk = r.data['id']
        self.assertEqual(len(self.client.get('/api/tasks/').data), 1)
        self.assertEqual(self.client.patch(f'/api/tasks/{pk}/', {'completed': True}, format='json').data['completed'], True)
        self.assertEqual(self.client.put(f'/api/tasks/{pk}/', {'title': 'New title'}, format='json').status_code, 200)
        self.assertEqual(self.client.delete(f'/api/tasks/{pk}/').status_code, 204)
        self.assertEqual(self.client.get(f'/api/tasks/{pk}/').status_code, 404)

    def test_validation(self):
        self.assertEqual(self.client.post('/api/tasks/', {'title': 'ab'}, format='json').status_code, 400)

    def test_ui_page(self):
        self.assertEqual(self.client.get('/').status_code, 200)
