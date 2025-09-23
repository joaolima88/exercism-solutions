"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = "ABCD"
    ind = 0

    for _ in range(number):
        yield letters[ind]
        ind += 1
        if ind == 4:
            ind = 0
    
def generate_numbers(number):

    counter = 0
    seat = 1
    for _ in range(number):
        
        if seat == 13:
            seat += 1

        yield seat
        counter += 1

        if counter == 4:
            counter = 0
            seat += 1

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    letters = generate_seat_letters(number)
    numbers = generate_numbers(number)
    for letter, number in zip(letters, numbers):
        yield f"{number}{letter}"

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return dict(zip(passengers, generate_seats(len(passengers))))


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for i in seat_numbers:
        yield i + flight_id + ((12 - len(i + flight_id)) * "0")
