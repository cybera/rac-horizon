from django.utils.translation import ugettext_lazy as _

from horizon.workflows.base import MembershipAction
from horizon.workflows.base import Step


class UpdateMembersStep(Step):
    template_name = "horizon/common/_workflow_step_update_members_cybera.html"
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
