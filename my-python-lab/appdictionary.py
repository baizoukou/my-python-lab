## allow us to use key value pairs
## create a program that will convert digit to num
## inside dic need {}
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May" :  "May",
    "Jun" : "June",
    "Jul": "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec": "December",

}
## key value can be anything as long as they are unique

### access them from the dic
## refer the key and then its going to go in dict and print the value
print(monthConversions["Jun"])
## second method
print(monthConversions.get("Lum", "Not a valid key"))## get fct specify default value that we want to use


