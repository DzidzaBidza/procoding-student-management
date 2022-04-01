# procoding-student-management

The application provides student management functionalities.

Runing the aplication opens a window with a drop-down menu and options for checking existing students or entering a new student.

![main window](https://user-images.githubusercontent.com/91345686/161242177-20a7faf7-b9ad-43a6-88e7-87bbb41d7cd8.png)

## Information extraction

By entering a student record number and after validation, a new window with information about the student opens (read from the JSON file `student_details.json`):
 - Name and surname 
 - Index number
 - Date of birth (extracted from JMBG)
 - Which course is enrolled (extracted from the student record number)
 - Year of enrollment at the faculty (extracted from the student record number)
 - Subjects enrolled in as well as grades
 - Average grade

![info](https://user-images.githubusercontent.com/91345686/161242449-6241a4f7-8435-4006-a761-5b2f065d83a5.png)

That window also contains three buttons: for saving data in `.txt` format, `.zip` format as well as to graphical display of grades. If such information already exists, it prints the appropriate message on the screen.

## New enrollment

By clicking on the drop-down menu "Upis novog studenta" a new window opens and allows you to enter the necessary data for new students to be enrolled. Information about the new student is written to the existing JSON `student_details.json` file.

![new_enrroling](https://user-images.githubusercontent.com/91345686/161244426-4bcbce48-bc14-4214-89fe-d269972a6760.png)




 
