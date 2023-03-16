/****************************************************************
 * Example1_Basics.ino
 * ICM 20948 Arduino Library Demo
 * Use the default configuration to stream 9-axis IMU data
 * Owen Lyke @ SparkFun Electronics
 * Original Creation Date: April 17 2019
 *
 * Please see License.md for the license information.
 *
 * Distributed as-is; no warranty is given.
 ***************************************************************/

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// port definition
#include <WiFi.h>
#include <PubSubClient.h>
 
#include "ICM_20948.h" // Click here to get the library: http://librarymanager/All#SparkFun_ICM_20948_IMU
//#define USE_SPI       // Uncomment this to use SPI
#define SERIAL_PORT Serial
#define SPI_PORT SPI // Your desired SPI port.       Used only when "USE_SPI" is defined
#define CS_PIN 2     // Which pin you connect CS to. Used only when "USE_SPI" is defined
#define WIRE_PORT Wire // Your desired Wire port.      Used when "USE_SPI" is not defined
// The value of the last bit of the I2C address.
// On the SparkFun 9DoF IMU breakout the default is 1, and when the ADR jumper is closed the value becomes 0
#define AD0_VAL 1

#ifdef USE_SPI
ICM_20948_SPI myICM; // If using SPI create an ICM_20948_SPI object
#else
ICM_20948_I2C myICM; // Otherwise create an ICM_20948_I2C object
#endif

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// wifi and mqtt initiation

// WiFi
const char *ssid = "ming"; // Enter your WiFi name
const char *password = "12345678";  // Enter WiFi password

// MQTT Broker
const char *mqtt_broker = "mqtt.eclipseprojects.io";
const char *topic = "meme/main";
const char *topic_it = "meme/it"; 
const char *topic_x = "meme/x";
const char *topic_y = "meme/y";
const char *topic_z = "meme/z";
const char *topic_gx = "meme/gx";
const char *topic_gy = "meme/gy";
const char *topic_gz = "meme/gz";
const char *topic_recog = "meme/recog";
// const char *mqtt_username = "emqx";
// const char *mqtt_password = "public";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//declarations 

int recog_counter = 0; 
const int THRESHOLD = 200;


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//setup
void setup()
{
  SERIAL_PORT.begin(115200);
  
  while (!SERIAL_PORT)
  {
  };

  // connecting to a WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  
  //connecting to a mqtt broker
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);
  while (!client.connected()) {
     String client_id = "esp32-client-";
     client_id += String(WiFi.macAddress());
     Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
     if (client.connect(client_id.c_str())) { //, mqtt_username, mqtt_password)) {
         Serial.println("mqtt broker connected");
     } else {
         Serial.print("failed with state ");
         Serial.print(client.state());
         delay(2000);
     }
  }
  // publish and subscribe
  client.publish(topic, "Hi I'm ESP32 ^^");
  client.subscribe(topic);


  // initialize IMU 
  #ifdef USE_SPI
    SPI_PORT.begin();
  #else
    WIRE_PORT.begin();
    WIRE_PORT.setClock(400000);
  #endif
  
    //myICM.enableDebugging(); // Uncomment this line to enable helpful debug messages on Serial
  
    bool initialized = false;
    while (!initialized)
    {
  
  #ifdef USE_SPI
      myICM.begin(CS_PIN, SPI_PORT);
  #else
      myICM.begin(WIRE_PORT, AD0_VAL);
  #endif
  
      SERIAL_PORT.print(F("Initialization of the sensor returned: "));
      SERIAL_PORT.println(myICM.statusString());
      if (myICM.status != ICM_20948_Stat_Ok)
      {
        SERIAL_PORT.println("Trying again...");
        delay(500);
      }
      else
      {
        initialized = true;
      }
    }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//callback
void callback(char *topic, byte *payload, unsigned int length) {
  Serial.print("Message arrived in topic: ");
  Serial.println(topic);
  Serial.print("Message:");
  for (int i = 0; i < length; i++) {
    Serial.print((char) payload[i]);
  }
  Serial.println();
  Serial.println("-----------------------");
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void loop()
{

  // counter to keep track of num of trials 
  int bye = 0;
  int trial_num = 0;
  char trial_num_char[10]; 
  char recog_reg [4];
  while (bye < 1){
    
    
    
    
  
    // collect 150 data points
    // 3000/20 = 150, this is about 3 secs of data, delay(20) delays 20 ms, suppose the program itself takes a while too, so this probaly takes a little longer than 3 sec 
    
      //initalize vars
      //float x_acc;
      /*
      float y_acc;
      float z_acc;
      float gx;
      float gy;
      float gz;
      */
      
      if (myICM.dataReady())
      {
        myICM.getAGMT();         // The values are only updated when you call 'getAGMT'
                                 //    printRawAGMT( myICM.agmt );     // Uncomment this to see the raw values, taken directly from the agmt structure
       // printScaledAGMT(&myICM); // This function takes into account the scale settings from when the measurement was made to calculate the values with units
  
//        if(i==0){
//          client.publish(topic, "1");
//          
//          SERIAL_PORT.print("Start");
//          delay(3000);
//        }
        // get 6 readings 
        char bufx[10];
        snprintf(bufx, 10, "%f", myICM.accX());  
        //x_acc = bufx;
  
        char bufy[10];
        snprintf(bufy, 10, "%f", myICM.accY());  

  
        char bufz[10];
        snprintf(bufz, 10, "%f", myICM.accZ());  

    
        char bufgx[10];
        snprintf(bufgx, 10, "%f", myICM.gyrX());  
 
  
        char bufgy[10];
        snprintf(bufgy, 10, "%f", myICM.gyrY());  

  
        char bufgz[10];
        snprintf(bufgz, 10, "%f", myICM.gyrZ());  

//        int counter =0;
//        int i=0;
//        const int THRESHOLD = 5;
//        if (bufgz[i]>THRESHOLD)
//        {  
//          i++; 
//
//        }
        //print to serial montior so i know what is going on 

        
    
        SERIAL_PORT.print("values:  ");
        SERIAL_PORT.print((float)atof(bufx));
        SERIAL_PORT.print("  ");
        SERIAL_PORT.print((float)atof(bufy));
        SERIAL_PORT.print("  ");
        SERIAL_PORT.print((float)atof(bufz));
        SERIAL_PORT.print("  ");
        SERIAL_PORT.print((float)atof(bufgx));
        SERIAL_PORT.print("  ");
        SERIAL_PORT.print((float)atof(bufgy));
        SERIAL_PORT.print("  ");
        SERIAL_PORT.println((float)atof(bufgz));


        float gy = float(atof(bufgy));

        if (gy>THRESHOLD)
        {  
          recog_counter++; 

        }

        if(recog_counter > 5){
          SERIAL_PORT.print("FORWARD!!!!");
          itoa( 1, recog_reg, 10);
          client.publish(topic_recog, recog_reg);
          delay(2000);
          recog_counter = 0;
        }
  
    /*
        SERIAL_PORT.print("Z_acc:  ");
        SERIAL_PORT.println(z_acc);
    
        SERIAL_PORT.print("X_gyr:  ");
        SERIAL_PORT.println(x_gyr);
  */
  
//        client.publish(topic_x, bufx);
//        client.publish(topic_y, bufy);
//        client.publish(topic_z, bufz);
//        client.publish(topic_gx, bufgx);
//        client.publish(topic_gy, bufgy);
//        client.publish(topic_gz, bufgz);

  
//        if(i==149){
//          trial_num ++;
//          itoa(trial_num, trial_num_char, 10);
//          client.publish(topic_it, trial_num_char);
//          client.publish(topic, "0");
//          SERIAL_PORT.print("Over");
//          SERIAL_PORT.println(trial_num);
//          
//          delay(2000);
//          
//        }
        
        delay(20);
    
      }
      else
      {
        SERIAL_PORT.println("Waiting for data");
        delay(500);
      }
    
  }
}


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Below here are some helper functions to print the data nicely!

void printPaddedInt16b(int16_t val)
{
  if (val > 0)
  {
    SERIAL_PORT.print(" ");
    if (val < 10000)
    {
      SERIAL_PORT.print("0");
    }
    if (val < 1000)
    {
      SERIAL_PORT.print("0");
    }
    if (val < 100)
    {
      SERIAL_PORT.print("0");
    }
    if (val < 10)
    {
      SERIAL_PORT.print("0");
    }
  }
  else
  {
    SERIAL_PORT.print("-");
    if (abs(val) < 10000)
    {
      SERIAL_PORT.print("0");
    }
    if (abs(val) < 1000)
    {
      SERIAL_PORT.print("0");
    }
    if (abs(val) < 100)
    {
      SERIAL_PORT.print("0");
    }
    if (abs(val) < 10)
    {
      SERIAL_PORT.print("0");
    }
  }
  SERIAL_PORT.print(abs(val));
}

void printRawAGMT(ICM_20948_AGMT_t agmt)
{
  SERIAL_PORT.print("RAW. Acc [ ");
  printPaddedInt16b(agmt.acc.axes.x);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.acc.axes.y);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.acc.axes.z);
  SERIAL_PORT.print(" ], Gyr [ ");
  printPaddedInt16b(agmt.gyr.axes.x);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.gyr.axes.y);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.gyr.axes.z);
  SERIAL_PORT.print(" ], Mag [ ");
  printPaddedInt16b(agmt.mag.axes.x);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.mag.axes.y);
  SERIAL_PORT.print(", ");
  printPaddedInt16b(agmt.mag.axes.z);
  SERIAL_PORT.print(" ], Tmp [ ");
  printPaddedInt16b(agmt.tmp.val);
  SERIAL_PORT.print(" ]");
  SERIAL_PORT.println();
}

void printFormattedFloat(float val, uint8_t leading, uint8_t decimals)
{
  float aval = abs(val);
  if (val < 0)
  {
    SERIAL_PORT.print("-");
  }
  else
  {
    SERIAL_PORT.print(" ");
  }
  for (uint8_t indi = 0; indi < leading; indi++)
  {
    uint32_t tenpow = 0;
    if (indi < (leading - 1))
    {
      tenpow = 1;
    }
    for (uint8_t c = 0; c < (leading - 1 - indi); c++)
    {
      tenpow *= 10;
    }
    if (aval < tenpow)
    {
      SERIAL_PORT.print("0");
    }
    else
    {
      break;
    }
  }
  if (val < 0)
  {
    SERIAL_PORT.print(-val, decimals);
  }
  else
  {
    SERIAL_PORT.print(val, decimals);
  }
}

#ifdef USE_SPI
void printScaledAGMT(ICM_20948_SPI *sensor)
{
#else
void printScaledAGMT(ICM_20948_I2C *sensor)
{
#endif
  SERIAL_PORT.print("Scaled. Acc (mg) [ ");
  printFormattedFloat(sensor->accX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->accZ(), 5, 2);
  SERIAL_PORT.print(" ], Gyr (DPS) [ ");
  printFormattedFloat(sensor->gyrX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->gyrZ(), 5, 2);
  SERIAL_PORT.print(" ], Mag (uT) [ ");
  printFormattedFloat(sensor->magX(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magY(), 5, 2);
  SERIAL_PORT.print(", ");
  printFormattedFloat(sensor->magZ(), 5, 2);
  SERIAL_PORT.print(" ], Tmp (C) [ ");
  printFormattedFloat(sensor->temp(), 5, 2);
  SERIAL_PORT.print(" ]");
  SERIAL_PORT.println();
}

/*
#ifdef USE_SPI
void thresholding(ICM_20948_SPI *sensor)
{
#else
void thresholding(ICM_20948_I2C *sensor)
{
#endif
*/
  
