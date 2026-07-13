from core.workflow import WORKFLOW
from core.catalog import FIELDS


class Planner:

    def get_current_step(self, state):
        for step in WORKFLOW:
            if step["step"] == state.current_step:
                return step
        return None

    def get_missing_fields(self, state):
        step = self.get_current_step(state)

        missing = []

        for field in step["fields"]:
            if getattr(state, field, None) is None:
                missing.append(field)

        return missing

    def can_execute(self, state):
        return len(self.get_missing_fields(state)) == 0

    def next_step(self, state):
        step = self.get_current_step(state)
        return step["next"]