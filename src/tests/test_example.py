from templatepackage.example import Example 

## Using Pytest "Simple" Version 
## Anything named "test_" will be run as a test 
## Assert is used to confirm things pass. 
## Failed tests determiend by assert triggering. 
def test_example_mirrors_input(): 
    e = Example(E=100)
    assert e.get() == 100

# Comment out and run to see test fail 
# def test_fail(): 
#     e = Example(E=100)
#     assert e.get() != 100

def test_example_default(): 
    e = Example()
    assert e.get() == Example.E_DEFAULT