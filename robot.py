#!/usr/bin/env python3


import wpilib
import wpilib.drive
import rev
from wpilib import AnalogEncoder
import navx


class MyRobot(wpilib.TimedRobot):


    def robotInit(self):
        """Robot initialization function"""

        self.right_front_drive_motor = rev.CANSparkMax(22, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.right_front_drive_encoder = self.right_front_drive_motor.getEncoder()

        self.left_front_drive_motor = rev.CANSparkMax(20, rev.CANSparkLowLevel.MotorType.kBrushless)

        self.left_front_drive_encoder = self.left_front_drive_motor.getEncoder()

        FrontLeft_analogPort = 0 
        FrontRight_analogPort = 1
        BackLeft_analogPort = 2
        BackRight_analogPort = 3

        # navX MXP using SPI
        self.gyro = navx.AHRS(wpilib.SPI.Port.kMXP)



        self.FrontLeftencoder = AnalogEncoder(FrontLeft_analogPort)
        self.FrontRightencoder = AnalogEncoder(FrontRight_analogPort)
        self.BackLeftencoder = AnalogEncoder(BackLeft_analogPort)
        self.BackRightencoder = AnalogEncoder(BackRight_analogPort)

        self.FrontLeftencoder.reset()
        self.FrontRightencoder.reset()
        self.BackLeftencoder.reset()
        self.BackRightencoder.reset()

    def teleopPeriodic(self):

        wpilib.SmartDashboard.putNumber("Front Left Encoder", self.FrontLeftencoder.getAbsolutePosition())
        wpilib.SmartDashboard.putNumber("Front Right Encoder", self.FrontRightencoder.getAbsolutePosition())
        wpilib.SmartDashboard.putNumber("Back Left Encoder", self.BackLeftencoder.getAbsolutePosition())
        wpilib.SmartDashboard.putNumber("Back Right Encoder", self.BackRightencoder.getAbsolutePosition())

        wpilib.SmartDashboard.putNumber("Front Right Drive Encoder", self.right_front_drive_encoder.getPosition())
        wpilib.SmartDashboard.putNumber("Front Left Drive Encoder", self.left_front_drive_encoder.getPosition())

        wpilib.SmartDashboard.putNumber("Yaw Angle", self.gyro.getYaw())
        wpilib.SmartDashboard.putNumber("Pitch Angle", self.gyro.getPitch())

