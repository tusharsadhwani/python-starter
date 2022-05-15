from {{cookiecutter.project_name}} import test_function


def function_test() -> None:
    """Tests test_function from the package"""
    output = test_function()
    assert output == "This is a test"
