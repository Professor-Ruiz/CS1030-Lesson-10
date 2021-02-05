import pytest
import src.exercise

inp_1 = ["Snickerdoodle Cupcake","Biscoff Lava","Pumpkin Chocolate Chip"]
out_1 = ['Biscoff Lava','Pumpkin Chocolate Chip','Snickerdoodle Cupcake']

inp_2 = ["Lemon Glaze","Confetti Cake","Reese's Peanut Butter Chip"]
out_2 = ["Confetti Cake","Lemon Glaze","Reese's Peanut Butter Chip"]

# run the test function for each input/output pair
@pytest.mark.parametrize("test_input, expected", [(inp_1, out_1), (inp_2, out_2)])
def test_capture_stdout(capsys, test_input, expected):

    # Load the test input for the program execution:
    def mock_input(s):
        return test_input.pop(0)
    src.exercise.input = mock_input
    
    # Execute the student program, and capture the output (print statements):
    src.exercise.main()
    out, err = capsys.readouterr()
    
    # Reformat program output as a list of strings.
    # Each line of output will be a list element, excluding blank newlines.
    out = out.strip().split('\n')
    out = [i for i in out if i]
    
    # Test the actual program output against the anticipated program output:
    assert out == expected
