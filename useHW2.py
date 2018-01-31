#step 1 = import HW2 file
import HW2 as eq
#set score
print("Best possible health score: [1,1,1,1,1,1,1,1]")
print(eq.scoreHUI3(vision=1, hearing=1, speech=1, ambulation=1, dexterity=1, emotion=1, cognition=1, pain=1))
print("Hypothetical patient: [3,1,5,2,3,3,5,1]") #add in potenital scores to get a potential paitent.
print(eq.scoreHUI3(vision=3, hearing=1, speech=5, ambulation=2, dexterity=3, emotion=3, cognition=5, pain=1))#and make it print
