from random import sample

class SortError(Exception):
    pass

class User(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.authorized = False

    def login(self, usr, psswrd):
        usersfile = open("app/users.txt")

        if (usr + ' ' + psswrd) in usersfile.readlines():
            self.authorized = True
            self.username = usr
            self.password = psswrd
        # Denies access if previously logged in
        # (for first login would be necessary)
        else:
            self.authorized = False

        usersfile.close()

class Classe(object):

    def __init__(self):
        # Classname
        self.name = None
        # List of surnames (imported from the file and to be sorted)
        self.surnames = []
        # List of Student() istances
        self.members = {}
        self.average = None

    # Acquires data from file (referred to by the string classe)
    def getdata(self, classe):
        # 1st part: acquires classname, surnames list and does some
        # preliminary editing (strips chars, sorts in alph. order)
        # (New inizialization of istance due to use of function extend)
        self.__init__()
        self.name = classe
        surfilename = self.name + ".txt"
        membersfile = open(surfilename)
        # Appends list of lines (returned from readlines)
        self.surnames.extend(membersfile.readlines())

        # (Strips '\n' substring)
        for surname_index in range(0, len(self.surnames)):
            self.surnames[surname_index] = self.surnames[surname_index].replace(
                                                                       '\n', '')
        # (Double checks alphabetical order)
        self.surnames.sort()
        membersfile.close()

        # 2nd part: initialize Student() istances (and members list)
        for surname in self.surnames:
             self.members[surname] = Student(surname)

        # 3rd part: downloads all previous marks from a saved file
        # Defines a standard filename for marks
        marksfilename = self.name + "marks" + ".txt"
        marksfile = open(marksfilename)
        # (The marks file stores "examplesurname", float_example_mark lines)
        # Only marked students are included
        # First off, creates a list of the lines of the mark file
        lines = marksfile.readlines()
        # (Strips '\n' substring)
        for line_index in range(0, len(lines)):
            lines[line_index] = lines[line_index].replace('\n', '')
        # Assigns marks in members
        for line in lines:
            # Split surnames and marks by ','
            splitline = line.split(',')
            # (Mark assignment)
            self.members[splitline[0]].mark = splitline[1]
            # (Test boolean assignment)
            self.members[splitline[0]].tested = True
        marksfile.close()

    def randomsort(self):
        #First off, checks there are students to test
        alltested = True
        for surname in self.surnames:

            if not(self.members[surname].tested):
                alltested = False

        if alltested:
            raise SortError
        else:
            sortedsurname = sample(self.surnames, 1)[0]
            # sortedstudent has to be found among non tested students
            while self.members[sortedsurname].tested:
                sortedsurname = sample(self.surnames, 1)[0]
            # Returns sortedsurname for server.py to use
            return sortedsurname

    def assignmark(self, surname, mark):
        # 1st part: Assigns mark to student istance in class istance
        self.members[surname].mark = mark
        self.members[surname].tested = True
        # 2nd part: Stores information in marks file
        # Defines a standard filename for marks
        marksfilename = self.name + "marks" + ".txt"
        marksfile = open(marksfilename, 'a')
        # (The marks file stores "examplesurname", float_example_mark lines)
        # Only marked students are included
        # Adds line in marks file
        marksfile.write(f"{surname},{mark}\n")
        marksfile.close()

class Student(object):

    def __init__(self, surname):
        self.surname = surname
        # Student hasn't got a mark yet
        self.mark = None
        # Student has not taken the test yet
        self.tested = False
