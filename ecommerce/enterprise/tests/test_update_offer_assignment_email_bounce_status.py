# encoding: utf-8
"""
Contains the tests for updating offer assignment email bounce status command.
"""

import mock
from django.core.management import call_command

from ecommerce.extensions.offer.constants import OFFER_ASSIGNED, OFFER_ASSIGNMENT_EMAIL_BOUNCED
from ecommerce.extensions.test.factories import OfferAssignmentFactory
from ecommerce.programs.custom import get_model
from ecommerce.tests.testcases import TestCase

OfferAssignment = get_model('offer', 'OfferAssignment')


class UpdateOfferAssignmentEmailBounceStatusTests(TestCase):
    """
    Tests the update offer assignment email bounce status command.
    """

    def setUp(self):
        """
        Setup the test data
        """
        super(UpdateOfferAssignmentEmailBounceStatusTests, self).setUp()
        for x in range(3):
            assignment = OfferAssignmentFactory(code='test-code{}'.format(x), user_email='test{}@example.com'.format(x))
            assignment.status = OFFER_ASSIGNED
            assignment.save()

    def test_bounce_status_update(self):
        with mock.patch(
                'ecommerce.enterprise.management.commands.update_offer_assignment_email_bounce_status.'
                'get_braze_client'
        ) as mock_get_braze_client:
            mock_get_braze_client.return_value = mock.Mock()
            call_command('update_offer_assignment_email_bounce_status')
            assert mock_get_braze_client.call_count == 1
            offer_assignments = OfferAssignment.objects.all()
            for assignment in offer_assignments:
                self.assertEqual(assignment.status, OFFER_ASSIGNMENT_EMAIL_BOUNCED)
