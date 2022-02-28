class Student:
    """
    This class represents Student
    """
    # what is self & why we need self
    def enter_extra_details(self, key, value):
        """
        This method allows us to enter extra details
        """
        print(key, value)


class PrimarySchoolStudent(Student):
    pass

class HighSchoolStudent(Student):
    pass

if __name__ == "__main__":
    hstd = HighSchoolStudent()
    pstd = PrimarySchoolStudent()

    hstd.enter_extra_details(1,2)
    pstd.enter_extra_details(1,2)
    object