-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Talent_transformation
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Talent_transformation
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Talent_transformation` DEFAULT CHARACTER SET utf8 ;
USE `Talent_transformation` ;

-- -----------------------------------------------------
-- Table `Talent_transformation`.`1_personal_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Talent_transformation`.`1_personal_data` (
  `Employeenumber` INT NOT NULL,
  `Age` INT NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `Maritalstatus` VARCHAR(45) NULL,
  `Datebirth` INT NULL,
  PRIMARY KEY (`Employeenumber`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Talent_transformation`.`2_laboral_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Talent_transformation`.`2_laboral_data` (
  `id_ficha` INT NOT NULL AUTO_INCREMENT,
  `Joblevel` VARCHAR(100) NULL,
  `Jobrole` VARCHAR(100) NULL,
  `Businesstravel` VARCHAR(100) NULL,
  `Department` VARCHAR(100) NULL,
  `Overtime` VARCHAR(100) NULL,
  `Distancefromhome` DECIMAL(3,1) NULL,
  `Yearssincelastpromotion` INT NULL,
  `Yearsatcompany` INT NULL,
  `Yearswithcurrentmanager` INT NULL,
  `Remotework` VARCHAR(45) NULL,
  `Trainingtimeslastyear` INT NULL,
  `Attrition` VARCHAR(45) NULL,
  `1_personal_data_Employeenumber` INT NOT NULL,
  PRIMARY KEY (`id_ficha`),
  INDEX `fk_2_laboral_data_1_personal_data_idx` (`1_personal_data_Employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_2_laboral_data_1_personal_data`
    FOREIGN KEY (`1_personal_data_Employeenumber`)
    REFERENCES `Talent_transformation`.`1_personal_data` (`Employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Talent_transformation`.`2B_laboral_life`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Talent_transformation`.`2B_laboral_life` (
  `id_life` INT NOT NULL AUTO_INCREMENT,
  `Numcompaniesworked` INT NULL,
  `Totalworkingyears` INT NULL,
  `Education` INT NULL,
  `Educationfield` VARCHAR(225) NULL,
  `1_personal_data_Employeenumber` INT NOT NULL,
  PRIMARY KEY (`id_life`),
  INDEX `fk_2B_laboral_life_1_personal_data1_idx` (`1_personal_data_Employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_2B_laboral_life_1_personal_data1`
    FOREIGN KEY (`1_personal_data_Employeenumber`)
    REFERENCES `Talent_transformation`.`1_personal_data` (`Employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Talent_transformation`.`3_economic_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Talent_transformation`.`3_economic_data` (
  `id_economic` INT NOT NULL AUTO_INCREMENT,
  `Monthlyrate` INT NULL,
  `Percentsalaryhike` INT NULL,
  `Stockoptionlevel` INT NULL,
  `Dailyrate` DECIMAL(10,2) NULL,
  `Monthlyincome` DECIMAL(15,2) NULL,
  `Hourlyrate` DECIMAL(10,2) NULL,
  `1_personal_data_Employeenumber` INT NOT NULL,
  PRIMARY KEY (`id_economic`),
  INDEX `fk_3_economic_data_1_personal_data1_idx` (`1_personal_data_Employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_3_economic_data_1_personal_data1`
    FOREIGN KEY (`1_personal_data_Employeenumber`)
    REFERENCES `Talent_transformation`.`1_personal_data` (`Employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Talent_transformation`.`4_satisfaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Talent_transformation`.`4_satisfaction` (
  `id4_satisfaction` INT NOT NULL AUTO_INCREMENT,
  `Environmentsatisfaction` VARCHAR(45) NULL,
  `Jobinvolvement` VARCHAR(45) NULL,
  `Jobsatisfaction` VARCHAR(45) NULL,
  `Relationshipsatisfaction` VARCHAR(45) NULL,
  `Performancerating` DECIMAL(5,2) NULL,
  `Worklifebalance` DECIMAL(5,2) NULL,
  `1_personal_data_Employeenumber` INT NOT NULL,
  PRIMARY KEY (`id4_satisfaction`),
  INDEX `fk_4_satisfaction_1_personal_data1_idx` (`1_personal_data_Employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_4_satisfaction_1_personal_data1`
    FOREIGN KEY (`1_personal_data_Employeenumber`)
    REFERENCES `Talent_transformation`.`1_personal_data` (`Employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
