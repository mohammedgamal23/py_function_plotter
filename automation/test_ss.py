from numpy import True_
import function_plotter
import pytest

@pytest.fixture
def app():
   testerApp = function_plotter.App()
   return testerApp


@pytest.mark.parametrize("value, valid",
 [('x^2*y', True),('y+23', True),
 ('3*x%3', True), ('x^2 - x&2', True),
 ( '13*x^4 - 31*x + 25', False), ('', True), 
 ('12*x+42', False), ('4*x^2 - 2*x / 4', False),
 ('z^2 +5*x +4*x^2', True),
])
def test_equation_after_click(app, value, valid):
   event, values = app.window.read()
   app.event == 'Plot'
   app.values['-FUNCTION-']=(value)
   assert (app.FUNCTION_NOT_VALID_FLAG) == valid
   #something wrong i don't get it