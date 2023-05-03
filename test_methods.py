import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_area_triangulo(windth, height):
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.area_triangulo(width, height)
    
    # then the perimeter should be 10
    assert output == 10

def test_area_quadrado(windth):
    # given a width of 2 
    width = 2
  

    # when we calculate the perimeter
    output = methods.area_quadrado(width)
    
    # then the perimeter should be 4
    assert output == 4

def test_soma(valor1, valor2)
    #given a value1 of 5 and a value2 of 3
    valor1 = 5
    valor2 = 3


    #when we calculate the sum
    output = methods.soma(valor1, valor2)

    #then the result should be 8
    assert output = 8

def test_subtracao(v1, v2)
    #given a value1 of 5 and a value2 of 3
    v1 = 5
    v2 = 3


    #when we calculate the subtraction
    output = methods.subtracao(v1, v2)

    #then the result should be 2
    assert output = 2

def test_multiplicacao(v1, v2)
    #given a value1 of 5 and a value2 of 3
    v1 = 5
    v2 = 3


    #when we calculate the multiplication
    output = methods.multiplicacao(v1, v2)

    #then the result should be 15
    assert output = 15

def test_divisao(v1, v2)
    #given a value1 of 10 and a value2 of 2
    v1 = 10
    v2 = 2


    #when we calculate the division
    output = methods.divisao(v1, v2)

    #then the result should be 5
    assert output = 5  