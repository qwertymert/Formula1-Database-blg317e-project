CREATE DATABASE IF NOT EXISTS FORMULA1;

use FORMULA1;

CREATE TABLE IF NOT EXISTS drivers (
                    driverId int AUTO_INCREMENT,
                    driverRef varchar(50),
                    number int,
                    code varchar(4),
                    forename varchar(50),
                    surname varchar(50),
                    dob datetime,
                    nationality varchar(50),
                    url varchar(100),
                    PRIMARY KEY (driverId)
                );

CREATE TABLE IF NOT EXISTS circuits (
                    circuitId int AUTO_INCREMENT,
                    circuitRef varchar(50),
                    name varchar(100),
                    location varchar(100),
                    country varchar(50),
                    lat float,
                    lng float,
                    alt int,
                    url varchar(100),
                    PRIMARY KEY (circuitId)
                );

CREATE TABLE IF NOT EXISTS races (
                    raceId int AUTO_INCREMENT,
                    year int,
                    round int,
                    circuitId int,
                    name varchar(100),
                    date date,
                    time time,
                    url varchar(100),
                    PRIMARY KEY (raceId),
                    FOREIGN KEY (circuitId) REFERENCES circuits(circuitId)
                );
                
CREATE TABLE IF NOT EXISTS driver_standings (
                    driverStandingsId int AUTO_INCREMENT,
                    raceId int,
                    driverId int,
                    points int,
                    position int,
                    positionText char(3),
                    wins int,
                    PRIMARY KEY (driverStandingsId),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
                );

CREATE TABLE IF NOT EXISTS pit_stops (
                    raceId int,
                    driverId int,
                    stop int,
                    lap int,
                    time time,
                    duration time,
                    milliseconds int,
                    PRIMARY KEY (raceId, driverId, stop),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
                );

CREATE TABLE IF NOT EXISTS lap_times (
                    raceId int,
                    driverId int,
                    lap int,
                    position int,
                    time time,
                    milliseconds int,
                    PRIMARY KEY (raceId, driverId, lap),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (driverId) REFERENCES drivers(driverId)
                );

CREATE TABLE IF NOT EXISTS constructors (
                    constructorId int AUTO_INCREMENT,
                    constructorRef varchar(50),
                    name varchar(100),
                    nationality varchar(50),
                    url varchar(100),
                    PRIMARY KEY (constructorId)
                );

CREATE TABLE IF NOT EXISTS constructor_standings (
                    constructorStandingsId int AUTO_INCREMENT,
                    raceId int,
                    constructorId int,
                    points int,
                    position int,
                    positionText char(3),
                    wins int,
                    PRIMARY KEY (constructorStandingsId),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
                );

CREATE TABLE IF NOT EXISTS constructor_results (
                    constructorResultsId int AUTO_INCREMENT,
                    raceId int,
                    constructorId int,
                    points int,
                    status varchar(50),
                    PRIMARY KEY (constructorResultsId),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
                );

CREATE TABLE IF NOT EXISTS qualifying (
                    qualifyId int AUTO_INCREMENT,
                    raceId int,
                    driverId int,
                    constructorId int,
                    number int,
                    position int,
                    q1 time,
                    q2 time,
                    q3 time,
                    PRIMARY KEY (qualifyId),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
                    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
                );

CREATE TABLE IF NOT EXISTS results (
                    resultId int AUTO_INCREMENT,
                    raceId int,
                    driverId int,
                    constructorId int,
                    number int,
                    grid int,
                    position int,
                    positionText char(3),
                    positionOrder int,
                    points int,
                    laps int,
                    time varchar(20),
                    milliseconds int,
                    fastestLap int,
                    ranks int,
                    fastestLapTime time,
                    fastestLapSpeed decimal,
                    statusId int,
                    PRIMARY KEY (resultId),
                    FOREIGN KEY (raceId) REFERENCES races(raceId),
                    FOREIGN KEY (driverId) REFERENCES drivers(driverId),
                    FOREIGN KEY (constructorId) REFERENCES constructors(constructorId)
                );

CREATE TABLE IF NOT EXISTS status (
                    statusId int AUTO_INCREMENT,
                    status varchar(50),
                    PRIMARY KEY (statusId)
                );

CREATE TABLE IF NOT EXISTS seasons (
                    year int,
                    url varchar(100),
                    PRIMARY KEY (year)
                );