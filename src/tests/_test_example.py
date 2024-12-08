import pytest
from tests.mock import Mockable

## To run and experiment: 
## Start environment
## From src directory call: pytest tests/_test_example.py

class ExampleDependency(Mockable): 
    def bool_method(self, *args, **kwargs): 
        return True 
    
class ClassUnderTest(): 
    def __init__(self, e: ExampleDependency): 
        self.e = e
    
    def func1(self): 
        return self.e.bool_method()
    
    def func2(self): 
        return not self.e.bool_method()

@pytest.fixture
def input_value():
    """ Fixture Example: 
        This allows you do do something and then clean it up afterwards. 
        It doesn't require you to have 2 functions to do it and guarantees
        (apart from ctrl+c) that the cleanup will happen. 
    """
    print("\nFixture Prep... ")
    yield 5
    print("\nFixture Cleanup... ")

class TestExample:
    @classmethod
    def setup_class(cls):
        print("\nRun Once per Class at Setup...")
        cls.class_value = 10

    @classmethod
    def teardown_class(cls):
        print("\nRun Once per Class at Cleanup...")
        cls.class_value = None

    def setup_method(self, method):
        print("\nRun Once per Test as Setup...")
        self.cut_dependency = ExampleDependency()

    def teardown_method(self, method):
        print("\nRun Once per Test as Cleanup...")
        self.cut_dependency.check_mock_expectations()
        self.cut_dependency.mock_reset()


    def test_CUT_f1_ignore(self): 
        e = ClassUnderTest(self.cut_dependency)
        self.cut_dependency.bool_method.ignore_calls()
        assert e.func1()

    def test_CUT_f1_expect_one_call(self): 
        e = ClassUnderTest(self.cut_dependency)
        self.cut_dependency.bool_method.expect_call(True)
        assert e.func1()

    def test_CUT_f1_expect_one_call_false(self): 
        e = ClassUnderTest(self.cut_dependency)
        self.cut_dependency.bool_method.expect_call(False)
        assert not e.func1()