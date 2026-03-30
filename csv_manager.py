import csv 

def save_csv(students, route):
   if not students: 
      print("No information has been saved")
      return
   try:
      with open(route,'w', newline='', encoding='utf-8') as csvfile:
         fieldnames=['Id', 'Name','Age','Program', 'State']
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
         writer.writeheader()
         writer.writerows(students)
      return f"\nThe students list stored in: {route}"

   except FileExistsError :
      print("The csv file could not be saved")