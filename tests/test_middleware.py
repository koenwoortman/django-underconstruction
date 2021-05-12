from django.conf import settings
from unittest.mock import Mock, patch
from django.test import TestCase, RequestFactory
from django_underconstruction.middleware import UnderConstructionMiddleware

class MiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_response_called_when_not_under_construction(self):
        get_response_mock = Mock()
        middleware = UnderConstructionMiddleware(get_response_mock)

        request = self.factory.get('/')
        middleware(request)

        get_response_mock.assert_called_once_with(request)

    @patch('django_underconstruction.middleware.render')
    def test_render_construction_template_when_under_construction(self, render):
        settings.UNDER_CONSTRUCTION = True

        get_response_mock = Mock()
        middleware = UnderConstructionMiddleware(get_response_mock)

        request = self.factory.get('/')
        middleware(request)

        render.assert_called_once_with(request, 'django_underconstruction/construction.html')
        get_response_mock.assert_not_called()

    @patch('django_underconstruction.middleware.render')
    def test_under_construction_template_overridden(self, render):
        settings.UNDER_CONSTRUCTION = True
        settings.UNDER_CONSTRUCTION_TEMPLATE = 'test.html'

        get_response_mock = Mock()
        middleware = UnderConstructionMiddleware(get_response_mock)

        request = self.factory.get('/')
        middleware(request)

        render.assert_called_once_with(request, 'test.html')
        get_response_mock.assert_not_called()
