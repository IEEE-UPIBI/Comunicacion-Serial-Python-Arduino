#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

double accelX = 0, accelY =0, accelZ;
double gyroX = 0, gyroY =0, gyroZ;

unsigned long lastTime = 0, sampleTime = 100;

void setup() {
  Serial.begin(9600);
  
  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    delay(500);
  }
}

void loop() {
  
  if(millis()-lastTime>=sampleTime)
  {
    lastTime = millis();  
    
    Vector normAccel = mpu.readNormalizeAccel();
    Vector normGyro = mpu.readNormalizeGyro();
    accelX = normAccel.XAxis;
    accelY = normAccel.YAxis;
    accelZ = normAccel.ZAxis;
    gyroX = normGyro.XAxis;
    gyroY = normGyro.YAxis;
    gyroZ = normGyro.ZAxis;

    Serial.println("ax:"+String(accelX));
    Serial.println("ay:"+String(accelY));
    Serial.println("az:"+String(accelZ));
    Serial.println("gx:"+String(gyroX));
    Serial.println("gy:"+String(gyroY));
    Serial.println("gz:"+String(gyroZ));
    
  }
}
