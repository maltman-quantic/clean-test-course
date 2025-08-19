from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

def test_LittleItems():
  #Arrange
  # TODO: Arrange the items to run the test
  order = MockSet()
  order.add(MockModel(quantity=3))
  order.add(MockModel(quantity=1))
  delivery_distance = 2
  #Act
  # TODO: Call the function that will be tested
  cost = Delivery.calculate(order, delivery_distance) 
  #Assert
  # TODO: replace the pass with an assert to test the value returned.
  #pass  <-- no longer needed
  assert cost == 2.50
