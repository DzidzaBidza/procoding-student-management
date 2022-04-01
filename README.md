# procoding-student-management

The application provides student management functionalities.

Runing the aplication opens a window with a drop-down menu and options for checking existing students or entering a new student.
By entering a student record number and after validation, a new window with information about the student opens (read from the JSON file `student_details.json`):
·	Name and surname
·	Index number
· Date of birth (extracted from JMBG)
· which course is enrolled (extracted from the student record number)
· Year of enrollment at the faculty (extracted from the student record number)
· Subjects enrolled in as well as grades
· Average grade

That window also contains three buttons: for saving data in .txt format, .zip format as well as to graphical display of grades. If such information already exists, it prints the appropriate message on the screen.


 
