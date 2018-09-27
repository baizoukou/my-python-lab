## first thing to do is to access the file
## r = read
## w = write
## a = append
## r++ = read and write
##open(" name of file + extension", "r" | "w" | "a", "r+")
## writing and appending to files
## writing new file and appending to existing

##employee_file = open("employees.txt", "a" )
#check if file is readable
#print(employee_file.readable())
## loop trough all d employees and employefile arr
##for employee in employee_file.readlines():
##       print(employee)
##print(employee_file.readlines()[1])
##\n help to skyp to next line
employee_file = open("emploees1.txt", "w")
employee_file.write("\nJohn - Assistant Manager" )

employee_file.close()

## w overwrite a file
## in order to use it its better to create a new file





