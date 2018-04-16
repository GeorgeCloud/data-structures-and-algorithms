from queue import Queue


class Dog:
    pass


class Cat:
    pass


cat, dog = Cat(), Dog()


class AnimalShelter:
    '''DOC STRINGS'''
    def __init__(self, iter=()):
        self.shelter = Queue(iter)
        self.empty = Queue()
        self.other = type(None)

    def enqueue(self, new_pet):
        if not isinstance(new_pet, (Dog, Cat)):
            raise TypeError('This shelter only accepts cats and dogs')
        self.shelter.enqueue(new_pet)

    def dequeue(self, preference=None):
        if preference is None:
            if self.empty:
                return self.emp.dequeue()
            return self.shelter.dequeue()
        if preference not in (Cat, Dog):
            raise ValueError('Shelter only contains cats and dogs.')
        if preference == self.other:
            return self.empty.dequeue()
        while True:
            head = self.shelter.dequeue()
            if isinstance(head, preference):
                return head
            self.empty.enqueue(head)
            self.other = type(head)
