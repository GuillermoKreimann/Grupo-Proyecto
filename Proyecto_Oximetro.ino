#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include OLED_RESET 13
Adafruit_SSD1306 display(OLED_RESET);

// VARIABLES //
float apo2=0;  
float apo2total=0; //sumatoria de ambas señales

int sensor=A0; //Fototransistor 790nm - 1050nm
int valorSensor; 
int sensor2=A1; //Fototransistor 400nm - 1000nm
int valorSensor2;

unsigned int intensidad_infrarrojo; //Intensidad reflejada EbO2
unsigned int intensidad_rojo; //Intensidad reflejada Eb

conat int numReadings=50; //Numero de muestras promedio
int readings(numReadings); //Lecturas de la entrada analogica
int indexs=0; //El indice de la lectura actual
int total=0; //Total
float average=0; //Promedio



void setup() {
 
}
void loop() {
  

}
