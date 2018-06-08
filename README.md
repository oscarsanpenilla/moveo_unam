
# MOVEO UNAM

## Requisitos:

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
