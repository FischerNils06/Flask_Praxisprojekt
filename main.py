from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def start_page():
    return 'Welcome to the start page!'

# Eine pure function, die das gleiche Ergebnis für die gleichen Eingaben liefert
def pure_add_numbers(x, y):
    return x + y

# Eine Prozedur, die eine globale Variable ändert
total = 0

def procedural_add_numbers(x, y):
    global total
    total += x + y

@app.route('/a1g')
def a1g_endpoint():
    result_pure = pure_add_numbers(3, 4)
    procedural_add_numbers(3, 4)
    return f'Result of pure_add_numbers: {result_pure}, Total after procedural_add_numbers: {total}'

immutable_values = (1, 2, 3, 4, 5)

@app.route('/a1f')
def a1f_endpoint():
    # Versuch, die immutable Werte zu ändern, führt zu einem Fehler
    try:
        immutable_values[0] = 10  # Dies wird einen Fehler auslösen
    except TypeError as e:
        return jsonify({"error": str(e)})

    return jsonify({"immutable_values": immutable_values})

# Objektorientierte Klasse
class CalculatorOO:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        return self.x + y

# Funktionale Funktion
def add_functional(x, y):
    return x + y

total = 0

def add_to_total(x):
    global total
    total += x

add_to_total(5)
add_to_total(3)

@app.route('/a1e')
def a1e_calculator_endpoint():
    # Objektorientiert
    oo_calculator = CalculatorOO(3)
    oo_result = oo_calculator.add(5)

    # Funktional
    functional_result = add_functional(3, 5)

    # Prozedural
    procedural_result = total

    comparison = {
        "OO Result": oo_result,
        "Functional Result": functional_result,
        "Procedural Result": procedural_result
    }

    return jsonify(comparison)

@app.route('/b1g')
def b1g_endpoint():
    def bubble_pass(unsorted_list):
        if len(unsorted_list) <= 1:
            return unsorted_list
        if unsorted_list[0] > unsorted_list[1]:
            return [unsorted_list[1]] + bubble_pass([unsorted_list[0]] + unsorted_list[2:])
        return [unsorted_list[0]] + bubble_pass(unsorted_list[1:])

    def bubblesort(unsorted_list, n=None):
        if n is None:
            n = len(unsorted_list)
        if n == 1:
            return unsorted_list
        unsorted_list = bubble_pass(unsorted_list)
        return bubblesort(unsorted_list, n - 1)

    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubblesort(unsorted_list)

    print("Sortierte Liste:")
    print(sorted_list)

    return jsonify({"unsorted_list": unsorted_list, "sorted_list": sorted_list})

@app.route('/b1f')
def b1f_endpoint():
    # Funktion zur Überprüfung, ob eine Zahl gerade ist
    is_even = lambda x: x % 2 == 0

    # Funktion zur Berechnung der Summe aller geraden Zahlen von 1 bis n
    sum_even_numbers = lambda n: sum(filter(is_even, range(1, n + 1)))

    # Beispielaufruf
    n = 10
    result = sum_even_numbers(n)
    print("Die Summe aller geraden Zahlen von 1 bis", n, "ist:", result)

    return jsonify({"result": result})


@app.route('/b1e')
def b1e_endpoint():
    def calculate_sum(numbers):
        total = 0
        for num in numbers:
            total += num
        return total

    def calculate_average(numbers):
        total = calculate_sum(numbers)
        average = total / len(numbers)
        return average

    # Liste von Zahlen
    numbers = [10, 20, 30, 40, 50]

    # Gesamtergebnis und Durchschnitt berechnen
    total_result = calculate_sum(numbers)
    average_result = calculate_average(numbers)

    return {"total_result": total_result, "average_result": average_result}


def greet(name):
    return f"Hello, {name}!"

# Funktion in einer Variable speichern
my_function = greet


@app.route('/b2g', methods=['GET'])
def b2g_endpoint():
    name = "Alice"  # Hier könnten Sie den Namen dynamisch aus einer Anfrage erhalten
    result = my_function(name)

    return f"Result: {result}"


@app.route('/b2f')
def b2f_endpoint():
    # Funktion zur Demonstration der Behandlung von Funktionen als Objekte
    def manipulate_functions(func, *args):
        result = func(*args)
        return result

    # Beispiel: Funktion, die die Summe von Zahlen berechnet
    def sum_numbers(numbers):
        total = sum(numbers)
        return total

    # Beispiel: Funktion, die das Produkt von Zahlen berechnet
    def multiply_numbers(numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    numbers = [1, 2, 3, 4, 5]

    # Funktionen als Argumente verwenden
    sum_result = manipulate_functions(sum_numbers, numbers)
    multiply_result = manipulate_functions(multiply_numbers, numbers)

    return jsonify({"sum_result": sum_result, "multiply_result": multiply_result})


@app.route('/b2e')
def b2e_endpoint():
    # Funktion zur Erstellung einer Closure-Funktion
    def create_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier

    # Closure-Funktionen erstellen
    double = create_multiplier(2)
    triple = create_multiplier(3)

    # Anwendung von Closure-Funktionen
    result_double = double(5)
    result_triple = triple(5)

    return jsonify({"result_double": result_double, "result_triple": result_triple})



square = lambda x: x**2

@app.route('/b3g')
def b3g_endpoint():
    num = 5  # Beispielzahl
    result = square(num)
    return f'Das Quadrat von {num} ist {result}'


multiply = lambda x, y: x * y

@app.route('/b3f')
def b3f_endpoint():
    num1 = 3  # Beispielzahl 1
    num2 = 7  # Beispielzahl 2
    result = multiply(num1, num2)
    return f'Das Produkt von {num1} und {num2} ist {result}'


sort_by_length = lambda x: sorted(x, key=lambda item: len(item))

@app.route('/b3e')
def b3e_endpoint():
    strings = ["Apfel", "Banane", "Kirsche", "Erdbeere", "Orange"]
    sorted_strings = sort_by_length(strings)
    return f'Sortierte Liste: {sorted_strings}'





if __name__ == '__main__':
    app.run()