class Tests(object):
  def __init__(self):
    self.OKGREEN = '\033[92m'
    self.WARNING = '\033[93m'
    self.FAIL    = '\033[91m'
    self.ENDC    = '\033[0m'

  def print_with_color(self, text, color):
    print(f'{color}{text}{self.ENDC}')

  def assert_true(self, condition, error_message, successful_message=''):
    assert condition, error_message
    self.print_with_color(successful_message, self.OKGREEN)

  def assert_false(self, condition, error_message, successful_message=''):
    self.assert_true(not condition, error_message, successful_message)

  def warning(self, condition, error_message, successful_message=''):
    if condition:
      self.print_with_color(successful_message, self.OKGREEN)
    else:
      self.print_with_color(error_message, self.WARNING)

  def run_all_tests(self):
    for method in list(self.__class__.__dict__):
      if method.startswith('__') is False:
        getattr(self, method)()
