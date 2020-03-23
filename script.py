# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
#print(email_one)
def censor_word(email):
  censored_email = email.replace("learning algorithms" , "-"*len("learning algorithms"))
  return censored_email
#print(censor_word(email_one))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_word_list(email):
  censored_email = email
  for word in proprietary_terms:
    if proprietary_terms.index(word) == 0:
      censored_email = email.replace(word, "-"*len(word))
    else:
      censored_email = censored_email.replace(word, "-"*len(word))
  return censored_email

negative_words = ["concerned", "concerning" "behind",  "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "horrible", "horribly", "Horribly", "questionable"]

def censor_negative(email):
  not_negative_email = censor_word_list(email) 
  negative_count = 0
  for n_word in negative_words:
    if n_word in not_negative_email:
      negative_count += 1 
      print(negative_count)
      if negative_count > 1:
        #print(n_word)
        not_negative_email = not_negative_email.replace(n_word, "-"*len(n_word))    
  return not_negative_email

def censor_alot(email):
  censored_email = censor_negative(email)
  split_email = censored_email.split()
  for i in range(len(split_email) - 1):
    if i > 0 or i < (len(split_email) - 2):
      if split_email[i] == "---censord---" and split_email[i-1] != "---censord---":
        split_email[i - 1] = "---censord---"
        split_email[i + 1] = "---censord---"
    else:
      continue
  censored_email = " ".join(split_email)
  return censored_email

  
#print(email_four)  
#print(censor_word_list(email_two))
#print(censor_negative(email_three))
print(censor_alot(email_four))