-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 18, 2021 at 04:07 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mini_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `note`
--

CREATE TABLE `note` (
  `id` int(11) NOT NULL,
  `notice` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `note`
--

INSERT INTO `note` (`id`, `notice`) VALUES
(1, 'hey there');

-- --------------------------------------------------------

--
-- Table structure for table `rating`
--

CREATE TABLE `rating` (
  `roomno` int(3) NOT NULL,
  `name` text NOT NULL,
  `rate` text NOT NULL,
  `add_comments` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rating`
--

INSERT INTO `rating` (`roomno`, `name`, `rate`, `add_comments`) VALUES
(101, 'john', '4', ''),
(203, 'john', '4', ''),
(203, 'john', '2', ''),
(204, 'john', '3', '');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `username` varchar(10) NOT NULL,
  `name` text NOT NULL,
  `contact` text NOT NULL,
  `age` int(2) NOT NULL,
  `password` varchar(15) NOT NULL,
  `avaliable` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`username`, `name`, `contact`, `age`, `password`, `avaliable`) VALUES
('bob45', 'bob', '1237896540', 36, 'bob123', 'yes'),
('brian6', 'brian', '9874621530', 31, 'brian123', 'yes'),
('john2', 'john', '1234567890', 26, 'john123', 'yes'),
('lee4', 'lee', '7896541230', 30, 'lee123', 'yes'),
('mark8', 'mark', '1254698730', 40, 'mark123', 'no'),
('roy45', 'roy', '4569871230', 36, 'roy123', 'yes'),
('stokes65', 'stokes', '2564789130', 29, 'stokes', 'yes'),
('white7', 'white', '1456987630', 35, 'white123', 'no');

-- --------------------------------------------------------

--
-- Table structure for table `todo`
--

CREATE TABLE `todo` (
  `roomno` int(3) NOT NULL,
  `name` text NOT NULL,
  `tasks` text NOT NULL,
  `extra_req` varchar(50) NOT NULL,
  `status` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `todo`
--

INSERT INTO `todo` (`roomno`, `name`, `tasks`, `extra_req`, `status`) VALUES
(102, 'white', 'Make Bed,Change Bedding', '', 'done'),
(203, 'john', 'Make Bed,Clean Room', '', 'done'),
(401, 'lee', 'Clean Room,Change Bedding,Clean Bathroom,Extra Bed', '', 'done'),
(202, 'brian', 'Change Bedding,Make Bed', '', 'done'),
(103, 'john', 'Make Bed', '', 'done'),
(101, 'white', 'Clean Room,Clean Bathroom', 'clean bedsheets please', 'in progress'),
(102, 'mark', 'Make Bed,Change Bedding', '', 'in progress');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
