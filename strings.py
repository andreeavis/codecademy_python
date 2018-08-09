
# # def substring_between_letters(word, start, end):
# #   for index in word:
# #     if start, end in word:
# #       index[start]

# # print(substring_between_letters("apple", "p", "e"))

# plays = {'Purple Haze': 1, 
# 'Like a Rolling Stone': 78, 
# 'Satisfaction': 29, 
# 'Respect': 89, 
# "What's Going On": 21, 
# 'Imagine': 44, 
# 'Good Vibrations': 5}

# # new_dict = {}
# # new_dict[plays['Respect']] = {}
# # print(new_dict)

# # newDict = {key: playsValue, key :{}}

# new_dict = {"The Best Songs": plays, "Sunday Feelings": {}}
# print(new_dict)


# letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# zipped_lists = zip(letters, points)
# # print(list(zipped_lists))
# # list(zipped_lists) = [('A', 1), ('B', 3), ('C', 3), ('D', 2), ('E', 1), ('F', 4), ('G', 2), ('H', 4), ('I', 1), ('J', 8), ('K', 5), ('L', 1), ('M', 3), ('N', 4), ('O', 1), ('P', 3), ('Q', 10), ('R', 1), ('S', 1), ('T', 1), ('U', 1), ('V', 4), ('W', 4), ('X', 8), ('Y', 4), ('Z', 10)]
# print("<>" * 10)

# letter_to_points = {key: value for key, value in zipped_lists}
# print(letter_to_points)

# letter_to_points[" "] = 0

# def score_word(word):
#   point_total = 0
#   for letter in word:
#     point_total += letter_to_points.get(letter, 0)
#   return point_total

# print("<>" * 10)
# print(score_word("CAR"))

# brownie_points = score_word("BROWNIE")
# print(brownie_points)

# print("<>" * 10)
# player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
# print(player_to_words)

# print("<>" * 10)
# player_to_points = {}

# for player, words in player_to_words.items():
#   player_points = 0
#   for word in words:
#     player_points += score_word(word)
#   player_to_points[player] = player_points
  
# print(player_to_points)

# class Circle:
#   pi = 3.14
#   def __init__(self, diameter):
#   	self.diameter = diameter
#   	print(f"Creating circle with diameter {self.diameter}")


# circle = Circle(36)
# # print(circle)


# class Circle:
#   pi = 3.14
  
#   def __init__(self, diameter):
#     print("Creating circle with diameter {d}".format(d=diameter))
#     # Add assignment for self.radius here:
    
#     self.radius = diameter / 2
#   def circumference(self):
#     return 2 * self.pi * self.radius
    
# medium_pizza = Circle(12)
# teaching_table = Circle(36)
# round_room = Circle(11460)

# print(medium_pizza.circumference())
# print(teaching_table.circumference())
# print(round_room.circumference())


# class Employee():
#   def __init__(self, name):
#     self.name = name


#   # def __repr__(self):
#   #   return self.name

# argus = Employee("Argus Filch")
# print(argus)
# prints "Argus Filch"
  
	
# class Student:
# 	def __init__(self, name, year):
# 	  self.name = name
# 	  self.year = year
    

# roger = Student('Roger van der Weyden', 10)
# sandro = Student('Sandro Botticelli', 12)
# pieter = Student('Pieter Bruegel', 8)
  
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
      
  def __repr__(self):
    return "{name} is a students in class {year}.".format(name=self.name, year=self.year)

# class Grade:
#   minimum_passing = 65
  
#   def __init__(self, score):
#     self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
# pieter.add_grade(Grade(100))

print(roger)
print(sandro)
print(pieter)



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  