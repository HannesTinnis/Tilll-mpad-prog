import os
class Pupil:
    
    def __init__(self, name: str, age: int, studying: str, school: str) -> None:
        
        self.name = name 
        self.age= age
        self.studying = studying
        self.school= school

    
    def __str__(self) -> str:
        
        return_string = f"{self.name} är {self.age} år gammal och pluggar {self.studying} på {self.school}"
        return return_string
    

    def greet (self) -> str:

        return (f"Hej jag heter {self.name} och jag är {self.age} år gammal, jag pluggar {self.studying} på {self.school}")
    


def main (): 
    simon = Pupil ("Simon", 18, "Teknik", "Drottning Blanka")
    filip = Pupil ("Filip", 18, "Teknik", "Drottning Blanka")
    leo = Pupil ("leo", 18, "Teknik", "Drottning Blanka")
    victor = Pupil ("Victor", 18, "Teknik", "Drottning Blanka")
    jag = Pupil ("Hannes", 18, "Teknik", "Drottning Blanka")



    persons = [simon, filip, leo, victor]
    
    os.system('cls')
    print(jag.greet())
    for person in persons:
        print (person)

if __name__ == "__main__":
    main()
    



        
    
