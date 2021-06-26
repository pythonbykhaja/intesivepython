import string
import textwrap
import difflib

if __name__ == '__main__':
    message = "quality thought has python course"
    print(string.capwords(message))
    sample_text = """
    The textwrap module provides some convenience functions, 
        as well as TextWrapper, 
    the class that does all the work. 

        If you’re just wrapping or filling one or two text strings, 
    the convenience functions should be good enough; 
    otherwise, you should use an instance of TextWrapper for efficiency.
    """
    print(textwrap.fill(sample_text, width=50))
    print(textwrap.dedent(sample_text))

    sample_text_2 = """
    The textwraps module provides some convenience functions, 
        as well as TextWrapper, 
    the class that does all the work. 

        If you’re just wrappings or filling one or two text strings, 
    the convenience functions should be good enough; 
    otherwises, you should use an instance of TextWrapper for efficiency.
    """
    differ = difflib.Differ()
    difference = differ.compare(sample_text.splitlines(), sample_text_2.splitlines())
    print("\n".join(difference))