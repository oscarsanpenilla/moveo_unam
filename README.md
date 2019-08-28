
# MOVEO UNAM

## Requirements:
1. Using a LINUX distribution, ubuntu 16 was used
2. Install ROS, the KINECTIC version is recommended
3. Set up the workspace correctly. (my workspace is named catkin_ws)

## Download the corresponding files
0. You can download the corresponding files from the following [link](https://github.com/oscarsanpenilla/moveo_unam)
1. Open a terminal in the ROS workspace catkin_ws / src
2. `git clone https://github.com/oscarsanpenilla/moveo_unam`
3. Change to the catkin_ws directory again `cd ../..`
4. `catkin_make`

## Handling using the Xbox 360 control
1. Install the following package this [tutorial](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick)
2. Program the Arduino Mega 2560 with the program xbox_joy_control.ino
3. `source devel / setup.bash` (execute this command every time a new terminal is opened)
4. `roscore`
5. `rosrun rosserial`
6. `rosrun rosserial_python serial_node.py _port: = / arduino_port`
7. Connect the xbox control
8. `rosrun joy joy_node`
9. Move the robot to the user's desire
Replicate paths using the Xbox 360 control
Create a folder using the `mkdir ~/catkin_ws/src/bagfiles` command Execute the previous steps from 1 to 6 
8. `cd ~/catkin_ws/src/bagfiles` 
9. `rosrun joy joy_node` 
10. To save the movements made execute rosbag record -a 11 Press Control + C to stop recording 12. Play the saved track using rosbag play "file name"

## Direct and Reverse Kinematics
For the calculation of direct and reverse kinematics, mathematical software was used. The corresponding file is named moveo.nb which is located in moveo_unam / scripts

Within it you can modify the path and run the entire program again, it will generate two files "Plot.png" generates an image with the path to follow. While "Trajectory.csv" generates a file with all the articular values ​​that the robot must follow.

To run the program follow the following steps:

1. Upload the kinematics.ino program to Arduino
2. Issue roscore in case it is not running.
3. Start the Arduino-Ros connection using the `rosrun rosserial_python serial_node.py _port command: = / arduino_port`
4. `rosrun moveo_unam kinematics_math.py`
The robot will begin to follow the trajectory, you can know the position of each link, thanks to the direct kinematics programmed in "kinematics_math.py" for this just execute the command

5. `rosrun moveo_unam position.py`


## Requisitos: (Spanish)

1. Utlizar una distribucion de LINUX, se empleo ubuntu 16
2. Instalar ROS, se recomienda la version KINECTIC
3. Configurar correctamente el workspace. (mi workspace lleva el nombre de catkin_ws)

## Descarga los archivos correspondientes

0. Puedes descargar los archivos correspondientes del siguiente enlace
https://github.com/oscarsanpenilla/moveo_unam
1. Abrir una terminal en el workspace de ROS catkin_ws/src
2. git clone https://github.com/oscarsanpenilla/moveo_unam
3. Cambiar al directorio catkin_ws nuevamente    cd ../..
4. catkin_make

## Manupulación mediante el control Xbox 360

0. Instalar el paquete siguiente este tutorial http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick
1. Programar el Arduino Mega 2560 con el programa       xbox_joy_control.ino
2. source devel/setup.bash  (ejecutar este comando cada vez que se abra una nueva terminal)
3. roscore
4. rosrun rosserial
5. rosrun rosserial_python serial_node.py _port:=/puerto_arduino
6. Conectar el control de xbox
7. rosrun joy joy_node
8. Mover el robot al deseo del usuario

## Replicar trayectorias mediante el control Xbox 360

Crear una carpeta mediante el comando     mkdir ~/catkin_ws/src/bagfiles
Ejecutar los pasos anteriores del 1 al 6
8. cd ~/catkin_ws/src/bagfiles
9. rosrun joy joy_node
10. Para guardar los movimientos realizados ejecutar      rosbag record -a
11. presiona Control + C para dejar de grabar
12. Reproducir la trayectoría guardada mediante rosbag play "nombre del archivo"

## Cinematica Directa e Inversa

Para el calculo de la cinematica directa e inversa, se utilizo el software mathematica. El archivo correspondiente lleva por nombre moveo.nb el cual se localiza en moveo_unam/scripts

Dentro del mismo se puede modificar la trayectoria y correr nuevamente todo el programa, este generara dos archivos "Plot.png" genera una imagen con la trayectoria a seguir. Mientras que  "Trayectoria.csv" genera un archivo con todos los valores articulares que el robot debe de seguir.

Para ejecutar el programa seguir los siguientes pasos:

1. Cargar al Arduino el programa kinematics.ino
2. Ejectutar roscore   en caso de que no este corriendo.
3. Iniciar la conexión Arduino-Ros mediane el comando rosrun rosserial_python serial_node.py _port:=/puerto_arduino
4. rosrun moveo_unam kinematics_math.py

El robot empezara a seguir la trayectoria, se puede saber la posición de cada eslabon, gracias a la cinematica directa programada en "kinematics_math.py" para ello basta con ejecutar el comando 

5. rosrun moveo_unam position.py
