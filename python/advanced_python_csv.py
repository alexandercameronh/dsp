emailList=tuple(emailList)

with open('emails.csv', 'w') as f:
    f_csv=csv.writer(f, delimiter='\n')
    f_csv.writerow(emailList)

   
