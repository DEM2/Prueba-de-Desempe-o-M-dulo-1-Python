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
      
def upload(route):
   invalid_rows=0
   csv_upload=[]
   try:
      with open(route,'r', encoding='utf-8') as csvfile:
         result= csv.reader(csvfile)
         header= next(result)
         if(header!=['Id', 'Name','Age','Program', 'State']):
            print("The header of the CSV file does not contain what was expected ")
         else:
            for i, fila in enumerate(result, start=2):
               if len(fila)==5:
                   if not fila[0] or not fila[1] or not fila[2] or not fila[3] or not fila[4]:
                      invalid_rows+=1
                   else:
                      try:
                         register=dict(zip(header, fila))
                         register['Id']=int(register['Id'])
                         register['State']=bool(register['State'])
                         
                         csv_upload.append(register)
                      except ValueError: 
                         invalid_rows+=1
                         continue              
               else: invalid_rows+=1
      return csv_upload
   except FileNotFoundError:
      print("File not Found")