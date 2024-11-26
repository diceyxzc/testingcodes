#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define maximum lengths for strings
#define MAX_NAME_LENGTH 50
#define MAX_FLIGHT_CODE_LENGTH 10

// Seat struct inside Flight
typedef struct Seat {
    int seatNumber;
    int isBooked;
    struct Seat *next;
} Seat;

// Flight struct
typedef struct Flight {
    char flightCode[MAX_FLIGHT_CODE_LENGTH];
    char origin[MAX_NAME_LENGTH];
    char destination[MAX_NAME_LENGTH];
    char schedule[MAX_NAME_LENGTH];
    Seat *seats;  // Head of seat linked list
    struct Flight *next;
} Flight;

// Booking struct inside Passenger
typedef struct Booking {
    char flightCode[MAX_FLIGHT_CODE_LENGTH];
    int seatNumber;
    struct Booking *next;
} Booking;

// Passenger struct
typedef struct Passenger {
    char name[MAX_NAME_LENGTH];
    char contact[MAX_NAME_LENGTH];
    Booking *bookings;  // Head of booking linked list
    struct Passenger *next;
} Passenger;

// Define heads of linked lists
Flight *flights = NULL;
Passenger *passengers = NULL;

// Function Prototypes
void addFlight(char *flightCode, char *origin, char *destination, char *schedule, int seatCount);
void deleteFlight(char *flightCode);
void addPassenger(char *name, char *contact);
void deletePassenger(char *name);
void bookSeat(char *passengerName, char *flightCode);
void cancelBooking(char *passengerName, char *flightCode);
void trackSchedule();
void generateReports();

// Function to add a flight
void addFlight(char *flightCode, char *origin, char *destination, char *schedule, int seatCount) {
    Flight *newFlight = (Flight *)malloc(sizeof(Flight));
    strcpy(newFlight->flightCode, flightCode);
    strcpy(newFlight->origin, origin);
    strcpy(newFlight->destination, destination);
    strcpy(newFlight->schedule, schedule);

    // Initialize seats linked list
    newFlight->seats = NULL;
    for (int i = 0; i < seatCount; i++) {
        Seat *newSeat = (Seat *)malloc(sizeof(Seat));
        newSeat->seatNumber = i + 1;
        newSeat->isBooked = 0;
        newSeat->next = newFlight->seats;
        newFlight->seats = newSeat;
    }

    newFlight->next = flights;
    flights = newFlight;
}

// Function to delete a flight
void deleteFlight(char *flightCode) {
    Flight *current = flights, *previous = NULL;
    while (current != NULL && strcmp(current->flightCode, flightCode) != 0) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) return; // Flight not found

    if (previous == NULL)
        flights = current->next;
    else
        previous->next = current->next;

    // Free seats
    Seat *seat = current->seats;
    while (seat != NULL) {
        Seat *temp = seat;
        seat = seat->next;
        free(temp);
    }

    free(current);
}

// Function to add a passenger
void addPassenger(char *name, char *contact) {
    Passenger *newPassenger = (Passenger *)malloc(sizeof(Passenger));
    strcpy(newPassenger->name, name);
    strcpy(newPassenger->contact, contact);
    newPassenger->bookings = NULL;
    newPassenger->next = passengers;
    passengers = newPassenger;
}

// Function to delete a passenger
void deletePassenger(char *name) {
    Passenger *current = passengers, *previous = NULL;
    while (current != NULL && strcmp(current->name, name) != 0) {
        previous = current;
        current = current->next;
    }

    if (current == NULL) return; // Passenger not found

    if (previous == NULL)
        passengers = current->next;
    else
        previous->next = current->next;

    // Free bookings
    Booking *booking = current->bookings;
    while (booking != NULL) {
        Booking *temp = booking;
        booking = booking->next;
        free(temp);
    }

    free(current);
}

// Function to book a seat for a passenger
void bookSeat(char *passengerName, char *flightCode) {
    Passenger *passenger = passengers;
    while (passenger != NULL && strcmp(passenger->name, passengerName) != 0) {
        passenger = passenger->next;
    }
    if (passenger == NULL) return; // Passenger not found

    Flight *flight = flights;
    while (flight != NULL && strcmp(flight->flightCode, flightCode) != 0) {
        flight = flight->next;
    }
    if (flight == NULL) return; // Flight not found

    Seat *seat = flight->seats;
    while (seat != NULL && seat->isBooked) {
        seat = seat->next;
    }
    if (seat == NULL) return; // No available seats

    seat->isBooked = 1;

    Booking *newBooking = (Booking *)malloc(sizeof(Booking));
    strcpy(newBooking->flightCode, flightCode);
    newBooking->seatNumber = seat->seatNumber;
    newBooking->next = passenger->bookings;
    passenger->bookings = newBooking;
}

// Function to cancel a booking for a passenger
void cancelBooking(char *passengerName, char *flightCode) {
    Passenger *passenger = passengers;
    while (passenger != NULL && strcmp(passenger->name, passengerName) != 0) {
        passenger = passenger->next;
    }
    if (passenger == NULL) return; // Passenger not found

    Booking *booking = passenger->bookings, *prevBooking = NULL;
    while (booking != NULL && strcmp(booking->flightCode, flightCode) != 0) {
        prevBooking = booking;
        booking = booking->next;
    }
    if (booking == NULL) return; // Booking not found

    if (prevBooking == NULL)
        passenger->bookings = booking->next;
    else
        prevBooking->next = booking->next;

    Flight *flight = flights;
    while (flight != NULL && strcmp(flight->flightCode, flightCode) != 0) {
        flight = flight->next;
    }
    if (flight != NULL) {
        Seat *seat = flight->seats;
        while (seat != NULL) {
            if (seat->seatNumber == booking->seatNumber) {
                seat->isBooked = 0;
                break;
            }
            seat = seat->next;
        }
    }

    free(booking);
}

// Functions to track schedules and generate reports would be added similarly

int main() {
    // Example usage
    addFlight("FL123", "New York", "Los Angeles", "12:00", 100);
    addPassenger("John Doe", "123-456-7890");
    bookSeat("John Doe", "FL123");
    
    // Further operations can be called here...

    return 0;
}
