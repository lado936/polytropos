from dataclasses import dataclass
import os


@dataclass
class TaskPathLocator:
    scenario: str

    @property
    def base_dir(self):
        return os.path.abspath(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                '../../../',
            )
        )

    @property
    def scenario_dir(self):
        return os.path.join(self.base_dir, 'fixtures', self.scenario)

    @property
    def conf_dir(self):
        return os.path.join(self.scenario_dir, 'conf')

    @property
    def data_dir(self):
        return os.path.join(self.scenario_dir, 'data')

    @property
    def tasks_dir(self):
        return os.path.join(self.conf_dir, 'tasks')

    @property
    def changes_dir(self):
        return os.path.join(self.conf_dir, 'changes')

    @property
    def changes_import(self):
        return os.path.relpath(
            self.changes_dir, self.base_dir
        ).replace('/', '.')

    @property
    def schemas_dir(self):
        return os.path.join(self.conf_dir, 'schemas')

    @property
    def lookups_dir(self):
        return os.path.join(self.data_dir, 'lookups')

    @property
    def entities_dir(self):
        return os.path.join(self.data_dir, 'entities')
