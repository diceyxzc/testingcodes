#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define MAX_BUFFER_SIZE 200
#define FILENAME_SIZE 1024
#define MAX_LINE 2048
#define TEMP_FILENAME "temp____.txt"
#define FILENAME "flightInformation.txt"

// Flight Related Functions

void displayFlightRecords();
void flightInput();
int flightModifier();
int deleteFlightRecords();
int updateFlightRecords();

// Flight Reports Functions

int flightStatus();
void displayFlightReport();
int addFlightReport();

// Passenger Related Functions

int displayPassengerRecords();
int passengerInput();

// Misc.

int mainMenu();
void clearScreen();

int main() {

	mainMenu();
    return 0;
}

int mainMenu() {
    char response[10];
	
    clearScreen();
    while (1) {
        printf("|========================================|\n");
        printf("|----CALVIN'S AIRLINE MANAGING SYSTEM----|\n");
        printf("|========================================|\n");
        printf("|---------------MAIN MENU----------------|\n");
        printf("| 1. FLIGHT RECORDS                      |\n"); //done
        printf("| 2. PASSENGER RECORDS                   |\n"); //done
        printf("| 3. FLIGHT CREATION                     |\n"); //done
        printf("| 4. PASSENGER INFO CREATION             |\n"); //done
        printf("| 5. FLIGHT MODIFIER                     |\n"); //last
        printf("| 6. FLIGHT STATUS AND REPORTS           |\n"); //done
        printf("| 0. EXIT                                |\n");
        printf("|----------------------------------------|\n");
        printf("Enter Subcategory (0-7): ");
        
        fgets(response, sizeof(response), stdin);
        response[strcspn(response, "\n")] = 0; 

    if (strcmp(response, "0") == 0) {
            printf("Exiting the system.\n");
            break;
        } else if (strcmp(response, "1") == 0) {
            displayFlightRecords();
        } else if (strcmp(response, "2") == 0) {
            displayPassengerRecords();
        } else if (strcmp(response, "3") == 0) {
            flightInput();
        } else if (strcmp(response, "4") == 0) {
            passengerInput();
        } else if (strcmp(response, "5") == 0) {
            flightModifier();
        } else if (strcmp(response, "6") == 0) {
            flightStatus();
        } else {
            clearScreen();
            printf("| Invalid option! Please Try Again       |\n");
        }
    }
}

void displayFlightRecords() {
    FILE *fptr;
    char response[10];
    char line[256]; 

    fptr = fopen("flightInformation.txt", "r"); 
    if (fptr == NULL) {
        printf("Error! Unable to open file.\n");
        return;
    }

    clearScreen();
    printf("|=======================================|\n");
    printf("|=============FLIGHT RECORDS============|\n");
    printf("=========================================\n");
    while (fgets(line, sizeof(line), fptr)) { 
        printf("%s", line); 
    }
    fclose(fptr); 

    while (1){
        printf("=========================================\n");
        printf("| Press 1 to Return to Main Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                clearScreen();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
}

int displayPassengerRecords() {
    FILE *fptr;
    char buffer[MAX_BUFFER_SIZE];
    char response[10];
    
    fptr = fopen("passengerInformation.txt", "r");
	if (fptr == NULL) {
		printf("Error! Unable to open file for reading.\n");
		return 1;
	}

    clearScreen();
    printf("=========================");
	printf("\n| Passenger Information |\n");
	printf("=========================\n");
	while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
		printf("%s", buffer);
	}

    while (1){
        printf("| Press 1 to Return to Main Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                clearScreen();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
	return 0;
}

void flightInput() {
	FILE *fptr;
    char response[10];

	fptr = fopen("flightInformation.txt", "a");
	if (fptr == NULL) {
		printf("Error! Unable to open file.\n");
	} else{
    
    char input[50];
	int seatAvailability;
	
	// Flight Number
    
        clearScreen();
        printf("|========================================|\n");
        printf("|-------------FLGIHT CREATION------------|\n");
        printf("==========================================\n");
        fprintf(fptr, "| Flight Number: ");
        printf("| Flight Number: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);

    // Flight Availability

        fprintf(fptr, "\t\t| Flight Availability: ");
        while (1) {
            printf("| Flight Availability (Y or N): ");
            fgets(input, sizeof(input), stdin);
            input[strcspn(input, "\n")] = '\0';

            if (strcasecmp(input, "Y") == 0 || strcasecmp(input, "N") == 0) {
                fprintf(fptr, "%s", input);
                break;
            } else {
                printf("--Invalid input! Please enter 'Y' for Yes or 'N' for No--\n");
            }
        }

    // Seat Availability

        fprintf(fptr, "\t| Seat Availability: ");
        while (1) {
            printf("| Number of Seats Available: ");
            if (scanf("%d", &seatAvailability) == 1) {
                fprintf(fptr, "%d", seatAvailability);
                break;
            } else {
                printf("--Invalid input! Please enter an integer--\n");
                while (getchar() != '\n');
            }
        }
        while (getchar() != '\n');

    // Destination

        fprintf(fptr, "\t\t| Flight Destination: ");
        printf("| Flight Destination: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);

    // Schedule of Flight

        fprintf(fptr, "\t\t| Date of Flight: ");
        printf("| Date of Flight: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);
        
    // Time of Flight

        fprintf(fptr, "\t\t| Time of Flight: ");
        printf("| Time of Flight: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);

    // Arrival of Flight

        fprintf(fptr, "\t| Arrival: ");
        printf("| Arrival of Flight: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);

        fprintf(fptr, "\n");

        fclose(fptr);
    }
    while (1){
        printf("==========================================\n");
        printf("| Press 1 to Return to Main Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                clearScreen();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
}

int passengerInput() {
	FILE *fptr, *fptrflightInfo;
	char buffer[MAX_BUFFER_SIZE];
	char file_content[100][MAX_BUFFER_SIZE];
    char line[256]; 
    char input[50];
	char response[10];
    int seatAvailability;
    int numPassengers;
    int flightNumber;

	fptr = fopen("passengerInformation.txt", "a");
	if (fptr == NULL) {
		printf("Error! Unable to open passengerInformation.txt for writing.\n");
		return 1;
	}

	fptrflightInfo = fopen("flightInformation.txt", "r");
	if (fptrflightInfo == NULL) {
		printf("Error! Unable to open flightInformation.txt for writing.\n");
		fclose(fptr);
		return 1;
	}
	
    clearScreen();
    printf("|=======================================|\n");
    printf("|=============FLIGHT RECORDS============|\n");
    printf("=========================================\n");
    while (fgets(line, sizeof(line), fptrflightInfo)) { 
        printf("%s", line); 
    }
    printf("=========================================\n");

    printf("| Select Flight Number: ");
    scanf("%d", &flightNumber);

	printf("| Number of Passengers: ");
	scanf("%d", &numPassengers);
	getchar();

    clearScreen();
    printf("=========Flight %d==========\n", flightNumber);
    printf("| Total Passengers: %d     \n", numPassengers);
    printf("===========================\n", flightNumber);
    
    fprintf(fptr, "|=======Flight %d=======|\n", flightNumber);
    fprintf(fptr, "| Total Passengers: %d  |", numPassengers);
    fprintf(fptr, "\n========================\n");

	for (int i = 0; i < numPassengers; i++) {
		fprintf(fptr, "--Passenger %d--\n", i + 1);

		printf("| Details for Passenger %d |\n", i + 1);

		// Passenger Name

		fprintf(fptr, "Name: ");
		printf("Passenger Name: ");
		fgets(input, sizeof(input), stdin);
		input[strcspn(input, "\n")] = '\0';
		fprintf(fptr, "%s", input);

		// Passenger Class

		fprintf(fptr, "\nPassenger Class: ");
		printf("Passenger Class: ");
		fgets(input, sizeof(input), stdin);
		input[strcspn(input, "\n")] = '\0';
		fprintf(fptr, "%s", input);
        
        // Passenger ID Number

		fprintf(fptr, "\nSeat Number: ");
		printf("Passenger Seat Number: ");
		fgets(input, sizeof(input), stdin);
		input[strcspn(input, "\n")] = '\0';
		fprintf(fptr, "%s", input);

		// Passenger Booking

		fprintf(fptr, "\nBooking: ");
		while (1) {
			printf("Passenger Booking (Y or N): ");
			fgets(input, sizeof(input), stdin);
			input[strcspn(input, "\n")] = '\0';

			if (strcasecmp(input, "Y") == 0 || strcasecmp(input, "N") == 0) {
				fprintf(fptr, "%s", input);
                fprintf(fptr, "\n========================\n");
				break;
			} else {
				printf("Invalid input! Please enter 'Y' for Yes or 'N' for No.\n");
			}
		}
	}
	fclose(fptr);

	fptr = fopen("passengerInformation.txt", "r");
	if (fptr == NULL) {
		printf("Error! Unable to open file for reading.\n");
		return 1;
	}

    clearScreen();
    printf("=========================");
	printf("\n| Passenger Information |\n");
	printf("=========================\n");
	while (fgets(buffer, sizeof(buffer), fptr) != NULL) {
		printf("%s", buffer);
	}
	
    while (1){
        printf("| Press 1 to Return to Main Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                clearScreen();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
	return 0;
}

int flightStatus() {
    FILE *fptr;
    
    fptr = fopen("flightrecords.txt", "a");
	if (fptr == NULL) {
		printf("Error! Unable to open flightrecords.txt for writing.\n");
		return 1;
	} else{
        char input[200];
        char response[10];

        clearScreen();
        while (1){
            printf("|========================================|\n");
            printf("|=============FLIGHT RECORDS=============|\n");
            printf("|========================================|\n");
            printf("| 1. DISPLAY FLIGHT RECRODS              |\n");
            printf("| 2. ADD FLIGHT RECORDS                  |\n");
            printf("| 0. EXIT                                |\n");
            printf("Enter Category: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

        if (strcmp(response, "0") == 0) {
                clearScreen();
                break;
            } else if (strcmp(response, "1") == 0) {
                displayFlightReport();
            } else if (strcmp(response, "2") == 0) {
                addFlightReport();
            } else {
                clearScreen();
                printf("| Invalid option! Please Try Again       |\n");
            }
        }
    }
}

void displayFlightReport() {
    FILE *fptr;
    char response[10];
    char line[256]; 

    fptr = fopen("flightrecords.txt", "r"); 
    if (fptr == NULL) {
        printf("Error! Unable to open file.\n");
        return;
    }

    clearScreen();
    printf("|=======================================|\n");
    printf("|=============FLIGHT REPORTS============|\n");
    printf("=========================================\n");
    while (fgets(line, sizeof(line), fptr)) { 
        printf("%s", line); 
    }
    fclose(fptr); 

    while (1){
        printf("=========================================\n");
        printf("| Press 1 to Return to Main Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                clearScreen();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
}

int addFlightReport() {
    FILE *fptr;
    fptr = fopen("flightrecords.txt", "a"); 
    if (fptr == NULL) {
        printf("Error! Unable to open file.\n");
        return 1;
    } else {

        char input[200];
        int flightNumber;

        clearScreen();
        printf("|========================================|\n");
        printf("|--------------FLGIHT RECORD-------------|\n");
        printf("==========================================\n");
        
        FILE *fptrInfo;
        char response[10];
        char line[256]; 

        fptrInfo = fopen("flightInformation.txt", "r"); 
        if (fptrInfo == NULL) {
            printf("Error! Unable to open file.\n");
            return 1;
        }

        clearScreen();
        printf("|=======================================|\n");
        printf("|=============FLIGHT RECORDS============|\n");
        printf("=========================================\n");
        while (fgets(line, sizeof(line), fptrInfo)) { 
            printf("%s", line); 
        }
        fclose(fptrInfo);

        printf("=========================================");
        fprintf(fptr, "--Flight Number: ");
        printf("\n| Flight Number: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s--", input);
        fprintf(fptr, "\n============================");
        fprintf(fptr, "\n");

        clearScreen();
        printf("Adding Record to Flight %s \n", input);
        printf("====================================\n");

        // Flight Status

        fprintf(fptr, "| Flight Status: ");
        printf("| Flight Status: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);
        fprintf(fptr, "\n");

        // Flight Report

        fprintf(fptr, "| Flight Report: ");
        printf("| Flight Report: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        fprintf(fptr, "%s", input);
        fprintf(fptr, "\n");

        // Time of Report
        time_t rawtime;
        struct tm * timeinfo;
        time ( &rawtime );
        timeinfo = localtime ( &rawtime );
        fprintf(fptr, "| Time of Report: %s",  asctime (timeinfo));
        fprintf(fptr, "____________________________");
        fprintf(fptr, "\n");

        fclose(fptr);
    }
    while (1){
        char response[10];
        printf("| Press 1 to Return to Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                flightStatus();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
}

int flightModifier() {
    char response[10];

    while (1) {
        clearScreen();
        printf("|========================================|\n");
        printf("|=============FLIGHT RECORDS=============|\n");
        printf("|========================================|\n");
        printf("| 1. DELETE FLIGHT RECORDS               |\n");
        printf("| 2. UPDATE FLIGHT RECORDS               |\n");
        printf("| 0. EXIT                                |\n");
        printf("Enter Category (0-2): ");

        fgets(response, sizeof(response), stdin);
        response[strcspn(response, "\n")] = 0;

        if (strcmp(response, "0") == 0) {
            clearScreen();
            break;
        } else if (strcmp(response, "1") == 0) {
            deleteFlightRecords();
        } else if (strcmp(response, "2") == 0) {
            updateFlightRecords();
            break;
        } else {
            printf("| Invalid option! Please Try Again       |\n");
        }
    }
    return 0; 
}

int deleteFlightRecords() {
    FILE *file, *temp;
    char buffer[MAX_LINE];
    int delete_line = 0;
    int current_line = 1;
    bool line_found = false;

    file = fopen(FILENAME, "r");
    if (file == NULL) {
        printf("Error! Unable to open %s for reading.\n", FILENAME);
        return 1;
    }

    clearScreen();
    printf("|=======================================|\n");
    printf("|=============FLIGHT RECORDS============|\n");
    printf("|=======================================|\n");
    while (fgets(buffer, sizeof(buffer), file)) {
        printf("%d. %s", current_line++, buffer); 
    }
    fclose(file);

    printf("=========================================\n");
    printf("Select Flight Number to Delete: ");
    if (scanf("%d", &delete_line) != 1 || delete_line < 1) {
        printf("Invalid input. Please enter a valid line number.\n");
        while (getchar() != '\n'); 
        return 1;
    }
    while (getchar() != '\n'); 

    file = fopen(FILENAME, "r");
    temp = fopen(TEMP_FILENAME, "w");
    if (file == NULL || temp == NULL) {
        printf("Error opening files for processing.\n");
        return 1;
    }

    current_line = 1;
    while (fgets(buffer, sizeof(buffer), file)) {
        if (current_line == delete_line) {
            line_found = true;
        } else {
            fputs(buffer, temp);
        }
        current_line++;
    }

    fclose(file);
    fclose(temp);

    if (!line_found) {
        printf("Line %d does not exist in the file.\n", delete_line);
        remove(TEMP_FILENAME); 
        return 1;
    }

    remove(FILENAME);
    rename(TEMP_FILENAME, FILENAME);

    clearScreen();

    file = fopen(FILENAME, "r");
    if (file == NULL) {
        printf("Error! Unable to open %s for reading.\n", FILENAME);
        return 1;
    }
    printf("|=======================================|\n");
    printf("|=========UPDATED FLIGHT RECORDS========|\n");
    printf("=========================================\n");
    while (fgets(buffer, sizeof(buffer), file)) {
        printf("%s", buffer);
    }
    fclose(file);

    printf("=========================================\n");
    printf("| Flight %d Record Deleted Successfully!  |\n", delete_line);
    printf("=========================================\n");
    printf("| Press 1 to Return to Menu: ");
    while (getchar() != '1'); 

    clearScreen();
    return 0;
}

int updateFlightRecords() {
    FILE *file, *temp;
    char filename[] = "flightInformation.txt";
    char temp_filename[FILENAME_SIZE];
    char buffer[MAX_LINE];
    char input[MAX_LINE];
    char replace[MAX_LINE];
    int replace_line = 0;
    int seatAvailability;

    strcpy(temp_filename, "temp____");
    strcat(temp_filename, filename);

    // Get the line number to update

    FILE *fptr;
    char response[10];
    char line[256]; 

    fptr = fopen("flightInformation.txt", "r"); 
    if (fptr == NULL) {
        printf("Error! Unable to open file.\n");
        return 1;
    }

    clearScreen();
    printf("|=======================================|\n");
    printf("|=============FLIGHT RECORDS============|\n");
    printf("=========================================\n");
    while (fgets(line, sizeof(line), fptr)) { 
        printf("%s", line); 
    }
    fclose(fptr); 

    printf("=========================================\n");
    printf("| Update Flight Number: ");
    scanf("%d", &replace_line);
    getchar();  

    printf("=========================================\n");
    printf("| Flight Number: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; 
    strcpy(replace, "| Flight Number: ");
    strcat(replace, input);

    // Flight Availability

    strcat(replace, "\t\t| Flight Availability: ");
    while (1) {
        printf("| Flight Availability (Y or N): ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0';
        if (strcasecmp(input, "Y") == 0 || strcasecmp(input, "N") == 0) {
            strcat(replace, input);
            break;
        } else {
            printf("--Invalid input! Please enter 'Y' for Yes or 'N' for No--\n");
        }
    }

    // Seat Availability

    strcat(replace, "\t| Seat Availability: ");
    while (1) {
        printf("| Number of Seats Available: ");
        if (scanf("%d", &seatAvailability) == 1) {
            char seat_str[10];
            sprintf(seat_str, "%d", seatAvailability);
            strcat(replace, seat_str);
            break;
        } else {
            printf("--Invalid input! Please enter an integer--\n");
            while (getchar() != '\n');
        }
    }
    getchar();  

    // Destination

    strcat(replace, "\t\t| Flight Destination: ");
    printf("| Flight Destination: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; 
    strcat(replace, input);

    // Date of Flight

    strcat(replace, "\t\t| Date of Flight: ");
    printf("| Date of Flight: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; 
    strcat(replace, input);

    // Time of Flight

    strcat(replace, "\t\t| Time of Flight: ");
    printf("| Time of Flight: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; 
    strcat(replace, input);

    // Arrival of Flight

    strcat(replace, "\t| Arrival: ");
    printf("| Arrival of Flight: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; 
    strcat(replace, input);
    strcat(replace, "\n");

    file = fopen(filename, "r");
    temp = fopen(temp_filename, "w");

    if (file == NULL || temp == NULL) {
        printf("Error opening files(s).\n");
        return 1;
    }

    bool keep_reading = true;
    int current_line = 1;

    do {
        fgets(buffer, MAX_LINE, file);

        if (feof(file)) {
            keep_reading = false;
        } else if (current_line == replace_line) {
            fputs(replace, temp); 
        } else {
            fputs(buffer, temp);  
        }

        current_line++;

    } while (keep_reading);

    fclose(file);
    fclose(temp);

    remove(filename);
    rename(temp_filename, filename);

    fptr = fopen("flightInformation.txt", "r"); 
    if (fptr == NULL) {
        printf("Error! Unable to open file.\n");
        return 1;
    }

    clearScreen();
    printf("|=======================================|\n");
    printf("|=========UPDATED FLIGHT RECORDS========|\n");
    printf("=========================================\n");
    while (fgets(line, sizeof(line), fptr)) { 
        printf("%s", line); 
    }
    fclose(fptr);

    printf("=========================================\n");
    printf("| Flight %d Record Updated Successfully! |\n", replace_line);
    printf("=========================================\n");
    while (1){
        char response[10];
        printf("| Press 1 to Return to Menu: ");

            fgets(response, sizeof(response), stdin);
            response[strcspn(response, "\n")] = 0; 

            if (strcmp(response, "1") == 0) {
                flightStatus();
                break; 
            } else {
                printf("Invalid input. Please press 1 to return to the main menu.\n");
            }
        }
}

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear"); 
#endif
}