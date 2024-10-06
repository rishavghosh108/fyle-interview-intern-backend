from flask import Blueprint
from core.apis import decorators
from core.models.assignments import Assignment
from .schema import AssignmentSchema,AssignmentGradeSchema
from core.apis.responses import APIResponse
from core import db

principal_assignments_resources = Blueprint("principal_assignments_resources",__name__)

@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_assignments(p):
    submitted_graded_assignments = Assignment.get_submitted_graded_assignment_by_principal()
    submitted_graded_assignments_dump = AssignmentSchema(many=True).dump(submitted_graded_assignments)
    return APIResponse.respond(data=submitted_graded_assignments_dump)

@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.authenticate_principal
@decorators.accept_payload
def regrade_assignment(incoming_payload,p):
    regrade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    regraded_assignment = Assignment.mark_grade(
        _id=regrade_assignment_payload.id,
        grade=regrade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(regraded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)