
#include <ros.h>
#include <sensor_msgs/Joy.h>
#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Servo.h>

// Joint 1
#define E1_STEP_PIN        42
#define E1_DIR_PIN         43


// Joint 2
#define Z_STEP_PIN         40
#define Z_DIR_PIN          41


// Joint 3
#define Y_STEP_PIN         44
#define Y_DIR_PIN          45


// Joint 4
#define X_STEP_PIN         46
#define X_DIR_PIN          47


// Joint 5 
#define E0_STEP_PIN        52
#define E0_DIR_PIN         53

AccelStepper joint1(1,E1_STEP_PIN, E1_DIR_PIN);
AccelStepper joint2(1,Z_STEP_PIN, Z_DIR_PIN);
AccelStepper joint3(1,Y_STEP_PIN, Y_DIR_PIN);
AccelStepper joint4(1,X_STEP_PIN, X_DIR_PIN);
AccelStepper joint5(1, E0_STEP_PIN, E0_DIR_PIN);
Servo myservo;
//Botones Control Xbox
int btn0; //A
int btn1; //B
int btn2; //X
int btn3; //Y
int btn4; //Sup Izq
int btn5; //Sup Der
int btn6; //Back
int btn7; //Start
int btn8; //Boton Central (Logo Xbox)
int btn9; //Palanca Izq
int btn10;//Palanca Der
int arrowH; //Flechas Izq [6]
int arrowV; //Flechas Vertical [7]
int triggerD; //Gatillo Der [5]
int triggerI; //Gatillo Izq [2]

int servoPos;
int triggerClose;
int triggerOpen;

int servoPin = 8;

ros::NodeHandle  nh;



//Creamos nuestra funcion que va ser llamada al cada vez que se reciba un mensaje del
//topic /joy
void messageCb(const sensor_msgs::Joy& msg){
  triggerD = msg.axes[5]; //Junta 1
  triggerI = msg.axes[2]; //Junta 1
  btn0  = msg.buttons[0];//Junta 2 abajo
  btn1  = msg.buttons[1];//Griper cerrado
  btn2  = msg.buttons[2]; //Griper abierto
  btn3  = msg.buttons[3];//Junta 2 arriba
  //Junta 3 arriba
  //Junta 3 abajo
  arrowH  = msg.axes[6]; //Junta 4
  arrowV = msg.axes[7]; //Junta 5 abajo
  
}
  
   

//Se crea el subscriber dentro del arduino, el cual esta escrito al topic /joy
ros::Subscriber<sensor_msgs::Joy> sub("joy",&messageCb);


void setup()
{
  myservo.attach(servoPin);
  
  nh.getHardware()->setBaud(115200);
  //Inicializamos el nodo
  nh.initNode();
  //Se subscribe el topic /joy
  nh.subscribe(sub);
}

void loop()
{
  //Junta 1 (base)
  if(triggerD == -1)
  {
   joint1.setMaxSpeed(100);
   joint1.setSpeed(100);
   joint1.runSpeed();  

  } 
  if(triggerI == -1)
  {
   joint1.setMaxSpeed(-100);
   joint1.setSpeed(-100);
   joint1.runSpeed();  

  } 
  //Junta 2
  if(btn0){
   joint2.setMaxSpeed(-10);
   joint2.setSpeed(-10);
   joint2.runSpeed();  

  } 
  if(btn3){
   joint2.setMaxSpeed(10);
   joint2.setSpeed(10);
   joint2.runSpeed();  

  }
  //Junta 3
  if(btn4){
   joint3.setMaxSpeed(-100);
   joint3.setSpeed(-100);
   joint3.runSpeed();  

  } 
  if(btn5){
   joint3.setMaxSpeed(100);
   joint3.setSpeed(100);
   joint3.runSpeed();  

  } 
  //Junta 4 
  if(arrowH == -1){
   joint4.setMaxSpeed(30);
   joint4.setSpeed(30);
   joint4.runSpeed();  

  } 
  if(arrowH == 1){
   joint4.setMaxSpeed(-30);
   joint4.setSpeed(-30);
   joint4.runSpeed();  

  } 
  //Gripper
  if(btn1)
  {
    myservo.write(180);   
  }
  if(btn2)
  {
    myservo.write(0);
     
  }
  //Junta 5
  if(arrowV == -1){
   joint5.setMaxSpeed(-30);
   joint5.setSpeed(-30);
   joint5.runSpeed();  

  } if(arrowV == 1){
   joint5.setMaxSpeed(30);
   joint5.setSpeed(30);
   joint5.runSpeed();  

  }
   
  nh.spinOnce();
  delay(1);
}

