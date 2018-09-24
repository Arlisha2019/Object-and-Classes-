class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __repr__(self):
        return "Person %r, %r, %r " % (self.name, self.email, self.phone)

    def add_friend(self, friend):
        self.friends.append(jordan)

    def number_friends(self, friends):
        return jordan.number_friends()

    def greet(self, other_person):
        self.greeting_count += 1
        print("Hello %s, I am %s!" % (other_person.name, self.name))

    # def print_contact_info(self):
    #     print("Sonny's email: {0}, Sonny's phone number: {1} ".format(self.email, self.phone))

sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')

jordan = Person('Jordan','jordan@aol.com','495-586-3456')

sonny.greet(jordan)
#print(sonny.greeting_count)

#print(sonny.email)
#print(sonny.phone)

jordan.greet(sonny)
#print(jordan.greeting_count)

#print(jordan.name)
#print(jordan.email)
#print(jordan.phone)

#sonny.print_contact_info()

jordan.add_friend(sonny)
print(sonny, jordan)
#print(len(jordan.friends))

#jordan.friends.append(sonny)
#jordan.friends.append(sonny)

#sonny.friends.append(jordan)

#print(len(jordan.friends))
