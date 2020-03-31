import serial
import serial.tools.list_ports

class CreateSerial: # class for creating and reading serial data.

    ports_available = []

    # init function, used to create an instance of the CreateSerial class
    def __init__(self, port=None):
        self.ser = serial.Serial()
        self.ser.baud_rate = 9600
        self.ser.port = port
        self.recordAvailablePorts()

    # used to keep a record of all Serial ports available. Updates for all instances.
    def recordAvailablePorts(self):
        ports = serial.tools.list_ports.comports()
        CreateSerial.ports_available = [str(port).split("-")[0].replace(" ", "") for port in ports]
        print("\n---------SERIAL PORTS AVAILABLE: BEGIN--------------")
        print(*CreateSerial.ports_available, sep="\n")
        print("---------SERIAL PORTS AVAILABLE: END----------------\n")

    # open the Serial port. Prints an error message and terminates the program if not possible.
    def openPort(self):
        if self.ser.name not in CreateSerial.ports_available:
            print("Port '%s' is not available. Check the following:" % str(self.ser.port))
            print("Is the device connected? See available ports above.")
            print("Is there a typo in the device name? Check mu-editor!")

        else:
            try:
                self.ser.open()
                print("Port '%s' has opened successfully." % str(self.ser.port))
            except serial.SerialException:
                print("Resource busy! Is the serial monitor still running in mu-editor?")
                quit()

    # check if the serial port is already open.
    def checkOpen(self):
        return self.ser.is_open

    # set the port
    def setPort(self, port):
        self.ser.port = port

    # get the port. Returns string representation of port.
    def getPort(self):
        return str(self.ser.port)

    #set baud rate for Serial connection
    def setBaudRate(self, new_baud):
        self.ser.baud_rate = new_baud

    #get baud rate. Returns string representation of baud rate.
    def getBaudRate(self):
        return str(self.ser.baud_rate)

    # this function reads in serial data if there is data in waiting.
    # returns the data in format in which it was sent
    def read(self):
        data_received = ""
        returned_data = []
        while self.ser.in_waiting:
            data_received = self.ser.readline().decode('utf-8')
            returned_data.append(data_received.split("\n")[0][:-1])
        if returned_data != []:
            return returned_data
        return None

    # close the serial port.
    def close(self):
        if not self.checkOpen():
            self.ser.close()
