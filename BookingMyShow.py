# HLD https://www.geeksforgeeks.org/design-bookmyshow-a-system-design-interview-question/

import datetime

class City:

    def __init__(self, name):
        self.name = name
        self.theatre_listed = []
    def add_theatre(self,theatre):
        self.theatre_listed.append(theatre)

class Movie:

    def __init__(self, title, duration, release_date):
        self.title = title
        self.duration = duration
        self.release_date = release_date
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

class Show:
    def __init__(self, start_time, seats):
        self.start_time = start_time
        self.available_seats = seats

    def book_seat(self, num_seats):

        if self.available_seats >= num_seats:
            self.available_seats -= num_seats
            return True
        else:
            return False
class Theatre:
    def __init__(self, city, name, capacity):
        self.city = city
        self.name = name
        self.capacity = capacity
        self.movies = []
        
    def add_movie(self, movie):
        self.movies.append(movie)

class PaymentGateway:
    def process_payment(self, ticket):
        return True

class Ticket:
    def __init__(self, user, show, num_seats):
        self.user = user
        self.show = show
        self.num_seats = num_seats
        self.booking_time = datetime.datetime.now()

class User:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def book_ticket(self,user, show, num_seats, payment_gateway):

        if show.book_seat(num_seats):
            ticket = Ticket(user, show, num_seats)
            if payment_gateway.process_payment(ticket):
                print("Tickets have been booked")
                return ticket
            else:
                raise "Payment Failed"
            
        else:
            show.available_seats += num_seats
            print("Not enough tickets available for this show.")
            return None
        
        
if __name__ == "__main__":
    city1 = City("City 1")
    theatre1 = Theatre("Theatre A", "Location X", 1000)
    movie1 = Movie("Movie 1", 120, datetime.datetime(2023, 11, 15, 14, 0))
    show1 = Show(datetime.datetime(2023, 11, 15, 14, 0), 100)

    city1.add_theatre(theatre1)
    theatre1.add_movie(movie1)
    movie1.add_show(show1)

    user1 = User("User 1", "user1@example.com", "123-456-7890")
    payment_gateway = PaymentGateway()
    ticket = user1.book_ticket(user1,show1, 2, payment_gateway)

    if ticket:
        print(f"Ticket booked for {user1.name} - {movie1.title}, Show Time: {show1.start_time}")
        print(f"Remaining seats for the show: {show1.available_seats}")
    else:
        print("Booking failed. Insufficient seats or payment issue.")