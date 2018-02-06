import taskflow.engines
from taskflow.patterns import linear_flow as lf
from taskflow import task

class call_jim(task.Task):
    def execute(self, jim_number, *args, **kwargs):
        print("Calling jim %s." % jim_number)

    def revert(self, jim_number, *args, **kwargs):
        print("Calling %s and apologizing." % jim_number)

class call_joe(task.Task):
    def execute(self, joe_number, *args, **kwargs):
        print("Calling joe %s." % joe_number)

    def revert(self, joe_number, *args, **kwargs):
        print("Calling %s and apologizing." % joe_number)

class call_suzzie(task.Task):
    def execute(self, suzzie_number, *args, **kwargs):
        raise IOError("Suzzie not home right now.")

flow = lf.Flow('Simple-linear').add(
    call_jim(),
    call_joe(),
    call_suzzie()
)

try:
    taskflow.engines.run(flow,
                         engine_conf = {'engine': 'serial'},
                         store = dict(joe_number=444,
                                      jim_number=555,
                                      suzzie_number=666))

except Exception as e:
    print("Flow failed: %s" %e)
