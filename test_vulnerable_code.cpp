// TEST SUITE: Designed to validate SAST detection for CWE-121 and CWE-798.

#include <iostream>
#include <cstring>

void login(char* password) {
    char buffer[10];
    strcpy(buffer, password); 
}

int main() {
    char* secret_key = "ADMIN12345"; 
    login("this_password_is_way_too_long_for_the_buffer");
    return 0;
}