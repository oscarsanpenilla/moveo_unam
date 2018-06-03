
#include <ros.h>
#include <moveo_unam/JointVariables.h>
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
MultiStepper steppers;
Servo myservo;


int servoPos;
int joint_step[6];
bool message_recived = false;
long positions[5]; 

ros::NodeHandle  nh;



//This funtion is call when it recibes a message from
//the topic named /joint_variables
void messageCb(const moveo_unam::JointVariables& msg){
  message_recived = true;
  joint_step[0] = msg.theta1;//
  joint_step[1] = msg.theta2;
  joint_step[2] = msg.theta3;
  joint_step[3] = msg.theta4;
  joint_step[4] = msg.theta5;
  joint_step[5] = msg.theta6;
  
}
  
   

//Se crea el subscriber dentro del arduino, el cual esta escrito al topic /joy
ros::Subscriber<moveo_unam::JointVariables> sub("joint_variables",&messageCb);


void setup()
{
  
  nh.getHardware()->setBaud(115200);
  //Inicializamos el nodo
  nh.initNode();
  //Se subscribe el topic /joint_variables
  nh.subscribe(sub);

  // Configure each stepper
  joint1.setMaxSpeed(100);
  joint2.setMaxSpeed(30);
  joint3.setMaxSpeed(100);
  joint4.setMaxSpeed(100);
  joint5.setMaxSpeed(100);
  

  //Then give them to MultiStepper to manage
  steppers.addStepper(joint1);
  steppers.addStepper(joint2);
  steppers.addStepper(joint3);
  steppers.addStepper(joint4);
  steppers.addStepper(joint5);
  
}

void loop()
{
  
     // Array of desired stepper positions must be long
    positions[0] = joint_step[0]*5.55; // negated since the real robot rotates in the opposite direction as ROS
    positions[1] = -joint_step[1]*2.77; 
    positions[2] = joint_step[2]; 
    positions[3] = joint_step[3]*0.55; 
    positions[4] = -joint_step[4]*2.22; 

    steppers.moveTo(positions);
    nh.spinOnce();
    steppers.runSpeedToPosition(); // Blocks until all are in position
    
  delay(1);
}

