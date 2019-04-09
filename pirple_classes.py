# -----------------------------------------------------------------------------------
# HOMEWORK #9: CLASSES
# -----------------------------------------------------------------------------------
'''Create a class called Vehicle with
    methods that allow setting of make, model, year, and weight
    a needs_maintenance boolean that defaults to False, and
    trips_since_maintenance integer that defaults to 0
    a repair method that resets the trips_since_maintenance and needs_maintenance

Make a "Car" class that inherits from Vehicle. It should contain
    a method called drive that sets the state of a boolean is_driving to True
    a method called stop that sets the value of is_driving to False

Switching is_driving from True to False should increment the trips_since_maintenance
counter. When it exceeds 100, the needs_maintenance boolean should be set to True

Create 3 different cars and drive them all a different number of times. Then
print out their values for make, model, year, and weight, needs_maintenance,
and trips_since_maintenance

extra: Create a Plane class that inherits from Vehicle. Add methods
fly and land (similar to drive and stop), but different in one respect: Once the
needs_maintenance boolean gets set to True, any attempt at flight should be rejected
(return False), and an error message printed that the plane can't fly until repaired.
'''



class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = False
        self.trips_since_maintenance = 0

    def repair(self):
        self.needs_maintenance = False
        self.trips_since_maintenance = 0


class Car(Vehicle):
    def __init__(self, make, model, year, weight):
        super(Car, self).__init__(make, model, year, weight)
        self.is_driving = False

    def drive(self):
        self.is_driving = True
        self.trips_since_maintenance += 1

        if self.trips_since_maintenance > 100:
            self.needs_maintenance = True

    def stop(self):
        self.is_driving = False


italien_job = Car(make='Fiat', model='500', year=1957, weight=499)
herbie = Car(make='VW', model='Beetle', year=1963, weight=800)
enzos_ride = Car(make='BMC', model='Mini Cooper', year=1961, weight=686)

italien_job.drive()
italien_job.drive()
herbie.drive()
enzos_ride.drive()
italien_job.drive()
italien_job.drive()
enzos_ride.drive()


sentence = '{} is a {} {} built in {} weighing {}kg.\nIt was used {} times since its last maintenance and it is {} that it needs another.\n\n'

print(sentence.format('The Italian Job', italien_job.make, italien_job.model, italien_job.year, italien_job.weight, italien_job.trips_since_maintenance, str(italien_job.needs_maintenance).lower()))
print(sentence.format('Herbie', herbie.make, herbie.model, herbie.year, herbie.weight, herbie.trips_since_maintenance, str(herbie.needs_maintenance).lower()))
print(sentence.format('Enzo\'sride', enzos_ride.make, enzos_ride.model, enzos_ride.year, enzos_ride.weight, enzos_ride.trips_since_maintenance, str(enzos_ride.needs_maintenance).lower()))

enzos_ride.trips_since_maintenance = 100
enzos_ride.drive()

print(f'Enzo is a prolific driver and it is {str(enzos_ride.needs_maintenance).lower()} that his car needs maintenance.\n')


# ---------------------------------extra--------------------------------------------------


class Plane(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.is_flying = False


    def fly(self):
        if self.needs_maintenance:
            print('This plane cannot take off until repaired.')
        else:
            self.is_flying = True
            self.trips_since_maintenance += 1

    def land(self):
        self.is_flying = False


ankh_morpork = Plane('Airbus', 'A380-800', 2009, 361000)

print(sentence.format('The Ankh Morpork', ankh_morpork.make, ankh_morpork.model, ankh_morpork.year, ankh_morpork.weight, ankh_morpork.trips_since_maintenance, str(ankh_morpork.needs_maintenance).lower()))

ankh_morpork.fly()
print('It is flying:', ankh_morpork.is_flying)
ankh_morpork.land()
print('The Ankh is flying:', ankh_morpork.is_flying)
ankh_morpork.needs_maintenance = True
ankh_morpork.fly()
