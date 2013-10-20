from electionsguess.model import election_data,candidate_data

def result(place):
  result=[]
  a = election_data.objects.get(consti_name = place)
  b = candidate_data.objects.all()
  
  for c in b.party:
  sum=0
    if c == a.last_winner:
      sum=.3
    if c == a.pre_winner:
      sum=sum+.1
    if b.cast_support == a.major_caste:
      sum=sum+.6
    else:
      sum=sum+.2
    sum=sum/2
    result.append({ c." has ".sum*100." chance of winning"})
  return result  
   
      
