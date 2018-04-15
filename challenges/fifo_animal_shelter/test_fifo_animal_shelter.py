import pytest
from fifo_animal_shelter import AnimalShelter, Dog, Cat

# Cat & dog instance
cat, dog = Cat(), Dog()

# animal_queue = AnimalShelter([cat, dog, dog, dog, cat, dog, cat])


def test_fifo_animal_dequeue_no_preference():
    """
    Dequeue an animal from queue of animals dequeue preference.
    Returns a random pet. Checks for all objects in random order.
    """
    animal_queue = AnimalShelter([cat, dog, dog, dog, cat, dog, cat])

    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    assert isinstance(animal_queue.dequeue(), (Dog, Cat)) is True
    with pytest.raises(AttributeError):
        animal_queue.dequeue()


def test_fifo_animal_dog_person():
    animal_queue = AnimalShelter([dog, dog, cat, dog, dog, dog])
    assert isinstance(animal_queue.dequeue(Dog), Dog)


def test_fifo_animal_cat_person():
    animal_queue = AnimalShelter([cat, cat, dog, cat, cat, cat])
    assert isinstance(animal_queue.dequeue(Cat), Cat) is True
