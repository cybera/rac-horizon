from django.utils.translation import ugettext_lazy as _

from horizon.workflows.base import MembershipAction
from horizon.workflows.base import Step


class UpdateMembersStep(Step):
    """A step that allows a user to add/remove members from a group.

    .. attribute:: show_roles

        Set to False to disable the display of the roles dropdown.

    .. attribute:: available_list_title

        The title used for the available list column.

    .. attribute:: members_list_title

        The title used for the members list column.

    .. attribute:: no_available_text

        The placeholder text used when the available list is empty.

    .. attribute:: no_members_text

        The placeholder text used when the members list is empty.

    """
    template_name = "horizon/common/_workflow_step_update_members.html"
    show_roles = True
    available_list_title = _("All available")
    members_list_title = _("Members")
    no_available_text = _("None available.")
    no_members_text = _("No members.")

    def get_member_field_name(self, role_id):
        if issubclass(self.action_class, MembershipAction):
            return self.action.get_member_field_name(role_id)
        else:
            return self.slug + "_role_" + role_id
