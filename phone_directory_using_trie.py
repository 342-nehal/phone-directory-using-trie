class TrieNode:

  def __init__(self): 
    self.children={}
    self.endOfWord = False
    self.contact=None

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None: 
    cur = self.root

    for c in word:
      if c not in cur.children: 
        cur.children[c] = TrieNode()
      cur = cur.children[c]
    cur.endOfWord = True

  def search(self, word: str) -> bool:
    cur = self.root
    string=""
    for c in word:
      if c not in cur.children:
        return False
      string=string+c
      cur = cur.children[c]
    if cur.endOfWord==True:
      print(string,"FOUND :>")
    return cur.endOfWord
    
  def startsWith(self, prefix: str) -> bool: 
    cur = self.root
    string=""
    for c in prefix:
      if c not in cur.children:
        return False
      string=string+c
      cur = cur.children[c]
    def printAllMatches(prefix,current):
      if current.endOfWord==True:
        print("found",prefix)
      for s in current.children:
        printAllMatches(prefix+s,current.children[s])
      return
      
    printAllMatches(string,cur)
    return True
  def deletecontact(self,contact:str)->None:
    cur=self.root
    for c in contact:
        if c in cur.children:
            if len(cur.children)==1:
                del cur.children[c]
                return
            cur=cur.children[c]
    cur.endOfWord=False
        
obj=Trie()
continued=True
print("Welcome to phone directory application!!!")
directory={}
while True:
  print('''Press:
  1:To create a new contact
  2:To update an existing contact
  3:To search for a contact
  4:To delete a contact''')
  n=int(input())
  if n==1:
    print("Give the name of contact to store")
    name=input()
    print("give the phone number/s")
    phone=[int(x) for x in input().split(" ")]
    directory[name]=phone
    obj.insert(name)
  if n==2:
    print("Give the name of person whose phone number is to be updated")
    name=input()
    if obj.search(name):
      print("give the new phone number/s")
      phone=[int(x) for x in input().split(" ")]
      directory[name]=phone
    else:
      print("contact to be updated is not found, you may insert it as a new contact")
  if n==3:
    print("give the contact you want to search for")
    full=""
    while True:
      n=input()
      full=full+n
      if obj.startsWith(full)== False:
        print("NOT FOUND :<")
        break
      print("do you want to type some more letters?")
      confirm=input()
      if confirm in ["yes","y","Y","ya"]:
        continue
      if confirm in ["no","n","N","No"]:
        if obj.search(full) == True:
          print("PHONE NUMBER : ",end=" ")
          print(directory[full])
        elif obj.search(full) != True:
          print("contact not found")
        break

      

      
  if n==4:
    print("give the name of contact to be deleted")
    delete=input()
    if delete in directory:
      del directory[delete]
      obj.deletecontact(delete)
      print("contact deleted successfully")
    else:
      print("contact to be deleted is not found, may have been already deleted by you")
    


  print("Do you want to continue using the application?? If yes then write -> Y/y/Yes/yes")
  again = input()
  if not (again == 'Y' or again == 'Yes' or again == 'y' or again == 'yes'):
    break
print("Thanks for using the application :> ")



