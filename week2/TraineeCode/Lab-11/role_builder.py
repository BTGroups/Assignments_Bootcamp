from roles import Roles
class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        if role_id == Roles.DEVELOPER:
            return "Developer"
        elif role_id == Roles.TEST_ENGINEER:
            return "Test Engineer"
        elif role_id == Roles.SR_DEVELOPER:
            return "Senior Developer"
        elif role_id == Roles.DESIGNER:
            return "Designer"
        else:
            return "Undefined"
